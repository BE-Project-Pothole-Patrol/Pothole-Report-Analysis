import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Data',
    page_icon='📈'
)

df = pd.DataFrame({'States': ['Maharashtra','Maharashtra','Maharashtra', 'Kerala','Kerala','Kerala','Kerala','Kerala','Karnataka','Karnataka','Karnataka','Karnataka','Karnataka','Karnataka','Karnataka','Karnataka','Karnataka', 'Delhi','Delhi']})
cnt = df.States.value_counts()

st.title('Project Stats')

x_p = [619, 1552, 352]
y_p = ['Unpaved','Normal','Potholes']

st.text('')
st.text('')
st.text('')
st.text('')

x2 = sum(x_p)
# st.subheader('Processed {} Reports So Far!!'.format(x2))

# st.text('')
st.text('')
st.text('')
# st.text('')

x_b = cnt.values
y_b = cnt.index

plt.figure(figsize=(12,8))

st.subheader('Number Of Reports vs States:')
fig_bar, ax = plt.subplots()
ax.set_facecolor('white')
fig_bar.set_facecolor('white')
ax.spines['bottom'].set_color('black')
ax.tick_params(colors='black')
ax.barh(y_b, x_b)
st.pyplot(fig_bar)

st.text('')
st.text('')
st.text('')
st.text('')

st.subheader('Images Classified Till Now.... :')
fig_bar, ax = plt.subplots()
legends = list(y_p)
colors = ['#2aa4f5','#55f74f','#ff9500']
ax.pie(x_p, labels=y_p, colors=colors)
ax.legend(legends)
st.pyplot(fig_bar)
