from django.shortcuts import render, redirect
from django.views import View
from form_apps.cbr.models import Cbr
# Create your views here.

class Home(View):
    def get(self, request):
        user = request.user
        forms = Cbr.objects.filter(instructor=user.id)
        if request.user.is_authenticated:
            return render(request, 'index.html', {'forms': forms})
        else:
            return redirect('login')