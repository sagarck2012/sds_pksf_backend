from django.db import models


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=100)
    division_code = models.CharField(max_length=20, blank=True, null=True)

    # ...
    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    district_code = models.CharField(max_length=20, blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True)

    # ...
    def __str__(self):
        return self.name


class Upazila(models.Model):
    name = models.CharField(max_length=100)
    upazila_code = models.CharField(max_length=20, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    # ...
    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)
    delete_status = models.IntegerField(default=0)


    # ...
    def __str__(self):
        return self.name


class CropType(models.Model):
    eng_name = models.CharField(max_length=100)
    local_name = models.CharField(max_length=100)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    photo = models.TextField(null=True, blank=True)
    scientific_name = models.CharField(max_length=100, null=True, blank=True)
    major_nutrient = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100, null=True, blank=True)
    delete_status = models.IntegerField(default=0)

    # ...
    def __str__(self):
        return self.local_name


class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    # vegetable_type: same as crop_type_id from api request
    vegetable_type = models.ForeignKey(CropType, on_delete=models.CASCADE)
    # photo = models.ImageField(upload_to='images/crops/', height_field=None, width_field=None, max_length=100,
    #                           blank=True, null=True)
    soil_type = models.CharField(max_length=255)
    # Duration in months
    # harvesting_period = models.IntegerField(default=0)
    # Duration: June-July
    harvesting_period = models.CharField(max_length=100)
    expected_production = models.CharField(max_length=100, null=True, blank=True)
    seasonal = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)
    delete_status = models.IntegerField(default=0)

    # ...
    # def __str__(self):
    #     return self.name, self.vegetable_type, self.local_name, self.scientific_name, self.major_nutrient, \
    #            self.soil_type, self.seasonal, self.harvesting_period
    def __str__(self):
        return self.name


class ProductionHouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    head_office = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=4)
    last_updated_at = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    class meta:
        db_table = "farm_production_house"


class Farmer(models.Model):
    present_division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True, related_name='farmer_present_division')
    present_district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True, related_name='farmer_present_district')
    present_upazilla = models.ForeignKey(Upazila, on_delete=models.CASCADE, blank=True, null=True, related_name='farmer_present_upazilla')
    present_post_code = models.CharField(max_length=4, blank=True, null=True)
    present_address = models.CharField(max_length=200, null=True, blank=True)
    permanent_division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True)
    permanent_district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    permanent_upazilla = models.ForeignKey(Upazila, on_delete=models.CASCADE, blank=True, null=True)
    permanent_post_code = models.CharField(max_length=4, blank=True, null=True)
    permanent_address = models.CharField(max_length=200, null=True, blank=True)
    crop_list = models.CharField(max_length=200, null=True, blank=True)
    total_land = models.IntegerField(default=0)
    name = models.CharField(max_length=70)
    nid_number = models.CharField(max_length=10, null=True, blank=True)
    # photo = models.BinaryField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    secondary_contact_no = models.CharField(max_length=11, blank=True, null=True)
    is_local = models.BooleanField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)
    delete_status = models.IntegerField(default=0)

    # ...
    def __str__(self):
        # return self.name, self.phone_number, self.nid_number, self.crop_list, self.total_land, self.is_local, \
        #        self.permanent_address, self.post_code, self.secondary_contact
        return self.name


class Owner(models.Model):
    present_division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='owner_present_division')
    present_district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='owner_present_district')
    present_upazilla = models.ForeignKey(Upazila, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='owner_present_upazilla')
    present_post_code = models.CharField(max_length=4, blank=True, null=True)
    present_address = models.CharField(max_length=200, null=True, blank=True)
    permanent_division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True)
    permanent_district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    permanent_upazilla = models.ForeignKey(Upazila, on_delete=models.CASCADE, blank=True, null=True)
    permanent_post_code = models.CharField(max_length=4, blank=True, null=True)
    permanent_address = models.CharField(max_length=200, null=True, blank=True)
    crop_list = models.CharField(max_length=100)
    total_land = models.IntegerField()
    name = models.CharField(max_length=70)
    nid_number = models.CharField(max_length=10)
    # photo = models.ImageField(upload_to='images/farmers/', height_field=None, width_field=None, max_length=100,
    #                           blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    secondary_contact_no = models.CharField(max_length=200, blank=True, null=True)
    is_local = models.BooleanField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100, null=True, blank=True)
    delete_status = models.IntegerField(default=0)

    # ...
    def __str__(self):
        # return self.name, self.phone_number, self.nid_number, self.crop_list, self.total_land, self.is_local, \
        #        self.permanent_address, self.post_code, self.secondary_contact
        return self.name


class Land(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    longitude = models.CharField(max_length=11)
    latitude = models.CharField(max_length=11)
    area = models.FloatField()
    # photo = models.ImageField(upload_to='images/lands/', height_field=None, width_field=None, max_length=100,
    #                           blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    soil_type = models.CharField(max_length=100, null=True, blank=True)
    climate_type = models.CharField(max_length=100, null=True, blank=True)
    flood_prone = models.BooleanField(default=None)
    farmer_is_owner = models.BooleanField(default=None)
    # status: ready, partially occupied, fully occupied
    status = models.CharField(max_length=20, null=True, blank=True)
    land_division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True)
    land_district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    land_upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE, blank=True, null=True)
    post_code = models.CharField(max_length=4, null=True, blank=True)
    thana = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    production_house = models.ForeignKey(ProductionHouse, on_delete=models.CASCADE)

    # ...
    def __str__(self):
        # return self.owner, self.longitude, self.latitude, self.area, self.photo, self.soil_type, self.flood_prone,\
        #        self.climate_type, self.farmer_is_owner, self.status, self.post_code
        return f"{self.owner.name}"

    class Meta:
        db_table = "farm_land"


# class CropTypeConfig(models.Model):
#     crop_type = models.ForeignKey(CropType, on_delete=models.CASCADE)
#     unit = models.CharField(max_length=24)
#     unit_per_package = models.CharField(max_length=24)
#     expected_exp_days = models.CharField(max_length=64)
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     created_by = models.CharField(max_length=100)
#     last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     last_updated_by = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"{self.crop_type.name}"




