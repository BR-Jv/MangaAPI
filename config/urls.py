from django.contrib import admin
from django.urls import path, include
from apps.mangaapi.urls import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mangaapi/v1/', include(router.urls))
]
