import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import date, timedelta
from sqlalchemy import create_engine
import plotly.graph_objects as go
from src.extract.extract import extract_global_flights
from pathlib import Path


    
st.set_page_config(page_title="Global Flights", layout="centered")

def display_homepage():
    st.title("✈️ Welcome to Global Flight Dashboard ✈️")

    # Choose the processed CSV once here; pages will reuse it
    default_csv = "data/processed/cleaned_global_flights_data.csv"
    csv_path = st.text_input("CSV path", value=default_csv, help="Path to your processed CSV")
    st.session_state["csv_path"] = csv_path

    p = Path(csv_path)
    if not p.exists():
        st.warning(f"File not found: {p}")

    st.markdown(
        """
        **Global Flight Dashboard** lets you explore routes, airlines, prices, durations, and emissions.
        Use the buttons below to navigate.
        """
    )
    st.subheader("👥 Dedicated to:")
    st.markdown(
        "- Friends and Family  \n"
        "- Cycle 13 cohort of the Digital Futures Academy  \n"
        "- Trainers and Mentors"
    )

    st.divider()
    st.write("Pick a section:") # Buttons at bottom of page 
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📊 Overview", use_container_width=True):
            st.switch_page("pages/1_Overview.py")
    with col2:
        if st.button("🌍 CO₂ by Aircraft", use_container_width=True):
            st.switch_page("pages/3_CO2_by_Aircraft.py")
    
        

if __name__ == "__main__":
    display_homepage()
 

# Load clean data
#df = pd.read_csv('data/processed/cleaned_global_flights_data.csv')





#st.bar_chart

#Set in a face off-like feature of two countries for comparison

#col1, col2 = st.columns(2)


























