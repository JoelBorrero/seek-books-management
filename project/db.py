from dataclasses import dataclass, field
from datetime import datetime

from bson.objectid import ObjectId
from pymongo.collection import Collection
from pymongo.cursor import Cursor

from project.settings import db_client


@dataclass
class ModelMetaclass:
    collection_name: str
    fields: dict = field(default_factory=dict)


class MongoDBClient:
    @staticmethod
    def get_collection(collection_name: str) -> Collection:
        return db_client["seek"][collection_name]


class QuerySet:
    """
    Implements Django-like queryset functionality.

    All Mongo queries are done here.
    """

    class Query:
        """
        Wraps a MongoDB cursor and provides Django-like queryset functionality.

        Most of the methods here are used by the Django Paginator.
        """

        def __init__(self, data: Cursor):
            self.data = data.to_list()

        def __len__(self) -> int:
            return len(self.data)

        def __getitem__(self, index: int):
            items = self.data[index]
            for item in items:
                item["_id"] = str(item["_id"])
            return items

    def __init__(self, model_class: type):
        self.model_class = model_class
        self.collection = MongoDBClient.get_collection(
            model_class._meta.collection_name
        )

    def all(self) -> Query:
        return QuerySet.Query(self.collection.find())

    def create(self, data: dict) -> "BaseModel":
        self.collection.insert_one(data)
        return self.model_class._from_db(data)

    def delete(self, id: str) -> bool:
        return self.collection.delete_one({"_id": ObjectId(id)}).deleted_count > 0

    def get(self, id: str) -> "BaseModel":
        data = self.collection.find_one(ObjectId(id))
        return self.model_class._from_db(data)

    def update(self, id: str, data: dict) -> "BaseModel":
        self.collection.replace_one(ObjectId(id), data, upsert=True)
        return self.model_class._from_db(data)


class BaseModel:
    _id: str = None
    created_at: datetime = None
    updated_at: datetime = None
    objects: QuerySet = None
    _meta: ModelMetaclass = None

    def __init__(self, **kwargs):
        """Initialize model instance with given attributes"""
        for key, value in kwargs.items():
            if key in self._meta.fields:
                setattr(self, key, value)
            else:
                raise ValueError(f"Unknown field {key} for {self.__class__.__name__}")

    def __repr__(self):
        return f"<{self.__class__.__name__}|{self._id}>"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Set up metadata for the model
        collection_name = kwargs.get("collection_name", cls.__name__.lower())
        fields = {name: field_type for name, field_type in cls.__annotations__.items()}
        cls._meta = ModelMetaclass(
            collection_name=collection_name, fields={**fields, "_id": str}
        )
        cls.objects = QuerySet(cls)

    @classmethod
    def _from_db(cls, data: dict) -> "BaseModel":
        """Convert database dictionary to model instance"""
        if data is None:
            return None

        instance = cls()
        for key, value in data.items():
            setattr(instance, key, str(value) if key == "_id" else value)
        return instance

    def delete(self) -> bool:
        """Delete the current instance from the database"""
        return self.objects.delete(self._id)

    def save(self) -> None:
        """Save the current instance to the database"""
        data = self.to_dict()
        data["updated_at"] = datetime.now()
        if self._id:
            self.objects.update(self._id, data)
        else:
            data["created_at"] = datetime.now()
            if "_id" in data:
                del data["_id"]
            self.objects.create(data)
            self._id = str(data["_id"])
            self.created_at = data["created_at"]
            self.updated_at = data["updated_at"]

    def to_dict(self) -> dict:
        """Convert model instance to dictionary for database storage"""
        return {
            key: getattr(self, key) for key in self._meta.fields if hasattr(self, key)
        }
