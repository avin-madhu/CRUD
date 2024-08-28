from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name="book_list"),
    path('book/new/', views.create_book, name="create_book"),
    path('book/edit/<int:pk>', views.edit_book, name="edit_book"),
    path('book/delete/<int:pk>', views.delete_book, name="delete_book"),


]