from django.db import models
from farm.models import Farmer, Land, Crop, CropType, Vegetable


# Create your models here.
class Seeding(models.Model):
    seed_name = models.CharField(max_length=100, null=True, blank=True)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, blank=True, null=True)
    # initial_land_usage = models.IntegerField()
    # default seeding_status: ready, occupied, damaged
    status = models.CharField(max_length=64, null=True, blank=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100, blank=True, null=True)
    max_no_of_plots = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    sensor_data_N = models.CharField(max_length=100, null=True, blank=True)
    sensor_data_P = models.CharField(max_length=100, null=True, blank=True)
    sensor_data_K = models.CharField(max_length=100, null=True, blank=True)
    # active_land_usage = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.seed_name}"

    class Meta:
        db_table = "production_seeding"


class Plot(models.Model):
    seeding = models.ForeignKey(Seeding, on_delete=models.CASCADE, blank=True, null=True)
    seed_procurement = models.CharField(max_length=50, blank=True, null=True)
    costing = models.IntegerField(default=0)
    expected_harvesting_time = models.IntegerField(default=0)
    # start_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    start_time = models.DateField(null=True, blank=True)
    # default crop_status: ready, partially harvested, fully harvested, damaged
    status = models.CharField(max_length=50, blank=True, null=True)
    total_labor_hour = models.IntegerField(default=0)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True, null=True)
    crop_type = models.ForeignKey(CropType, on_delete=models.CASCADE, blank=True, null=True)
    crop_variant = models.IntegerField(default=0)
    fertilizers = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100, null=True, blank=True)
    plot_uuid = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    land_usage = models.IntegerField(default=0)
    harvest_id = models.IntegerField(default=0)

    # ...
    def __str__(self):
        # return self.seeding, self.seed_name, self.seed_procurement, self.start_time, self.costing, \
        #        self.expected_harvesting_time, self.crop_status, self.total_labor_hour, self.farmer, self.crop_id, \
        #        self.crop_name, self.fertilizers
        return self.status

    class Meta:
        db_table = "production_plot"


class Harvesting(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, null=True, blank=True)
    harvest_cycle = models.IntegerField(default=1)
    crop_status = models.CharField(max_length=50, null=True, blank=True)
    total_labor_hour = models.IntegerField(default=0)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.CharField(max_length=64)
    processing_id = models.CharField(max_length=128, blank=True, null=True)
    # default status: partially harvested, fully harvested, packaged
    status = models.CharField(max_length=64)
    created_at = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)
    sensor_data_N = models.CharField(max_length=100, null=True, blank=True)
    sensor_data_P = models.CharField(max_length=100, null=True, blank=True)
    sensor_data_K = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.status

    class Meta:
        db_table = "production_harvesting"


# class HarvestingStatusLog(models.Model):
#     harvesting = models.ForeignKey(Harvesting, on_delete=models.CASCADE, blank=True, null=True)
#     # default crop_status: partially harvested, fully harvested
#     status = models.CharField(max_length=64, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     created_by = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = "production_harvesting_log"
