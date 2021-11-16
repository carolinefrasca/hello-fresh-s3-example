import streamlit as st
import s3fs
import os

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

# Print results.
for line in content.strip().split("\n"):
    first_name, last_name, dietary_restrictions, fave_ingredients = line.split(",")
    st.write(f"First name: {first_name}; Last name: {last_name}")
