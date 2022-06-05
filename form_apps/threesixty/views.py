import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from .forms import ThreeSixtyForm
from .models import Threesixty
from forms.models import Forms

test = {
    '1': {'num': '101', 't': True, 'crit': 'Operator Safety & Observation', 'pen': '0'},
    '2': {'num': '1', 't': False, 'crit': 'Mounts/dismounts incorrectly', 'pen': '3'},
    '3': {'num': '2', 't': False, 'crit': 'Limb(s) outside confines of cab', 'pen': '5'},
    '4': {'num': '3', 't': False, 'crit': 'Fails to make all around checks', 'pen': '3'},
    '5': {'num': '4', 't': False, 'crit': 'Fails to look in direction of travel', 'pen': '5'},
    '6': {'num': '5', 't': False, 'crit': 'Fails to use appropriate safety devices', 'pen': '5'},
    '7': {'num': '6', 't': False, 'crit': 'Fails to wear safety equipment', 'pen': '1'},
    '8': {'num': '7', 't': False, 'crit': 'Fails to make vehicle safe on approach of instructor', 'pen': '3'},
    '9': {'num': '102', 't': True, 'crit': 'Manoeuvring & Operating Controls', 'pen': '0'},
    '10': {'num': '8', 't': False, 'crit': 'Failes to release parking brake(w/a)', 'pen': '1'},
    '11': {'num': '9', 't': False, 'crit': 'Fails to lift blade/stabilisers(w/a)', 'pen': '1'},
    '12': {'num': '10', 't': False, 'crit': 'Activates wrong direction control', 'pen': '5'},
    '13': {'num': '11', 't': False, 'crit': 'Operates erratically', 'pen': '5'},
    '14': {'num': '12', 't': False, 'crit': 'Incorrect travel mode selected', 'pen': '3'},
    '15': {'num': '13', 't': False, 'crit': 'Cab "drifts" during travel', 'pen': '3'},
    '16': {'num': '14', 't': False, 'crit': 'Selects wrong hydraulic control', 'pen': '5'},
    '17': {'num': '15', 't': False, 'crit': 'Rough use of hydraulic controls', 'pen': '3'},
    '18': {'num': '16', 't': False, 'crit': 'Fails to hold steering assistor(w/a)', 'pen': '5'},
    '19': {'num': '17', 't': False, 'crit': 'Travels with bucket raised too high', 'pen': '5'},
    '20': {'num': '18', 't': False, 'crit': 'Travels with bucket too low', 'pen': '1'},
    '21': {'num': '19', 't': False, 'crit': 'Travels with bucket extended', 'pen': '5'},
    '22': {'num': '20', 't': False, 'crit': 'Touches course', 'pen': '3'},
    '23': {'num': '21', 't': False, 'crit': 'Shunts in chicane', 'pen': '1'},
    '24': {'num': '103', 't': True, 'crit': 'Excavation & Re-instatement', 'pen': '0'},
    '25': {'num': '22', 't': False, 'crit': 'Machine incorrectly positioned', 'pen': '5'},
    '26': {'num': '23', 't': False, 'crit': 'Fails to apply stabilisers/blade axle lock', 'pen': '3'},
}
test2 = {
    '1': {'num': '24', 't': False, 'crit': 'Fails to extract layers', 'pen': '1'},
    '2': {'num': '25', 't': False, 'crit': 'Incorrect placement of spiol', 'pen': '3'},
    '3': {'num': '26', 't': False, 'crit': 'Edges/trench bottom left untidy', 'pen': '1'},
    '4': {'num': '27', 't': False, 'crit': 'Incorrect levels (+/- 50mm)', 'pen': '1'},
    '5': {'num': '28', 't': False, 'crit': 'Incorrect line', 'pen': '3'},
    '6': {'num': '29', 't': False, 'crit': 'Excessive material spilage', 'pen': '3'},
    '7': {'num': '30', 't': False, 'crit': 'Excessive side-swipe', 'pen': '1'},
    '8': {'num': '31', 't': False, 'crit': 'Material not compacted in laters', 'pen': '1'},
    '9': {'num': '32', 't': False, 'crit': 'Incorrect use of grading blade', 'pen': '1'},
    '10': {'num': '202', 't': True, 'crit': 'Working on stockpiles/loading', 'pen': '0'},
    '11': {'num': '33', 't': False, 'crit': 'Incorrect travel on inclines', 'pen': '5'},
    '12': {'num': '34', 't': False, 'crit': 'Incorrect setting up at the face', 'pen': '5'},
    '13': {'num': '35', 't': False, 'crit': 'Fails to load vehicle/hopper centrally', 'pen': '3'},
    '14': {'num': '36', 't': False, 'crit': 'Makes contact with vehicle/hopper', 'pen': '3'},
    '15': {'num': '37', 't': False, 'crit': 'Fails to erect safety bund', 'pen': '5'},
    '16': {'num': '203', 't': True, 'crit': 'Un-loading and loading onto transporter (w/a)', 'pen': '0'},
    '17': {'num': '38', 't': False, 'crit': 'Fails to check transporter for security', 'pen': '5'},
    '18': {'num': '39', 't': False, 'crit': 'Fails to deploy ramps correctly', 'pen': '5'},
    '19': {'num': '40', 't': False, 'crit': 'Loses traction on loading/unloading', 'pen': '3'},
    '20': {'num': '41', 't': False, 'crit': 'Incorrect configuration of machine', 'pen': '5'},
    '21': {'num': '42', 't': False, 'crit': 'Machine incorrectly positioned', 'pen': '3'},
    '22': {'num': '203', 't': True, 'crit': 'Parking and Shut Down', 'pen': '0'},
    '23': {'num': '43', 't': False, 'crit': 'Fails to lower hydraulics', 'pen': '3'},
    '24': {'num': '44', 't': False, 'crit': 'Fails to apply parking brake/neutral', 'pen': '5'},
    '25': {'num': '45', 't': False, 'crit': 'Fails to switch off and remove key', 'pen': '3'},
    '26': {'num': '46', 't': False, 'crit': 'Fails to complete post-stop checks', 'pen': '3'},
}
carry_forward = 23
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
    'Operates dangerously',
    'Exceeds maximum time',
    'Violent collision',
    'Dismounts unnecessarily',
    'Incorrect detachment/re-attachment of the bucket',
    'Failts theoretical test (see separate marking/test sheet)'
]
checks = [
    'Walk-round inspection',
    'Tracks/running gear',
    'Wheels/tyres (w/a)',
    'Hydraulic systems',
    'Engine compartment including oil level',
    'Coolant',
    'Swing pump reservoir',
    'Fuel level',
    'Battery',
    'Boom/dipper',
    'Bucket',
    'Roll over protection structure(ROPS)',
    'Falling objects protection(FOPS)',
    'Steps and handrails',
    'Seat',
    'Seat belt',
    'Electrical system',
    'Lights',
    'Reverse warning system (w/a)',
    'Rear view monitor (w/a)',
    'Mirrors',
    'Gauges',
    'Horn',
    'Beacon',
    'Lever isolation system',
    'Park-brake test (w/a)',
    'Steering and braking',
    'Greasing',
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
class ThreeSixtyPage(View):
    def get(self, request):
        instructor = request.user
        form = ThreeSixtyForm(initial={'start_Date': datetime.datetime.today(), 'instructor': instructor})
        return render(request, 'threesixty.html', {
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
        form = ThreeSixtyForm(request.POST)
        print (form.errors)
        if form.is_valid():
            form.save()
            last_form = Threesixty.objects.last()
            form = Forms(form_type=last_form)
            form.save()
            return redirect('/')


class EditThreeSixty(UpdateView):
    model = Threesixty
    form_class = ThreeSixtyForm
    template_name = 'threesixty.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        ctx = super(EditThreeSixty, self).get_context_data(**kwargs)
        form = ThreeSixtyForm(instance=self.object)
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
