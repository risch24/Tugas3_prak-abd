import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🍨 Aplikasi Visualisasi Dessert Internasional")
st.write("Selamat datang! Ini adalah aplikasi visualisasi 10 dessert internasional lengkap dengan deskripsi, gambar, dan grafik interaktif.")

data = pd.DataFrame({
    "Dessert": [
        "Tiramisu (Italia)",
        "Cheesecake (Amerika Serikat)",
        "Macaron (Prancis)",
        "Mochi (Jepang)",
        "Churros (Spanyol)",
        "Lamington (Australia)",
        "Taiyaki (Jepang)",
        "Serabi (Indonesia)",
        "Trifle (Inggris)",
        "Bingsu (Korea Selatan)"
    ],
    "Deskripsi": [
        "Dessert berlapis krim mascarpone, kopi, dan kakao dari Italia.",
        "Kue lembut dengan krim keju yang populer di seluruh dunia.",
        "Kue kecil berwarna-warni dengan tekstur renyah di luar dan lembut di dalam.",
        "Kue beras ketan Jepang dengan tekstur kenyal.",
        "Camilan goreng berbentuk panjang, biasa disajikan dengan gula dan coklat.",
        "Kue sponge dilapisi coklat dan kelapa parut khas Australia.",
        "Kue ikan Jepang berisi pasta kacang merah atau custard.",
        "Pancake tradisional Indonesia berbahan santan dengan aroma pandan.",
        "Dessert berlapis krim, buah, jelly, dan sponge cake dari Inggris.",
        "Es serut ala Korea dengan topping buah, kacang, atau susu kental manis."
    ],
    "Kalori (kcal)": [300, 450, 90, 110, 280, 170, 230, 150, 320, 180],
    "Gambar": [
        "tiramisu cake.jpg",
        "cheesecake.jpg",
        "macarons.jpg",
        "mochi.jpg",
        "churros.jpg",
        "lamington.jpg",
        "taiyaki.jpg",
        "serabi.jpg",
        "trifle.jpg",
        "bingsu.jpg",
    ]
})

# GAMBAR & DESKRIPSI
st.subheader("📸 Gambar & Deskripsi Dessert Internasional")
for i, row in data.iterrows():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(row["Gambar"], width=250)
    
    with col2:
        st.markdown(f"### 🍰 {row['Dessert']}")
        st.write(row["Deskripsi"])
        st.write(f"**Kalori:** {row['Kalori (kcal)']} kcal")
    st.markdown("---")

# DATAFRAME
st.subheader("📊 Tabel Data Dessert")
st.dataframe(data)

# GRAFIK
st.subheader("🎛 Pilih Jenis Grafik")
tipe = st.selectbox(
    "Pilih grafik yang ingin ditampilkan:",
    ["Bar Chart", "Pie Chart", "Line Chart", "Area Chart", "Map Lokasi"]
)

if tipe == "Bar Chart":
    st.bar_chart(data.set_index("Dessert")["Kalori (kcal)"])

elif tipe == "Line Chart":
    st.line_chart(data.set_index("Dessert")["Kalori (kcal)"])

elif tipe == "Area Chart":
    st.area_chart(data.set_index("Dessert")["Kalori (kcal)"])

elif tipe == "Pie Chart":
    fig, ax = plt.subplots()
    ax.pie(
        data["Kalori (kcal)"],
        labels=data["Dessert"],
        autopct="%1.1f%%",
        textprops={'fontsize': 7}
    )
    st.pyplot(fig)

elif tipe == "Map Lokasi":
    st.subheader("🗺 Lokasi Asal Dessert (Perkiraan)")
    map_data = pd.DataFrame({
        "Dessert": data["Dessert"],
        "lat": [41.9, 40.7, 48.8, 35.6, 40.4, -33.8, 35.6, -6.9, 51.5, 37.5],
        "lon": [12.5, -74.0, 2.3, 139.7, -3.7, 151.2, 139.7, 107.6, -0.1, 127.0]
    })
    st.map(map_data)

# FILTER KALORI
st.subheader("🔍 Filter Dessert Berdasarkan Kalori")
nilai = st.slider("Tampilkan dessert dengan kalori minimum:", 0, 500, 100)
st.dataframe(data[data["Kalori (kcal)"] >= nilai])

# DASHBOARD MINI
st.title("📈 Dashboard Mini Dessert")
pilih = st.selectbox("Pilih dessert:", data["Dessert"])
row = data[data["Dessert"] == pilih].iloc[0]

st.metric("Kalori Dessert", f"{row['Kalori (kcal)']} kcal", delta=row["Kalori (kcal)"] - 200)
st.progress(min(row["Kalori (kcal)"] / 500, 1))

fig2, ax2 = plt.subplots()
ax2.bar(data["Dessert"], data["Kalori (kcal)"], color="orange")
ax2.set_ylabel("Kalori (kcal)")
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig2)

# RATING
st.subheader("⭐ Beri Rating Dessert")
dessert_rating = st.selectbox("Pilih dessert yang ingin dinilai:", data["Dessert"])
rating = st.number_input("Masukkan rating (1–5):", min_value=1, max_value=5, value=3, step=1)
st.write(f"Rating untuk **{dessert_rating}** adalah **{rating} ⭐**")

# PENUTUP
st.markdown("""
### 🍰 Tentang Dessert Internasional  
Dessert dari berbagai negara memiliki ciri khas tersendiri, baik dari bahan, rasa, hingga teknik pembuatannya.  
Aplikasi ini membantu memvisualisasikan perbedaan dessert melalui data interaktif yang menarik.
""")
