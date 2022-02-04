from django.shortcuts import render, redirect
from django.views import View
from form_apps.cbr.models import Cbr
<<<<<<< HEAD
from forms.models import Forms
=======
>>>>>>> main
# Create your views here.

class Home(View):
    def get(self, request):
        user = request.user
        if request.user.is_authenticated:
            if user.is_auditor:
                cbr_ids = list(Cbr.objects.filter(audit_Completed=False).values_list('pk', flat=True))
                all_ids = cbr_ids
                forms = Forms.objects.filter(object_id__in=all_ids)

                cbr_certs = list(Cbr.objects.filter(has_Certificate=True).values_list('pk', flat=True))
                all_certs = cbr_certs
                create_certificates = Forms.objects.filter(object_id__in=all_certs).filter(certificate=False)
                return render(request, 'index.html', {'forms': forms, 'create_certificates': create_certificates})
            else:
                cbr_ids = list(Cbr.objects.filter(audit_Completed=False).values_list('pk', flat=True))
                forms = Forms.objects.filter(object_id__in=cbr_ids)
                return render(request, 'index.html', {'forms': forms})
        else:
            return redirect('login')