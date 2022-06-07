from django.shortcuts import render, redirect
from django.views import View
from form_apps.cbr.models import Cbr
from form_apps.mewp.models import Mewp
from form_apps.ohc.models import Ohc
from form_apps.aw.models import Aw
from form_apps.ppt.models import Ppt
from form_apps.boom.models import Boom
from form_apps.pivot_steer.models import Pivot
from form_apps.loading_shovel.models import Shovel
from django.db.models import Q
from itertools import chain
from form_apps.threesixty.models import Threesixty
from forms.models import Forms
from django.contrib.contenttypes.models import ContentType
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
                boom_ids = Boom.objects.filter(Q(audit_Completed=False),Q(completed=True))
                pivot_ids = Pivot.objects.filter(Q(audit_Completed=False),Q(completed=True))
                threesixty_ids = Threesixty.objects.filter(Q(audit_Completed=False),Q(completed=True))
                shovel_ids = Shovel.objects.filter(Q(audit_Completed=False),Q(completed=True))
                forms = chain(shovel_ids, cbr_ids, mewp_ids, ohc_ids, aw_ids, ppt_ids, boom_ids, pivot_ids, threesixty_ids)

                self_cbr_ids = Cbr.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_mewp_ids = Mewp.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_ohc_ids = Ohc.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_aw_ids = Aw.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_ppt_ids = Ppt.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_boom_ids = Boom.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_pivot_ids = Pivot.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_three_ids = Threesixty.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_shovel_ids = Shovel.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_forms = chain(self_shovel_ids, self_three_ids,self_cbr_ids, self_mewp_ids, self_ohc_ids, self_aw_ids, self_ppt_ids, self_boom_ids, self_pivot_ids)

                cbr_certs = Cbr.objects.filter(Q(has_Certificate=True))
                mewp_certs = Mewp.objects.filter(Q(has_Certificate=True))
                ohc_certs = Ohc.objects.filter(Q(has_Certificate=True))
                aw_certs = Aw.objects.filter(Q(has_Certificate=True))
                ppt_certs = Ppt.objects.filter(Q(has_Certificate=True))
                boom_certs = Boom.objects.filter(Q(has_Certificate=True))
                pivot_certs = Pivot.objects.filter(Q(has_Certificate=True))
                three_certs = Threesixty.objects.filter(Q(has_Certificate=True))
                shovel_certs = Shovel.objects.filter(Q(has_Certificate=True))
                query = list(chain(shovel_certs, three_certs, cbr_certs, mewp_certs, ohc_certs, aw_certs, ppt_certs, boom_certs, pivot_certs))
                form_certs = Forms.objects.filter(Q(certificate=False))
                create_certificates = list()
                for form in query:
                    for x in form_certs:
                        if x.content_type_id==ContentType.objects.get(model=form).id and x.object_id==form.id and x.certificate == False:
                            create_certificates.append(x)

                return render(request, 'index.html', {'forms': forms, 'create_certificates': create_certificates, 'query': query, 'self_forms': self_forms})
            else:
                cbr_ids = Cbr.objects.filter(Q(instructor=user.id),Q(completed=False))
                mewp_ids = Mewp.objects.filter(Q(instructor=user.id),Q(completed=False))
                ohc_ids = Ohc.objects.filter(Q(instructor=user.id),Q(completed=False))
                aw_ids = Aw.objects.filter(Q(instructor=user.id),Q(completed=False))
                ppt_ids = Ppt.objects.filter(Q(instructor=user.id),Q(completed=False))
                boom_ids = Boom.objects.filter(Q(instructor=user.id),Q(completed=False))
                pivot_ids = Pivot.objects.filter(Q(instructor=user.id),Q(completed=False))
                threesixty_ids = Threesixty.objects.filter(Q(instructor=user.id),Q(completed=False))
                shovel_ids = Shovel.objects.filter(Q(instructor=user.id),Q(completed=False))
                self_forms = chain(shovel_ids, threesixty_ids, cbr_ids, mewp_ids, ohc_ids, aw_ids, ppt_ids, boom_ids, pivot_ids)
                return render(request, 'index.html', {'self_forms': self_forms})
        else:
            return redirect('login')
