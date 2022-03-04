import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from .forms import PptForm
from .models import Ppt
from forms.models import Forms

test = {
    '1': {'num': '101', 't': True, 'crit': 'Operator Safety & Observation', 'pen': '0'},
    '2': {'num': '1', 't': False, 'crit': 'Mounts/dismounts incorrectly', 'pen': '3'},
    '3': {'num': '2', 't': False, 'crit': 'Limb/body outside confines of truck', 'pen': '5'},
    '4': {'num': '3', 't': False, 'crit': 'Fails to check all round', 'pen': '5'},
    '5': {'num': '4', 't': False, 'crit': 'Fails to look in direction of travel', 'pen': '5'},
    '6': {'num': '5', 't': False, 'crit': 'Fails to use appropriate Safety devices', 'pen': '5'},
    '7': {'num': '102', 't': True, 'crit': 'Steering & Operating Controls', 'pen': '0'},
    '8': {'num': '6', 't': False, 'crit': 'Travels in wrong direction', 'pen': '5'},
    '9': {'num': '7', 't': False, 'crit': 'Brakes harshly/erratically', 'pen': '3'},
    '10': {'num': '8', 't': False, 'crit': 'Fails to release parking brake', 'pen': '1'},
    '11': {'num': '9', 't': False, 'crit': 'Operates hydraulic controls when moving', 'pen': '5'},
    '12': {'num': '10', 't': False, 'crit': 'Selects wrong hydraulic controls when moving', 'pen': '3'},
    '13': {'num': '11', 't': False, 'crit': 'Excessive use of hydraulic controls', 'pen': '1*'},
    '14': {'num': '12', 't': False, 'crit': 'Rough use of hydraulic controls', 'pen': '3'},
    '15': {'num': '13', 't': False, 'crit': 'Fails to hold steering control/tiller when moving', 'pen': '5'},
    '16': {'num': '103', 't': True, 'crit': 'Manoeuvring & Transporting', 'pen': '0'},
    '17': {'num': '14', 't': False, 'crit': 'Forks/load too high (travelling)', 'pen': '5**'},
    '18': {'num': '15', 't': False, 'crit': 'Forks/load too low (travelling)', 'pen': '5**'},
    '19': {'num': '16', 't': False, 'crit': 'Touches course/racking/load', 'pen': '5'},
    '20': {'num': '17', 't': False, 'crit': 'Shunts in chicane', 'pen': '3'},
    '21': {'num': '18', 't': False, 'crit': 'Incorrect personal positioning', 'pen': '5'},
    '22': {'num': '19', 't': False, 'crit': 'Fails to use fold down platform', 'pen': '3'},
    '23': {'num': '20', 't': False, 'crit': 'Fails to dismount from fold down platform', 'pen': '3'},
}
test2 = {
    '1': {'num': '201', 't': True, 'crit': 'Stacking / De-stacking', 'pen': '0'},
    '2': {'num': '21', 't': False, 'crit': 'Incorrect set down at vertical face', 'pen': '1'},
    '3': {'num': '22', 't': False, 'crit': 'Shunts when stacking/destacking', 'pen': '3*'},
    '4': {'num': '23', 't': False, 'crit': 'Fails to secure truck', 'pen': '5'},
    '5': {'num': '24', 't': False, 'crit': 'Fork arms not central under load', 'pen': '3**'},
    '6': {'num': '25', 't': False, 'crit': 'Fork arms rubbing(entry/withdrawal)', 'pen': '3**'},
    '7': {'num': '26', 't': False, 'crit': 'Fork arms not fully inserted', 'pen': '5**'},
    '8': {'num': '27', 't': False, 'crit': 'Fork tips touch stack/load', 'pen': '3**'},
    '9': {'num': '28', 't': False, 'crit': 'Load incorrectly positioned', 'pen': '3'},
    '10': {'num': '29', 't': False, 'crit': 'Wheels/tiller not straight', 'pen': '3'},
    '11': {'num': '30', 't': False, 'crit': 'Fails to lower fork arms', 'pen': '3**'},
    '12': {'num': '202', 't': True, 'crit': 'Parking', 'pen': '0'},
    '13': {'num': '31', 't': False, 'crit': 'Fails to switch off/remove key', 'pen': '3'},
    '14': {'num': '32', 't': False, 'crit': 'Wheels / tiller arm not straight', 'pen': '3'},
}
carry_forward = 20
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
    'Exceeds 3 occurrences of any one 5-point fault',
    'Unsafe stacking',
    'Exceeds maximum time',
    'Violent collision',
    'Dismounts unnecessarily',
    'Operates dangerously',
    'Fails theoretical test (see separate marking/test sheet)'
]
checks = [
    'Fork arms (MC)',
    'Carriage-plate (MC)',
    'Backrest extension',
    'Mast (MC)',
    'Mat rollers/slides (MC)',
    'Lift chains (MC)',
    'Chain Pulleys (MC)',
    'Hydraulic systems (MC)',
    'Wheels (MC)',
    'Tyres (MC)',
    'External condition',
    'Rated capacity plate (MC)',
    'Operating position',
    'Fold down platform',
    'Operators seat',
    'Starting procedure - Electric Trucks',
    'Starting procedure - Engine Trucks',
    'Repel pad (MC)',
    'Lights',
    'Audible warnings',
    'Hydraulic controls (MC)',
    'Drive & Braking (MC)',
    'Steering (MC)',
    'Fault reporting procedure',
    ]
operator_training = {
    '1': {'num': '1', 'crit': 'Course induction', 'ref': 'N/E/SR/C'},
    '2': {'num': '2', 'crit': 'The need and reasons to training & statutory requirements (HASAWA 1974 etc.)', 'ref': 'N/E/SR/C'},
    '3': {'num': '3', 'crit': 'Introduction to equipment/control familiarisation/principles of operation', 'ref': 'N/E/SR/C'},
    '4': {'num': '4', 'crit': 'Manual Handling Techniques', 'ref': 'N/E/SR/C'},
    '5': {'num': '5', 'crit': 'Identification/use/adjustment of attachments in pre-determined positions including forks', 'ref': 'N/E/C'},
    '6': {'num': '6', 'crit': 'Recommended mount and dismount', 'ref': 'N/E/SR/C'},
    '7': {'num': '7', 'crit': 'Introduction to motive, steering controls and practice', 'ref': 'N'},
    '8': {'num': '8', 'crit': 'Basic steering exercises - simple courses', 'ref': 'N'},
    '9': {'num': '9', 'crit': 'Advanced steering exercises - figure of 8/chicane/90\N{DEGREE SIGN} approaches/reverse orientation', 'ref': 'N/E/C'},
    '10': {'num': '10', 'crit': 'Battery charging procedures/maintenance', 'ref': 'N/E/SR/C'},
    '11': {'num': '11', 'crit': 'Operator safety code and relevant handout', 'ref': 'N/E/SR/C'},
    '12': {'num': '12', 'crit': 'Daily pre-use inspections/refueling procedures', 'ref': 'N/E/SR/C'},
    '13': {'num': '13', 'crit': 'Engineering principles/rated capacity/stability', 'ref': 'N/E/SR/C'},
    '14': {'num': '14', 'crit': 'Simple hydraulics (theory) Introduction to hydraulic controls, handling empty pallets low level', 'ref': 'N'},
    '15': {'num': '15', 'crit': 'Load types/handling and weight assessment', 'ref': 'N'},
    '16': {'num': '16', 'crit': 'Stacking/de-stacking at low; eye and high level on industrial racking*', 'ref': 'N/E/SR/C'},
    '17': {'num': '17', 'crit': 'Stacking/de-stacking at low; eye and high level bulk stacks*', 'ref': 'N/E/SR/C'},
    '18': {'num': '18', 'crit': 'Stacking/de-stacking at low; eye and high level cup post pallets*', 'ref': 'N/E/SR/C'},
    '19': {'num': '19', 'crit': 'Manoeuvring with/handling awkward loads*', 'ref': 'N/E/C'},
    '20': {'num': '20', 'crit': 'Relevant safety film', 'ref': 'N/E/SR/C'},
    '21': {'num': '21', 'crit': 'Vehicle loading and unloading (theory)*', 'ref': 'N/E/C'},
    '22': {'num': '22', 'crit': 'Vehicle loading and unloading(practical)*', 'ref': 'N/E/SR/C'},
    '23': {'num': '23', 'crit': 'Multi choice theory test', 'ref': 'N/E/SR/C'},
    '24': {'num': '24', 'crit': 'Pre-use inspection test', 'ref': 'N/E/SR/C'},
    '25': {'num': '25', 'crit': 'Practical skills test', 'ref': 'N/E/SR/C'},
}
disclaimers = [
    '* Allow 1 adjustment per operation',
    '** The phrase "forks" includes attachments if applicable',
]
class PptPage(View):
    def get(self, request):
        instructor = request.user
        form = PptForm(initial={'start_Date': datetime.datetime.today(), 'instructor': instructor})
        return render(request, 'ppt.html', {
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
            'disclaimers': disclaimers,
            })
    
    def post(self, request):
        pptForm = PptForm(request.POST)
        print (pptForm.errors)
        if pptForm.is_valid():
            pptForm.save()
            last_form = Ppt.objects.last()
            form = Forms(form_type=last_form)
            form.save()
            return redirect('/')


class EditPpt(UpdateView):
    model = Ppt
    form_class = PptForm
    template_name = 'ppt.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        ctx = super(EditPpt, self).get_context_data(**kwargs)
        form = PptForm(instance=self.object)
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
            'disclaimers': disclaimers,
        }
        return ctx
