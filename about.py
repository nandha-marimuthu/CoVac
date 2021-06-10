import streamlit as st

def about():
    st.title('Covid Guide')
    a=st.video("covid.mp4")
    st.header("Helpline")
    e1 = st.beta_expander("Medical Assisstance Helpline")
    e1.write("Chennai : 1800-001")
    e1.write("Trichy  : 1800-002")
    e1.write("Madurai : 1800-003")
    e1.write("Nellore : 1800-004")

    e2 = st.beta_expander("For covid related issues")
    e2.write("Chennai : 1800-005")
    e2.write("Trichy  : 1800-006")
    e2.write("Madurai : 1800-007")
    e2.write("Nellore : 1800-008")

    e3 = st.beta_expander("Official mail")
    e3.write("tnvaccinationportal@gmail.com")

