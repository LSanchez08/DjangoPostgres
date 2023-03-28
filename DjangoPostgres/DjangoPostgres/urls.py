from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('', home, name='home'),
    path('update/<id_pet>/<name_pet>/<description_pet>/<price_pet>', update, name='update'),
    path('create/', create, name='create'),
    path('admin/', admin.site.urls),
    path('user/', index_page, name='index_page'),
    path('api/odooGet', odooGet, name='odooGet'),
    path('api/odooGetOne', odooGetOne, name='odooGetOne'),
    path('api/odooPost', odooPost, name='odooPost'),
    path('api/odooPut', odooPut, name='odooPut'),
    path('api/odooDelete', odooDelete, name='odooDelete'),
    path('api/odooAddImage', odooAddImage, name='odooAddImage'),
]
