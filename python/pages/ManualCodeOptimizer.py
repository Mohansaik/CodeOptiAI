import streamlit as st
import os
import sys


from streamlit_pyspark_optimizer import PySparkOptimizerLLMApp


# initialize variables here

if "user_file_input" not in st.session_state:
    st.session_state.user_file_input = None
if "user_code_input" not in st.session_state:
    st.session_state.user_code_input = ""



st.markdown("<h1 style='font-size: 2em;'> Code Optimizer </h1>",unsafe_allow_html=True)


user_file_input = st.file_uploader("Upload file (e.g., .py, .sql, .scala, .java, .r, .go, .sh, .rs)")

# st.write("or")

user_code_input = st.text_area(label="or",placeholder="Paste your code here to optimize")
if st.button("Submit"):
    if user_file_input and user_code_input:

        st.warning("You cannot upload both a file and text simultaneously. Please remove and Try again.")

    elif user_file_input or user_code_input:

        if user_file_input:
            user_input = user_file_input.getvalue().decode("utf-8")
            file_name = st.session_state.user_file_input.name
        else:
            user_input = user_code_input
            file_name = "Pasted Code"
        
        st.write(f"📂 **Analyzing:** `{file_name}`")

        with st.spinner("Processing"):
            suggestions = PySparkOptimizerLLMApp(user_input,"common").run()

        st.markdown(f"{suggestions}")

if st.button("clear"):
    st.session_state.user_file_input = None
    st.session_state.user_code_input = ""
