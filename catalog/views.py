from .serializers import BookSerializer
from .models import Book

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
# @csrf_exempt
def books_list(request, format=None):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def book_details(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)
        
