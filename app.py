import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load('rf_pipeline.joblib')

st.title("Prediksi Performa Mahasiswa")

# === INPUT FORM ===
with st.form("prediction_form"):
    st.header("Data Mahasiswa")

    # 1. Gender (Dropdown)
    gender = st.selectbox("Gender", ["Laki-Laki", "Perempuan"])

    # 2. Umur & IPK
    col1, col2 = st.columns(2)
    with col1:
        umur = st.number_input("Umur", min_value=15, step=1, format="%d")
    with col2:
        ipk = st.number_input("IPK", min_value=0.0, max_value=4.0, step=0.01)

    # 3. Akademik (Input Integer 0, tanpa 0.00)
    col3, col4 = st.columns(2)
    with col3:
        jam_belajar = st.number_input("Jam Belajar per Hari", min_value=0, step=1, format="%d")
    with col4:
        tugas_besar = st.number_input("Jumlah Tugas Besar per Minggu", min_value=0, step=1, format="%d")

    # 4. Lifestyle (Input Integer 0, tanpa 0.00)
    jam_tidur = st.number_input("Jam Tidur per Hari", min_value=0, step=1, format="%d")

    # 5. Dropdowns Khusus
    col5, col6 = st.columns(2)
    with col5:
        # Pemasukan Keluarga (sesuai request: Pemasukan Olahraga saya asumsikan Pemasukan Keluarga)
        pemasukan = st.selectbox("Pemasukan Keluarga", ["Rendah", "Sedang", "Tinggi"])
    with col6:
        # Frekuensi Olahraga
        olahraga = st.selectbox("Frekuensi Olahraga", ["Jarang", "Kadang", "Sering"])

    # 6. Status Hubungan
    hubungan = st.selectbox("Status Hubungan", ["Dalam Hubungan", "Jomblo"])

    # 7. Jurusan (Input Manual atau Dropdown tambahan)
    # Note: Karena list jurusan tidak diberikan spesifik, saya buat text input. 
    # Jika ingin dropdown, ganti st.text_input dengan st.selectbox(['Informatika', 'Sistem Informasi', ...])
    jurusan = st.text_input("Jurusan/Program Studi", "Informatika")

    # Tombol Submit
    submit_btn = st.form_submit_button("Prediksi")

if submit_btn:
    # Buat DataFrame dari input
    data_input = {
        'Jam Belajar per Hari': [jam_belajar],
        'Jam Tidur per Hari': [jam_tidur],
        'IPK': [ipk],
        'Jumlah Tugas Besar per Minggu': [tugas_besar],
        'Umur': [umur],
        'Gender': [gender],
        'Frekuensi Olahraga': [olahraga],
        'Status Hubungan': [hubungan],
        'Jurusan/Program Studi': [jurusan],
        'Pemasukan Keluarga': [pemasukan]
    }
    
    df_new = pd.DataFrame(data_input)

    try:
        # Prediksi
        prediction = model.predict(df_new)
        st.success(f"Hasil Prediksi: **{prediction[0]}**")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")