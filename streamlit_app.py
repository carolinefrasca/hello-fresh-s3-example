import streamlit as st
import s3fs
import os
import pandas as pd

st.title("Streamlit x HelloFresh")
st.header("AWS S3 Demo")
         
# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents. 
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

content = read_file("hellofreshexample/HelloFreshExample - SampleData.csv")

pd.read_csv(fs.open("hellofreshexample/HelloFreshExample - SampleData.csv"))
#data = pd.read_csv("hellofreshexample/HelloFreshExample - SampleData.csv")
st.dataframe(data)

# Print results.
st.subheader("Read data from CSV file:")
for line in content.strip().split("\n")[1:]:
    first_name, last_name, dietary_restrictions, fave_ingredient = line.split(",")
    st.write(f"{first_name} {last_name}'s favorite ingredient is {fave_ingredient}.")
#     st.write(f"First name: {first_name}; Last name: {last_name}")
