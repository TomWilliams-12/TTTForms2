from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from .forms import CbrForm

class CbrPage(View):
    test = {
        '1': {'num': '101', 't': True, 'crit': 'Operator Safety & Observation', 'pen': '0'},
        '2': {'num': '1', 't': False, 'crit': 'Mounts/dismounts incorrectly', 'pen': '3'},
        '3': {'num': '2', 't': False, 'crit': 'Limb/body outside confines of truck', 'pen': '5'},
        '4': {'num': '3', 't': False, 'crit': 'Fails to check all around', 'pen': '5'},
        '5': {'num': '4', 't': False, 'crit': 'Fails to look in direction of travel', 'pen': '5'},
        '6': {'num': '5', 't': False, 'crit': 'Fails to use appropriate safety devices', 'pen': '5'},
        '7': {'num': '102', 't': True, 'crit': 'Steering & Operating Controls', 'pen': '0'},
        '8': {'num': '6', 't': False, 'crit': 'Travels in wrong direction', 'pen': '5'},
        '9': {'num': '7', 't': False, 'crit': 'Brakes/harshly/erratically', 'pen': '3'},
        '10': {'num': '8', 't': False, 'crit': 'Fails to release parking brake', 'pen': '1'},
        '11': {'num': '9', 't': False, 'crit': 'Rides foot Brake', 'pen': '1'},
        '12': {'num': '10', 't': False, 'crit': 'Operates hydraulic controls when moving', 'pen': '5'},
        '13': {'num': '11', 't': False, 'crit': 'Selects wrong hydraulic control', 'pen': '3'},
        '14': {'num': '12', 't': False, 'crit': 'Excessive use of hydraulic controls', 'pen': '1*'},
        '15': {'num': '13', 't': False, 'crit': 'Rough use of hydraulic controls', 'pen': '3'},
        '16': {'num': '14', 't': False, 'crit': 'Fails to hold steering wheel/assistor', 'pen': '5'},
        '17': {'num': '103', 't': True, 'crit': 'Manoeuvring & Transporting', 'pen': '0'},
        '18': {'num': '15', 't': False, 'crit': 'Fork arms/load too high when travelling', 'pen': '5**'},
        '19': {'num': '16', 't': False, 'crit': 'Fork arms/load too low when travelling', 'pen': '5**'},
        '20': {'num': '17', 't': False, 'crit': 'Incorrect tilt when travelling', 'pen': '3'},
        '21': {'num': '18', 't': False, 'crit': 'Touches course/tracking/load', 'pen': '5'},
        '22': {'num': '19', 't': False, 'crit': 'Shunts in chicane', 'pen': '3*'},
    }
    test2 = {
        '1': {'num': '201', 't': True, 'crit': 'Stacking & De-Stacking', 'pen': '0'},
        '2': {'num': '20', 't': False, 'crit': 'Incorrect set down at vertical face', 'pen': '1'},
        '3': {'num': '21', 't': False, 'crit': 'Shunts when stacking & de-stacking', 'pen': '3*'},
        '4': {'num': '22', 't': False, 'crit': 'Fails to apply parking brake/neutral', 'pen': '5'},
        '5': {'num': '23', 't': False, 'crit': 'Fork arms not central under load', 'pen': '3**'},
        '6': {'num': '24', 't': False, 'crit': 'Fork arms rubbing(entry/withdrawal)', 'pen': '3**'},
        '7': {'num': '25', 't': False, 'crit': 'Fork arms not fully inserted', 'pen': '5**'},
        '8': {'num': '26', 't': False, 'crit': 'Mast base touches stack/load', 'pen': '3'},
        '9': {'num': '27', 't': False, 'crit': 'Fork tips touch stack/load', 'pen': '3**'},
        '10': {'num': '28', 't': False, 'crit': 'Load/fork arms not level', 'pen': '3**'},
        '11': {'num': '29', 't': False, 'crit': 'Load incorrectly stacked', 'pen': '3'},
        '12': {'num': '30', 't': False, 'crit': 'Wheels not straight', 'pen': '3'},
        '13': {'num': '202', 't': True, 'crit': 'Parking', 'pen': '0'},
        '14': {'num': '31', 't': False, 'crit': 'Fails to apply parking brake/neutral', 'pen': '5'},
        '15': {'num': '32', 't': False, 'crit': 'Fails to apply forward tilt', 'pen': '3'},
        '16': {'num': '33', 't': False, 'crit': 'Fails to lower fork arms', 'pen': '3**'},
        '17': {'num': '34', 't': False, 'crit': 'Fails to switch off/remove key', 'pen': '3'},
        '18': {'num': '35', 't': False, 'crit': 'Wheels not straight', 'pen': '3'},
        '19': {'num': '203', 't': True, 'crit': 'Reach Trucks Only', 'pen': '0'},
        '20': {'num': '36', 't': False, 'crit': 'Lowers load onto reach truck', 'pen': '5'},
        '21': {'num': '37', 't': False, 'crit': 'Travels with reach extended', 'pen': '5'},
    }
    carry_forward = 19
    review_choices = (
        ('review_1','1'),
        ('review_2','2'),
        ('review_3','3'),
        ('review_4','4'),
        ('review_5','5'),
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
        'Skill and dexterity': 'SD',
        'Response to instruction': 'RTI',
        'Motivation': 'M',
        'Safety Attitude': 'SA'
    }
    md = [
        'Does not complete pre-use check',
        'Unsafe stacking',
        'Exceeds maximum time',
        'Violent collision',
        'Dismounts unnecessarily',
        'Operates dangerously',
        'Exceeds 3 occurances of any one fault'
    ]
    checks = [
        'Fork Arms/Attachment (MC)',
        'Carriage-Plate (MC)',
        'Backrest Extension',
        'Mast (MC)',
        'Mast Rollers/Sliders (MC)',
        'Lift Chains(MC)',
        'Chain Pulleys (MC)',
        'Hydraulics (MC)',
        'Wheels (MC)',
        'Tyres (MC)',
        'External Condition',
        'Rated Capactiy Plate (MC)', ]
    checks2 = [
        'Operating Position',
        'Operators Seat',
        'Gas Trucks',
        'Starting Procedure - Engine Trucks',
        'Starting Procedure - Electric Trucks',
        'Lights',
        'Audible Warnings (MC)',
        'Hydraulic Controls (MC)',
        'Drive & Braking (MC)',
        'Steering (MC)',
        'Fault Reporting Procedure'
    ]
    operator_training = {
        '1': {'num': '1', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Course induction, the need and reasons to train and relevant statutory requirements', 'ref': 'N/E/SR'},
        '2': {'num': '2', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Introduction to equipment/control familiarisation/principles of operation', 'ref': 'N/E/SR'},
        '3': {'num': '3', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Recommend mount/dismount, lift truck security, introduction to motive and steering controls', 'ref': 'N/E/SR'},
        '4': {'num': '4', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Identification/use/adjustment of attachments in pre-determined positions including forks', 'ref': 'N/E'},
        '5': {'num': '5', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Basic/advanced steering exercises - simple courses/figure of 8/chicane/90\u00B0  approaches', 'ref': 'N/E/SR'},
        '6': {'num': '6', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Battery charging procedures/maintenance/Re-fuelling procedures', 'ref': 'N/E/SR'},
        '7': {'num': '7', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Operator safety code and relevant course hand-out', 'ref': 'N/E/SR'},
        '8': {'num': '8', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Daily pre-use inspections', 'ref': 'N/E/SR'},
        '9': {'num': '9', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Engineering principles/rated capacity/stability', 'ref': 'N/E/SR'},
        '10': {'num': '10', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Simple hydraulics (theory) and introduction to hydraulic controls', 'ref': 'N'},
        '11': {'num': '11', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Load types, handling empty pallets low level and weight assessment', 'ref': 'N'},
        '12': {'num': '12*', 'low': True, 'med': True, 'high': True, 'pre': False, 'theory': False, 'practical': False, 'crit': '(Racking) Stacking/de-stacking', 'ref': 'N/E/SR'},
        '13': {'num': '13*', 'low': True, 'med': True, 'high': True, 'pre': False, 'theory': False, 'practical': False, 'crit': '(Bulk stacks) Stacking/de-stacking', 'ref': 'N/E/SR'},
        '14': {'num': '14*', 'low': True, 'med': True, 'high': True, 'pre': False, 'theory': False, 'practical': False, 'crit': '(Corner locating loads) Stacking/de-stacking', 'ref': 'N/E/SR'},
        '15': {'num': '15', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Transporting/handling awkward loads', 'ref': 'N/E'},
        '16': {'num': '16', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': False, 'practical': False, 'crit': 'Relevant safety film', 'ref': 'N/E/SR'},
        '17': {'num': '17*', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': True, 'practical': True, 'crit': 'Ramps and inclines', 'ref': 'N/E/SR'},
        '18': {'num': '18*', 'low': False, 'med': False, 'high': False, 'pre': False, 'theory': True, 'practical': True, 'crit': 'Vehicle loading and unloading', 'ref': 'N/E'},
        '19': {'num': '19*', 'low': False, 'med': False, 'high': False, 'pre': True, 'theory': True, 'practical': True, 'crit': 'Testing', 'ref': 'N/E/SR'},
    }
    def get(self, request):
        instructor = self.request.user
        form = CbrForm(initial={'start_Date': datetime.today(), 'instructor': instructor})

        return render(request, 'cbr.html', {
            'form': form,
            'operatorContent': self.operatorContent,
            'test': self.test,
            'test2': self.test2,
            'carry_forward': self.carry_forward,
            'md': self.md,
            'checks': self.checks,
            'checks2': self.checks2,
            'operator_training': self.operator_training,
            'eval': self.eval,
            'instructor': instructor,
            })
    
    def post(self, request):
        cbrForm = CbrForm(request.POST)

        if cbrForm.is_valid():
            cbrForm.save()
            return redirect('/')
