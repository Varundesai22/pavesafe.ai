import streamlit as st
import streamlit.components.v1 as components

st.title('PaveSafe.AI')

st.subheader('Live Video Feed')
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.subheader('Road Defect Map')
with open("map.html", 'r') as f:
    html_string = f.read()
components.html(html_string, height=600)

# Alternatively, explore if there's a direct Streamlit component for displaying interactive maps
# st.map() might be suitable for simpler map visualizations but embedding HTML is more straightforward for Leaflet integration.