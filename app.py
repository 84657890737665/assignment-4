# Python streamlit BMI Calculator 

# Import
import streamlit as st 

# Title of the web-app
st.title("BMIfy ⚖")

# Input Fields for the User

height = st.number_input("Enter your Height in meters (e.g: 1.75): ", min_value=0.00,  format="%.2f")
weight = st.number_input("Enter your Weight in kilograms (e.g: 65): ",  min_value=0.00,  format="%.2f")

# Calculator 

if st.button("Calculate"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI IS: {bmi: .2f}")


# category

        if bmi < 20.5:        
           st.info("You're Underweight!")
        elif 20.5 <= bmi > 35.5:
          st.success("You're Fit! You've normal weight.")
        elif 35.5 <= bmi > 70:
         st.warning("You're overwight!")
        else:
           st.error("You're obese.")
else:
    st.error("Please eneter the correct values..")    