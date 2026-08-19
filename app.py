import streamlit as st
import matplotlib.pyplot as plt
from analysis import *

st.set_page_config(page_title="Netflix Dashboard", layout="wide")

st.title("🎬 Netflix Analytics Dashboard")

df = load_data()

# Sidebar filter
st.sidebar.header("Filter")
type_filter = st.sidebar.selectbox("Select Type", df['type'].unique())

filtered_df = df[df['type'] == type_filter]

# Content Distribution
st.subheader("Content Distribution")
st.bar_chart(content_by_type(df))

# Top Countries
st.subheader("Top 10 Countries")
st.bar_chart(top_countries(df))

# Growth Over Time
st.subheader("Content Growth Over Years")
growth = content_growth(df)

fig, ax = plt.subplots()
ax.plot(growth.index, growth.values)
plt.xticks(rotation=45)
st.pyplot(fig)

# Top Genres
st.subheader("Top Genres")
st.bar_chart(top_genres(df))