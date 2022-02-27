from django.shortcuts import render, redirect
from django.views import View
from form_apps.cbr.models import Cbr
from form_apps.mewp.models import Mewp
from form_apps.ohc.models import Ohc
from form_apps.aw.models import Aw
from forms.models import Forms
# Create your views here.

class Home(View):
    def get(self, request):
        user = request.user
        if request.user.is_authenticated:
            if user.is_auditor:
                cbr_ids = list(Cbr.objects.filter(audit_Completed=False).filter(completed=True).values_list('pk', flat=True))
                mewp_ids = list(Mewp.objects.filter(audit_Completed=False).filter(completed=True).values_list('pk', flat=True))
                ohc_ids = list(Ohc.objects.filter(audit_Completed=False).filter(completed=True).values_list('pk', flat=True))
                aw_ids = list(Aw.objects.filter(audit_Completed=False).filter(completed=True).values_list('pk', flat=True))
                all_ids = cbr_ids + mewp_ids + ohc_ids + aw_ids
                forms = Forms.objects.filter(object_id__in=all_ids)

                cbr_certs = list(Cbr.objects.filter(has_Certificate=True).values_list('pk', flat=True))
                mewp_certs = list(Mewp.objects.filter(has_Certificate=True).values_list('pk', flat=True))
                ohc_certs = list(Ohc.objects.filter(has_Certificate=True).values_list('pk', flat=True))
                aw_certs = list(Aw.objects.filter(has_Certificate=True).values_list('pk', flat=True))
                all_certs = cbr_certs + mewp_certs + ohc_certs + aw_certs
                create_certificates = Forms.objects.filter(object_id__in=all_certs).filter(certificate=False)
                return render(request, 'index.html', {'forms': forms, 'create_certificates': create_certificates})
            else:
                cbr_ids = list(Cbr.objects.filter(instructor=user.id).filter(completed=False).values_list('pk', flat=True))
                mewp_ids = list(Mewp.objects.filter(instructor=user.id).filter(completed=False).values_list('pk', flat=True))
                ohc_ids = list(Ohc.objects.filter(instructor=user.id).filter(completed=False).values_list('pk', flat=True))
                aw_ids = list(Aw.objects.filter(instructor=user.id).filter(completed=False).values_list('pk', flat=True))
                all_ids = cbr_ids + mewp_ids + ohc_ids
                forms = Forms.objects.filter(object_id__in=all_ids)
                return render(request, 'index.html', {'forms': forms})
        else:
            return redirect('login')