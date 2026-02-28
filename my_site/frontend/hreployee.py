import streamlit as st
import requests


def check_hremployee():
    st.title('HR Employee Attrition Prediction')
    api_url = 'http://127.0.0.1:8000/predict/'
    Age = st.number_input('Age', min_value=18, max_value=65)
    DailyRate = st.number_input('Daily Rate', min_value=100, max_value=2000)
    DistanceFromHome = st.number_input('Distance From Home', min_value=1, max_value=50)
    Education = st.number_input('Education', min_value=1, max_value=5)
    EnvironmentSatisfaction = st.number_input('Environment Satisfaction', min_value=1, max_value=4)
    HourlyRate = st.number_input('Hourly Rate', min_value=10, max_value=100)
    JobInvolvement = st.number_input('Job Involvement', min_value=1, max_value=4)
    JobLevel = st.number_input('Job Level', min_value=1, max_value=5)
    JobSatisfaction = st.number_input('Job Satisfaction', min_value=1, max_value=4)
    MonthlyIncome = st.number_input('Monthly Income', min_value=1000, max_value=20000)
    MonthlyRate = st.number_input('Monthly Rate', min_value=2000, max_value=30000)
    NumCompaniesWorked = st.number_input('Number of Companies Worked', min_value=0, max_value=10)
    PercentSalaryHike = st.number_input('Percent Salary Hike', min_value=0, max_value=30)
    PerformanceRating = st.number_input('Performance Rating', min_value=1, max_value=4)
    RelationshipSatisfaction = st.number_input('Relationship Satisfaction', min_value=1, max_value=4)
    StockOptionLevel = st.number_input('Stock Option Level', min_value=0, max_value=3)
    TotalWorkingYears = st.number_input('Total Working Years', min_value=0, max_value=40)
    TrainingTimesLastYear = st.number_input('Training Times Last Year', min_value=0, max_value=10)
    WorkLifeBalance = st.number_input('Work Life Balance', min_value=1, max_value=4)
    YearsAtCompany = st.number_input('Years At Company', min_value=0, max_value=40)
    YearsInCurrentRole = st.number_input('Years In Current Role', min_value=0, max_value=20)
    YearsSinceLastPromotion = st.number_input('Years Since Last Promotion', min_value=0, max_value=15)
    YearsWithCurrManager = st.number_input('Years With Current Manager', min_value=0, max_value=20)
    BusinessTravel = st.selectbox('Business Travel',['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    Department = st.selectbox('Department',['Research & Development', 'Sales', 'Human Resources'])
    EducationField = st.selectbox('Education Field',['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other', 'Human Resources'])
    Gender = st.selectbox('Gender',['Male', 'Female'])
    JobRole = st.selectbox('Job Role',['Sales Executive','Research Scientist','Laboratory Technician',
            'Manufacturing Director','Healthcare Representative','Manager','Sales Representative','Research Director',
            'Human Resources'])
    MaritalStatus = st.selectbox('Marital Status',['Single', 'Married', 'Divorced'])
    OverTime = st.selectbox('Over Time',['Yes', 'No'])
    employee_dict = {
        'Age': Age,
        'DailyRate': DailyRate,
        'DistanceFromHome': DistanceFromHome,
        'Education': Education,
        'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'HourlyRate': HourlyRate,
        'JobInvolvement': JobInvolvement,
        'JobLevel': JobLevel,
        'JobSatisfaction': JobSatisfaction,
        'MonthlyIncome': MonthlyIncome,
        'MonthlyRate': MonthlyRate,
        'NumCompaniesWorked': NumCompaniesWorked,
        'PercentSalaryHike': PercentSalaryHike,
        'PerformanceRating': PerformanceRating,
        'RelationshipSatisfaction': RelationshipSatisfaction,
        'StockOptionLevel': StockOptionLevel,
        'TotalWorkingYears': TotalWorkingYears,
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': WorkLifeBalance,
        'YearsAtCompany': YearsAtCompany,
        'YearsInCurrentRole': YearsInCurrentRole,
        'YearsSinceLastPromotion': YearsSinceLastPromotion,
        'YearsWithCurrManager': YearsWithCurrManager,
        'BusinessTravel': BusinessTravel,
        'Department': Department,
        'EducationField': EducationField,
        'Gender': Gender,
        'JobRole': JobRole,
        'MaritalStatus': MaritalStatus,
        'OverTime': OverTime
    }
    if st.button('Predict'):
        try:
            response = requests.post(api_url, json=employee_dict, timeout=10)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Prediction: {result['prediction']}")
            else:
                st.error(f"API Error: {response.status_code}")
        except requests.exceptions.RequestException:
            st.error('Cannot connect to API')