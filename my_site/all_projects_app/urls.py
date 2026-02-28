from django.urls import path, include
from .views import (HousePredict, DiabetesPredict, AvacadoPredict, BankPredict, TitanicPredict,
                    MushroomPredict, TelecomPredict)
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('house', HousePredict.as_view(), name='house_model'),
    path('diabetes', DiabetesPredict.as_view(), name='diabetes_model'),
    path('avacado', AvacadoPredict.as_view(), name='avacado_model'),
    path('bank', BankPredict.as_view(), name='bank_model'),
    path('titanic', TitanicPredict.as_view(), name='titanic_model'),
    path('mushroom', MushroomPredict.as_view(), name='mushroom_model'),
    path('telecom', TelecomPredict.as_view(), name='telecom_model')
]




