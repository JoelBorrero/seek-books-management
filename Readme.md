# Steps to run the project (WIP)

1. `cp dev.env .env`
2. `make build` - Shorthand for `docker compose build`
3. `make up` - Shorthand for `docker compose up -d`

# Populate the database
To populate the database with some data, run the following command:
```bash
make shell
```
Then, copy and paste the following code:
```python
with open('setup/populate_db.py') as f:
    exec(f.read())
```
