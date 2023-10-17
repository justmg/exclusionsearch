import streamlit as st
import requests

# Function to query the Exclusions API
def query_exclusions_api(uei):
    url = f"https://api.gsa.gov/entity-information/v1/exclusions/{uei}"
    headers = {
        'Authorization': 'poORnzZwlTFovtdCgNJHvkwCyrdvD7w6I66fBmki',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to retrieve data: {response.text}")

# Streamlit interface
st.title("Exclusions API Query")
uei = st.text_input("Enter Unique Entity Identifier (UEI):")
if uei:
    data = query_exclusions_api(uei)
    if data:
        st.write(data)
