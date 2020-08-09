import flask
from flask import request, jsonify
from werkzeug.utils import redirect

regressions = \
[
    {
        'id': 'alcholoic beverages',
        'regression': .106
    },
    {
        'id': 'animal products',
        'regression': .281
    },
    {
         'id': 'animal fats',
         'regression': .118
    },
    {
        'id': 'aquatic products, other',
        'regression' : -.057
    },
    {
        'id': 'cereals - excluding beer',
        'regression' : -.218
    },
    {
        'id': 'eggs',
        'regression': .352
    },
    {
        'id': 'fish',
        'regression': .005
    },
    {
        'id': 'fruits - excluding wine',
        'regression': .183
    },
    {
        'id': 'meat',
        'regression': .241
    },
    {
        'id': 'milk - excluding butter',
        'regression': .274
    },
    {
        'id': 'miscellaneous',
        'regression': .033
    },
    {
        'id': 'offals',
        'regression': .010
    },
    {
        'id': 'oilcrops',
        'regression': -.222
    },
    {
        'id': 'pulses',
        'regression': -.180
    },
    {
        'id': 'spices',
        'regression': -.086
    },
    {
        'id': 'starchy roots',
        'regression': -.180
    },
    {
        'id': 'stimulants',
        'regression': .219
    },
    {
        'id': 'sugar crops',
        'regression': -.077
    },
    {
        'id': 'sugar and sweeteners',
        'regression': .210
    },
    {
        'id': 'treenuts',
        'regression': .140
    },
    {
        'id': 'vegetal products',
        'regression': -.281
    },
    {
        'id': 'vegetable oils',
        'regression': .092
    },
    {
        'id': 'vegetables',
        'regression': .144
    }
]

strong_regressions = [regression['id'] for regression in regressions if regression['regression'] > .22]

medium_regressions = [regression['id'] for regression in regressions if .22 > regression['regression'] > .1]

weak_regressions = [regression['id'] for regression in regressions if regression['regression'] < .100]

print("strong: {}".format(strong_regressions))
print("medium: {}".format(medium_regressions))
print("weak: {}".format(weak_regressions))

def determine_risk_level(slider_inputs):
    score = 0
    for input in slider_inputs:
        if input['id'] in strong_regressions:
            score += ((input['score'] * .1) * strong_regressions['id']) * 150 #finds score on regression line then multiplies it by 100
        elif input['id'] in medium_regressions:
            score += ((input['score'] * .1) * medium_regressions['id']) * 125
        else:
            score += ((input['score'] * .1) * weak_regressions['id']) * 100

    if score >= 8:
        return 0
    if score >= 4:
        return 1
    return 2
