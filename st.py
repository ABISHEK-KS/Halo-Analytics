import streamlit as st
import requests
import pandas as pd

# Define API endpoints
API_BASE_URL = "https://www.freetogame.com/api/games"

# Function to fetch data from API
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return pd.DataFrame(data)

# Streamlit app
st.title("FreeToGame Data Viewer")

# Tabs for different views
tabs = st.sidebar.radio("Select View", ["Live Games List", "Games by Platform", "Games by Category", "Games by Sort"])

if tabs == "Live Games List":
    st.header("Live Games List")
    data = fetch_data(API_BASE_URL)
    st.write(data)

elif tabs == "Games by Platform":
    st.header("Games by Platform")
    platform = st.selectbox("Select Platform", ["pc", "browser", "all"])
    endpoint = f"{API_BASE_URL}?platform={platform}"
    data = fetch_data(endpoint)
    st.write(data)

elif tabs == "Games by Category":
    st.header("Games by Category")
    category = st.selectbox("Select Category", ["mmorpg", "shooter", "pvp", "mmofps", "all"])
    endpoint = f"{API_BASE_URL}?category={category}"
    data = fetch_data(endpoint)
    st.write(data)

elif tabs == "Games by Sort":
    st.header("Games by Sort")
    sort_by = st.selectbox("Select Sort Type", ["release-date", "popularity", "alphabetical", "relevance"])
    endpoint = f"{API_BASE_URL}?sort-by={sort_by}"
    data = fetch_data(endpoint)
    st.write(data)

# Download button
if st.button("Download Data"):
    df = fetch_data(API_BASE_URL)
    csv = df.to_csv(index=False)
    st.download_button(label="Download CSV", data=csv, file_name='games_data.csv', mime='text/csv')
