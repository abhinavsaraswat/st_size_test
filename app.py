import streamlit as st
import pandas as pd

# write config 
st.set_page_config(
    page_title="Streamlit App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# write title
st.title("Streamlit App")

# write text 
st.text("Small app to test loading data from csv and parquet files. All data is fake and generated using Faker and numpy.")

# function to load csv data 
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    return df

# function to read parquet data
@st.cache_data
def read_data(file):
    df = pd.read_parquet(file)
    return df

csv = load_data("fake_data.csv")
parquet = read_data("fake_data.parquet")

# write dataframe
st.header("CSV Dataframe")
st.write("size of dataframe: " + str(csv.shape))
st.dataframe(csv)

st.header("Parquet Dataframe")
st.write("size of dataframe: " + str(parquet.shape))
st.dataframe(parquet)
