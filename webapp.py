import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect('data1.db')
cursor = connection.cursor()

# 1 获取时间戳 date
cursor.execute('SELECT timestamp FROM temperatures')
timestamp = cursor.fetchall()
# print(timestamp) # [('24-07-03-16-26-09',), ('24-07-03-16-26-18',), ('24-07-03-16-26-21',)]
date = [item[0] for item in timestamp]
# print(date) # ['24-07-03-16-26-09', '24-07-03-16-26-18', '24-07-03-16-26-21']

# 2 获取 温度 temperature
cursor.execute('SELECT temperature FROM temperatures')
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

figure = px.line(x=date,y=temperature,labels={'x':'Date', 'y':'Temperature'})

st.plotly_chart(figure)