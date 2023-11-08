import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Baca data dari file CSV
df = pd.read_csv('Mlbb_Heroes.csv')

# Tampilkan data dalam aplikasi Streamlit
st.title('Data Hero MLBB')
st.write(df)

# Buat chart pie dengan Plotly
fig = px.pie(df, names='Primary_Role', title='Role Hero')
st.plotly_chart(fig)

fig = px.bar(df, x='Name', y='Esport_Wins', title='Match Esport')
st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Load data from CSV # Cache the data to improve performance
def load_data():
    df = pd.read_csv('MPL_ID_S10.csv')
    return df

df = load_data()

# Display the DataFrame in Streamlit
st.title('DATA MPL ID S10')
st.write(df)

# Create a bar chart with Plotly Express
fig = px.pie(df, names='Bs_picked', title='Best Picked')
st.plotly_chart(fig)

fig = px.bar(df, x='Hero', y='T_winrate', title='Win Rate of MPL Mobile Legends Heroes')
st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load data from CSV
def load_data():
    df = pd.read_csv('best-selling-manga.csv')
    return df

df = load_data()

# Display the DataFrame in Streamlit
st.title('DATA PENJUALAN MANGA TERBAIK')
st.write(df)

# Create a bar chart with Plotly Express
fig = px.pie(df, names='Publisher', title='Manga Publisher')
st.plotly_chart(fig)

fig = px.bar(df, x='Manga series', y='Approximate sales in million(s)', title='Best Selling Manga')
st.plotly_chart(fig)

