from django.urls import path
from .views import FarmerListAPIView, FarmerAddAPIView, FarmerEditAPIView, \
    FarmerSearchAPIView, FarmerDeleteAPIView, DivisionAPIView, DistrictAPIView,\
    UpazilaAPIView, OwnerAddAPIView, OwnerListAPIView, OwnerSearchAPIView, \
    OwnerEditAPIView, OwnerDeleteAPIView, LandAddAPIView, LandListAPIView, \
    LandSearchAPIView, LandDeleteAPIView, LandEditAPIView, CropListAPIView, \
    CropTypeListAPIView, CropVariantAPIView, CropTypeAddAPIView, CropTypeEditAPIView, \
    CropTypeDeleteAPIView, VegetableVariantAddAPIView, DistrictSearchAPIView, ProductionHouseListAPIView

urlpatterns = [
    path('farmer/list/', FarmerListAPIView.as_view()),
    path('farmer/add/', FarmerAddAPIView.as_view()),
    path('farmer/edit/', FarmerEditAPIView.as_view()),
    path('farmer/search/', FarmerSearchAPIView.as_view()),
    path('farmer/delete/', FarmerDeleteAPIView.as_view()),

    path('division/', DivisionAPIView.as_view()),
    path('district/', DistrictAPIView.as_view()),
    path('upazila/', UpazilaAPIView.as_view()),
    # path('district/search/', DistrictSearchAPIView.as_view()),

    path('owner/list/', OwnerListAPIView.as_view()),
    path('owner/add/', OwnerAddAPIView.as_view()),
    path('owner/edit/', OwnerEditAPIView.as_view()),
    path('owner/search/', OwnerSearchAPIView.as_view()),
    path('owner/delete/', OwnerDeleteAPIView.as_view()),

    path('land/list/', LandListAPIView.as_view()),
    path('land/add/', LandAddAPIView.as_view()),
    path('land/edit/', LandEditAPIView.as_view()),
    path('land/search/', LandSearchAPIView.as_view()),
    path('land/inactive/', LandDeleteAPIView.as_view()),

    path('crop/list/', CropListAPIView.as_view()),

    path('croptype/list/', CropTypeListAPIView.as_view()),
    # path('croptype/add/', CropTypeAddAPIView.as_view()),
    # path('croptype/edit/', CropTypeEditAPIView.as_view()),
    # path('croptype/delete/', CropTypeDeleteAPIView.as_view()),

    path('crop_variant/list/', CropVariantAPIView.as_view()),
    # path('vegetable/variant/add/', VegetableVariantAddAPIView.as_view()),
    # path('vegetable/variant/edit/', VegetableVariantEditAPIView.as_view()),

    path('production_house/list/', ProductionHouseListAPIView.as_view()),

]
