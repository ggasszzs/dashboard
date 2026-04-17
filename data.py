import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv("dataset\covid_19_indonesia_time_series_all.csv")
    return df

def show_data():
    df = load_data()
    st.subheader("📊Dashboard Covid-19")
    st.dataframe(df.head(10)) # Menampilkan 10 data pertama
    st.subheader("📊 Statistik Deskriptif Dataset")
    st.write(df.describe()) # Menampilkan statistik deskriptif