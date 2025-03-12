from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.mangaapi.views import MangasviewSet


router = routers.DefaultRouter()
router.register(r'mangas', MangasviewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mangaapi/v1/', include(router.urls)),
]
