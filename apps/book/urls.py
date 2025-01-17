from django.urls import re_path

from .views import book_average_price, book_detail, book_list


urlpatterns = [
    re_path(r"books/$", book_list),
    re_path(r"books/(?P<id>[0-9a-f]+)/$", book_detail),
    re_path(r"books/average-price/(?P<year>[0-9]+)/$", book_average_price),
]
