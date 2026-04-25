import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul
st.title("Bike Sharing Dashboard 🚴‍♂️")

# 🔥 Tambahan deskripsi (taruh di sini)
st.write("Dashboard ini menampilkan analisis pengaruh cuaca dan hari kerja terhadap jumlah penyewaan sepeda.")

# Load data
day_df = pd.read_csv("day.csv")

# Ubah tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Mapping cuaca
day_df['weathersit'] = day_df['weathersit'].map({
    1: 'Clear',
    2: 'Mist',
    3: 'Light Rain',
    4: 'Heavy Rain'
})

# =========================
# Visualisasi 1
# =========================
st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")

fig1, ax1 = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=day_df, ax=ax1)

# 🔥 Tambahan label
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig1)

# 🔥 Tambahan insight
st.write("Cuaca cerah menunjukkan jumlah penyewaan sepeda tertinggi dibandingkan kondisi lainnya.")

# =========================
# Visualisasi 2
# =========================
st.subheader("Perbandingan Hari Kerja vs Akhir Pekan")

fig2, ax2 = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=day_df, ax=ax2)

# 🔥 Tambahan label
ax2.set_xlabel("Hari Kerja (0 = Libur, 1 = Kerja)")
ax2.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig2)

# 🔥 Tambahan insight
st.write("Jumlah penyewaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan.")