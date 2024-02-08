#Import Library
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from PIL import Image
import matplotlib.pyplot as plt

# #Load Semua File
with open('classes.pkl', 'rb') as file_1:
  classes = pickle.load(file_1)

with open('model.pkl', 'rb') as file_2:
  model_rf = pickle.load(file_2)
  

def run():
    
    #Menampilkan gambar header
    image = Image.open('header.jpg')
    st.image(image)
    
    tab1, tab2 = st.tabs(["Prediction Form", "Bulk Predictions"])
    
    #Tab untuk form prediction
    with tab1:
        with st.form('form_patient_information'):

            #Title Patient Data
            st.subheader('Patient Data', divider='blue')
            
            #Field sex
            Gender = st.selectbox('Gender', ('Male', 'Female'), index=1)
            
            #Field age
            Age = st.number_input('Age', min_value = 1, max_value = 100, value = 25, step = 1, help = 'Age in years')
            
            #Field Occupation
            Occupation = st.selectbox('Occupation', ('Software Engineer', 'Doctor', 'Sales Representative', 'Teacher',
        'Nurse', 'Engineer', 'Accountant', 'Scientist', 'Lawyer',
        'Salesperson', 'Manager'), index=0)
            
            # Title Physical Data
            st.subheader('Physical Data', divider='blue')
            
            #Field Physical_Activity_Level
            Physical_Activity_Level = st.number_input('Physical Activity Level (Minutes/Day)', min_value = 1, max_value = 100, value = 1, step = 1, help = 'The number of Aaverage minutes the person engages in physical activity daily in minutes/day')
            
            #Field Daily_Steps
            Daily_Steps = st.number_input('Daily Steps', min_value = 0, max_value = 100000, value = 1, step = 1, help = 'The number of steps the person takes per day')
            
            #Field BMI Category
            BMI_Category = st.selectbox('BMI_Category', ('Overweight', 'Normal', 'Obese', 'Normal Weight'), index=1, help='The BMI category of the person (e.g., Underweight, Normal, Overweight)')

            
            # Title Medical Data
            st.subheader('Medical Data', divider='blue')
            
            #Field Heart_Rate
            Heart_Rate = st.number_input('Heart_Rate(BPM)', min_value = 30, max_value = 200, value = 60, step = 1, help = 'The resting heart rate of the person in beats per minute')
            
            #Field Stess Level
            Stress_Level = st.slider("Stress Level", min_value=1, max_value=10, value=5, help='A subjective rating of the stress level experienced by the person, ranging from 1 to 10')
            
            #Field Bp_Systolic
            Bp_Systolic = st.number_input('Blood Preasure Systolic', min_value = 1, max_value = 200, value = 120, step = 1, help = 'The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure, example 120/90 and Blood Preasure Systolic is 120')
            
            #Field Bp_Diastolic
            Bp_Diastolic = st.number_input('Blood Preasure Diastolic', min_value = 1, max_value = 200, value = 80, step = 1, help = 'The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure, example 120/90 and Blood Preasure Systolic is 90')

            # Title Sleep Data
            st.subheader('Sleep Data', divider='blue')

            #Field Sleep Duration
            Sleep_Duration = st.number_input('Sleep Duration Perday(Hour)', min_value = 1, max_value = 24, value = 1, step = 1, help = 'The number of hours the person sleeps per day')

            #Field Stess Level
            Quality_of_Sleep = st.slider("Quality of Sleep", min_value=1, max_value=10, value=5, help='A subjective rating of the quality of sleep, ranging from 1 to 10')
            
            #submit button
            submitted = st.form_submit_button('Predict')


        # #Inference table
        data_inf = {
            'Gender':Gender, 
            'Age':Age, 
            'Occupation':Occupation,
            'Physical_Activity_Level':Physical_Activity_Level,
            'Daily_Steps':Daily_Steps, 
            'BMI_Category':BMI_Category,
            'Heart_Rate':Heart_Rate, 
            'Stress_Level':Stress_Level,
            'Bp_Systolic':Bp_Systolic, 
            'Bp_Diastolic':Bp_Diastolic,
            'Sleep_Duration':Sleep_Duration,
            'Quality_of_Sleep':Quality_of_Sleep
        }

        #convert ke dataframe
        data_inf = pd.DataFrame([data_inf])
        

        #condition ketika predic button ditekan
        if submitted:
            
            #Membuat tabs area
            tab3, tab4, tab5, tab6 = st.tabs(["Patient Data", "Physical Data", "Medical Data", "Sleep Data"])
            
            #tabs untuk patient data
            with tab3:
                #Declare Container
                container = st.container(border=True)
                
                #Header
                container.header("Patient Data")
                
                #Menampilkan tabel
                container.dataframe(data_inf[['Gender', 'Age', 'Occupation']])

            #tabs untuk Physical data
            with tab4:
                #Declare Container
                container = st.container(border=True)
                
                #Header
                container.header("Physical Data")
                
                #Menampilkan tabel
                container.dataframe(data_inf[['Physical_Activity_Level', 'Daily_Steps','BMI_Category']])
                
                #Menampilkan tulisan
                container.write('**Important Notes**')
                
                #Condition untuk menampilkan suggestion berdasarkan data yang di input
                if BMI_Category != 'Normal':
                    container.write(f'BMI Category is {BMI_Category}, don\'t Forget to Maintain regular exercise, control weight, adhere to a healthy eating pattern')
                else:
                    container.write(f'BMI Category is {BMI_Category}, Good Job!!')
                
                #Condition untuk menampilkan suggestion berdasarkan data yang di input
                if Daily_Steps <= 8000:
                    container.write(f'Your Daily Steps is less than 8000, don\'t forget to stay active and consider taking short walks throughout the day to increase your step count.')
                else:
                    container.write(f'Your Daily Steps > 8000, Good Job!!')
                    
                #Condition untuk menampilkan suggestion berdasarkan data yang di input
                if Physical_Activity_Level <= 30:
                    container.write(f'Your Daily Physical Activity is less than 30 minutes per day. It\'s important to prioritize regular exercise for better health. Consider incorporating activities like brisk walking, jogging, or cycling into your routine. Find activities you enjoy to make it more enjoyable and sustainable.')
                else:
                    container.write(f'Your Daily Physical Activity is > 30 minutes per day, Good Job!!')
                
            #tabs untuk Medical data
            with tab5:
                #Declare Container
                container = st.container(border=True)
                
                #Header
                container.header("Medical Data")
                
                #Menampilkan tabel
                container.dataframe(data_inf[['Heart_Rate','Stress_Level', 'Bp_Systolic', 'Bp_Diastolic']])
                
                            #Menampilkan tulisan
                container.write('**Important Notes**')
                
                #Condition untuk menampilkan suggestion berdasarkan data yang di input
                if 60 <= Heart_Rate <= 100:
                    container.write(f'Heart Rate is within the normal range wich is 60-100 BPM. Good job on staying aware of your health!')
                else:
                    container.write(f'Your heart Rate is outside the normal range wich is 60-100 BPM. It\'s advisable to consult with a healthcare professional to evaluate your heart health. Consider maintaining regular physical activity, managing stress, and adopting a heart-healthy lifestyle. Keep track of your heart rate over time and seek medical advice for personalized guidance.')
                
                #Condition untuk menampilkan suggestion berdasarkan data yang di input
                if Stress_Level > 5:
                    container.write("Your stress level seems elevated. It's important to find effective ways to manage stress. Consider incorporating relaxation techniques such as deep breathing, meditation, or taking short breaks throughout the day. Don't hesitate to seek support from friends, family, or a professional if needed.")
                else:
                    container.write("Your stress level is manageable. Good job on maintaining a healthy balance! Remember to continue practicing stress-reducing activities and taking care of your well-being.")
                    
                #Condition untuk menampilkan suggestion berdasarkan data yang di input
                if Bp_Systolic > 120:
                    container.write(f'Your Daily Physical Activity is less than 30 minutes per day. It\'s important to prioritize regular exercise for better health. Consider incorporating activities like brisk walking, jogging, or cycling into your routine. Find activities you enjoy to make it more enjoyable and sustainable.')
                else:
                    container.write(f'Your Daily Physical Activity is > 30 minutes per day, Good Job!!')
                    
                if 90 <= Bp_Diastolic <= 120 and 60 <= Bp_Systolic <= 80:
                    container.write("Your blood pressure is within the normal range. Keep up the good work!")
                else:
                    container.write("Your blood pressure is outside the normal range. It's advisable to monitor and consult with a healthcare professional for personalized advice.")
                
            
            #tabs untuk Sleep data          
            with tab6:
                #Declare Container
                container = st.container(border=True)
                
                #Header
                container.header("Sleep Data")
                
                #Menampilkan tabel
                container.dataframe(data_inf[['Sleep_Duration','Quality_of_Sleep']])
                
                #Condition untuk menampilkan suggestion berdasarkan data yang di input
                if 7 <= Sleep_Duration <= 9:
                    container.write("Your sleep duration is within the normal range. Keep prioritizing good sleep habits!")
                else:
                    container.write("Your sleep duration is outside the recommended range. Consider adjusting your sleep routine between 7-9 hour per day for better overall health")
                
                #Condition untuk menampilkan suggestion berdasarkan data yang di input
                if Quality_of_Sleep >= 5:
                    container.write("Your quality of sleep is within the normal range. Keep practicing good sleep hygiene!")
                else:
                    container.write("Your quality of sleep is not good. Consider making adjustments to improve your sleep environment and habits.")
                
            # Predict menggunakan logistic regression model
            y_pred_inf = model_rf.predict(data_inf)
            
            # #condition jika pred==0 maka insomnia
            if y_pred_inf == 0:
                
                # membuat container
                container = st.container(border=True)
                
                #Menampilkan tulisan
                container.write('## Sleep Disorder: <span style="color: Red;">Insomnia</span>', unsafe_allow_html=True)
                
                #Menampilkan tulisan
                container.write('Insomnia is a common sleep disorder that can make it hard to fall asleep, hard to stay asleep, or cause you to wake up too early and not be able to get back to sleep. You may still feel tired when you wake up. Insomnia can sap not only your energy level and mood but also your health, work performance and quality of life.')
                
                # Menampilkan hyperlink
                container.markdown(f"[{'Click here for more information'}]({'https://www.sleepfoundation.org/insomnia'})")
                
                #Menampilkan tulisan
                container.write('**Suggestion** : Engaging in regular exercise is essential. If the body weight is not within the normal range, weight reduction is mandatory. Maintaining a healthy eating pattern and avoiding foods that contribute to hypertension, such as high-salt foods, fast food, and high-fat foods and similar items.')
                
                #Menampilkan tulisan
                container.write('**Disclaimer: <span style="color: Red;">This prediction is not 100% Correct, if you have a sympton of sleep disorder, you can consult with doctor </span>**', unsafe_allow_html=True)
                
            # #condition jika pred==0 maka none
            elif y_pred_inf == 1:
                
                #Membuat Container
                container = st.container(border=True)
                
                #Menampilkan tulisan
                container.write('## Sleep Disorder: <span style="color: green;">None</span>', unsafe_allow_html=True)
                
                #Menampilkan tulisan
                container.write('Congratulation!!! You dont have sleep disorder, but it is really important to taking care of yourself and have a good sleep.')
                
                # Menampilkan hyperlink
                container.markdown(f"[{'Here it is some tips for you'}]({'https://www.sleepfoundation.org/sleep-hygiene'})")
                
                #Menampilkan tulisan
                container.write('**Suggestion** : Maintain regular exercise, control weight, adhere to a healthy eating pattern, and avoid foods that can lead to hypertension, such as high-salt foods, fast food, high-fat foods, and similar items.')
                
                #Menampilkan tulisan
                container.write('**Disclaimer: <span style="color: Red;">This prediction is not 100% Correct, if you have a sympton of sleep disorder, you can consult with doctor </span>**', unsafe_allow_html=True)
                
            #condition jika selain 0 dan 1
            else:
                
                # Membuat Container
                container = st.container(border=True)
                
                #Menampilkan tulisan
                container.write('## Payment Prediction: <span style="color: red;">Sleep Apnea</span>', unsafe_allow_html=True)
                
                #Menampilkan tulisan
                container.write('Sleep apnea is a potentially serious sleep disorder in which breathing repeatedly stops and starts. If you snore loudly and feel tired even after a full night sleep, you might have sleep apnea.')
                
                # Menampilkan hyperlink
                container.markdown(f"[{'Click here for more information'}]({'https://www.sleepfoundation.org/sleep-apnea'})")
                
                #Menampilkan tulisan
                container.write('**Suggestion** : Reduce strenuous activities that can lead to fatigue, engage in regular and moderate exercise, regulate sleep patterns, manage weight, and maintain a healthy eating pattern while avoiding foods that contribute to hypertension, such as high-salt foods, fast food, and high-fat foods  and similar items.')
                
                #Menampilkan tulisan
                container.write('**Disclaimer: <span style="color: Red;">This prediction is not 100% Correct, if you have a sympton of sleep disorder, you can consult with doctor </span>**', unsafe_allow_html=True)
    
    #Tab untuk bulk prediction        
    with tab2:
        #Fungsi running file 
            st.write('## Bulk Prediction Sleep Disorder')
            st.write('### Pantient Data')
            uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

            #Condition upload data
            if uploaded_file is not None:
                df_uploaded = pd.read_csv(uploaded_file)
                # Mengubah spasi menjadi '_' langsung pada kolom
                df_uploaded.columns = df_uploaded.columns.str.replace(' ', '_')
                
                # Condition jika ada kolom Person_ID maka akan di drop
                if 'Person_ID' in df_uploaded.columns:

                    #Drop kolom
                    df_uploaded.drop('Person_ID', axis=1, inplace=True)
                
                # Condition jika ada kolom Sleep_Disorder maka akan di drop
                if 'Sleep_Disorder' in df_uploaded.columns:
                
                    #Drop kolom
                    df_uploaded.drop('Sleep_Disorder', axis=1, inplace=True)
                
                # Condition jika ada kolom Blood_Preassure maka akan di pisah jadi 2 kolom
                if 'Blood_Pressure' in df_uploaded.columns:
                
                    # Melakukan split value
                    df_uploaded[['Bp_Systolic', 'Bp_Diastolic']] = df_uploaded['Blood_Pressure'].str.split('/', expand=True)
                
                    # Drop kolom asli
                    df_uploaded.drop('Blood_Pressure', axis=1, inplace=True)
                    
                    # Drop Merubah type data
                    df_uploaded['Bp_Systolic'] = df_uploaded['Bp_Systolic'].astype('int64')
                    df_uploaded['Bp_Diastolic'] = df_uploaded['Bp_Diastolic'].astype('int64')

                # Nama kolom dataset
                df_uploaded.columns = ['Gender', 'Age', 'Occupation', 'Sleep_Duration',
            'Quality_of_Sleep', 'Physical_Activity_Level', 'Stress_Level',
            'BMI_Category', 'Heart_Rate', 'Daily_Steps',
            'Bp_Systolic', 'Bp_Diastolic']


                # Predict menggunakan logistic regression model
                y_pred_inf = model_rf.predict(df_uploaded)

                #Menambahkan hasil predict ke dataframe
                df_uploaded['Sleep_Disorder'] = np.array(classes)[y_pred_inf]

                #Judul tabel prediction
                st.write('## Prediction Results for Uploaded Data')
                #Menampilkan dataframe
                final_df = df_uploaded[['Gender', 'Age', 'Occupation', 'Sleep_Duration',
            'Quality_of_Sleep', 'Physical_Activity_Level', 'Stress_Level',
            'BMI_Category', 'Heart_Rate', 'Daily_Steps',
            'Bp_Systolic', 'Bp_Diastolic', 'Sleep_Disorder']]
                
                #Container untuk prediction summary
                container = st.container(border=True)
                #Judul Container
                container.write('## **Prediction Summary**')
                #Menampilkan total data
                container.write(f'Total Data :**{len(final_df)}**')
                #Menampilkan total data dengan hasil prediksi insomnia
                container.write(f'Total Prediction for Patient With Insomnia :**{len(final_df[(final_df["Sleep_Disorder"] == "Insomnia")])}**')
                #Menampilkan total data dengan hasil prediksi sleep apnea
                container.write(f'Total Prediction for Patient With Sleep Apnea :**{len(final_df[(final_df["Sleep_Disorder"] == "Sleep Apnea")])}**')
                #Menampilkan total data dengan hasil prediksi none
                container.write(f'Total Prediction Of Patient Without Sleep Disorder :**{len(final_df[(final_df["Sleep_Disorder"] == "None")])}**')
                
                
                # # #Membuat bar plot
                # # menghitung total masing-masing uniq value pada kolom 'default_payment_next_month'
                default_counts = final_df['Sleep_Disorder'].value_counts()
                # judul grafik
                st.title('Distribution of Sleep Disorder Prediction')
                #Membuat grafik
                fig, ax = plt.subplots(figsize=(4, 4))
                colors = ['lightgreen', 'lightcoral', 'Yellow']
                ax.pie(default_counts, labels=default_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
                ax.axis('equal')

                # Menampilkan grafik
                st.pyplot(fig)
                
                #Membuat tab untuk menampilkan tabel sesuai hasil prediksi
                tab1, tab2, tab3 = st.tabs(["Patient With Insomnia", "Patient with Sleep Apnea", "Patient Without Sleep Disorder"])

                #Membuat tab untuk menampilkan tabel dengan prediksi insomnia
                with tab1:
                    #Header
                    st.write('## **Prediction Results for Patient With Insomnia**')
                    
                    #Menampilkan tabel dengan hasil prediksi insomnia
                    st.dataframe(final_df[(final_df['Sleep_Disorder'] == 'Insomnia')])
                    
                    #Menampilkan tulisan dengan warna merah
                    st.write('## Sleep Disorder: <span style="color: Red;">Insomnia</span>', unsafe_allow_html=True)
                    
                    #Menampilkan tulisan
                    st.write('Insomnia is a common sleep disorder that can make it hard to fall asleep, hard to stay asleep, or cause you to wake up too early and not be able to get back to sleep. You may still feel tired when you wake up. Insomnia can sap not only your energy level and mood but also your health, work performance and quality of life.')
                    
                    #Menampilkan hyperlink
                    st.markdown(f"[{'Click here for more information'}]({'https://www.sleepfoundation.org/insomnia'})")
                    
                    #Menampilkan tulisan
                    st.write('**Suggestion** : Engaging in regular exercise is essential. If the body weight is not within the normal range, weight reduction is mandatory. Maintaining a healthy eating pattern and avoiding foods that contribute to hypertension, such as high-salt foods, fast food, and high-fat foods and similar items.')
                    
                with tab2:
                #Header
                    st.write('## **Prediction Results for Patient with Sleep Apnea**')
                    
                    #Menampilkan tabel dengan hasil prediksi Sleep Apnea
                    st.dataframe(final_df[(final_df['Sleep_Disorder'] == 'Sleep Apnea')])
                    
                    #Menampilkan tulisan dengan warna merah
                    st.write('## Payment Prediction: <span style="color: red;">Sleep Apnea</span>', unsafe_allow_html=True)
                    
                    #Menampilkan tulisan
                    st.write('Sleep apnea is a potentially serious sleep disorder in which breathing repeatedly stops and starts. If you snore loudly and feel tired even after a full night sleep, you might have sleep apnea.')
                    
                    #Menampilkan hyperlink
                    st.markdown(f"[{'Click here for more information'}]({'https://www.sleepfoundation.org/sleep-apnea'})")
                    
                    #Menampilkan tulisan
                    st.write('**Suggestion** : Reduce strenuous activities that can lead to fatigue, engage in regular and moderate exercise, regulate sleep patterns, manage weight, and maintain a healthy eating pattern while avoiding foods that contribute to hypertension, such as high-salt foods, fast food, and high-fat foods  and similar items.')
                    

                with tab3:
                    #Header
                    st.write('## **Prediction Results for Patient Without Sleep Disorder**')
                    
                    #Menampilkan tabel dengan hasil prediksi insomnia
                    st.dataframe(final_df[(final_df['Sleep_Disorder'] == 'None')])
                    
                    #Menampilkan tulisan dengan warna merah
                    st.write('## Sleep Disorder: <span style="color: green;">None</span>', unsafe_allow_html=True)
                    
                    #Menampilkan tulisan
                    st.write('Congratulation!!! You dont have sleep disorder, but it is really important to taking care of yourself and have a good sleep.')
                    
                    #Menampilkan hyperlink
                    st.markdown(f"[{'Here it is some tips for you'}]({'https://www.sleepfoundation.org/sleep-hygiene'})")
                    
                    #Menampilkan tulisan
                    st.write('**Suggestion** : Maintain regular exercise, control weight, adhere to a healthy eating pattern, and avoid foods that can lead to hypertension, such as high-salt foods, fast food, high-fat foods, and similar items.')
                    
                    #Menampilkan tulisan
                    st.write('**Disclaimer: <span style="color: Red;">This prediction is not 100% Correct, if you have a sympton of sleep disorder, you can consult with doctor </span>**', unsafe_allow_html=True)
                    
# condition run
if __name__ == '__main__':
   run()