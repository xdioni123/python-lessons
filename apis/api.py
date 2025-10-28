import streamlit as st
import request
import pandas as pd

st.title("Project Managment App")

st.header("Add developer")
dev_name = st.text_input("Developer name")
dev_experience = st.text_input("Experience (Years)", min_value=0 , max_value=50 value=0)

if st.button ("Create Developer"):
    dev_data = {"name" : dev_name, "experience" : dev_experience}
    response = request.post("http://localhost:8000/developers", json = dev_data)
    st.json(response.json())

st.header("Add Project")
proj_title=st.text_input("Project title")
proj_desc=st.text_area("Project description")
proj_lang=st.text_input("Language used")
proj_lead_dev=st.text_input("Lead developer name")
proj_lead_dev_exp=st.number_input("Lead developer experience" min_value=0 , max_value=50 , value=0)

if st.button("Create Project"):
    lead_dev_data = {"name": proj_lead_dev , "Experience": proj_lead_dev_exp}
    proj_data = {
        "title": proj_title,
        "project description": proj_desc,
        "languages": proj_lang.split(","),
        "Lead Devs": lead_dev_data
    }
    response = request.post("http://localhost:8000/projects/" , json = proj_data)
    st.json(response.json())

st.header("Project Dashboard")

if st.button("Get projects"):
    response = request.get("http://localhost:8000/projects/")
    project_data = response.json()['projects']

    if project_data:
        project_df = pd.DataFrame(project_data)


        st.subheader("Project Overview")
        st.datafrane(project_df)

        
        st.subheader("Project Details")
        for project in project_data:
            st.markdown(f"Title {project['title']}")
            st.markdown(f"Disc {project['description']}")
            st.markdown(f"languages {project['languages']}")
            st.markdown(f"Lead Developer  {project['lead_developer']['name']} with {project['lead_developer']['experience']} years of experience")
            st.markdown("------------")
        else:
            st.warning("No Projects found")
