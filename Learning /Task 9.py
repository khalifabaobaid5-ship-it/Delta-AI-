import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------------
# Data URL
# -----------------------------------
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/"
    "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

st.set_page_config(page_title="Uber Pickups Analysis", layout="wide")

st.title("🚖 Uber Pickups Analysis - September 2014")

# -----------------------------------
# Load Data
# -----------------------------------
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)

    # Clean column names
    data.columns = data.columns.str.strip().str.lower()

    # Convert datetime
    data["date/time"] = pd.to_datetime(data["date/time"])

    # Extract hour
    data["hour"] = data["date/time"].dt.hour

    return data


# -----------------------------------
# Sidebar Controls
# -----------------------------------
st.sidebar.header("Settings")
nrows = st.sidebar.slider("Number of rows to load", 1000, 100000, 50000)

# Load dataset
data = load_data(nrows)

# -----------------------------------
# Download Button
# -----------------------------------
st.sidebar.subheader("Download Data")

csv = data.to_csv(index=False).encode("utf-8")

st.sidebar.download_button(
    label="⬇ Download Raw Data as CSV",
    data=csv,
    file_name="uber_pickups_sep2014.csv",
    mime="text/csv",
)

# -----------------------------------
# Show Raw Data
# -----------------------------------
st.subheader("📄 Raw Data Preview")
if st.checkbox("Show raw data"):
    st.write(data.head())

# -----------------------------------
# Pickup Hour Distribution
# -----------------------------------
st.subheader("📊 Distribution of Pickup Hours")

hourly_distribution = data["hour"].value_counts().sort_index()

st.bar_chart(hourly_distribution)

# -----------------------------------
# Map by Selected Hour
# -----------------------------------
st.subheader("🗺️ Pickup Locations by Hour")

hour_to_filter = st.slider("Select hour", 0, 23, 17)

filtered_data = data[data["hour"] == hour_to_filter]

st.write(f"Showing pickups for hour: {hour_to_filter}:00")
st.write(f"Total pickups at this hour: {len(filtered_data)}")

if not filtered_data.empty:
    st.map(filtered_data[["lat", "lon"]])
else:
    st.warning("No data available for this hour.")

# -----------------------------------
# Overall Density Map
# -----------------------------------
st.subheader("🔥 Overall Pickup Density Map")

st.write(f"Total pickups in dataset: {len(data)}")

st.map(data[["lat", "lon"]])