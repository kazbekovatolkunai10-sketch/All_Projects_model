from rest_framework import serializers
from .models import House,  DiabetesPrediction, Avacado, Bank, Titanic, Mushroom, Telecom

class HousePredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class DiabetesPredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabetesPrediction
        fields = '__all__'


class AvacadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avacado
        fields = '__all__'


class BankPredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class TitanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titanic
        fields = '__all__'


class MushroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mushroom
        fields = '__all__'


class TelecomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telecom
        fields = '__all__'