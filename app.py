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
    clean_option = st.checkbox("Clean data for testing report")
    if clean_option:
        df = df.drop_duplicates()
        df = df.fillna(df.mean(numeric_only=True))
        st.success("✔️ Data cleaned successfully!")
    
    # Column Selection
    st.subheader("🎯 Select Columns to Keep")
    columns = st.multiselect("Choose columns to keep:", df.columns, default=list(df.columns))
    df = df[columns]
    
    # Data Visualization Option
    st.subheader("📊 Data Visualization")
    visualize_option = st.checkbox("Show visualization for uploaded file")
    if visualize_option:
        st.line_chart(df.select_dtypes(include=['number']))
    
    # File Conversion Option
    st.subheader("🔄 Conversion Options")
    convert_to = st.radio("Convert file to:", ("CSV", "Excel"))
    if convert_to == "CSV":
        converted_file = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download as CSV", converted_file, "cleaned_data.csv", "text/csv")
    else:
        converted_file = df.to_excel(index=False).encode("utf-8")
        st.download_button("Download as Excel", converted_file, "cleaned_data.xlsx", "application/vnd.ms-excel")
