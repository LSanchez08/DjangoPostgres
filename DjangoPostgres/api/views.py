import xmlrpc.client
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
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
    if (len(ids) == 0):
      response['response'] = []
    else:
      response['response'] = ids
  except Exception as error:
    print(error)
    response['error'] = True
    response['response'] = []

  context = {
    "services": response['response']
  }

  return render(request, "pages/home.html", context)

def update(request):
  return render(request, "pages/update.html")

def create(request):
  return render(request, "pages/create.html")

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

def odooGetOne(request):
  response = {}
  try:
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    ids = models.execute_kw(db, uid, password, 'product.product', 'search_read', [[['id', '=', body['id']]]])
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
  response = {}
  try:
    
    body = {
      'name': request.POST.get('name'),
      'description': request.POST.get('description'),
      'price': request.POST.get('price'),
    }

    id = models.execute_kw(db, uid, password, 'product.product', 'create', [body])
    response['response'] = 'Object Added.'
    response['id'] = id
  except Exception as error:
    print(error)
    response['error'] = True
    response['response'] = []


  return home(request)

def odooPut(request):
  response = {}
  try:
    body = {
      'id': request.POST.get('id'),
      'name': request.POST.get('name'),
      'description': request.POST.get('description'),
      'price': request.POST.get('price'),
    }

    id = models.execute_kw(db, uid, password, 'product.product', 'write', [[body['id']], body])
    response['response'] = 'Object Updated.'
    response['id'] = id
  except Exception as error:
    print(error)
    response['error'] = True
    response['response'] = []


  return HttpResponse(json.dumps(response), content_type="application/json")

def odooDelete(request):
  response = {}
  try:
    
    body = {
      'id': request.POST.get('id'),
    }

    id = models.execute_kw(db, uid, password, 'product.product', 'unlink', [[body['id']]])
    response['response'] = 'Object Deleted.'
    response['id'] = id
  except Exception as error:
    print(error)
    response['error'] = True
    response['response'] = []


  return HttpResponse(json.dumps(response), content_type="application/json")

def odooAddImage (request):
  response = {}
  try:
    
    name = request.FILES['file'].name
    print(name)

    yourImage = request.files.get(name)

    # id = models.execute_kw(db, uid, password, 'product.product', 'write', [[body['id']], body])
    response['response'] = 'Object Updated.'
    # response['id'] = id
  except Exception as error:
    print(error)
    response['error'] = True
    response['response'] = []


  return HttpResponse(json.dumps(response), content_type="application/json")