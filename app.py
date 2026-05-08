import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات متقدمة
st.set_page_config(page_title="AI Health Coach", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f4f8; }
    .stMetric { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .css-145vsf3 { border-radius: 20px; }
    .card-pro { background: white; padding: 25px; border-radius: 20px; border-left: 8px solid #007bff; box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر
st.markdown("# 🧬 نظام الذكاء الصحي المتكامل")
st.write("---")

# 3. المدخلات الذكية
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3843/3843184.png", width=100)
    st.header("مركز التحكم")
    name = st.text_input("👤 اسم البطل:", "أحمد")
    age = st.number_input("🎂 العمر:", 10, 100, 20)
    gender = st.selectbox("🧬 الجنس:", ["ذكر", "أنثى"])
    weight = st.number_input("⚖️ الوزن الحالي (كجم):", 30, 200, 75)
    height = st.number_input("📏 الطول (سم):", 100, 250, 170)
    goal = st.selectbox("🎯 هدفك:", ["خسارة وزن", "بناء عضلات", "تحسين لياقة"])

# 4. لوحة البيانات
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("### 📱 التكنولوجيا")
    phone = st.slider("ساعات الموبايل:", 0, 16, 5)
    water = st.number_input("💧 أكواب الماء:", 0, 20, 8)

with col2:
    st.markdown("### 😴 الراحة")
    sleep = st.slider("ساعات النوم:", 0, 12, 8)
    stress = st.select_slider("🤯 مستوى الإرهاق:", options=["منخفض", "متوسط", "مرتفع"])

with col3:
    st.markdown("### 🏃 النشاط")
    workout = st.number_input("أيام الرياضة أسبوعياً:", 0, 7, 3)

st.write("---")

if st.button("🌟 تحليل البيانات وإنشاء الخطة"):
    bmi = weight / ((height/100)**2)
    
    # حساب السعرات
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "ذكر" else -161)
    
    st.balloons()
    
    # عرض النتائج بشكل مودرن
    st.subheader(f"📊 لوحة تحكم الصحة لـ {name}")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("كتلة الجسم", f"{bmi:.1f}", "مثالي" if 18.5 < bmi < 25 else "انتبه")
    m2.metric("السعرات الأساسية", f"{int(bmr)}")
    m3.metric("هدف المياه", "8 أكواب", f"{water-8}")
    m4.metric("ساعات الموبايل", f"{phone} س", "-2" if phone > 4 else "أحسنت")

    # 5. ميزة التنبؤ بالمستقبل (الرسم البياني)
    st.write("### 📈 التوقعات المستقبلية (خلال 30 يوم)")
    
    days = np.array(range(1, 31))
    # معادلة بسيطة للتوقع بناءً على الهدف
    if goal == "خسارة وزن":
        predicted_weight = weight - (days * 0.1)  # يتوقع خسارة 3 كيلو في الشهر
    elif goal == "بناء عضلات":
        predicted_weight = weight + (days * 0.05) # يتوقع زيادة عضلية بسيطة
    else:
        predicted_weight = [weight] * 30
        
    chart_data = pd.DataFrame({
        'اليوم': days,
        'الوزن المتوقع': predicted_weight
    }).set_index('اليوم')
    
    st.line_chart(chart_data)
    st.caption("ملاحظة: هذه التوقعات تعتمد على التزامك بالخطة الغذائية والرياضية.")

    # 6. التوصيات النهائية
    st.markdown(f"""
    <div class="card-pro">
        <h3>💡 نصيحة الـ AI المخصصة:</h3>
        يا {name}، بناءً على بياناتك، أنت تحتاج لشرب {max(8, water)} أكواب ماء لتعويض المجهود. 
        بما أن هدفك هو <b>{goal}</b>، ننصحك بتقليل استخدام الموبايل قبل النوم بـ 60 دقيقة 
        لرفع هرمون النمو الطبيعي في جسمك.
    </div>
    """, unsafe_allow_html=True)
    st.snow()