import xmlrpc.client
import json

from django.shortcuts import render
from django.http import HttpResponse
from api.models import ResUsers

url = 'http://18.223.171.177:8069'
db = 'Parcial2'
username = 'admin@email.com'
password = 'odoo'

common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
models = xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % url)
uid = common.authenticate(db, username, password, {})

# Create your views here.
def index_page(request):
  users = ResUsers.objects.all()

  data = {
    'users': users
  }

  return render(request, 'user/index.html', data)

def home(request):
  return render(request, "pages/home.html")

def odooTest(request):
  ids = models.execute_kw(db, uid, password, 'res.users', 'search', [[['password', '=', 'none']]], {'limit': 1})
  [record] = models.execute_kw(db, uid, password, 'res.users', 'read', [ids])
  response = {}
  response['message'] = record
  print(len(record))

  return HttpResponse(json.dumps(response), content_type="application/json")


