from django.shortcuts import render, redirect
from django.views import View
from form_apps.cbr.models import Cbr
from form_apps.mewp.models import Mewp
from form_apps.ohc.models import Ohc
from form_apps.aw.models import Aw
from form_apps.ppt.models import Ppt
from django.db.models import Q
from itertools import chain
from forms.models import Forms
# Create your views here.

class Home(View):
    def get(self, request):
        user = request.user
        if request.user.is_authenticated:
            if user.is_auditor:
                cbr_ids = Cbr.objects.filter(Q(audit_Completed=False),Q(completed=True))
                mewp_ids = Mewp.objects.filter(Q(audit_Completed=False),Q(completed=True))
                ohc_ids = Ohc.objects.filter(Q(audit_Completed=False),Q(completed=True))
                aw_ids = Aw.objects.filter(Q(audit_Completed=False),Q(completed=True))
                ppt_ids = Ppt.objects.filter(Q(audit_Completed=False),Q(completed=True))
                forms = chain(cbr_ids, mewp_ids, ohc_ids, aw_ids, ppt_ids)

                cbr_certs = Cbr.objects.filter(Q(has_Certificate=True))
                mewp_certs = Mewp.objects.filter(Q(has_Certificate=True))
                ohc_certs = Ohc.objects.filter(Q(has_Certificate=True))
                aw_certs = Aw.objects.filter(Q(has_Certificate=True))
                ppt_certs = Ppt.objects.filter(Q(has_Certificate=True))
                create_certificates = chain(cbr_certs, mewp_certs, ohc_certs, aw_certs, ppt_certs)  
                return render(request, 'index.html', {'forms': forms, 'create_certificates': create_certificates})
            else:
                cbr_ids = Cbr.objects.filter(Q(instructor=user.id),Q(completed=False))
                mewp_ids = Mewp.objects.filter(Q(instructor=user.id),Q(completed=False))
                ohc_ids = Ohc.objects.filter(Q(instructor=user.id),Q(completed=False))
                aw_ids = Aw.objects.filter(Q(instructor=user.id),Q(completed=False))
                ppt_ids = Ppt.objects.filter(Q(instructor=user.id),Q(completed=False))
                forms = chain(cbr_ids, mewp_ids, ohc_ids, aw_ids, ppt_ids)
                return render(request, 'index.html', {'forms': forms})
        else:
            return redirect('login')