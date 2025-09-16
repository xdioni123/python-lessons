import pandas as pd
import streamlit as st
import plotly.express as px

# df = pd.DataFrame({

#     "Name":['Jhon','Bob','Charles'],
#     "Age":[22,25,27],
#     "City":["Tirana","Paris","Berlin"]  
# })

# st.write(df)


books_df=pd.read_csv('file.csv')
st.title("Best selling books")
st.write("The best selling books from 2009 and 2022")
st.subheader("The summery of statistics")
totalbooks=books_df.shape[0]
unique_name = books_df['Name'].nunique()
avarage_rating = books_df['User Rating'].mean()
avarage_price = books_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total books",totalbooks)
col2.metric("Name",unique_name)
col3.metric("Raiting",avarage_rating)
col4.metric("Price",avarage_price)