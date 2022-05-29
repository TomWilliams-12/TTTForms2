import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from .forms import PivotForm
from .models import Pivot
from forms.models import Forms

test = {
    '1': {'num': '101', 't': True, 'crit': 'Operator Safety & Observation', 'pen': '0'},
    '2': {'num': '1', 't': False, 'crit': 'Mounts/dismounts incorrectly', 'pen': '3'},
    '3': {'num': '2', 't': False, 'crit': 'Limb/body outside confines of truck', 'pen': '5'},
    '4': {'num': '3', 't': False, 'crit': 'Fails to make all around checks', 'pen': '3'},
    '5': {'num': '4', 't': False, 'crit': 'Fails to look in direction of travel', 'pen': '5'},
    '6': {'num': '5', 't': False, 'crit': 'Fails to use appropriate safety devices', 'pen': '5'},
    '7': {'num': '102', 't': True, 'crit': 'Steering & Operating Controls', 'pen': '0'},
    '8': {'num': '6', 't': False, 'crit': 'Travels in wrong direction', 'pen': '5'},
    '9': {'num': '7', 't': False, 'crit': 'Brakes harshly/erratically', 'pen': '3'},
    '10': {'num': '8', 't': False, 'crit': 'Fails to release parking brake', 'pen': '1'},
    '11': {'num': '9', 't': False, 'crit': 'Rides foot brake', 'pen': '1'},
    '12': {'num': '10', 't': False, 'crit': 'Operates Hydraulic controls when moving', 'pen': '5'},
    '13': {'num': '11', 't': False, 'crit': 'Selects wrong hydraulic control', 'pen': '3'},
    '14': {'num': '12', 't': False, 'crit': 'Excessive use of hydraulic controls', 'pen': '1*'},
    '15': {'num': '13', 't': False, 'crit': 'Rough use of hydraulic controls', 'pen': '3'},
    '16': {'num': '14', 't': False, 'crit': 'Fails to hold steering wheel/assistor', 'pen': '5'},
    '17': {'num': '103', 't': True, 'crit': 'Manoeuvring & Transporting', 'pen': '0'},
    '18': {'num': '15', 't': False, 'crit': 'Fork arms/load too high when travelling', 'pen': '5**'},
    '19': {'num': '16', 't': False, 'crit': 'Fork arms/load too low when travelling', 'pen': '3**'},
    '20': {'num': '17', 't': False, 'crit': 'Incorrect tile when travelling', 'pen': '3'},
    '21': {'num': '18', 't': False, 'crit': 'Touches course/racking/load', 'pen': '3'},
    '22': {'num': '19', 't': False, 'crit': 'Shunts in chicane', 'pen': '1'},
}
test2 = {
    '1': {'num': '201', 't': True, 'crit': 'Stacking/De-Stacking', 'pen': '0'},
    '2': {'num': '20', 't': False, 'crit': 'Incorrect set down at vertical face', 'pen': '1'},
    '3': {'num': '21', 't': False, 'crit': 'Shunts when stacking/de-stacking', 'pen': '1*'},
    '4': {'num': '22', 't': False, 'crit': 'Fails to apply parking brake/neutral', 'pen': '5'},
    '5': {'num': '23', 't': False, 'crit': 'Fork arms not central under load', 'pen': '3**'},
    '6': {'num': '24', 't': False, 'crit': 'Fork arms rubbing(entry/withdrawal)', 'pen': '3**'},
    '7': {'num': '25', 't': False, 'crit': 'Fork arms not fully inserted', 'pen': '5**'},
    '8': {'num': '26', 't': False, 'crit': 'Mast base touches stack/load', 'pen': '3'},
    '9': {'num': '27', 't': False, 'crit': 'Fork tips touch stack/load', 'pen': '3**'},
    '10': {'num': '28', 't': False, 'crit': 'Load/Fork arms not level', 'pen': '3**'},
    '11': {'num': '29', 't': False, 'crit': 'Load incorrectly stacked', 'pen': '3'},
    '12': {'num': '202', 't': True, 'crit': 'Parking', 'pen': '0'},
    '13': {'num': '30', 't': False, 'crit': 'Fails to apply parking brake', 'pen': '5'},
    '14': {'num': '31', 't': False, 'crit': 'Fails to apply tilt forward', 'pen': '3'},
    '15': {'num': '32', 't': False, 'crit': 'Fails to lower fork arms', 'pen': '3**'},
    '16': {'num': '33', 't': False, 'crit': 'Fails to switch off/remove key', 'pen': '3'},
    '17': {'num': '34', 't': False, 'crit': 'Wheels not straight', 'pen': '1'},
    '18': {'num': '203', 't': True, 'crit': 'Pivot-steer Truck Features Only', 'pen': '0'},
    '19': {'num': '35', 't': False, 'crit': 'Applies brake when pivoting', 'pen': '3'},
    '20': {'num': '36', 't': False, 'crit': 'Failes to straighten before lowering', 'pen': '5'},
    '21': {'num': '37', 't': False, 'crit': 'Fails to centralise side shift', 'pen': '3'},
    '22': {'num': '38', 't': False, 'crit': 'Truck incorrectly positioned when stacking/de-stacking', 'pen': '5'},
}
carry_forward = 18
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
    'Incomplete pre-use/function check',
    'Unsafe operator practices',
    'Operates dangerously',
    'Violent collision',
    'Fails to use stabilisers correctly',
    'Fails to complete lifting criteria',
    'Failts theoretical test (see separate marking/test sheet)'
]
checks = [
    'Fork arms',
    'Carriage plate',
    'Backrest extension',
    'Mast',
    'Mast rollers/sliders',
    'List chains',
    'Chain pulleys',
    'Hydarulics',
    'Wheels',
    'Tyres',
    'External condition',
    'Operating position',
    'Gas trucks',
    'Starting procedures - Engine trucks',
    'Starting procedures - Electric trucks',
    'Lights',
    'Audible warnings',
    'Hydraulic controls',
    'Drive & braking',
    'Steering',
    'Fault reporting procedure',
    ]
operator_training = {
    '1': {'num': '1', 'crit': 'Course induction', 'ref': 'N/E/SR'},
    '2': {'num': '2', 'crit': 'The need and reasons to training & statutory requirements (HASAWA 1974 etc.)', 'ref': 'N/E/SR'},
    '3': {'num': '3', 'crit': 'Introduction to equipment/control familiarisation/principles of operation', 'ref': 'N/E/SR'},
    '4': {'num': '4', 'crit': 'Identification/use/adjustment of attachments in pre-determined positions including forks', 'ref': 'N/E'},
    '5': {'num': '5', 'crit': 'Recommended mount and dismounts', 'ref': 'N/E/SR'},
    '6': {'num': '6', 'crit': 'Introduction to motive, steering controls & practice', 'ref': 'N'},
    '7': {'num': '7', 'crit': 'Basic steering exercises - simple courses', 'ref': 'N'},
    '8': {'num': '8', 'crit': 'Advanced steering exercises - figure of 8/chicane/90\N{DEGREE SIGN} approaches', 'ref': 'N/E'},
    '9': {'num': '9', 'crit': 'Battery changing procedures/maintenance', 'ref': 'N/E/SR'},
    '10': {'num': '10', 'crit': 'Operator safety code and relevant handout', 'ref': 'N/E/SR'},
    '11': {'num': '11', 'crit': 'Daily pre-use inspections/refueling procedures', 'ref': 'N/E/SR'},
    '12': {'num': '12', 'crit': 'Engineering principles/rated capacity/stability', 'ref': 'N/E/SR'},
    '13': {'num': '13', 'crit': 'Simple hydraulics (theory) Introduction to hydraulic controls, handling empty pallets at low level', 'ref': 'N'},
    '14': {'num': '14', 'crit': 'Load types/handling and weight assessment', 'ref': 'N'},
    '15': {'num': '15', 'crit': 'Stacking/de-stacking at low; eye & high level on industrial racking', 'ref': 'N/E/SR'},
    '16': {'num': '16', 'crit': 'Stacking/de-stacking at low; eye & high level on bulk stacks', 'ref': 'N/E/SR'},
    '17': {'num': '17', 'crit': 'Stacking/de-stacking at low; eye & high level on cup post pallets', 'ref': 'N/E/SR'},
    '18': {'num': '18', 'crit': 'Maneuvering with loads/ramps & inclines/handling awkawrd loads', 'ref': 'N/E'},
    '19': {'num': '19', 'crit': 'Relevant safety film', 'ref': 'N/E/SR'},
    '20': {'num': '20', 'crit': 'Vehicle loading and unloading (Theory)', 'ref': 'N/E'},
    '21': {'num': '21', 'crit': 'Vehicle loading and unloading (Practical)', 'ref': 'N/E'},
    '22': {'num': '22', 'crit': 'Multi choice theory test', 'ref': 'N/E/SR'},
    '23': {'num': '23', 'crit': 'Pre-use inspection test', 'ref': 'N/E/SR'},
    '24': {'num': '24', 'crit': 'Practical skills test', 'ref': 'N/E/SR'},
}
class PivotPage(View):
    def get(self, request):
        instructor = request.user
        form = PivotForm(initial={'start_Date': datetime.datetime.today(), 'instructor': instructor})
        return render(request, 'pivot_steer.html', {
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
        form = PivotForm(request.POST)
        print (form.errors)
        if form.is_valid():
            form.save()
            last_form = Pivot.objects.last()
            form = Forms(form_type=last_form)
            form.save()
            return redirect('/')


class EditPivot(UpdateView):
    model = Pivot
    form_class = PivotForm
    template_name = 'pivot_steer.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        ctx = super(EditPivot, self).get_context_data(**kwargs)
        form = PivotForm(instance=self.object)
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
