from django.urls import path
from .views import *

urlpatterns = [
    path('packaging/harvest_search/', HarvestSearchAPIView.as_view()),
    path('packaging/add/', PackagingAddAPIView.as_view()),
    path('packaging/package_search/', PackagingSearchAPIView.as_view()),
    path('packaging/sticker_search/', StickerSearchAPIView.as_view()),
    path('packaging/sticker_damaged/', StickerDamagedAPIView.as_view()),
    path('packaging/sticker_printed/', StickerPrintedAPIView.as_view()),
    path('packaging/detail/', StickerDetailAPIView.as_view()),

    path('crate/ready/', ReadyCrateListAPIView.as_view()),
    path('crate/register/', CrateRegisterAPIView.as_view()),
    path('crate/edit/', CrateEditAPIView.as_view()),
    path('crate/delete/', CrateDeleteAPIView.as_view()),

    path('crating/add_package/', CratingAddAPIView.as_view()),
    path('crating/detail/', CratingDetailAPIView.as_view()),

    path('shipment/ready/', ReadyShipmentAPIView.as_view()),
    path('shipment/add/', ShipmentAddAPIView.as_view()),
    path('shipment/edit/', ShipmentEditAPIView.as_view()),
    path('shipment/delete/', ShipmentDeleteAPIView.as_view()),
    path('packaging/edit/', PackagingEditAPIView.as_view()),


]