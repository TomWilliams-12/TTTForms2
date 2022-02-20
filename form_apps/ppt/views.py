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
    '3': {'num': '2', 't': False, 'crit': 'Fails to secure fall protection correctly', 'pen': '5'},
    '4': {'num': '3', 't': False, 'crit': 'Limbs outside carrier during manoeuvring', 'pen': '5'},
    '5': {'num': '4', 't': False, 'crit': 'Fails to make all around checks', 'pen': '3'},
    '6': {'num': '5', 't': False, 'crit': 'Fails to look in direction of travel', 'pen': '5'},
    '7': {'num': '6', 't': False, 'crit': 'Misinterpretation of banksman signalling', 'pen': '3'},
    '8': {'num': '7', 't': False, 'crit': 'Access gates not fully closed/engaged', 'pen': '3'},
    '9': {'num': '102', 't': True, 'crit': 'Manoeuvring', 'pen': '0'},
    '10': {'num': '8', 't': False, 'crit': 'Touches Course', 'pen': '3'},
    '11': {'num': '9', 't': False, 'crit': 'Shunts in chicane/bay areas', 'pen': '1*'},
    '12': {'num': '10', 't': False, 'crit': 'Activates wrong direction control', 'pen': '5'},
    '13': {'num': '11', 't': False, 'crit': 'Steers erratically', 'pen': '5'},
    '14': {'num': '12', 't': False, 'crit': 'Brakes harshly/erratically', 'pen': '3'},
    '15': {'num': '13', 't': False, 'crit': 'Erratic change of direction', 'pen': '5'},
    '16': {'num': '103', 't': True, 'crit': 'Lifting Operations', 'pen': '0'},
    '17': {'num': '14', 't': False, 'crit': 'Failts to position equipment accurately', 'pen': '3'},
    '18': {'num': '15', 't': False, 'crit': 'Fails to cordon off area', 'pen': '3'},
    '19': {'num': '16', 't': False, 'crit': 'Fails to check stabiliser engagement', 'pen': '5'},
    '20': {'num': '17', 't': False, 'crit': 'Fails to level equipment correctly', 'pen': '5'},
    '21': {'num': '18', 't': False, 'crit': 'Fails to lock stabilisers', 'pen': '5'},
}
test2 = {
    '1': {'num': '19', 't': False, 'crit': 'Selects wrong hydraulic control', 'pen': '3'},
    '2': {'num': '20', 't': False, 'crit': 'Rough use of hydraulic controls', 'pen': '3'},
    '3': {'num': '21', 't': False, 'crit': 'Excessive use of hydraulic controls', 'pen': '1*'},
    '4': {'num': '22', 't': False, 'crit': 'Operates too close to hazards', 'pen': '3'},
    '5': {'num': '23', 't': False, 'crit': 'Touches structure', 'pen': '3'},
    '6': {'num': '24', 't': False, 'crit': 'Uses toe-plates/railings to gain height', 'pen': '5'},
    '7': {'num': '25', 't': False, 'crit': 'Fails to lock platform extensions', 'pen': '5'},
    '8': {'num': '26', 't': False, 'crit': 'Fails to check below before lowering', 'pen': '3'},
    '9': {'num': '27', 't': False, 'crit': 'Fails to re-configfure for travelling', 'pen': '5'},
    '10': {'num': '202', 't': True, 'crit': 'Parking and Shut Down', 'pen': '0'},
    '11': {'num': '28', 't': False, 'crit': 'fails to position correctly', 'pen': '3'},
    '12': {'num': '29', 't': False, 'crit': 'Fails to switch off and isolate', 'pen': '5'},
    '13': {'num': '30', 't': False, 'crit': 'Fails to remove key', 'pen': '3'},
    '14': {'num': '31', 't': False, 'crit': 'Fails to complete post-stop checks', 'pen': '5'},
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
    'Engine oil/coolant/hyd. oil levels',
    'Battery/batteries/charging system', 
    'Engine Compartment', 
    'All pivot pins/retaining clips', 
    'Hydraulic/engine system for leaks', 
    'Wheels/tyres/tracks', 
    'Steps/handrails/access points', 
    'Carrier condition/anchorage points', 
    'All guarding/covers secure', 
    'Warning decals/control symbols', 
    'SWL identified', 
    'Overall condition', 
    'Greasing', 
    'Harness/lanyard inspected', 
    'Power source', 
    'Emergency lowering system', 
    'Overload/tilt proection systems', 
    'Access gates function/lock correctly', 
    'Electrical system', 
    'Audible warning systems', 
    'Hydraulic/motive control function', 
    'Brakes/steering', 
    'Limit switches', 
    'Carrier levelling system', 
    'Stabiliser/outrigger locking system', 
    'Extending platform system', 
    'Power take off', 
    'Emergency stop control', 
    'Manufacturers manual', 
    'Fault reporting procedure', 
    ]
operator_training = {
    '1': {'num': '1', 'crit': 'Course induction', 'ref': 'N/E/SR'},
    '2': {'num': '2', 'crit': 'The need and reasons to training & statutory requirements (HASAWA 1974 etc.)', 'ref': 'N/E/SR'},
    '3': {'num': '3', 'crit': 'Introduction to equipment/control familiarisation/principles of operation', 'ref': 'N/E/SR'},
    '4': {'num': '4', 'crit': 'Identification/use/adjustment of stabilizers, outriggers/extended platforms', 'ref': 'N/E'},
    '5': {'num': '5', 'crit': 'Recommended mount and dismount/ground access/step access', 'ref': 'N/E/SR'},
    '6': {'num': '6', 'crit': 'Introduction to motive, steering controls & practice', 'ref': 'N'},
    '7': {'num': '7', 'crit': 'Basic steering exercises - simple courses', 'ref': 'N'},
    '8': {'num': '8', 'crit': 'Advanced steering exercises - figure of 8/chicane/90\N{DEGREE SIGN} approaches/reverse orientation', 'ref': 'N/E'},
    '9': {'num': '9', 'crit': 'Battery changing procedures/maintenance', 'ref': 'N/E/SR'},
    '10': {'num': '10', 'crit': 'Operator safety code and relevant handout', 'ref': 'N/E/SR'},
    '11': {'num': '11', 'crit': 'Daily pre-use inspections/refueling procedures', 'ref': 'N/E/SR'},
    '12': {'num': '12', 'crit': 'Engineering principles/rated capacity/stability', 'ref': 'N/E/SR'},
    '13': {'num': '13', 'crit': 'Simple hydraulics (theory) Introduction to hydraulic controls', 'ref': 'N'},
    '14': {'num': '14', 'crit': 'Safety harness awareness', 'ref': 'N'},
    '15': {'num': '15', 'crit': 'Anchor points*', 'ref': 'N/E/SR'},
    '16': {'num': '16', 'crit': 'Elevating at low/medium/high level', 'ref': 'N/E/SR'},
    '17': {'num': '17', 'crit': 'Operating at low/medium/high level', 'ref': 'N/E/SR'},
    '18': {'num': '18', 'crit': 'Maneuvering/ramps & inclines*', 'ref': 'N/E'},
    '19': {'num': '19', 'crit': 'Relevant safety film', 'ref': 'N/E/SR'},
    '20': {'num': '20', 'crit': 'Emergency lowering', 'ref': 'N/E'},
    '21': {'num': '21', 'crit': 'Safety decals', 'ref': 'N/E'},
    '22': {'num': '22', 'crit': 'Multi choice theory test', 'ref': 'N/E/SR'},
    '23': {'num': '23', 'crit': 'Pre-use inspection test', 'ref': 'N/E/SR'},
    '24': {'num': '24', 'crit': 'Practical skills test', 'ref': 'N/E/SR'},
}
disclaimers = [
    '* As appropriate to operating environment and company policies',
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
        mewpForm = PptForm(request.POST)
        print (mewpForm.errors)
        if mewpForm.is_valid():
            mewpForm.save()
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
        ctx = super(PptForm, self).get_context_data(**kwargs)
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
