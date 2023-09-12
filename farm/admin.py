from django.contrib import admin
from farm.models import Crop, CropType, Vegetable
# Register your models here.

crop_models = [Crop, CropType, Vegetable]
admin.site.register(crop_models)
