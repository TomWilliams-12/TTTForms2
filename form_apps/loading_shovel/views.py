import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from .forms import ShovelForm
from .models import Shovel
from forms.models import Forms

test = {
    '1': {'num': '101', 't': True, 'crit': 'General Safety', 'pen': '0'},
    '2': {'num': '1', 't': False, 'crit': 'Fails to carry out pre shift check', 'pen': '5'},
    '3': {'num': '102', 't': True, 'crit': 'Operator Safety', 'pen': '0'},
    '4': {'num': '2', 't': False, 'crit': 'Mounts/dismounts incorrectly', 'pen': '3'},
    '5': {'num': '3', 't': False, 'crit': 'Fails to wear safety equipment', 'pen': '5'},
    '6': {'num': '4', 't': False, 'crit': 'Limbs outside cab', 'pen': '5'},
    '7': {'num': '103', 't': True, 'crit': 'Observation', 'pen': '0'},
    '8': {'num': '5', 't': False, 'crit': 'Pedestrian enters work envelope', 'pen': '5'},
    '9': {'num': '6', 't': False, 'crit': 'Fails to look in direction of travel', 'pen': '5'},
    '10': {'num': '7', 't': False, 'crit': 'Fails to check all round before moving', 'pen': '3'},
    '11': {'num': '104', 't': True, 'crit': 'Shovel Operation', 'pen': '0'},
    '12': {'num': '8', 't': False, 'crit': 'Selects wrong hydraulic motion', 'pen': '3'},
    '13': {'num': '9', 't': False, 'crit': 'Rough use of hydraulic controls', 'pen': '3'},
    '14': {'num': '10', 't': False, 'crit': 'Moves bucket violently', 'pen': '5'},
    '15': {'num': '11', 't': False, 'crit': 'Incorrect loading procedure', 'pen': '3'},
    '16': {'num': '12', 't': False, 'crit': 'Undercuts embankment', 'pen': '1'},
    '17': {'num': '13', 't': False, 'crit': 'Spills material from bucket*', 'pen': '1'},
    '18': {'num': '14', 't': False, 'crit': 'Fails to use short cycle*', 'pen': '1'},
    '19': {'num': '15', 't': False, 'crit': 'Loads over cab', 'pen': '1'},
    '20': {'num': '16', 't': False, 'crit': 'Brakes sharply bucket raised', 'pen': '3'},
    '21': {'num': '17', 't': False, 'crit': 'Excessive forward tilt [digging]', 'pen': '1'},
    '22': {'num': '18', 't': False, 'crit': 'Incorrect bucket tilt travel', 'pen': '1'},
    '23': {'num': '19', 't': False, 'crit': 'Fails to use hydraulic detents +', 'pen': '1'},
}
test2 = {
    '1': {'num': '20', 't': False, 'crit': 'Touches vehicle hopper', 'pen': '5'},
    '2': {'num': '21', 't': False, 'crit': 'Works to near tip edge', 'pen': '5'},
    '3': {'num': '22', 't': False, 'crit': 'Incorrect use of bucket', 'pen': '1'},
    '4': {'num': '23', 't': False, 'crit': 'Loads across inline', 'pen': '3'},
    '5': {'num': '201', 't': True, 'crit': 'Driving', 'pen': '0'},
    '6': {'num': '24', 't': False, 'crit': 'Brakes sharply bucket raised', 'pen': '3'},
    '7': {'num': '25', 't': False, 'crit': 'Incorrect use of individual brakes', 'pen': '3'},
    '8': {'num': '26', 't': False, 'crit': 'Steers erratically', 'pen': '3'},
    '9': {'num': '27', 't': False, 'crit': 'Hits course with machine', 'pen': '5'},
    '10': {'num': '28', 't': False, 'crit': 'Turns too sharply', 'pen': '3'},
    '11': {'num': '29', 't': False, 'crit': 'Moves in wrong direction', 'pen': '5'},
    '12': {'num': '30', 't': False, 'crit': 'Fails to release parking brake', 'pen': '1'},
    '13': {'num': '31', 't': False, 'crit': 'Incorrect use of 4WD/difflocks*', 'pen': '3'},
    '14': {'num': '32', 't': False, 'crit': 'Tracks/Sprockets not to rear', 'pen': '3'},
    '15': {'num': '33', 't': False, 'crit': 'Wrong direction on incline', 'pen': '3'},
    '16': {'num': '202', 't': True, 'crit': 'Parking', 'pen': '0'},
    '17': {'num': '34', 't': False, 'crit': 'Fails to apply parking brake/neutral', 'pen': '5'},
    '18': {'num': '35', 't': False, 'crit': 'Fails to lower attachments', 'pen': '3'},
    '19': {'num': '36', 't': False, 'crit': 'Fails to relax hydraulics', 'pen': '5'},
    '20': {'num': '37', 't': False, 'crit': 'Fails to remove key & lock cab', 'pen': '3'},
}
carry_forward = 19
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
    'Unsafe loading',
    'Exceeds maximum time',
    'Violent collision',
    'Dismounts unnecessarily',
    'Operates dangerously',
    'Fails theoretical test (see separate marking/test sheet)'
]
checks = [
    'Bucket/attachments',
    'Lifting arms',
    'Piston and rams',
    'Hydraulic hoses',
    'Hydraulic fluid level',
    'Engine oil level',
    'Coolant level',
    'Windscreen washer level',
    'Wheels /* Track tension',
    'Tyres',
    'External condition',
    'Operators position',
    'Cab visibility',
    'Starting procedure for diesel truck',
    'Flashing beacon',
    'Lights',
    'Audible warning devices',
    'Hydraulic controls',
    'Driving test',
    'Brake test',
    'Steering test wheeled/ *Track slew',
    'Fault reporting procedure',
    ]
operator_training = {
    '1': {'num': '1', 'crit': 'Course induction', 'ref': 'N/E/SR/C'},
    '2': {'num': '2', 'crit': 'The need and reasons to training & statutory requirements (HASAWA 1974 etc.)', 'ref': 'N/E/SR/C'},
    '3': {'num': '3', 'crit': 'Introduction to equipment/control familiarisation/principles of operation', 'ref': 'N/E/SR/C'},
    '4': {'num': '4', 'crit': 'Identification/use/adjustment of attachments in pre-determined positions including forks', 'ref': 'N/E/C'},
    '5': {'num': '5', 'crit': 'Recommended mount and dismount', 'ref': 'N/E/SR/C'},
    '6': {'num': '6', 'crit': 'Introduction to motive, steering controls and practice', 'ref': 'N'},
    '7': {'num': '7', 'crit': 'Basic steering exercises - simple courses', 'ref': 'N'},
    '8': {'num': '8', 'crit': 'Advanced steering exercises - figure of 8/chicane/90\N{DEGREE SIGN} approaches/reverse orientation', 'ref': 'N/E/C'},
    '9': {'num': '9', 'crit': 'Battery charging procedures/maintenance', 'ref': 'N/E/SR/C'},
    '10': {'num': '10', 'crit': 'Operator safety code and relevant handout', 'ref': 'N/E/SR/C'},
    '11': {'num': '11', 'crit': 'Daily pre-use inspections/refueling procedures', 'ref': 'N/E/SR/C'},
    '12': {'num': '12', 'crit': 'Engineering principles/rated capacity/stability', 'ref': 'N/E/SR/C'},
    '13': {'num': '13', 'crit': 'Simple hydraulics (theory) Introduction to hydraulic controls, handling empty pallets low level', 'ref': 'N'},
    '14': {'num': '14', 'crit': 'Load types/handling and weight assessment', 'ref': 'N'},
    '15': {'num': '15', 'crit': 'Stacking/de-stacking at low; eye and high level on industrial racking*', 'ref': 'N/E/SR/C'},
    '16': {'num': '16', 'crit': 'Stacking/de-stacking at low; eye and high level bulk stacks*', 'ref': 'N/E/SR/C'},
    '17': {'num': '17', 'crit': 'Stacking/de-stacking at low; eye and high level cup post pallets*', 'ref': 'N/E/SR/C'},
    '18': {'num': '18', 'crit': 'Manoeuvring with/handling awkward loads*', 'ref': 'N/E/C'},
    '19': {'num': '19', 'crit': 'Relevant safety film', 'ref': 'N/E/SR/C'},
    '20': {'num': '20', 'crit': 'Vehicle loading and unloading (theory)*', 'ref': 'N/E/C'},
    '21': {'num': '21', 'crit': 'Vehicle loading and unloading(practical)*', 'ref': 'N/E/SR/C'},
    '22': {'num': '22', 'crit': 'Multi choice theory test', 'ref': 'N/E/SR/C'},
    '23': {'num': '23', 'crit': 'Pre-use inspection test', 'ref': 'N/E/SR/C'},
    '24': {'num': '24', 'crit': 'Practical skills test', 'ref': 'N/E/SR/C'},
}
disclaimers = [
    '* Allow 1 error per operation',
    '+ As Applicable',
]
class ShovelPage(View):
    def get(self, request):
        instructor = request.user
        form = ShovelForm(initial={'start_Date': datetime.datetime.today(), 'instructor': instructor})
        return render(request, 'loadingshovel.html', {
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
        shovelForm = ShovelForm(request.POST)
        print (shovelForm.errors)
        if shovelForm.is_valid():
            shovelForm.save()
            last_form = Shovel.objects.last()
            form = Forms(form_type=last_form)
            form.save()
            return redirect('/')


class EditShovel(UpdateView):
    model = Shovel
    form_class = ShovelForm
    template_name = 'loadingshovel.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        ctx = super(EditShovel, self).get_context_data(**kwargs)
        form = ShovelForm(instance=self.object)
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
