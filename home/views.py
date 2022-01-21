from django.shortcuts import render, redirect
from django.views import View
from form_apps.cbr.models import Cbr
# Create your views here.

class Home(View):
    def get(self, request):
        user = request.user
        if request.user.is_authenticated:
            if user.is_auditor:
                forms = Cbr.objects.filter(audit_Completed=False)
            else:
                forms = Cbr.objects.filter(instructor=user.id).filter(completed=False)
            return render(request, 'index.html', {'forms': forms})
        else:
            return redirect('login')