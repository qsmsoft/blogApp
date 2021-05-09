from django.contrib import admin
from django.http.request import RawPostDataException
from .models import Post


# Register your models here.


admin.site.register(Post)