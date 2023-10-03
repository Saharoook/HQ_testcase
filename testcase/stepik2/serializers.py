from rest_framework import serializers
from stepik2.models import Product, User, Lesson, UsersToLessons


class LessonsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):

    lessons = LessonsListSerializer(many=True, source='Lesson.all', read_only=True)

    class Meta:
        depth = 3
        model = Product
        fields = ['owner', 'name', 'lessons']


class UserToLessonsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersToLessons
        fields = '__all__'


class ProductWithUser(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'owner']


class UserListSerializer(serializers.ModelSerializer):

    products = ProductWithUser(many=True, read_only=True)
    lessons = LessonsListSerializer(many=True, read_only=True)
    info = UserToLessonsListSerializer(many=True, source='UsersToLessons', read_only=True)

    class Meta:
        depth = 0
        model = User
        fields = ['data', 'lessons', 'products', 'info']

