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

@st.cache_data
def read_data(file):
    df = pd.read_parquet(file)
    return df

parquet = read_data("fake_data.parquet")

column_options = ['job', 'company', 'blood_group', 'sex']

# write selectbox
column = st.sidebar.selectbox("Select column", column_options)

column_value = parquet[column].unique()

# write multiselect
column_value = st.sidebar.multiselect("Select value", column_value)

# add apply button
apply_button = st.sidebar.button("Apply")

# function to filter dataframe
@st.cache_data
def filter_dataframe(df, column, column_value):
    df = df[df[column].isin(column_value)]
    return df

if apply_button:
    parquet = filter_dataframe(parquet, column, column_value)
    # write dataframe
    st.header("Parquet Dataframe")
    st.write("size of dataframe: " + str(parquet.shape))
    st.dataframe(filter_dataframe(parquet, column, column_value))
else: 
    pass


