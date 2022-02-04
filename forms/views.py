from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from forms.models import Forms
import datetime
from django.views.generic.list import ListView
from accounts.models import Profile
from forms.utils import render_to_pdf 

class CreateCertificate(View):
    def post(self, request):
        form_id = request.POST.get('form_id')
        form = Forms.objects.get(id=form_id)
        form.certificate = True
        year = datetime.datetime.now()
        cert_number = 'TTT/' + str(year.year) + '/' + str(form.id).zfill(4)
        form.certificateNumber = cert_number
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CertificateListView(ListView):
    model = Forms
    template_name = 'certificate_list.html'
    paginate_by = 100
    def get_queryset(self):
        form = Forms.objects.filter(certificate=True)
        return form


class Certificate(View):
    def get(self, request, pk):
        certificate = Forms.objects.get(pk=pk)
        startDate = certificate.form_type.start_Date
        endDate = certificate.form_type.finish_Date
        george = Profile.objects.get(user_name='george')
        diff = endDate - startDate
        duration = diff.days + 1
        if duration == 0:
            duration = 1
        return render(request, 'certificate.html', {'certificate': certificate, 'george': george, 'duration': duration })

class PDFCertificate(View):
    def get(self, request, pk):
        certificate = Forms.objects.get(pk=pk)
        startDate = certificate.form_type.start_Date
        endDate = certificate.form_type.finish_Date
        george = Profile.objects.get(user_name='george')
        diff = endDate - startDate
        duration = diff.days + 1
        if duration == 0:
            duration = 1
        context = {
            'certificate': certificate, 
            'george': george,
            'duration': duration,
        }
        pdf = render_to_pdf('pdf_certificate.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
