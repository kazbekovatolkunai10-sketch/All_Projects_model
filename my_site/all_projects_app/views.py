from .serializer import (HousePredictSerializer, DiabetesPredictSerializer,
                        AvacadoSerializer, BankPredictSerializer, TitanicSerializer,
                        MushroomSerializer, TelecomSerializer, StudentPerformanceSerializer)
import os
import  joblib
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response


house_model_path = os.path.join(settings.BASE_DIR, 'house_log_model.pkl')
model = joblib.load(house_model_path)

house_scaler_path = os.path.join(settings.BASE_DIR, 'house_scaler.pkl')
scaler = joblib.load(house_scaler_path)

Neighborhoods = [
    'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor', 'Edwards',
    'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes',
    'NoRidge', 'NridgHt', 'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst',
    'StoneBr', 'Timber', 'Veenker'
]

class HousePredict(views.APIView):
    def post(self, request):
        instance = HousePredictSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_neighborhood = data.get('Neighborhood')
            neighborhood1_0 = [1 if new_neighborhood == i else 0 for i in Neighborhoods]
            features = [data['GrLivArea'],
                        data['YearBuilt'],
                        data['GarageCars'],
                        data['TotalBsmtSF'],
                        data['FullBath'],
                        data['OverallQual'],
                        ] + neighborhood1_0
            scaler_data = scaler.transform([features])
            pred = model.predict(scaler_data)[0]
            house = instance.save(predicted_price=pred)

            return Response({'PredictPrice': round(pred),
                             'data': HousePredictSerializer(house).data}, status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


model_path = os.path.join(settings.BASE_DIR, 'diabetes_log_model.pkl')
diabetes_model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'diabetes_scalers.pkl')
diabetes_scaler = joblib.load(scaler_path)


class DiabetesPredict(views.APIView):
    def post(self, request):
        instance = DiabetesPredictSerializer(data=request.data)

        if instance.is_valid():
            data = instance.validated_data

            features = [
                data['Pregnancies'],
                data['Glucose'],
                data['BloodPressure'],
                data['SkinThickness'],
                data['Insulin'],
                data['BMI'],
                data['DiabetesPedigreeFunction'],
                data['Age'],
            ]

            scaler_data = diabetes_scaler.transform([features])
            pred_proba = diabetes_model.predict_proba(scaler_data)[0][1]

            result = 'Yes' if pred_proba > 0.5 else 'No'

            diabetes = instance.save(
                predicted_label=result,
                probability=pred_proba
            )

            return Response({
                'Diabetes': result,
                'Probability': round(pred_proba, 2),
                'data': DiabetesPredictSerializer(diabetes).data
            }, status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)




model_path = os.path.join(settings.BASE_DIR, 'avacodo_log_model.pkl')
avacado_model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'avacado_scalers.pkl')
avacado_scaler = joblib.load(scaler_path)


class AvacadoPredict(views.APIView):
    def post(self, request):
        instance = AvacadoSerializer(data=request.data)

        if instance.is_valid():
            data = instance.validated_data

            avacado_color = data.get('color_category')
            avacado_color_1_0 = [
                1 if avacado_color == 'dark_green' else 0,
                1 if avacado_color == 'green' else 0,
                1 if avacado_color == 'purple' else 0
            ]
            features = [
                data['firmness'],
                data['hue'],
                data['saturation'],
                data['brightness'],
                data['sound_db'],
                data['weight_g'],
                data['size_cm3'],
            ] + avacado_color_1_0

            scaled_data = avacado_scaler.transform([features])
            pred = avacado_model.predict(scaled_data)[0]

            labels = {
                0: 'hard',
                1: 'pre-conditioned',
                2: 'breaking',
                3: 'firm-ripe',
                4: 'ripe',
            }

            pred_label = labels[int(pred)]

            avacado = instance.save(predicted_label=pred_label)

            return Response({
                'predict': pred_label,
                'data': AvacadoSerializer(avacado).data
            }, status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)




model_path = os.path.join(settings.BASE_DIR, 'bank_model.pkl')
bank_model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'bank_scaler.pkl')
bank_scaler = joblib.load(scaler_path)


gender_list = ['male']
education_list = ['Bachelor', 'Doctorate', 'High School', 'Master']
ownership_list = ['OTHER', 'OWN', 'RENT']
loan_intent_list = ['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE']
previous_loan_defaults_on_file_list = ['Yes']


class BankPredict(views.APIView):

    def post(self, request):
        instance = BankPredictSerializer(data=request.data)

        if instance.is_valid():
            data = instance.validated_data

            person_gender = data.get('person_gender')
            person_gender_1_0 = [1 if person_gender == i else 0 for i in gender_list]

            person_education = data.get('person_education')
            person_education_1_0 = [
                1 if person_education == i else 0 for i in education_list
            ]

            person_home_ownership = data.get('person_home_ownership')
            person_home_ownership_1_0 = [
                1 if person_home_ownership == i else 0 for i in ownership_list
            ]

            loan_intent = data.get('loan_intent')
            loan_intent_1_0 = [
                1 if loan_intent == i else 0 for i in loan_intent_list
            ]

            previous_loan_defaults_on_file = data.get('previous_loan_defaults_on_file')
            previous_loan_defaults_on_file_1_0 = [
                1 if previous_loan_defaults_on_file == i else 0
                for i in previous_loan_defaults_on_file_list
            ]

            features = [
                data['person_age'],
                data['person_income'],
                data['person_emp_exp'],
                data['loan_famnt'],
                data['loan_int_rate'],
                data['loan_percent_income'],
                data['cb_person_cred_hist_length'],
                data['credit_score'],
            ] + person_gender_1_0 + person_education_1_0 + \
                person_home_ownership_1_0 + loan_intent_1_0 + \
                previous_loan_defaults_on_file_1_0

            scaler_data = bank_scaler.transform([features])
            pred = bank_model.predict(scaler_data)[0]

            answer = 'Approve' if pred == 1 else 'Rejected'

            bank = instance.save(predicted_result=answer)

            return Response({
                'Answer': answer,
                'data': BankPredictSerializer(bank).data
            }, status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)



model_path = os.path.join(settings.BASE_DIR, 'titanic_model.pkl')
titanic_model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'titanic_scaler.pkl')
titanic_scaler = joblib.load(scaler_path)


class TitanicPredict(views.APIView):

    def post(self, request):
        instance = TitanicSerializer(data=request.data)

        if instance.is_valid():
            data = instance.validated_data

            person_sex = data.get('Sex')
            person_sex_1_0 = [
                1 if person_sex == 'male' else 0
            ]

            person_embarked = data.get('embarked')
            person_embarked_1_0 = [
                1 if person_embarked == 'Q' else 0,
                1 if person_embarked == 'S' else 0
            ]

            features = [
                data['Pclass'],
                data['age'],
                data['Fare'],
            ] + person_sex_1_0 + person_embarked_1_0

            scaler_data = titanic_scaler.transform([features])
            pred = titanic_model.predict(scaler_data)[0]

            answer = 'alive' if pred == 1 else 'drowed'

            titanic = instance.save(predicted_result=answer)

            return Response({
                'Answer': answer,
                'data': TitanicSerializer(titanic).data
            }, status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)



model_path = os.path.join(settings.BASE_DIR, 'mushrooms_random_model.pkl')
mushrooms_model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'mushrooms_scaler.pkl')
mushrooms_scaler = joblib.load(scaler_path)


cap_shapes = ['c', 'f', 'k', 's', 'x']
cap_surfaces = ['g', 's', 'y']
cap_colors = ['c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y']
odors = ['c', 'f', 'l', 'm', 'n', 'p', 's', 'y']
gill_colors = ['e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y']
stalk_roots = ['c', 'e', 'r']
stalk_surfaces = ['k', 's', 'y']
stalk_colors = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
veil_colors = ['o', 'w', 'y']
ring_types = ['f', 'l', 'n', 'p']
spore_print_colors = ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y']
populations = ['c', 'n', 's', 'v', 'y']
habitats = ['g', 'l', 'm', 'p', 'u', 'w']


class MushroomPredict(views.APIView):

    def post(self, request):
        instance = MushroomSerializer(data=request.data)

        if instance.is_valid():
            data = instance.validated_data

            cap_shape = [1 if data['cap_shape'] == i else 0 for i in cap_shapes]
            cap_surface = [1 if data['cap_surface'] == i else 0 for i in cap_surfaces]
            cap_color = [1 if data['cap_color'] == i else 0 for i in cap_colors]
            bruises = [1 if data['bruises'] == 't' else 0]
            odor = [1 if data['odor'] == i else 0 for i in odors]
            gill_attachment = [1 if data['gill_attachment'] == 'f' else 0]
            gill_spacing = [1 if data['gill_spacing'] == 'w' else 0]
            gill_size = [1 if data['gill_size'] == 'n' else 0]
            gill_color = [1 if data['gill_color'] == i else 0 for i in gill_colors]
            stalk_shape = [1 if data['stalk_shape'] == 't' else 0]
            stalk_root = [1 if data['stalk_root'] == i else 0 for i in stalk_roots]
            stalk_surface_above = [1 if data['stalk_surface_above_ring'] == i else 0 for i in stalk_surfaces]
            stalk_surface_below = [1 if data['stalk_surface_below_ring'] == i else 0 for i in stalk_surfaces]
            stalk_color_above = [1 if data['stalk_color_above_ring'] == i else 0 for i in stalk_colors]
            stalk_color_below = [1 if data['stalk_color_below_ring'] == i else 0 for i in stalk_colors]
            veil_color = [1 if data['veil_color'] == i else 0 for i in veil_colors]
            veil_type = [1 if data['veil_type'] == 'p' else 0]
            ring_number = [1 if data['ring_number'] == i else 0 for i in ['o', 't']]
            ring_type = [1 if data['ring_type'] == i else 0 for i in ring_types]
            spore_print_color = [1 if data['spore_print_color'] == i else 0 for i in spore_print_colors]
            population = [1 if data['population'] == i else 0 for i in populations]
            habitat = [1 if data['habitat'] == i else 0 for i in habitats]

            features = (
                cap_shape + cap_surface + cap_color + bruises + odor +
                gill_attachment + gill_spacing + gill_size + gill_color +
                stalk_shape + stalk_root + stalk_surface_above + stalk_surface_below +
                stalk_color_above + stalk_color_below + veil_color + veil_type +
                ring_number + ring_type + spore_print_color + population + habitat
            )

            scaled_data = mushrooms_scaler.transform([features])
            proba = mushrooms_model.predict_proba(scaled_data)[0][1]

            label = "Yes" if proba > 0.5 else "No"

            mushroom = instance.save(
                predicted_label=label,
                probability=proba
            )

            return Response({
                'poisonous': label,
                'probability': round(proba, 2),
                'data': MushroomSerializer(mushroom).data
            }, status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)



model_path = os.path.join(settings.BASE_DIR, 'telecom_model.pkl')
telecom_model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'telecom_scaler.pkl')
telecom_scaler = joblib.load(scaler_path)


gender_list = ['Male']

Partner_list = ['No']

Dependents_list = ['Yes']

PhoneService_list = ['Yes']

MultipleLines_list = ['No', 'Yes']

InternetService_list = ['Fiber optic', 'No']

OnlineSecurity_list = ['Yes', 'No internet service']

OnlineBackup_list = ['No', 'No internet service']

DeviceProtection_list = ['Yes', 'No internet service']

TechSupport_list = ['Yes', 'No internet service']

StreamingTV_list = ['Yes', 'No internet service']

StreamingMovies_list = ['Yes', 'No internet service']

Contract_list = ['One year', 'Two year']

PaperlessBilling_list = ['No']

PaymentMethod_list = ['Mailed check', 'Bank transfer (automatic)',
    'Credit card (automatic)']


class TelecomPredict(views.APIView):
    def post(self, request):
        instance = TelecomSerializer(data=request.data)

        if instance.is_valid():
            data = instance.validated_data

            gender = [1 if data['gender'] == i else 0 for i in gender_list]
            Partner = [1 if data['Partner'] == i else 0 for i in Partner_list]
            Dependents = [1 if data['Dependents'] == i else 0 for i in Dependents_list]
            PhoneService = [1 if data['PhoneService'] == i else 0 for i in PhoneService_list]
            MultipleLines = [1 if data['MultipleLines'] == i else 0 for i in MultipleLines_list]
            InternetService = [1 if data['InternetService'] == i else 0 for i in InternetService_list]
            OnlineSecurity = [1 if data['OnlineSecurity'] == i else 0 for i in OnlineSecurity_list]
            OnlineBackup = [1 if data['OnlineBackup'] == i else 0 for i in OnlineBackup_list]
            DeviceProtection = [1 if data['DeviceProtection'] == i else 0 for i in DeviceProtection_list]
            TechSupport = [1 if data['TechSupport'] == i else 0 for i in TechSupport_list]
            StreamingTV = [1 if data['StreamingTV'] == i else 0 for i in StreamingTV_list]
            StreamingMovies = [1 if data['StreamingMovies'] == i else 0 for i in StreamingMovies_list]
            Contract = [1 if data['Contract'] == i else 0 for i in Contract_list]
            PaperlessBilling = [1 if data['PaperlessBilling'] == i else 0 for i in PaperlessBilling_list]
            PaymentMethod = [1 if data['PaymentMethod'] == i else 0 for i in PaymentMethod_list]

            features = [
                data['SeniorCitizen'],
                data['tenure'],
                data['MonthlyCharges'],
                data['TotalCharges']
            ] + gender + Partner + Dependents + PhoneService + \
                MultipleLines + InternetService + OnlineSecurity + \
                OnlineBackup + DeviceProtection + TechSupport + \
                StreamingTV + StreamingMovies + Contract + \
                PaperlessBilling + PaymentMethod
            print(data)

            scaled = telecom_scaler.transform([features])
            proba = telecom_model.predict_proba(scaled)[0][1]

            label = "Stay" if proba > 0.5 else "Don't stay"

            telecom = instance.save(
                predicted_label=label,
                probability=proba
            )

            return Response({
                "Answer": label,
                "Probability": round(proba, 2),
                "data": TelecomSerializer(telecom).data
            }, status=status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


model_path = os.path.join(settings.BASE_DIR, 'my_site/hremploye_model.pkl')
model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'my_site/hremploye_scaler.pkl')
scaler = joblib.load(scaler_path)

BusinessTravel_list = ['Travel_Frequently', 'Travel_Rarely']
Department_list = ['Research & Development', 'Sales']
EducationField_list = ['Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree']
Gender_list = ['Male']
JobRole_list = ['Human Resources', 'Laboratory Technician', 'Manager', 'Manufacturing Director',
    'Research Director', 'Research Scientist', 'Sales Executive', 'Sales Representative']
MaritalStatus_list = ['Married', 'Single']
OverTime_list = ['Yes']


class HREmployeePredictAPIView(views.APIView):
    def post(self, request):
        try:
            data_dict = request.data.copy()
            BusinessTravel = data_dict.pop('BusinessTravel')
            BusinessTravel_encoded = [1 if BusinessTravel == i else 0 for i in BusinessTravel_list]

            Department = data_dict.pop('Department')
            Department_encoded = [1 if Department == i else 0 for i in Department_list]

            EducationField = data_dict.pop('EducationField')
            EducationField_encoded = [1 if EducationField == i else 0 for i in EducationField_list]

            Gender = data_dict.pop('Gender')
            Gender_encoded = [1 if Gender == i else 0 for i in Gender_list]

            JobRole = data_dict.pop('JobRole')
            JobRole_encoded = [1 if JobRole == i else 0 for i in JobRole_list]

            MaritalStatus = data_dict.pop('MaritalStatus')
            MaritalStatus_encoded = [1 if MaritalStatus == i else 0 for i in MaritalStatus_list]


            OverTime = data_dict.pop('OverTime')
            OverTime_encoded = [1 if OverTime == i else 0 for i in OverTime_list]

            final_data = (list(data_dict.values()) + BusinessTravel_encoded + Department_encoded
                + EducationField_encoded + Gender_encoded + JobRole_encoded+ MaritalStatus_encoded
                + OverTime_encoded)

            scaled = scaler.transform([final_data])
            pred = model.predict(scaled)[0]
            answer = "Will Leave" if pred == 1 else "Will Stay"

            return Response({"prediction": answer})


        except Exception as e:return Response({"error": str(e)},
                                              status=status.HTTP_400_BAD_REQUEST)



model_path=os.path.join(settings.BASE_DIR,'my_site/student_model.pkl')
model=joblib.load(model_path)

scaler_path=os.path.join(settings.BASE_DIR,'my_site/student_scaler.pkl')
scaler=joblib.load(scaler_path)


gender_list=['male']
race_list=['group B','group C','group D','group E']
parent_edu_list=[
"bachelor's degree",
'high school',
"master's degree",
'some college',
'some high school'
]
lunch_list=['standard']
test_course_list=['none']


class StudentPredictAPIView(views.APIView):
    def post(self,request):
        serializer=StudentPerformanceSerializer(data=request.data)
        if serializer.is_valid():
            try:
                data_dict=serializer.validated_data.copy()

                gender=data_dict.pop('gender')
                gender_encoded=[1 if gender==i else 0 for i in gender_list]

                race=data_dict.pop('race_ethnicity')
                race_encoded=[1 if race==i else 0 for i in race_list]

                parent=data_dict.pop('parental_level_of_education')
                parent_encoded=[1 if parent==i else 0 for i in parent_edu_list]

                lunch=data_dict.pop('lunch')
                lunch_encoded=[1 if lunch==i else 0 for i in lunch_list]

                course=data_dict.pop('test_preparation_course')
                course_encoded=[1 if course==i else 0 for i in test_course_list]

                final_data=(
                    list(data_dict.values())+gender_encoded+race_encoded+parent_encoded+lunch_encoded+
                    course_encoded
                )

                scaled=scaler.transform([final_data])
                pred=model.predict(scaled)[0]
                return Response({
                    "prediction":pred
                })

            except Exception as e:
                return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


