from django.shortcuts import render
import os, json


# Create your views here.
def recommendation_view(request):
    # card_list = {}
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "recommender/temp/dummy_data.json"), 'r') as f:
        card_list = json.load(f)
    return render(request, "./dashboard/recommend.html", card_list)
