from django.shortcuts import render
from django.views import View
from forms.models import Forms

class AuditView(View):
    forms = Forms.objects.all()
    def get(self, request):
        return render(request, 'audit.html', {'forms': self.forms})
