from django.contrib import admin

# notice Model을 불러옴
from .models import Notice

# Register your models here.
# admin이 Notice 접근
admin.site.register(Notice)