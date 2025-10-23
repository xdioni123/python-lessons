from fastapi import FastApi
from models import Developer, Project

app = FastApi()

@app.post("/developers/")
def developer(developer: Developer):
    return{"message": "The developer has been sucssesful", "developer": developer}

@app.post("/projects/")
def developer(project: Project):
    return{"message": "The project has been sucssesful", "project": project}

@app.get("/projects")
def get_projects():
    sample_project=Project(
        title = "Project 1"
        description = "This project is about the coding langueges"
        languages = ["Python, javascript, Php"]
        lead_developer = Developer(emri="Jhon doe" , experience = 0)
    )