from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home_view(request):
    home_context = {
        "curr_year": datetime.now().year,
        "curr_month": datetime.now().month,
        "curr_day": datetime.now().day,
        "curr_month_str": datetime.now().strftime("%B")
    }
    return render(request, "home.html", home_context)