import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from .forms import AwForm
from .models import Aw
from forms.models import Forms

test = {
    '1': {'num': '101', 't': True, 'crit': 'Facilities'},
    '2': {'num': '1', 't': False, 'crit': 'Service area correctly chosen*'},
    '3': {'num': '2', 't': False, 'crit': 'Uses correct PPE'},
    '4': {'num': '3', 't': False, 'crit': 'Correct tools available/used'},
    '5': {'num': '4', 't': False, 'crit': 'HSE Posters / Register in place *'},
    '6': {'num': '102', 't': True, 'crit': 'Initial Visual Inspection(Electrical)'},
    '7': {'num': '5', 't': False, 'crit': 'Ensures power isolated/unplugged'},
    '8': {'num': '6', 't': False, 'crit': 'Grinder inspected for damage'},
    '9': {'num': '7', 't': False, 'crit': 'Spindle speed on machine fitted'},
    '10': {'num': '103', 't': True, 'crit': 'Initial Visual Inspection(Petrol)'},
    '11': {'num': '8', 't': False, 'crit': 'Sufficient fuel for task'},
    '12': {'num': '9', 't': False, 'crit': 'Cutter inspected for damage'},
    '13': {'num': '10', 't': False, 'crit': 'Spindle speed on machine fitted'},
    '14': {'num': '104', 't': True, 'crit': 'Mounting Procedure(Petrol Engine Machines)'},
    '15': {'num': '11', 't': False, 'crit': 'Flanges Removed'},
    '16': {'num': '12', 't': False, 'crit': 'Flanges inspected',},
    '17': {'num': '13', 't': False, 'crit': 'Ensures machine is clean'},
    '18': {'num': '14', 't': False, 'crit': 'Spindle speed checked (Tachometer)'},
    '19': {'num': '15', 't': False, 'crit': 'Correct wheel selected/speed checked', },
    '20': {'num': '16', 't': False, 'crit': 'Flanges refitted correctly', },
    '21': {'num': '17', 't': False, 'crit': 'Guards replaced/correctly adjusted'},
}
test2 = {
    '1': {'num': '201', 't': True, 'crit': 'Mounting Procedures (Hand Held Electric Machines)'},
    '2': {'num': '18', 't': False, 'crit': 'Flanges removed'},
    '3': {'num': '19', 't': False, 'crit': 'Flanges inspected'},
    '4': {'num': '20', 't': False, 'crit': 'Ensures machine is clean'},
    '5': {'num': '21', 't': False, 'crit': 'Spindle and disc speed checked'},
    '6': {'num': '22', 't': False, 'crit': 'Wheel selected & fitted correctly'},
    '7': {'num': '23', 't': False, 'crit': 'Flanges refitted correctly'},
    '8': {'num': '24', 't': False, 'crit': 'Guards replaced/correctly adjusted'},
    '9': {'num': '202', 't': True, 'crit': 'Mounting Procedure(Bench Grinding Machines)'},
    '10': {'num': '25', 't': False, 'crit': 'Guards removed'},
    '11': {'num': '26', 't': False, 'crit': 'Flanges removed'},
    '12': {'num': '27', 't': False, 'crit': 'Flanges inspected'},
    '13': {'num': '28', 't': False, 'crit': 'Ensures machine is clean'},
    '14': {'num': '29', 't': False, 'crit': 'Spindle and disc speed checked'},
    '15': {'num': '30', 't': False, 'crit': 'Flanges refitted correctly'},
    '16': {'num': '31', 't': False, 'crit': 'Flanges inspected',},
    '17': {'num': '32', 't': False, 'crit': 'Guards replaced/correctly adjusted'},
    '18': {'num': '203', 't': True, 'crit': 'All Machine Types'},
    '19': {'num': '33', 't': False, 'crit': 'Run up test completed correctly', },
}
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
    'Skill and dexterity': 'SD',
    'Learning capacity': 'LC',
    'Motivation': 'M',
    'Safety Attitude': 'SA'
}
md = [
    'Does not complete pre-use check',
    'Unsafe practice',
    'Exceeds maximum time',
    'Wrong selection of wheel',
    'Operates dangerously',
    'Fails knowledge test'
]
checks = [
    'Ensure electrical supply isolated',
    'Lead for cuts and abrasions',
    'Lead entry point at plug/connection box',
    'Lead at entry point to machine',
    'Machine body for damage',
    'Guards in place',
    'Guards correctly adjusted',
    'Correct wheel for operation',
    'Spindle speed & disc speed compatible',
    'Damage to disc',
    'Machine secured to bench/pedestal',
    'On/Off switches function correctly',
    'Isolation device operates correctly', 
    ]
checks2 = [
    'Machine body for damage',
    'Guards in place',
    'Guards Correctly adjusted',
    'Correct Wheel for operation',
    'Spindle speed & disc speed compatible',
    'Damage to disc',
    'Fuel level',
    'Oil level',
    'Fluid leaks',
    'Cooling system components for damage',
    'Disc does not rotate on tick over (engine at operating temperature)',
    'On/Off switches function correctly',
    'Cooling system operates correctly (after run up check)',
    'Fault reporting procedure',
]
operator_training = {
    '1': {'num': '1', 'crit': 'Course induction', 'ref': 'N/E/SR'},
    '2': {'num': '2', 'crit': 'The need and reasons to training & statutory requirements (HASAWA 1974 etc.)', 'ref': 'N/E/SR'},
    '3': {'num': '3', 'crit': 'PUWER 1998 and HSG 17', 'ref': 'N/E/SR'},
    '4': {'num': '4', 'crit': 'Introduction to equipment/control familiarisation/principles of operation', 'ref': 'N/E/SR'},
    '5': {'num': '5', 'crit': 'Identification/use/adjustment of guards and tool rests', 'ref': 'N/E/SR'},
    '6': {'num': '6', 'crit': 'Wheel and discs types', 'ref': 'N/E/SR'},
    '7': {'num': '7', 'crit': 'Wheel marking and wheels speeds MOS', 'ref': 'N/E/SR'},
    '8': {'num': '8', 'crit': 'Introduction to motive controls & practice', 'ref': 'N/E/SR'},
    '9': {'num': '9', 'crit': 'Basic exercises - simple courses', 'ref': 'N/E/SR'},
    '10': {'num': '10', 'crit': 'Advanced exercises - mounting, truing and dressing', 'ref': 'N/E/SR'},
    '11': {'num': '11', 'crit': 'Methods of inspections and testing, ring test', 'ref': 'N/E/SR'},
    '12': {'num': '12', 'crit': 'Operator safety code and relevant handout', 'ref': 'N/E/SR'},
    '13': {'num': '13', 'crit': 'Daily pre-use inspection procedures', 'ref': 'N/E/SR'},
    '14': {'num': '14', 'crit': 'Handling and transportation of wheels and discs', 'ref': 'N/E/SR'},
    '15': {'num': '15', 'crit': 'Storage of wheels and discs', 'ref': 'N/E/SR'},
    '16': {'num': '16', 'crit': 'Blotters, flanges, bushes and lock nuts', 'ref': 'N/E/SR'},
    '17': {'num': '17', 'crit': 'Common hazards', 'ref': 'N/E/SR'},
    '18': {'num': '18', 'crit': 'Personal protective equipment', 'ref': 'N/E/SR'},
    '19': {'num': '19', 'crit': 'Hot working procedures', 'ref': 'N/E/SR'},
    '20': {'num': '20', 'crit': 'Relevant safety film', 'ref': 'N/E/SR'},
    '21': {'num': '21', 'crit': 'Mounted practical skills test', 'ref': 'N/E/SR'},
    '22': {'num': '22', 'crit': 'Portable practical skills test', 'ref': 'N/E/SR'},
    '23': {'num': '23', 'crit': 'Multi choice theory test', 'ref': 'N/E/SR'},
    '24': {'num': '24', 'crit': 'Pre-use inspection test', 'ref': 'N/E/SR'},
    '25': {'num': '25', 'crit': 'Feedback', 'ref': 'N/E/SR'},
}
disclaimers = [
    '* As appropriate to operating environment and company policies',
]

class AwPage(View):
    def get(self, request):
        instructor = request.user
        form = AwForm(initial={'start_Date': datetime.datetime.today(), 'instructor': instructor})
        return render(request, 'aw.html', {
            'form': form,
            'operatorContent': operatorContent,
            'test': test,
            'test2': test2,
            'md': md,
            'checks': checks,
            'checks2': checks2,
            'operator_training': operator_training,
            'eval': eval,
            'instructor': instructor,
            'disclaimers': disclaimers,
            })
    
    def post(self, request):
        cbrForm = AwForm(request.POST)
        if cbrForm.is_valid():
            cbrForm.save()
            last_form = Aw.objects.last()
            form = Forms(form_type=last_form)
            form.save()
            return redirect('/')


class EditAw(UpdateView):
    model = Aw
    form_class = AwForm
    template_name = 'aw.html'
    success_url = "/"
    
    
    def get_context_data(self, **kwargs):
        ctx = super(EditAw, self).get_context_data(**kwargs)
        form = AwForm(instance=self.object)
        instructor = self.object.instructor
        instructor_2 = self.object.instructor_2
        ctx = {
            'form': form,
            'operatorContent': operatorContent,
            'test': test,
            'test2': test2,
            'md': md,
            'checks': checks,
            'checks2': checks2,
            'operator_training': operator_training,
            'eval': eval,
            'instructor': instructor,
            'instructor_2': instructor_2,
            'disclaimers': disclaimers,
        }
        return ctx