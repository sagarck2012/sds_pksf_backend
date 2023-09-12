from rest_framework import serializers
from farming.models import Seeding, Plot, Harvesting
from django.db.models import Sum


class SeedingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)
    land_id = serializers.IntegerField(required=True)
    farmer_id = serializers.IntegerField(required=True)
    # crop_id = serializers.IntegerField(required=True)
    # crop_type_id = serializers.IntegerField(required=True)
    # crop_variant_id = serializers.IntegerField(required=True)
    # no_of_plots = serializers.IntegerField(required=True)
    # sensor_data_N = serializers.CharField(required=False)
    # sensor_data_P = serializers.CharField(required=False)
    # sensor_data_K = serializers.CharField(required=False)

    class Meta:
        model = Seeding
        exclude = ['land', 'farmer', 'status', 'created_by', 'last_updated_by']


class PlotSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Plot
        # fields = '__all__'
        exclude = ('status', 'created_at', 'created_by', 'last_updated_at', 'last_updated_by', 'harvest_id', 'plot_uuid',
                   'comment')


# Unused (just for swagger documentation purpose)
class LandStatusSerializer(serializers.Serializer):
    land_id = serializers.IntegerField()
    land_status = serializers.CharField(label="damaged")
    update_by = serializers.IntegerField()
    update_at = serializers.CharField(label="2020-11-15")


class PlotStatusSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    plot_id = serializers.IntegerField(required=True)
    plot_status = serializers.CharField(required=True)


class SeedingIdSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    seeding_id = serializers.IntegerField()


class HarvestingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)
    plot_id = serializers.IntegerField(required=True)

    class Meta:
        model = Harvesting
        fields = ('crop_status', 'total_labor_hour', 'farmer', 'quantity', 'sensor_data_N', 'sensor_data_P',
                  'sensor_data_K', 'user_id', 'plot_id', 'status')


class PlotEditSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)
    plot_id = serializers.IntegerField(required=True)

    class Meta:
        model = Plot
        # fields = '__all__'
        exclude = ('status', 'created_at', 'created_by', 'last_updated_at', 'last_updated_by', 'harvest_id', 'plot_uuid',
                   'comment')


class PlotListSerializer(serializers.ModelSerializer):
    crop_name = serializers.CharField(source='crop')
    crop_type_name = serializers.CharField(source='crop_type')

    class Meta:
        model = Plot
        fields = ('id', 'crop_name', 'crop_type_name', 'seeding', 'seed_procurement', 'costing',
                  'expected_harvesting_time', 'start_time', 'status', 'total_labor_hour',
                  'fertilizers', 'comment', 'land_usage')


class HarvestingEditSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)
    harvesting_id = serializers.IntegerField(required=True)
    plot_id = serializers.IntegerField(required=True)

    class Meta:
        model = Harvesting
        fields = ('crop_status', 'total_labor_hour', 'farmer', 'quantity', 'sensor_data_N', 'sensor_data_P',
                  'sensor_data_K', 'user_id', 'harvesting_id', 'plot_id', 'status')


class HarvestListSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    plot_id = serializers.IntegerField(required=True)


class HarvestingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Harvesting
        fields = ('crop_status', 'total_labor_hour', 'farmer', 'quantity', 'sensor_data_N', 'sensor_data_P',
                  'sensor_data_K', 'plot_id', 'status', 'processing_id')


class SeedingEditSerializer(serializers.ModelSerializer):
    seeding_id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(required=False)
    land_id = serializers.IntegerField(required=True)
    farmer_id = serializers.IntegerField(required=True)
    # crop_id = serializers.IntegerField(required=True)
    # crop_type_id = serializers.IntegerField(required=True)
    # crop_variant_id = serializers.IntegerField(required=True)
    # no_of_plots = serializers.IntegerField(required=True)
    # sensor_data_N = serializers.CharField(required=False)
    # sensor_data_P = serializers.CharField(required=False)
    # sensor_data_K = serializers.CharField(required=False)

    class Meta:
        model = Seeding
        exclude = ['land', 'farmer', 'status', 'created_by', 'last_updated_by']


class SeedingStatusSerializer(serializers.Serializer):
    seeding_id = serializers.IntegerField()
    seeding_status = serializers.CharField(label="damaged")
    user_id = serializers.IntegerField()


class SeedingListSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False)
    land_id = serializers.IntegerField(required=True)
    land_usage = serializers.SerializerMethodField(method_name='get_land_usage')

    class Meta:
        model = Seeding
        exclude = ['land', 'farmer', 'status', 'created_by', 'last_updated_by']

    def get_land_usage(self, instance):
        try:
            # seeding_id = Seeding.objects.get(land=instance.id, status="occupied")
            current_land_usage = Plot.objects.filter(seeding_id=instance.id,
                                                     status__in=['ready', 'partially harvested']). \
                aggregate(Sum('land_usage'))
            if current_land_usage['land_usage__sum'] is None:  # when no plot is created yet
                land_usage = 0
            else:
                land_usage = current_land_usage['land_usage__sum']
        except Seeding.DoesNotExist:
            land_usage = 0
        return land_usage
