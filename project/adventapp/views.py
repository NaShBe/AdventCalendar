from django.shortcuts import render
from django.http import HttpResponse

from .models import AdventSlot

# Create your views here.
def get_slot(request):
    slots = AdventSlot.objects.all()
    return render(request, "", {"slots": slots})


def make_slot(request):
    date = request.slot_date
    text = request.slot_text
    image = request.slot_image
    AdventSlot.objects.create(date = date, text = text, image = image)
    response = HttpResponse()
    response.status_code = 200
    response.content = ""
    return response