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

st.subheader("Stats")
st.write(books_df.head())

col1 ,col2 = st.columns(2)

with col1:
    st.subheader("Top 10 most sold books")
    st_titles=books_df["Name"].value_counts().head(10)
    st.bar_chart(st_titles)

with col2:
    st.subheader("Top 10 viewd authors")
    st_authors=books_df["Author"].value_counts().head(10)
    st.bar_chart(st_authors)

st.subheader("Gemre Distribution")
fig = px.pie(books_df, names="Genre",title='Most liked Genre 2009-2022', color="Genre",
color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Top 15 Authors")
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns=['Author','Count']

figg = px.bar(top_authors, x='Count', y='Author',orientation='h',
              title='Top 15 authors',
              labels={'Count': 'Counts of Books Published','Author':'Author'},
              color='Count', color_continuous_scale=px.colors.sequential.Plasma
              )

st.plotly_chart(figg)