import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    #Menampilkan gambar header
    image = Image.open('header.jpg')
    st.image(image)
    #Membuat title
    st.title('Sleep Health Prediction') 

    #Membuat subheader
    st.subheader('EDA untuk Analisa Sleep Health')

    #Menampilkan gambar
    image = Image.open('Sleep.jpg')
    st.image(image, caption = 'Sleep Ilustration')

    
    #Membuat garis
    st.markdown('----')
    
    st.subheader('What are sleep disorders?', divider='blue')
    st.write('Sleep disorders are conditions that affect the quality, amount and timing of sleep you’re able to get at night. Common sleep disorders include insomnia, restless legs syndrome, narcolepsy and sleep apnea. Sleep disorders can affect your mental health and physical health.')
    
    #Membuat garis
    st.markdown('----')
    
    #Header for sleep disorder
    st.subheader('Data Patient with Sleep Disorder', divider='blue')
    
    # membaca CSV file
    file_path = r'P1M2_agus_susanto.csv'
    df = pd.read_csv(file_path, keep_default_na=False, na_filter=False)

    # Menampilkan dataframe
    st.dataframe(df)

    with st.container():
        
        # # #Membuat bar plot
        # # menghitung total masing-masing uniq value pada kolom 'default_payment_next_month'
        default_counts = df['Sleep Disorder'].value_counts()

        # judul grafik
        st.title('Distribution of Sleep Disorder')

        #Membuat grafik
        fig, ax = plt.subplots()
        colors = ['lightgreen', 'lightcoral', 'Yellow']
        ax.pie(default_counts, labels=default_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')

        # Menampilkan grafik
        st.pyplot(fig)
    
    st.markdown('----')
    # Membuat bar chart dengan Seaborn
    plt.figure(figsize=(6, 4))
    ax = sns.countplot(x='Sleep Disorder', hue='Gender', data=df, palette='pastel')

    # Membuat labels dan title
    plt.xlabel('Sleep Disorder')
    plt.ylabel('Count')
    plt.title('Comparison of Sleep Disorders by Gender')

    # Menampilkan bar chart di Streamlit
    st.pyplot(plt)
    
    st.markdown('----')
    # Membuat bar chart dengan Seaborn
    plt.figure(figsize=(10, 7))
    ax = sns.countplot(x='Sleep Disorder', hue='Occupation', data=df, palette='pastel')

    # Membuat labels dan title
    plt.xlabel('Sleep Disorder')
    plt.ylabel('Count')
    plt.title('Comparison of Sleep Disorders by Occupation')

    # Menampilkan bar chart di Streamlit
    st.pyplot(plt)

    #Menambahkan deskripsi
    st.write('Copyright by Susantohamzah')

#condition untuk run file
if __name__ == '__main__':
    run()
