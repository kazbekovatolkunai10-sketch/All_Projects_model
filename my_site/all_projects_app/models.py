from django.db import models


class House(models.Model):
    GrLivArea = models.IntegerField()
    YearBuilt = models.IntegerField()
    GarageCars = models.IntegerField()
    TotalBsmtSF = models.IntegerField()
    FullBath = models.IntegerField()
    OverallQual = models.IntegerField()
    Neighborhood = models.CharField(max_length=50)
    predicted_price = models.FloatField(null=True, blank=True)



class DiabetesPrediction(models.Model):
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField()
    predicted_label = models.CharField(max_length=10, blank=True)
    probability = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Avacado(models.Model):
    firmness = models.FloatField()
    hue = models.IntegerField()
    saturation = models.IntegerField()
    brightness = models.IntegerField()
    color_category = models.CharField(max_length=20)
    sound_db = models.IntegerField()
    weight_g = models.IntegerField()
    size_cm3 = models.IntegerField()
    predicted_label = models.CharField(max_length=30, null=True, blank=True)



class Bank(models.Model):
    person_age = models.FloatField()
    person_gender = models.CharField(max_length=20)
    person_education = models.CharField(max_length=50)
    person_income = models.FloatField()
    person_emp_exp = models.IntegerField()
    person_home_ownership = models.CharField(max_length=20)
    loan_famnt = models.FloatField()
    loan_intent = models.CharField(max_length=50)
    loan_int_rate = models.FloatField()
    loan_percent_income = models.FloatField()
    cb_person_cred_hist_length = models.FloatField()
    credit_score = models.IntegerField()
    previous_loan_defaults_on_file = models.CharField(max_length=10)
    predicted_result = models.CharField(max_length=20, null=True, blank=True)



class Titanic(models.Model):
    Pclass = models.IntegerField()
    Sex = models.CharField(max_length=10)
    age = models.IntegerField()
    Fare = models.FloatField()
    embarked = models.CharField(max_length=5)
    predicted_result = models.CharField(max_length=20, null=True, blank=True)



class Mushroom(models.Model):
    cap_shape = models.CharField(max_length=5)
    cap_surface = models.CharField(max_length=5)
    cap_color = models.CharField(max_length=5)
    bruises = models.CharField(max_length=5)
    odor = models.CharField(max_length=5)
    gill_attachment = models.CharField(max_length=5)
    gill_spacing = models.CharField(max_length=5)
    gill_size = models.CharField(max_length=5)
    gill_color = models.CharField(max_length=5)
    stalk_shape = models.CharField(max_length=5)
    stalk_root = models.CharField(max_length=5)
    stalk_surface_above_ring = models.CharField(max_length=5)
    stalk_surface_below_ring = models.CharField(max_length=5)
    stalk_color_above_ring = models.CharField(max_length=5)
    stalk_color_below_ring = models.CharField(max_length=5)
    veil_color = models.CharField(max_length=5)
    veil_type = models.CharField(max_length=5)
    ring_number = models.CharField(max_length=5)
    ring_type = models.CharField(max_length=5)
    spore_print_color = models.CharField(max_length=5)
    population = models.CharField(max_length=5)
    habitat = models.CharField(max_length=5)
    predicted_label = models.CharField(max_length=10, null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)



class Telecom(models.Model):
    gender = models.CharField(max_length=20)
    SeniorCitizen = models.IntegerField()
    Partner = models.CharField(max_length=10)
    Dependents = models.CharField(max_length=10)
    tenure = models.IntegerField()
    PhoneService = models.CharField(max_length=10)
    MultipleLines = models.CharField(max_length=20)
    InternetService = models.CharField(max_length=20)
    OnlineSecurity = models.CharField(max_length=30)
    OnlineBackup = models.CharField(max_length=30)
    DeviceProtection = models.CharField(max_length=30)
    TechSupport = models.CharField(max_length=30)
    StreamingTV = models.CharField(max_length=30)
    StreamingMovies = models.CharField(max_length=30)
    Contract = models.CharField(max_length=20)
    PaperlessBilling = models.CharField(max_length=10)
    PaymentMethod = models.CharField(max_length=50)
    MonthlyCharges = models.IntegerField()
    TotalCharges = models.IntegerField()
    predicted_label = models.CharField(max_length=20, null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)