import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Custom background color
# st.markdown("""
#     <style>
#         .main {
#             background-color: #f4ff;
#         }
#     </style>
#     """, unsafe_allow_html=True)
pd.options.mode.chained_assignment = None

# Load the datasets
dongsi_data = pd.read_csv("PRSA_Data_Dongsi_Clear.csv")
wanliu_data = pd.read_csv("PRSA_Data_Wanliu_Clear.csv")

# Set style for seaborn
sns.set_style("whitegrid")

# Sidebar
st.sidebar.header("Pengaturan Visualisasi")
selected_year = st.sidebar.slider("Pilih Tahun", 2013, 2017, 2013)
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
selected_pollutant = st.sidebar.selectbox("Pilih Polutan", pollutants)

# Filter data
dongsi_filtered = dongsi_data[dongsi_data['year'] == selected_year]
wanliu_filtered = wanliu_data[wanliu_data['year'] == selected_year]
dongsi_filtered['month'] = dongsi_filtered['month'].astype(str)
wanliu_filtered['month'] = wanliu_filtered['month'].astype(str)

# Main Content
st.title("Visualisasi Kualitas Udara")
st.subheader(f"Kualitas Udara di Dongsi dan Wanliu Tahun {selected_year}")

# Combined Plot
st.subheader(f"Rata-rata konsentrasi {selected_pollutant} di Dongsi dan Wanliu")
fig, ax = plt.subplots()
sns.lineplot(data=dongsi_filtered, x='month', y=selected_pollutant, ax=ax, label="Dongsi", marker="o", color="blue", ci=None)
sns.lineplot(data=wanliu_filtered, x='month', y=selected_pollutant, ax=ax, label="Wanliu", marker="D", linestyle=":", color="red", ci=None)
ax.set_title(f'Rata-rata konsentrasi {selected_pollutant} tahun {selected_year} per bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel(f'Konsentrasi {selected_pollutant}')
ax.legend()
st.pyplot(fig)

# Data Display
if st.sidebar.checkbox("Tampilkan Data", value=False):  # Default unchecked
    st.subheader("Data Dongsi")
    st.write(dongsi_filtered)
    st.subheader("Data Wanliu")
    st.write(wanliu_filtered)
