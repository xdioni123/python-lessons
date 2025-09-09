# from abc import ABC, abstractmethod


# class Person(ABC):
#     """
#     Abstract base class representing a person.
#     """

#     def __init__(self, name, age, weight, height):
#         """
#         Initializes a new instance of the Person class.
#         """
#         self.name = name
#         self.age = age
#         self._weight = weight
#         self._height = height

#     @property
#     def weight(self):
#         """
#         Gets the weight of the person.

#         Returns:
#             float: The weight of the person.
#         """
#         return self._weight

#     @weight.setter
#     def weight(self, value):
#         """
#         Sets the weight of the person.

#         Raises:
#             ValueError: If the weight is negative.
#         """
#         if value < 0:
#             raise ValueError("Weight cannot be negative")
#         self._weight = value

#     @property
#     def height(self):
#         """
#         Gets the height of the person.
#         """
#         return self._height

#     @height.setter
#     def height(self, value):
#         """
#         Sets the height of the person.

#         Raises:
#             ValueError: If the height is negative.
#         """
#         if value < 0:
#             raise ValueError("Height cannot be negative")
#         self._height = value

#     @abstractmethod
#     def calculate_bmi(self):
#         """
#         Calculates the BMI of the person.
#         """
#         pass

#     @abstractmethod
#     def get_bmi_category(self):
#         """
#         Gets the BMI category of the person.
#         """
#         pass

#     def print_info(self):
#         """
#         Prints the information of the person, including BMI and category.
#         """
#         print(f"{self.name}, Age: {self.age}, Weight: {self.weight} kg, Height: {self.height} m, "
#               f"BMI: {self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}")


# class Adult(Person):
#     """
#     Subclass representing an adult person.
#     """

#     def calculate_bmi(self):
#         """
#         Calculates the BMI of the adult using the formula weight/(height^2).
#         """
#         return self.weight / (self.height ** 2)

#     def get_bmi_category(self):
#         """
#         Gets the BMI category of the adult.
#         """
#         bmi = self.calculate_bmi()
#         if bmi < 18.5:
#             return "Underweight"
#         elif 18.5 <= bmi < 24.9:
#             return "Normal weight"
#         elif 24.9 <= bmi < 29.9:
#             return "Overweight"
#         else:
#             return "Obese"


# class Child(Person):
#     """
#     Subclass representing a child person.
#     """

#     def calculate_bmi(self):
#         """
#         Calculates the BMI of the child using the formula weight/(height**2)*1.3
#         """
#         return (self.weight / (self.height ** 2)) * 1.3

#     def get_bmi_category(self):
#         """
#         Gets the BMI category of the child.
#         """
#         bmi = self.calculate_bmi()
#         if bmi < 14:
#             return "Underweight"
#         elif 14 <= bmi < 18:
#             return "Normal weight"
#         elif 18 <= bmi < 24:
#             return "Overweight"
#         else:
#             return "Obese"


# class BMIApp:
#     """
#     Class representing the BMI application.
#     """

#     def __init__(self):
#         """
#         Initializes a new instance of the BMIApp class.
#         Creates an empty list to store Person objects.
#         """
#         self.people = []

#     def add_person(self, person):
#         """
#         Adds a person to the list of people.
#         """
#         self.people.append(person)

#     def collect_user_data(self):
#         """
#         Collects user data from the console and creates a Person object.
#         """
#         name = input("Enter name: ")
#         age = int(input("Enter age: "))
#         weight = float(input("Enter weight in kilograms: "))
#         height = float(input("Enter height in meters: "))

#         if age >= 18:
#             person = Adult(name, age, weight, height)
#         else:
#             person = Child(name, age, weight, height)

#         self.add_person(person)

#     def print_results(self):
#         """
#         Prints the results for all collected people.
#         """
#         for person in self.people:
#             person.print_info()

#     def run(self):
#         """
#         Runs the BMI application, collecting user data and printing results.
#         """
#         while True:
#             self.collect_user_data()
#             cont = input("Do you want to add another person? (yes/no): ").strip().lower()
#             if cont != 'yes':
#                 break
#         self.print_results()


# # Create an instance of BMIApp and run the application
# app = BMIApp()
# app.run()


from abc import ABC, abstractmethod
import streamlit as st

# Custom CSS for a futuristic, tech-themed look
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&family=Roboto+Mono&display=swap');

        html, body, .stApp {
            background-color: #0a0f1a;
            color: #cfd8dc;
            font-family: 'Roboto Mono', monospace;
        }

        .title {
            font-family: 'Orbitron', sans-serif;
            font-size: 3em;
            color: #00bfff;
            text-align: center;
            text-shadow: 0 0 10px #00bfff;
            margin-bottom: 20px;
        }

        .subtitle {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5em;
            color: #39c0ed;
            margin-top: 30px;
            border-left: 5px solid #39c0ed;
            padding-left: 10px;
        }

        .stTextInput > div > div > input,
        .stNumberInput input {
            background-color: #1c2331;
            color: #cfd8dc;
            border: 1px solid #39c0ed;
            border-radius: 4px;
        }

        .stButton > button {
            background-color: #39c0ed;
            color: black;
            font-weight: bold;
            border-radius: 5px;
            box-shadow: 0px 0px 10px #39c0ed;
            transition: 0.3s;
        }

        .stButton > button:hover {
            background-color: #00bfff;
            box-shadow: 0px 0px 20px #00bfff;
        }

        .table-container {
            margin-top: 30px;
            background-color: #111827;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,191,255, 0.3);
        }

        .stTable {
            font-family: 'Roboto Mono', monospace;
        }

    </style>
""", unsafe_allow_html=True)

# Abstract base class
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def get_info(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Weight (kg)": self.weight,
            "Height (m)": self.height,
            "BMI": f"{self.calculate_bmi():.2f}",
            "Category": self.get_bmi_category()
        }

class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"

# Session state for people list
if 'people' not in st.session_state:
    st.session_state.people = []

# Title
st.markdown('<div class="title">💻 BMI Calculator Dashboard</div>', unsafe_allow_html=True)

# Form to add a person
st.markdown('<div class="subtitle">➕ Enter Person Data</div>', unsafe_allow_html=True)

with st.form("bmi_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Height (m)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add Person")

    if submitted:
        try:
            person = Adult(name, age, weight, height) if age >= 18 else Child(name, age, weight, height)
            st.session_state.people.append(person)
            st.success(f"✅ {name} added successfully!")

        except ValueError as e:
            st.error(str(e))

# Display results
if st.session_state.people:
    st.markdown('<div class="subtitle">📊 Results</div>', unsafe_allow_html=True)
    people_info = [person.get_info() for person in st.session_state.people]
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.table(people_info)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Add a person to calculate BMI.")

