from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', index_page, name='index_page'),
]
