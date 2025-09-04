import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="CO₂ by Aircraft - Global Flights", layout="wide")

def main():
    st.title("🌍 CO₂ Emissions by Aircraft")
    
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
        
        st.markdown("### CO₂ Emissions Analysis by Aircraft Type")
        st.info("This page analyzes carbon emissions across different aircraft types and routes.")
        
        # Check for emissions-related columns
        emissions_cols = [col for col in df.columns if 'co2' in col.lower() or 'emission' in col.lower() or 'carbon' in col.lower()]
        aircraft_cols = [col for col in df.columns if 'aircraft' in col.lower() or 'plane' in col.lower() or 'airplane' in col.lower()]
        
        if emissions_cols and aircraft_cols:
            emissions_col = emissions_cols[0]
            aircraft_col = aircraft_cols[0]
            
            st.markdown(f"**Using:** {emissions_col} (emissions) and {aircraft_col} (aircraft)")
            
            # Summary statistics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                total_emissions = df[emissions_col].sum()
                st.metric("Total CO₂ Emissions", f"{total_emissions:,.0f}")
            
            with col2:
                avg_emissions = df[emissions_col].mean()
                st.metric("Average per Flight", f"{avg_emissions:.1f}")
            
            with col3:
                unique_aircraft = df[aircraft_col].nunique()
                st.metric("Aircraft Types", unique_aircraft)
            
            # Emissions by aircraft type
            st.markdown("### Emissions by Aircraft Type")
            
            aircraft_emissions = df.groupby(aircraft_col).agg({
                emissions_col: ['sum', 'mean', 'count']
            }).round(2)
            
            aircraft_emissions.columns = ['Total_Emissions', 'Avg_Emissions', 'Flight_Count']
            aircraft_emissions = aircraft_emissions.reset_index()
            aircraft_emissions = aircraft_emissions.sort_values('Total_Emissions', ascending=False)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.bar(aircraft_emissions.head(10), 
                           x='Total_Emissions', y=aircraft_col, orientation='h',
                           title="Top 10 Aircraft by Total CO₂ Emissions")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.bar(aircraft_emissions.head(10), 
                           x='Avg_Emissions', y=aircraft_col, orientation='h',
                           title="Top 10 Aircraft by Average CO₂ per Flight")
                st.plotly_chart(fig, use_container_width=True)
            
            # Emissions efficiency (if we have distance or duration data)
            if 'duration' in df.columns:
                st.markdown("### Emissions Efficiency")
                df['emissions_per_hour'] = df[emissions_col] / (df['duration'] / 60)  # assuming duration is in minutes
                
                efficiency = df.groupby(aircraft_col)['emissions_per_hour'].mean().reset_index()
                efficiency = efficiency.sort_values('emissions_per_hour')
                
                fig = px.bar(efficiency.head(15), 
                           x='emissions_per_hour', y=aircraft_col, orientation='h',
                           title="Most Fuel Efficient Aircraft (CO₂ per Hour)")
                st.plotly_chart(fig, use_container_width=True)
            
            # Detailed data table
            st.markdown("### Aircraft Emissions Summary")
            st.dataframe(aircraft_emissions, use_container_width=True)
            
            # Distribution of emissions
            st.markdown("### Emissions Distribution")
            fig = px.histogram(df, x=emissions_col, nbins=50, 
                             title="Distribution of CO₂ Emissions per Flight")
            st.plotly_chart(fig, use_container_width=True)
            
        elif emissions_cols:
            st.warning(f"Found emissions data ({emissions_cols[0]}) but no aircraft type column.")
            st.info("Available columns: " + ", ".join(df.columns.tolist()))
            
            # Show general emissions analysis
            emissions_col = emissions_cols[0]
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Emissions", f"{df[emissions_col].sum():,.0f}")
            with col2:
                st.metric("Average per Flight", f"{df[emissions_col].mean():.1f}")
            
            fig = px.histogram(df, x=emissions_col, nbins=50, 
                             title="Distribution of CO₂ Emissions per Flight")
            st.plotly_chart(fig, use_container_width=True)
            
        else:
            st.error("No CO₂ emissions or aircraft type columns found in the dataset.")
            st.info("Available columns: " + ", ".join(df.columns.tolist()))
            st.markdown("**Looking for columns containing:** co2, emission, carbon, aircraft, plane, airplane")
            
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.info("Please check your CSV file format and try again.")

if __name__ == "__main__":
    main()
