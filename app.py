import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Students Performance Dashboard")

st.sidebar.header("Filters")
selected_gender = st.sidebar.selectbox("Gender", options=["All"] + list(df["gender"].unique()))

filtered_df = df if selected_gender == "All" else df[df["gender"] == selected_gender]

st.write("## Dataset Preview")
st.dataframe(filtered_df.head())

st.write("## Score Distribution by Category")
selected_cat = st.selectbox("Select Categorical Variable", ['gender', 'race/ethnicity', 'parental level of education'])

fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x=selected_cat, y='math score', ax=ax)
st.pyplot(fig)
