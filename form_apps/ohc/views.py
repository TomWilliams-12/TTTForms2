import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from .forms import OhcForm
from .models import Ohc
from forms.models import Forms

test = {
    '1': {'num': '101', 't': True, 'crit': 'Operator Safety', 'pen': '0'},
    '2': {'num': '1', 't': False, 'crit': 'Handles controls incorrectly', 'pen': '5'},
    '3': {'num': '2', 't': False, 'crit': 'Fails to wear safety equipment', 'pen': '5'},
    '4': {'num': '3', 't': False, 'crit': 'Encroaches inside danger area', 'pen': '3'},
    '5': {'num': '4', 't': False, 'crit': 'Fails to use safety devices', 'pen': '5'},
    '6': {'num': '102', 't': True, 'crit': 'Operational Safety', 'pen': '0'},
    '7': {'num': '5', 't': False, 'crit': 'Fails to check for hazards', 'pen': '5'},
    '8': {'num': '6', 't': False, 'crit': 'Fails to cordon off area*', 'pen': '3'},
    '9': {'num': '7', 't': False, 'crit': 'Fails to check safe load indicator*', 'pen': '5'},
    '10': {'num': '8', 't': False, 'crit': 'Fails to energise system', 'pen': '3'},
    '11': {'num': '9', 't': False, 'crit': 'Fails to use corerct lifting equipment', 'pen': '5'},
    '12': {'num': '10', 't': False, 'crit': 'Fails to use tag line*', 'pen': '3'},
    '13': {'num': '11', 't': False, 'crit': 'Fails to conduct a test lift', 'pen': '5'},
    '14': {'num': '103', 't': True, 'crit': 'Observation', 'pen': '0'},
    '15': {'num': '12', 't': False, 'crit': 'Fails to look in direction of crane travel', 'pen': '5'},
    '16': {'num': '13', 't': False, 'crit': 'Fails to make all round check', 'pen': '3'},
}
test2 = {
    '1': {'num': '201', 't': True, 'crit': 'Lifting Operations', 'pen': '0'},
    '2': {'num': '14', 't': False, 'crit': 'Selects wrong control', 'pen': '3'},
    '3': {'num': '15', 't': False, 'crit': ' Rough use of controls', 'pen': '3'},
    '4': {'num': '16', 't': False, 'crit': 'Allows load to swing', 'pen': '5'},
    '5': {'num': '17', 't': False, 'crit': 'Shocks load/lifting gear', 'pen': '3'},
    '6': {'num': '18', 't': False, 'crit': 'Unnecessary use of controls', 'pen': '1'},
    '7': {'num': '19', 't': False, 'crit': 'Activates overload warning*', 'pen': '5'},
    '8': {'num': '20', 't': False, 'crit': 'Load touches course', 'pen': '3'},
    '9': {'num': '21', 't': False, 'crit': 'Fails to prepare landing area', 'pen': '3'},
    '10': {'num': '22', 't': False, 'crit': 'Position load incorrectly ', 'pen': '3'},
    '11': {'num': '23', 't': False, 'crit': 'Fails to follow signal', 'pen': '5'},
    '12': {'num': '24', 't': False, 'crit': 'Violent positioning of load', 'pen': '3'},
    '13': {'num': '202', 't': True, 'crit': 'Closing Down', 'pen': '0'},
    '14': {'num': '25', 't': False, 'crit': 'Fails to stow and check lifting equipment correctly', 'pen': '5'},
    '15': {'num': '26', 't': False, 'crit': 'Fails to secure attachment', 'pen': '5'},
    '16': {'num': '27', 't': False, 'crit': 'Fails to stow crane correctly', 'pen': '5'},
    '17': {'num': '202', 't': True, 'crit': 'Parking the Crane', 'pen': '0'},
    '18': {'num': '28', 't': False, 'crit': 'Fails to apply brake*', 'pen': '5'},
    '19': {'num': '29', 't': False, 'crit': 'Fails to remove key/isolate crane', 'pen': '5'},
}
carry_forward = 13
review_choices = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)
eval = [
    'Did you feel you had professional training?',
    'Did you feel the trainer had adequate enthusiasm?',
    'Did the trainer effectively communicate with you?',
    'Did you have the oppurtunity to ask questions?',
    'Was the course well structured?',
    'Did you find the course content easy to understand?',
    'Was there adequate balance between theory and practical?',
    'Was the course manual easy to read and informative?',
    'Were you satisfied with the facilities provided to you?',
]
operatorContent = {
    'Job Safety/Knowledge': 'JS',
    'Skill and Dexterity': 'SD',
    'Learning Capacity': 'LC',
    'Motivation': 'M',
    'Safety Attitude': 'SA'
}
md = [
    'Does not complete pre-use check',
    'Unsafe lifting/lowering/manoeuvring',
    'Exceeds maximum time',
    'Violent collision',
    'Exceeds safe working load',
    'Fails load over pedestrian',
    'Disregards personal safety',
    'Fails theoretical test (see separate marking/test sheet)'
]
checks = [
    'Isolator Switch',
    'Power supply cables', 
    'Emergency stop', 
    'Hoist motor & drum', 
    'Cross travel motor & driveshaft', 
    'Tracks', 
    'Hoist limit switch', 
    'Long travel motor(s)', 
    'Hoistrope(s)', 
    'Audible warning device', 
    'All controllers & crane motions', 
    'Travel limit switches', 
    'Swivel Hook & block', 
    'System operation lights', 
    'Fire extinguisher (if fitted)', 
    'Crane test certificates', 
    'Lifting accessories/lifting gear', 
    'Fault Reporting Procedure', 
    ]
operator_training = {
    '1': {'num': '1', 'crit': 'Course induction', 'ref': 'N/E/SR'},
    '2': {'num': '2', 'crit': 'The need and reasons to training & statutory requirements (HASAWA 1974 etc.)', 'ref': 'N/E/SR'},
    '3': {'num': '3', 'crit': 'Crane components', 'ref': 'N/E/SR'},
    '4': {'num': '4', 'crit': 'Types of lifting accessories', 'ref': 'N/E'},
    '5': {'num': '5', 'crit': 'Safe use of slings, shackles and eyebolts', 'ref': 'N/E/SR'},
    '6': {'num': '6', 'crit': 'Rating and derating factors', 'ref': 'N'},
    '7': {'num': '7', 'crit': 'Banksman signals', 'ref': 'N'},
    '8': {'num': '8', 'crit': 'General safety rules', 'ref': 'N/E'},
    '9': {'num': '9', 'crit': 'Pre-operational checks', 'ref': 'N/E/SR'},
    '10': {'num': '10', 'crit': 'Control Familiarisation', 'ref': 'N/E/SR'},
    '11': {'num': '11', 'crit': 'Correcting swing', 'ref': 'N/E/SR'},
    '12': {'num': '12', 'crit': 'Spotting the hook on a bolt', 'ref': 'N/E/SR'},
    '13': {'num': '13', 'crit': 'Lifting and Manoeuvring a basic load', 'ref': 'N'},
    '14': {'num': '14', 'crit': 'Lifting and Manoeuvring in an enclosed area', 'ref': 'N'},
    '15': {'num': '15', 'crit': 'Turning a load with 2 hooks', 'ref': 'N/E/SR'},
    '16': {'num': '16', 'crit': 'Turning a load with a single hook', 'ref': 'N/E/SR'},
    '17': {'num': '17', 'crit': 'Working to signals', 'ref': 'N/E/SR'},
    '18': {'num': '18', 'crit': 'Parking the crane', 'ref': 'N/E'},
    '19': {'num': '19', 'crit': 'Pre-use check test', 'ref': 'N/E/SR'},
    '20': {'num': '20', 'crit': 'Multi choice teory test', 'ref': 'N/E'},
    '21': {'num': '21', 'crit': 'Practical Test', 'ref': 'N/E'},
}
class OhcPage(View):
    def get(self, request):
        instructor = request.user
        form = OhcForm(initial={'start_Date': datetime.datetime.today(), 'instructor': instructor})
        return render(request, 'ohc.html', {
            'form': form,
            'operatorContent': operatorContent,
            'test': test,
            'test2': test2,
            'carry_forward': carry_forward,
            'md': md,
            'checks': checks,
            'eval': eval,
            'instructor': instructor,
            'operator_training': operator_training,
            })
    
    def post(self, request):
        ohcForm = OhcForm(request.POST)
        print (ohcForm.errors)
        if ohcForm.is_valid():
            ohcForm.save()
            last_form = Ohc.objects.last()
            form = Forms(form_type=last_form)
            form.save()
            return redirect('/')


class EditOhc(UpdateView):
    model = Ohc
    form_class = OhcForm
    template_name = 'ohc.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        ctx = super(EditOhc, self).get_context_data(**kwargs)
        form = OhcForm(instance=self.object)
        instructor = self.object.instructor
        instructor_2 = self.object.instructor_2
        ctx = {
            'form': form,
            'operatorContent': operatorContent,
            'test': test,
            'test2': test2,
            'carry_forward': carry_forward,
            'md': md,
            'checks': checks,
            'eval': eval,
            'instructor': instructor,
            'instructor_2': instructor_2,
            'operator_training': operator_training,
        }
        return ctx
