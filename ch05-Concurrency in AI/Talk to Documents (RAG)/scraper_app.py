import streamlit as st
import requests

st.title("Web Scraper AI Agent")

st.write("Enter a URL to scrape:")

url = st.text_input("Target URL", "https://example.com")

if st.button("Scrape"):  
    if not url or not url.startswith("http"):
        st.error("Please enter a valid URL (starting with http/https)")
    else:
        with st.spinner("Scraping..."):
            try:
                # Adjust the FastAPI endpoint below as required
                response = requests.post(
                    "http://localhost:8000/scrape", 
                    json={"url": url}
                )
                if response.status_code == 200:
                    st.success("Scrape successful!")
                    st.json(response.json())
                else:
                    st.error(f"Error from backend: {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Request failed: {str(e)}")
