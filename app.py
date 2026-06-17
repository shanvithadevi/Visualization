import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App title
st.title("📊 Dataset Analyzer & Visualizer")

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Load dataset
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📋 Dataset Preview")
    st.write(df.head())

    st.subheader("📈 Dataset Summary")
    st.write(df.describe(include="all"))

    # Column selection
    st.sidebar.header("Visualization Options")
    x_axis = st.sidebar.selectbox("Select X-axis", df.columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", df.columns)
    chart_type = st.sidebar.radio("Choose chart type", ["Scatter", "Line", "Bar", "Histogram", "Heatmap"])

    st.subheader("📊 Visualization")

    if chart_type == "Scatter":
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Line":
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Bar":
        fig, ax = plt.subplots()
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Histogram":
        fig, ax = plt.subplots()
        sns.histplot(df[x_axis], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Heatmap":
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

else:
    st.info("👆 Upload a dataset to get started.")
