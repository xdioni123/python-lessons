import streamlit as st
col1,col2,col3,col4,col5 = st.columns(5,gap="small",vertical_aligment="center")

with col1:
    st.header("Colum1")
    st.write("This is colum 1")
with col2:
    st.header("Colum2")
    st.write("This is colum 2")
with col3:
    st.header("Colum3")
    st.write("This is colum 3")
with col4:
    st.header("Colum4")
    st.write("This is colum 4")
with col5:
    st.header("Colum5")
    st.write("This is colum 5")


st.sidebar.header("Sidebar")
st.sidebar.write("This is sidebar")
# st.sidebar.selectbox("Chose an option",["Option 1","Option 2","Option 3"])
st.sidebar.radio("Chose an option",["Home","Contact Us","About Us"])

with st.form("my_form", clear_on_submit=True):
    name = st.text_input('name')
    surname = st.text_input('surname')
    age = st.slider('Age',min_value=0, max_value = 100)
    email = st.text_input('email')
    terms = st.checkbox('I agree to the terms and conditions')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'Name:{name}')
    st.write(f'Age:{age}')
    st.write(f'surname:{surname}')
    st.write(f'Email:{email}')

    if terms:
        st.write('You agreed to the terms and conditions')
    else:
        st.write('You didnt agree to the terms and conditions')


tab1,tab2,tab3=st.tabs(["Tab1","Tab2","Tab3"])

with tab1:
    st.header("This is tab 1")

with tab2:
    with st.form("your_form", clear_on_submit=True):
        name = st.text_input('name')
        surname = st.text_input('surname')
        age = st.slider('Age',min_value=0, max_value = 100)
        email = st.text_input('email')
        terms = st.checkbox('I agree to the terms and conditions')
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write(f'Name:{name}')
        st.write(f'Age:{age}')
        st.write(f'surname:{surname}')
        st.write(f'Email:{email}')

    if terms:
        st.write('You agreed to the terms and conditions')
    else:
        st.write('You didnt agree to the terms and conditions')

with tab3:
    st.header("Tab 3")
    st.write("This is the 3rd tab")

