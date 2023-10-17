import streamlit as st
import requests
import json

# Function to fetch exclusion data
def fetch_exclusion_data(uei, api_key):
    base_url = f"https://api.open.gsa.gov/exclusions/{uei}"
    headers = {
        "X-Api-Key": api_key,
    }
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI
st.title("Exclusion Information Checker")

# Taking UEI as input
uei = st.text_input("Enter UEI: ")

if uei:
    # Define your API Key here
    api_key = "poORnzZwlTFovtdCgNJHvkwCyrdvD7w6I66fBmki" # Replace with your actual API Key
    
    # Fetching and displaying data
    data = fetch_exclusion_data(uei, api_key)
    
    if data:
        st.write("### Exclusion Details:")
        st.json(data)
    else:
        st.write("No data found or an error occurred while fetching the data.")

