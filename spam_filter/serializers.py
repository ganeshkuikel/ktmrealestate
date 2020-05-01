from rest_framework import serializers
from .models import Spam_filtering

class Spam_filteringSerializers(serializers.ModelSerializer):

    class Meta:
        model = Spam_filtering
        fields = '__all__'


