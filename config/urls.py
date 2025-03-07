from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mangaapi/v1/', include('apps.mangaapi.urls'))
]
