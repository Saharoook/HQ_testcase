from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, User, Lesson, UsersToLessons, UsersToProducts
from .serializers import ProductListSerializer, UserListSerializer, LessonsListSerializer, UserToLessonsListSerializer


class ProductApiView(generics.ListAPIView):

    queryset = Product.objects.all().prefetch_related('lessons')
    serializer_class = ProductListSerializer


class UserApiView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(data=kwargs['name'])
        serializer_class = UserListSerializer(queryset, many=True)
        info = UserToLessonsListSerializer(UsersToLessons.objects.filter(user=User.objects.get(data=kwargs['name'])), many=True).data
        print(serializer_class.data[0]['lessons'][0])
        print(info[0])
        for i in range(len(serializer_class.data[0]['lessons'])):
            serializer_class.data[0]['lessons'][i].update(info[i])
        return Response(serializer_class.data)


class LessonsApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonsListSerializer
