from django.shortcuts import render, get_object_or_404
from . import models


def main_page_view(request):
   if request.method == 'GET':
       tours = models.Tour.objects.all()
       slider = models.Slider.objects.all()
       context = {
           'tours': tours,
           'slider': slider,
       }
       return render(request, 'main_page.html', context)


def tour_view(request, id):
    tour = get_object_or_404(models.Tour, id=id)
    return render(request, 'tour.html', {'tour': tour})
