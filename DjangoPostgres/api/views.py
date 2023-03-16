from django.shortcuts import render
from api.models import AccountAccountAccountJournalRel

# Create your views here.
def index_page(request):
  account = AccountAccountAccountJournalRel.objects.all()

  data = {
    'accounts': account
  }

  return render(request, 'account/index.html', data)
