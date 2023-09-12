from rest_framework import serializers
from processing.models import *
from farm.models import CropType


class HarvestSearchSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    crop_type_id = serializers.IntegerField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()

    class Meta:
        model = None
        fields = ['crop_id', 'start_date', 'end_date', 'user_id']


class PackagingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)  # required = False to bypass serializer.is_valid()
    harvest_id_list = serializers.CharField(required=False)

    class Meta:
        model = Packaging
        fields = ('packaging_unit', 'packaging_unit_per_package', 'total_no_of_sticker',
                  'user_id', 'harvest_id_list')


class PackagingSearchSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    # crop_id = serializers.IntegerField()
    crop_type_id = serializers.IntegerField()
    # start_date = serializers.CharField()
    # end_date = serializers.CharField()

    class Meta:
        model = None
        # fields = ['start_date', 'end_date', 'user_id', 'crop_type_id']
        fields = ['user_id', 'crop_type_id']


class StickerSearchSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    processing_id = serializers.CharField()

    class Meta:
        model = None
        fields = ['processing_id']


class StickerDamagedSerializer(serializers.Serializer):
    sticker_id = serializers.IntegerField(required=True)
    comment = serializers.CharField(required=True)
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = None
        fields = ['sticker_id', 'comment', 'user_id']


class StickerPrintedSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    sticker_id_list = serializers.CharField(required=True)

    class Meta:
        model = None
        fields = ['sticker_id', 'user_id']


class CrateRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrateInfo
        exclude = ('last_updated_by', 'last_updated_at', 'status', 'delete_status')


class CratingDetailSerializer(serializers.ModelSerializer):
    crate_info = serializers.SerializerMethodField(method_name='get_crate_info')

    class Meta:
        model = Crating
        exclude = ('crate', 'process_shipping_master', 'process_receiving_master',)

    def get_crate_info(self, instance):
        crate = CrateInfo.objects.get(id=instance.crate.id)
        crate_info = dict()
        crate_info['crate_no'] = crate.crate_no
        crate_info['crate_bar_code'] = crate.bar_code
        crate_info['crate_bar_code'] = crate.bar_code
        crate_info['production_house'] = crate.production_house.name
        crate_info['status'] = crate.status
        return crate_info


class PackagingDetailSerializer(serializers.ModelSerializer):
    crop_type = serializers.SerializerMethodField(method_name='get_crop_type')
    quantity = serializers.SerializerMethodField(method_name='get_quantity')

    class Meta:
        model = PackagingDetail
        exclude = ('process_packaging_master', 'process_crating_master', 'process_shipping_master',
                   'process_receiving_master',)

    def get_crop_type(self, instance):
        packaging_master = Packaging.objects.get(processing_id=instance.processing_id)
        crop_type = dict()
        crop_type['local_name'] = packaging_master.crop_type.local_name
        crop_type['eng_name'] = packaging_master.crop_type.eng_name
        return crop_type

    def get_quantity(self, instance):
        packaging_master = Packaging.objects.get(processing_id=instance.processing_id)
        quantity = dict()
        quantity['unit'] = packaging_master.packaging_unit
        quantity['amount'] = packaging_master.packaging_unit_per_package
        return quantity


class StickerDetailSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    harvest_id = serializers.IntegerField(required=True)

    class Meta:
        model = None
        fields = ['user_id', 'harvest_id']


class ShippingInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='created_by')

    class Meta:
        model = Shipping
        # fields = '__all__'
        exclude = ('last_updated_by', 'last_updated_at', 'status')


class PackagingEditSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)  # required = False to bypass serializer.is_valid()
    packaging_id = serializers.IntegerField(required=True)

    class Meta:
        model = Packaging
        fields = ('packaging_unit', 'packaging_unit_per_package', 'total_no_of_sticker',
                  'user_id', 'packaging_id')
