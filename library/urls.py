from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.book_list, name="book_list"),
    path("books/new/", views.book_create, name="book_create"),
    path("books/<int:book_id>/edit/", views.book_edit, name="book_edit"),
    path("books/<int:book_id>/delete/", views.book_delete, name="book_delete"),
    path("members/", views.member_list, name="member_list"),
    path("members/new/", views.member_create, name="member_create"),
    path("members/<int:member_id>/history/",
         views.member_history, name="member_history"),
    path("statistics/", views.statistics, name="statistics"),
    path("borrow/<int:book_id>/<int:member_id>/",
         views.borrow_book, name="borrow_book"),
    path("return/<int:book_id>/", views.return_book, name="return_book"),
]
