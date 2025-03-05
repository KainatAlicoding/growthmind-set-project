import streamlit as st
import pandas as pd

# Streamlit page setup
st.set_page_config(page_title="Datasweeper - CSV/Excel Cleaner", layout="wide")
st.title("🧹 Datasweeper Sterling Integrator")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

# File uploader
uploaded_file = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=False)

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]
    
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.success("✅ File uploaded successfully!")
    st.subheader("📊 Preview of Uploaded Data:")
    st.dataframe(df.head())
    
    # Data Cleaning Options
    st.subheader("🧼 Data Cleaning Options:")
    if st.button("Remove Duplicates"):
        df = df.drop_duplicates()
        st.success("✔️ Duplicates removed!")
    
    if st.button("Fill Missing Values with Mean"):
        df = df.fillna(df.mean(numeric_only=True))
        st.success("✔️ Missing values filled!")
    
    # File Download Option
    st.subheader("💾 Download Cleaned File:")
    cleaned_file = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download as CSV", cleaned_file, "cleaned_data.csv", "text/csv")
