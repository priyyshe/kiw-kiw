import streamlit as st

st.set_page_config(page_title="Tes MBTI", page_icon=":tada:", layout="centered")
st.title("Tes MBTI: Introvert vs Extrovert")
st.write("Pilih jawaban yang paling sesuai dengan dirimu untuk setiap pertanyaan berikut:")

#gambar tittle
st.image("https://www.digitalmomblog.com/wp-content/uploads/2022/01/introvert-vs-extrovert-meme-1080x720.jpeg", width=300)

# Inisialisasi skor
score = {
    "Introvert": 0,
    "Extrovert": 0,
}

# Pertanyaan 1
q1 = st.radio("1. Ketika berada di keramaian, saya merasa:", ["Energi penuh", "Lelah"])
if q1 == "Energi penuh":
    score["Extrovert"] += 1
elif q1 == "Lelah":
    score["Introvert"] += 1

# Pertanyaan 2
q2 = st.radio("2. Saya lebih suka:", ["Berbicara di depan umum", "Mendengarkan orang lain"])   
if q2 == "Berbicara di depan umum":
    score["Extrovert"] += 1
elif q2 == "Mendengarkan orang lain":
    score["Introvert"] += 1

# Pertanyaan 3
q3 = st.radio("3. Dalam situasi sosial, saya cenderung:", ["Menjadi pusat perhatian", "Mengamati dari jauh"])
if q3 == "Menjadi pusat perhatian":
    score["Extrovert"] += 1
elif q3 == "Mengamati dari jauh":
    score["Introvert"] += 1
    
#tombol untuk melihat hasil
if st.button("🎯 Lihat Hasil"):
    if q1 and q2 and q3:
        hasil = max(score, key=score.get)
        st.success(f"✅ Kamu cocok jadi: **{hasil}**!")
        st.balloons()
        
        # Tampilkan gambar dan penjelasan SESUAI hasil
        if hasil == "Introvert":
            st.image("https://monknotion.com/wp-content/uploads/2021/03/pexels-gustavo-fring-4149079-min-1024x683.jpg", width=300)
            st.write("Introvert adalah orang yang lebih suka menghabiskan waktu sendiri atau dengan sedikit orang...")
        elif hasil == "Extrovert":
            st.image("https://content.api.news/v3/images/bin/d05c48d2aa920f3a08c21500a03679ca", width=300)
            st.write("Extrovert adalah orang yang suka berinteraksi dan bersosialisasi...")
    else:
        st.warning("⚠️ Harap jawab semua pertanyaan dulu.")
