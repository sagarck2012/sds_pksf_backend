from django.db import models
from farm.models import Farmer, Land, Crop, CropType, Vegetable, ProductionHouse
from farming.models import Harvesting


class Packaging(models.Model):

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True, null=True)
    crop_type = models.ForeignKey(CropType, on_delete=models.CASCADE, blank=True, null=True)
    # crop_variant = models.IntegerField(default=0)
    quantity = models.CharField(max_length=64, blank=True, null=True)
    packaging_unit = models.CharField(max_length=64, blank=True, null=True)
    packaging_unit_per_package = models.IntegerField(default=0)
    total_no_of_sticker = models.IntegerField(default=0)
    exp_date = models.DateField(null=True, blank=True)
    # harvesting = models.ForeignKey(Harvesting, on_delete=models.CASCADE, blank=True, null=True)
    processing_id = models.CharField(max_length=128, blank=True, null=True)
    processing_date = models.DateField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100,  blank=True, null=True)

    def __str__(self):
        return self.processing_id

    class Meta:
        db_table = "process_packaging_master"


class PackagingDetail(models.Model):
    process_packaging_master = models.ForeignKey(Packaging, on_delete=models.CASCADE, blank=True, null=True)
    processing_id = models.CharField(max_length=128, blank=True, null=True)
    sticker_qr_code = models.CharField(max_length=255)
    sticker_bar_code = models.CharField(max_length=20)
    # reprinted_against = models.CharField(max_length=255, blank=True, null=True)
    # manual_print = models.BooleanField(default=False)
    process_crating_master = models.ForeignKey('Crating', on_delete=models.CASCADE, blank=True, null=True)
    process_shipping_master = models.ForeignKey('Shipping', on_delete=models.CASCADE, blank=True, null=True)
    process_receiving_master = models.ForeignKey('Receiving', on_delete=models.CASCADE, blank=True, null=True)
    shipping_id = models.CharField(max_length=128, blank=True, null=True)
    generated_by = models.CharField(max_length=100)
    generated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # Default: generated; printed, damaged, crated, shipped, received, deactivated (due to packaging edit)
    status = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.processing_id

    class Meta:
        db_table = "process_packaging_detail"


class PackagingDamaged(models.Model):
    process_packaging_master = models.ForeignKey(Packaging, on_delete=models.CASCADE, blank=True, null=True)
    processing_id = models.CharField(max_length=128, blank=True, null=True)
    sticker_qr_code = models.CharField(max_length=255)
    sticker_bar_code = models.CharField(max_length=20)
    # reprinted_against = models.CharField(max_length=255, blank=True, null=True)
    # manual_print = models.BooleanField(default=False)
    process_crating_master = models.ForeignKey('Crating', on_delete=models.CASCADE, blank=True, null=True)
    process_shipping_master = models.ForeignKey('Shipping', on_delete=models.CASCADE, blank=True, null=True)
    process_receiving_master = models.ForeignKey('Receiving', on_delete=models.CASCADE, blank=True, null=True)
    shipping_id = models.CharField(max_length=128, blank=True, null=True)
    deleted_by = models.CharField(max_length=100)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # Default: damaged
    status = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.processing_id

    class Meta:
        db_table = "process_packaging_damaged"


class CrateInfo(models.Model):
    crate_no = models.CharField(max_length=255, null=True, blank=True)
    bar_code = models.CharField(max_length=255, null=True, blank=True)
    dimension = models.CharField(max_length=255, null=True, blank=True, editable=True)
    empty_weight = models.IntegerField(null=True, blank=True)
    max_weight = models.IntegerField(null=True, blank=True)
    production_house = models.ForeignKey(ProductionHouse, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, default='ready')  # default : ready, crated , shipped
    delete_status = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    last_updated_at = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=100, null=True, blank=True)

    # ...
    def __str__(self):
        # return self.crate_no, self.capacity, self.total_number_of_package, self.weight
        return self.crate_no


class Crating(models.Model):
    crate = models.ForeignKey(CrateInfo, on_delete=models.CASCADE, blank=True, null=True)
    total_no_of_package = models.IntegerField(default=0)
    process_shipping_master = models.ForeignKey('Shipping', on_delete=models.CASCADE, blank=True, null=True)
    crating_code = models.CharField(max_length=12, blank=True, null=True)
    shipping_id = models.CharField(max_length=128, blank=True, null=True)
    process_receiving_master = models.ForeignKey('Receiving', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)  # Default: ready, crated, shipped
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    create_by = models.CharField(max_length=100)
    modify_at = models.DateTimeField(null=True, blank=True)
    modify_by = models.CharField(max_length=100)

    # ...

    def __str__(self):
        return self.crate

    class Meta:
        db_table = "process_crating_master"


class CratingDetail(models.Model):
    process_crating_master = models.ForeignKey(Crating, on_delete=models.CASCADE, blank=True, null=True)
    # crate = models.ForeignKey(CrateInfo, on_delete=models.CASCADE, blank=True, null=True)
    process_packaging_detail = models.ForeignKey(PackagingDetail, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)  # Default: ready, crated, shipped, received
    scanned_by = models.CharField(max_length=100)
    scanned_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    removed_by = models.CharField(max_length=100)
    removed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.process_crating_master

    class Meta:
        db_table = "process_crating_detail"


class Shipping(models.Model):
    destination = models.TextField()
    destination_contact = models.CharField(max_length=50, null=True, blank=True)
    origin = models.TextField()
    origin_contact = models.CharField(max_length=50, null=True, blank=True)
    shipping_agent = models.CharField(max_length=50)
    shipping_contact = models.CharField(max_length=50, null=True, blank=True)
    expected_shipping_date = models.DateTimeField(null=True, blank=True)
    expected_arrival_date = models.DateTimeField(null=True, blank=True)
    total_no_of_crate = models.IntegerField(default=0)
    shipping_code = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=24, default='ready')  # default: ready; shipped, received
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    last_updated_at = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.destination

    class Meta:
        db_table = "process_shipping_master"


class ShippingDetail(models.Model):
    process_shipping_master = models.ForeignKey(Shipping, on_delete=models.CASCADE, blank=True, null=True)
    process_crating_master = models.ForeignKey(Crating, on_delete=models.CASCADE, blank=True, null=True)
    shipping_id = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=24, default='ready')  # default: ready, shipped; delivered
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.process_shipping_master

    class Meta:
        db_table = "process_shipping_detail"


class Receiving(models.Model):
    hub_address = models.TextField()
    contact_no = models.CharField(max_length=16)
    shipping_id = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=24)  # default: delivered
    total_no_of_crate = models.IntegerField(default=0)
    received_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    received_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.hub_address

    class Meta:
        db_table = "process_receiving_master"


class ReceivingDetail(models.Model):
    process_receiving_master = models.ForeignKey(Receiving, on_delete=models.CASCADE, blank=True, null=True)
    contact_no = models.CharField(max_length=16)
    status = models.CharField(max_length=24)  # received
    shipping_id = models.CharField(max_length=128, blank=True, null=True)
    process_crating_master = models.ForeignKey(Crating, on_delete=models.CASCADE, blank=True, null=True)
    received_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    received_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.process_receiving_master

    class Meta:
        db_table = "process_receiving_detail"
