from django.shortcuts import render
from django.views import View
from forms.forms import InductionForm, ReviewForm

# Create your views here.
class InductionPage(View):
    choices = (
            ('',''),
            ('Counterbalance Novice','Counterbalance Novice'),
            ('Counterbalance Experienced','Counterbalance Experienced'),
            ('Counterbalance Refresher','Counterbalance Refresher'),
            ('Counterbalance Conversion','Counterbalance Conversion'),
            ('Reach Novice','Reach Novice'),
            ('Reach Experienced','Reach Experienced'),
            ('Reach Refresher','Reach Refresher'),
            ('Reach Conversion','Reach Conversion'),
        )
    def get(self, request):
        induction = InductionForm(self.choices, request=request)
        return render(request, 'induction.html', {'induction': induction})


class ReviewPage(View):
    def get(self, request):
        review = ReviewForm()
        induction = InductionForm()
        return render(request, 'review.html', {'review': review, 'induction': induction})