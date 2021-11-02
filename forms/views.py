from django.shortcuts import render
from django.views import View
from forms.forms import InductionForm, ReviewForm

# Create your views here.
class InductionPage(View):
    def get(self, request):
        induction = InductionForm()
        return render(request, 'induction.html', {'induction': induction})

class ReviewPage(View):
    def get(self, request):
        review = ReviewForm()
        induction = InductionForm()
        return render(request, 'review.html', {'review': review, 'induction': induction})