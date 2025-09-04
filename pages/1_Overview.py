import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Overview - Global Flights", layout="wide")

def main():
    st.title("📊 Flight Data Overview")
    
    # Get CSV path from session state
    csv_path = st.session_state.get("csv_path", "data/processed/cleaned_global_flights_data.csv")
    
    # Check if file exists
    if not Path(csv_path).exists():
        st.error(f"Data file not found: {csv_path}")
        st.info("Please go back to the home page and specify a valid CSV file path.")
        return
    
    try:
        # Load data
        df = pd.read_csv(csv_path)
        
        st.markdown("### Dataset Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Flights", len(df))
        with col2:
            st.metric("Unique Airlines", df['airline'].nunique() if 'airline' in df.columns else "N/A")
        with col3:
            st.metric("Unique Routes", f"{df['origin'].nunique() if 'origin' in df.columns else 'N/A'} → {df['destination'].nunique() if 'destination' in df.columns else 'N/A'}")
        with col4:
            st.metric("Date Range", f"{len(df)} records" if 'date' not in df.columns else f"{df['date'].min()} to {df['date'].max()}")
        
        st.markdown("### Data Preview")
        st.dataframe(df.head(10), use_container_width=True)
        
        # Show column information
        st.markdown("### Dataset Structure")
        col_info = pd.DataFrame({
            'Column': df.columns,
            'Data Type': df.dtypes.values,
            'Non-Null Count': df.count().values,
            'Null Count': df.isnull().sum().values
        })
        st.dataframe(col_info, use_container_width=True)
        
        # Basic visualizations if we have the right columns
        if 'price' in df.columns:
            st.markdown("### Price Distribution")
            fig = px.histogram(df, x='price', nbins=50, title="Flight Price Distribution")
            st.plotly_chart(fig, use_container_width=True)
        
        if 'duration' in df.columns:
            st.markdown("### Duration Distribution")
            fig = px.histogram(df, x='duration', nbins=50, title="Flight Duration Distribution")
            st.plotly_chart(fig, use_container_width=True)
            
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.info("Please check your CSV file format and try again.")

if __name__ == "__main__":
    main()
