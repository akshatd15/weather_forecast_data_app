import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", 1, 5, 1,
                 help="Select the number of forcasted days")
option = st.selectbox("Select data to view",
                      ['Temperature', 'Sky'])

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [temp['main']['temp']/10 for temp in filtered_data]
            date = [dt['dt_txt'] for dt in filtered_data ]
            figure = px.line(x=date, y=temperature, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":

            sky_dict = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky = [sky['weather'][0]['main'] for sky in filtered_data]
            sky_condition = [sky_dict[condition] for condition in sky]
            st.image(sky_condition, width=115)

    except KeyError:
        st.write("Entered place does not exist")

