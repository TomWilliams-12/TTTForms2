from django.shortcuts import render, redirect
from django.views import View
# Create your views here.

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html', {})
        else:
            return redirect('login')