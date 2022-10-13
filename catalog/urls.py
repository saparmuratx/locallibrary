from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('books/', views.books_list),
    path('books/<int:pk>/', views.book_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)
