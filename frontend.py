import streamlit as st
import plotly.express as px


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", 1, 5, 1,
                 help="Select the number of forcasted days")
option = st.selectbox("Select data to view",
                      ['Temperature', 'Sky'])

st.subheader(f"{option} for the next {days} days in {place}")

figure = px.line(x=, y=, labels=)
st.plotly_chart(figure)