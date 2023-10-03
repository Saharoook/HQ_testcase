from django.contrib import admin
from .models import User, Product, UsersToProducts, UsersToLessons, Lesson


admin.site.register(User)
admin.site.register(Product)
admin.site.register(UsersToProducts)
admin.site.register(UsersToLessons)
admin.site.register(Lesson)
