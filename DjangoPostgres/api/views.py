import xmlrpc.client
import json

from django.shortcuts import render
from django.http import HttpResponse
from api.models import ResUsers

from datetime import date

url = 'http://18.223.171.177:8069'
db = 'PetWell'
username = 'contacto@petwell.com'
password = 'odoo'

common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
models = xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % url)
uid = common.authenticate(db, username, password, {})

# Create your views here.
def index_page(request):
  users = ResUsers.objects.all()
  print(len(users))
  for e in users:
    print(e.id)
  data = {
    'users': users
  }

  return render(request, 'user/index.html', data)

def home(request):

  response = {}
  try:
    ids = models.execute_kw(db, uid, password, 'product.product', 'search_read', [])
    print(len(ids))
    if (len(ids) == 0):
      response['response'] = []
    else:
      response['response'] = ids
  except Exception as error:
    print(error)
    response['error'] = True
    response['response'] = []

  context = {
    "services": response
  }

  return render(request, "pages/home.html", context)

def odooGet(request):
  response = {}
  try:
    ids = models.execute_kw(db, uid, password, 'product.product', 'search_read', [])
    print(len(ids))
    if (len(ids) == 0):
      response['response'] = []
    else:
      response['response'] = ids
  except Exception as error:
    print(error)
    response['error'] = True
    response['response'] = []

  return HttpResponse(json.dumps(response), content_type="application/json")

def odooPost(request):
  try:
    response = {}
    id = models.execute_kw(db, uid, password, 'product.product', 'create', [{
      'name': 'Prueba',
      'description': 'Prueba',
      'list_price': 0
    }])
    response['response'] = 'Object Added.'
    response['id'] = id
  except Exception as error:
    print(error)
    response['error'] = True
    response['response'] = []


  return HttpResponse(json.dumps(response), content_type="application/json") 


