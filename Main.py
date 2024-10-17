import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd


# Set page configuration
st.set_page_config(page_title="Diab-Care",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('C:\\Users\\AYUSH\\Desktop\\Daiba care\\diabetes_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    selected = option_menu('DIAB-CARE',

                           ['Information','Diabetes Prediction'
                            ],
                           menu_icon='hospital-fill',
                           icons=['person','activity'],
                           default_index=0)

# Information page
if selected == 'Information':
    st.title('Information')
    st.write('Diabetes is a chronic metabolic disorder characterized by high blood sugar levels over a prolonged period. Early detection and prediction of diabetes are crucial for effective management and prevention of complications associated with the disease. Diab-Care with help of machine learning (ML) techniques offer promising solutions for early diagnosis and prediction of diabetes by analyzing various risk factors and patterns in patient data')
    image = Image.open("C:\\Users\\AYUSH\\Desktop\\Daiba care\\imgaa (1).jpg")

    # Display the image in the Streamlit app
    st.image(image,  use_column_width=False,width= 350)
    st.header('PIMA DATASET')

    df = pd.read_csv("C:\\Users\\AYUSH\\Desktop\\Daiba care\\diabetes_datasets.csv")

    # Show the first 5 rows of the dataset using head()
    st.write("### Displaying the First 5 Rows of the Dataset")
    st.write(df.head())


   


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

   

    #st.success(diab_diagnosis)
    if st.button('Diabetes Test Result'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]

            user_input = [float(x) for x in user_input]

            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic, Please consult a doctor'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.success(diab_diagnosis)

        except ValueError as e:
            st.error(f"Invalid input: {e}. Please ensure all inputs are valid numbers.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

