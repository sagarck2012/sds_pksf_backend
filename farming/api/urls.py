from django.urls import path
from .views import SeedingAddAPIView, PlotAddAPIView, PlotEditAPIView,\
    SeedingEditAPIView, SeedingListAPIView, PlotListAPIView, HarvestingAddAPIView,\
    HarvestingEditAPIView, PlotStatusUpdateAPIView, HarvestingListAPIView, SeedingStatusAPIView

urlpatterns = [
    path('seeding/add/', SeedingAddAPIView.as_view()),
    path('seeding/edit/', SeedingEditAPIView.as_view()),
    path('seeding/list/', SeedingListAPIView.as_view()),
    path('plot/add/', PlotAddAPIView.as_view()),
    path('plot/edit/', PlotEditAPIView.as_view()),
    path('plot/list/', PlotListAPIView.as_view()),
    # path('plot/status/', PlotStatusUpdateAPIView.as_view()),
    # path('land/status/', LandStatusAPIView.as_view()),
    path('harvesting/add/', HarvestingAddAPIView.as_view()),
    path('harvesting/edit/', HarvestingEditAPIView.as_view()),
    path('harvesting/list/', HarvestingListAPIView.as_view()),
    path('seeding/status/', SeedingStatusAPIView.as_view())

]
