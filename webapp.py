import streamlit as st
import plotly.express as px
import pandas

df = pandas.read_csv('date_temperature.txt')

figure = px.line(x=df['Date'],y=df['Temperature'],labels={'x':'Date', 'y':'Temperature'})

st.plotly_chart(figure)