from rest_framework import serializers
from farm.models import Farmer, Division, District, Upazila, Owner, Land, Crop, CropType, Vegetable, ProductionHouse
from django.db.models import Sum
from farming.models import Seeding, Plot
# import json
# import base64


class FarmerSerializer(serializers.ModelSerializer):
    # photo = models.BinaryField()
    user_id = serializers.IntegerField(required=False)
    # farmer_id = serializers.IntegerField(required=False)

    class Meta:
        model = Farmer
        # fields = ['photo', 'id', 'total_land']
        # fields = '__all__'
        exclude = ['created_by', 'last_updated_by', 'delete_status']

    # def to_representation(self, instance):
    #     """Convert bytes to str."""
    #     ret = super().to_representation(instance)
    #     if ret['photo'] is not None:
    #         ret['photo'] = ret['photo'].decode('utf-8')
    #     return ret


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = '__all__'


class UpazilaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upazila
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)

    class Meta:
        model = Owner
        # fields = '__all__'
        exclude = ['created_by', 'last_updated_by', 'delete_status']


class LandSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)
    # area_unit = serializers.CharField(max_length=10, read_only=True)
    area_unit = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = Land
        # fields = '__all__'
        exclude = ['created_by', 'last_updated_by', 'is_active', 'status']

# Unused (just for test purpose)
class DistrictSearchSerializer(serializers.Serializer):
    division_id = serializers.IntegerField()

    # class Meta:
    #     models = None
    #     fields = ['division_id']


class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop
        fields = ('id', 'name')


class VegetableSerializer(serializers.ModelSerializer):
    crop_type_id = serializers.IntegerField(source='id')
    crop_category_id = serializers.IntegerField(source='crop.id')
    crop_category = serializers.CharField(source='crop.name')

    class Meta:
        model = CropType
        fields = ('crop_type_id', 'local_name','eng_name', 'scientific_name', 'major_nutrient', 'crop_category_id', 'crop_category')


class CropTypeSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(required=False)
    # crop_id = serializers.IntegerField(required=False)
    class Meta:
        model = CropType
        fields = ('local_name', 'eng_name', 'scientific_name', 'major_nutrient')
        extra_kwargs = {'scientific_name': {'required': False}}


class VegetableVariantSerializer(serializers.ModelSerializer):
    variant_id = serializers.IntegerField(source='id', required=False)
    crop_type_id = serializers.CharField(source='vegetable_type.id', required=False)
    crop_type = serializers.CharField(source='vegetable_type.local_name', required=False)

    class Meta:
        model = Vegetable
        fields = ('variant_id', 'name', 'soil_type', 'harvesting_period', 'expected_production', 'seasonal',
                  'crop_type_id', 'crop_type')


# Unused (just for swagger documentation purpose)
class UpazilaSearchSerializer(serializers.Serializer):
    district_id = serializers.IntegerField()

    # class Meta:
    #     models = None
    #     fields = ['division_id']


class FarmerIdSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    farmer_id = serializers.IntegerField(required=False)


class LandIdSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    land_id = serializers.IntegerField()


class OwnerIdSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    owner_id = serializers.IntegerField()

class ProductionHouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductionHouse
        exclude = ('created_at', 'created_by', "last_updated_at", "last_updated_by")


class UserIdSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()


class FarmerEditSerializer(FarmerSerializer):
    farmer_id = serializers.IntegerField(required=False)


class OwnerEditSerializer(OwnerSerializer):
    owner_id = serializers.IntegerField(required=False)


class LandEditSerializer(LandSerializer):
    land_id = serializers.IntegerField(required=False)


class CropTypeSearchSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
    crop_id = serializers.IntegerField(required=False)


class CropVariantSearchSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
    crop_type_id = serializers.IntegerField(required=False)


class LandListSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)
    # area_unit = serializers.CharField(max_length=10, read_only=True)
    area_unit = serializers.CharField(max_length=10, required=False)
    land_usage = serializers.SerializerMethodField(method_name='get_land_usage')
    division = serializers.CharField(source='land_division.name', required=False)
    district = serializers.CharField(source='land_district.name', required=False)
    upazila = serializers.CharField(source='land_upazila.name', required=False)
    owner_name = serializers.CharField(source='owner.name', required=False)
    production_house_name = serializers.CharField(source='production_house.name', required=False)
    class Meta:
        model = Land
        # fields = '__all__'
        exclude = ['created_by', 'last_updated_by', 'is_active', 'status']

    def get_land_usage(self, instance):
        try:
            seeding_id = Seeding.objects.get(land=instance.id, status="occupied")
            current_land_usage = Plot.objects.filter(seeding_id=seeding_id,
                                                     status__in=['ready', 'partially harvested']). \
                aggregate(Sum('land_usage'))
            if current_land_usage['land_usage__sum'] is None:  # when no plot is created yet
                land_usage = 0
            else:
                land_usage = current_land_usage['land_usage__sum']
        except Seeding.DoesNotExist:
            land_usage = 0
        return land_usage


