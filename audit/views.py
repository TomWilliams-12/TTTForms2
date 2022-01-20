from django.shortcuts import render
from django.views import View
from form_apps.cbr.models import Cbr

class AuditView(View):
    forms = Cbr.objects.all()
    def get(self, request):
        return render(request, 'audit.html', {'forms': self.forms})
