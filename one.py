import joblib
import streamlit as st
import pandas as pd

# Streamlit ilovasining sarlavhasi
st.title("Avtomobil Yoqilg'i Sarfini Bashorat Qilish")

# Foydalanuvchi uchun kirish maydonlari
brand = st.selectbox("Brendni tanlang: ", ['Toyota', 'Lamborghini', 'BMW', 'Mercedes'])
price = st.number_input("Avtomobil ishlab chiqarilgan yili: ", min_value=0)
mileage = st.number_input("Yurgan masofani kiriting (km): ", min_value=0)
engine_size = st.number_input("Dvigatel hajmini kiriting (L): ", min_value=0.0)
tax = st.number_input("100 tezlikka necha sekuntda chiqishi: ", min_value=0)

# Modelni yuklash
try:
    model = joblib.load('/home/shohruh/Tolibjon/yoqilgi.pkl')
except FileNotFoundError:
    st.error("Model fayli topilmadi. Iltimos, to'g'ri yo'lni kiriting.")
    st.stop()

# Brendga qarab farqni o'rnatish
brand_mpgeffects = {
    'Toyota': 1,
    'Lamborghini': 2,
    'BMW': 1.5,
    'Mercedes': 1.2
}

# Bashorat qilishni amalga oshirish
if st.button("Yoqilg'i sarfini ko'rish uchun bosing!"):
    try:
        # Kiritilgan ma'lumotlarni DataFrame shaklida tayyorlash
        input_data = pd.DataFrame({
            'price': [price],
            'mileage': [mileage],
            'engineSize': [engine_size],
            'tax': [tax]
        })

        # Bashorat qilish
        prediction = model.predict(input_data)

        # Brendga qarab natijani sozlash
        mpg_prediction = prediction[0] - brand_mpgeffects.get(brand, 0)

        st.success(f"{brand} brendi uchun avtomobilning yoqilg'i sarfi: {round(mpg_prediction, 2)} MPG")
    except Exception as e:
        st.error(f"Bashorat qilishda xatolik yuz berd

i: {e}")
