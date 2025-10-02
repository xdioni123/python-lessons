import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Top Organizations Dashboard", layout="wide")

organizations_df = pd.read_csv('Organization.csv')

st.title(" Most Popular Organizations")
st.markdown("###  The most successful organizations as of **2025**")
st.markdown("---")

st.subheader(" Summary Statistics")

total_orgs = organizations_df.shape[0]
unique_names = organizations_df['Name'].nunique()
average_employees = organizations_df['Number of employees'].mean()
average_founded_year = organizations_df['Founded'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric(" Total Organizations", total_orgs)
col2.metric(" Unique Names", unique_names)
col3.metric(" Avg Employees", f"{average_employees:,.0f}")
col4.metric(" Avg Founded Year", f"{average_founded_year:.0f}")

st.markdown("---")

st.subheader(" Full Organization Dataset")
with st.expander("Click to view full data table"):
    st.dataframe(
        organizations_df.style.set_properties(**{
            'background-color': '#f9f9f9',
            'color': '#333333',
            'border-color': 'white'
        }),
        use_container_width=True
    )

st.markdown("---")
st.subheader(" Top 10 Organizations by Number of Employees")

top_orgs = organizations_df.sort_values(by="Number of employees", ascending=False).head(10)

fig = px.bar(
    top_orgs,
    x='Name',
    y='Number of employees',
    color='Industry',
    hover_data=['Country', 'Founded'],
    title="Top 10 Organizations by Employee Count",
    labels={'Number of employees': 'Employees', 'Name': 'Organization'},
    template='plotly_white'
)

fig.update_layout(
    xaxis_tickangle=-45,
    xaxis_title=None,
    yaxis_title="Employee Count",
    title_x=0.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)
