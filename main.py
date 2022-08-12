import streamlit as st
import pandas as pd


def main() -> None:
    st.write("Webform Site")
    with st.form('visa-form'):
        first_name = st.text_input("First name")
        last_name = st.text_input("Last name")
        country = st.selectbox("Country", ("USA", "Canada", "Mexico"))
        visa_type = st.selectbox("Visa type", ("Student", "Work", "Business"))
        date = st.date_input("Date")
        time = st.time_input("Time")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Name:", first_name, last_name, "Country:", country, "Visa type:", visa_type, "Date:", date, "Time:", time)

if __name__ == "__main__":
    st.set_page_config(
        "Webform Site",
        "🕴️",
        initial_sidebar_state="auto",
        layout="centered",
    )
    main()