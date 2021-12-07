from django.shortcuts import render
from django.views import View

class CbrPage(View):
    def get(self, request):
        return render(request, 'cbr.html', {})
