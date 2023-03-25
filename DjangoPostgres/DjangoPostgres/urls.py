from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('', home, name='home'),
    path('update/', update, name='update'),
    path('create/', create, name='create'),
    path('admin/', admin.site.urls),
    path('user/', index_page, name='index_page'),
    path('api/odooGet', odooGet, name='odooGet'),
    path('api/odooPost', odooPost, name='odooPost'),
]
