import streamlit as st
st.title("BMI CALCULATOR")
weight=st.number_input("Enter weight(kg):")
height=st.number_input("Enter height(m):") or 1
button=st.button("CALCULATE")
if button:
    bmi=weight/height**2
    st.write(f"your bmi is {bmi:.2f}")
    if bmi<18.5:
        st.warning("underweight")
    elif bmi<25:
        st.success("Normal")
    else:
        st.error("overweight")
