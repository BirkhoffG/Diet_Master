from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import os
import json


# Create your views here.
@login_required(login_url="/login/")
def recommendation_view(request):
    # card_list = {}
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "recommender/temp/dummy_data.json"), 'r') as f:
        card_list = json.load(f)
    return render(request, "./dashboard/recommend.html", card_list)
