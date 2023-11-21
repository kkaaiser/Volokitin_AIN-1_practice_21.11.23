from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page_view, name='main'),
    path('tour/<int:id>', views.tour_view),
]
