'''
As a user, I want to use a program which can generate random password and display the result on user interface. So that I can generate my password for any application.

Acceptance Criteria:

Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
You must import some required modules or packages.
The GUI of program must contain at least a button and a label.
The result should be display on the password label when the user click the generate button.
'''


# http://54.234.188.223:8501/
# streamlit run app.py

from random import choice,shuffle
import streamlit as st
html_temp = """
<div style="width:700px;background-color:black;padding:10px">
<h1 style="color:white;text-align:center;">Generate Your Password</h1>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

from PIL import Image
im = Image.open("image.jpg")
st.image(im, width=700)

upper_cases='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_cases='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
specials='!"#$%&\()*+,-./:;<=>?@[]^_`{|}~'
all_char=upper_cases+lower_cases+digits+specials

st.sidebar.header("Configure the Password Features:")
lenght=st.slider('What is the lenght of password?',0,20,10)
upper_case_count=st.sidebar.slider('What is the count of the upper cases at least?',0,10,2)
lower_case_count=st.sidebar.slider('What is the count of the lower cases at least?',0,10,2)  
digit_count=st.sidebar.slider('What is the count of the digits at least?',0,10,2)  
special_count=st.sidebar.slider('What is the count of the special characters at least?',0,10,2)


if st.button('Generate'):
    upper,lower,special,digit,password=['' for _ in range(5)]

    for i in range(upper_case_count):
        upper += choice(upper_cases)

    for i in range(lower_case_count):
        lower += choice(lower_cases)

    for i in range(digit_count):
        digit += choice(digits)

    for i in range(special_count):
        special += choice(specials)

    must_be = upper + lower + digit + special

    for i in range(lenght-len(must_be)):
        password += choice(all_char)

    password+=must_be
    password=list(password)
    shuffle(password)

    st.success(f'''Password: "{''.join(password)}"''')