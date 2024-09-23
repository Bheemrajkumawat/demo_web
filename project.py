import streamlit as st

st.title("Login Form")
name = st.text_input("Enter your name :")
fname = st.text_input("Enter your Father name :")
adr= st.text_area("Enter your text :")
classData = st.selectbox(" Enter your class: ",(1,2,3,4,5,6,7,8,9,10,11,12))
email= st.text_input("emailAddress")
password=st.text_input("password",type='password')
button= st.button("submit")
if button:
          st.markdown(f"""
                      Name :{name}
                      Father Name:{fname}
                      ClassData:{classData}
                      Address:{adr}
                      Email:{email}
                      Password:{password}
                      """)