from django.shortcuts import render
from django.views import View
from forms.forms import InductionForm, ReviewForm, PracticalForm, TheoryForm

class InductionPage(View):
    choices = (
            ('',''),
            ('Counterbalance Novice','Counterbalance Novice'),
            ('Counterbalance Experienced','Counterbalance Experienced'),
            ('Counterbalance Refresher','Counterbalance Refresher'),
            ('Counterbalance Conversion','Counterbalance Conversion'),
            ('Reach Novice','Reach Novice'),
            ('Reach Experienced','Reach Experienced'),
            ('Reach Refresher','Reach Refresher'),
            ('Reach Conversion','Reach Conversion'),
        )
    
    def get(self, request):
        induction = InductionForm(self.choices, request=request)
        return render(request, 'induction.html', {'induction': induction})


class ReviewPage(View):
    choices = (
            ('',''),
            ('Counterbalance Novice','Counterbalance Novice'),
            ('Counterbalance Experienced','Counterbalance Experienced'),
            ('Counterbalance Refresher','Counterbalance Refresher'),
            ('Counterbalance Conversion','Counterbalance Conversion'),
            ('Reach Novice','Reach Novice'),
            ('Reach Experienced','Reach Experienced'),
            ('Reach Refresher','Reach Refresher'),
            ('Reach Conversion','Reach Conversion'),
        )
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
        'What part of the training session will you use most at work?',
        'What part of the training session did you most enjoy?',
        'Generally, is there anything you wish to comment on regarding your training period with us?'
    ]
    def get(self, request):
        review = ReviewForm(self.review_choices, request=request)
        induction = InductionForm(self.choices, request=request)
        # induction = InductionPage()(self.request)
        return render(request, 'review.html', {'review': review, 'induction': induction, 'eval': self.eval})


class PracticalPage(View):
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
    md = [
        'Does not complete pre-use check',
        'Unsafe stacking',
        'Exceeds maximum time',
        'Violent collision',
        'Dismounts unnecessarily',
        'Operates dangerously',
        'Exceeds 3 occurances of any one fault'
    ]
    disclaimers = [
        '* Allow 1 adjustment per operation',
        '** The phrase "forks" includes attachments if applicable',
    ]
    carryForward = 19
    def get(self, request):
        practical = PracticalForm(self.test, self.test2, self.md, request=request)
        return render(request, 'practical_test.html', {
            'practical': practical,
            'test': self.test,
            'test2': self.test2,
            'md': self.md,
            'carryForward': self.carryForward,
            'disclaimers': self.disclaimers
                })


class TheoryPage(View):
    def get(self, request):
        theory = TheoryForm(request=request)
        return render(request, 'theory_test.html', {
            'theory': theory,
        })