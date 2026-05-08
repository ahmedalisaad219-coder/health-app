import streamlit as st
import pandas as pd
import numpy as np
import random

# 1. إعدادات متقدمة جداً
st.set_page_config(page_title="AI Health Coach v3.0", page_icon="🚀", layout="wide")

# تصميم احترافي للألوان والبطاقات
st.markdown("""
    <style>
    .main { background: linear-gradient(to bottom, #e8f5e9, #ffffff); }
    .score-box { background: white; padding: 25px; border-radius: 25px; text-align: center; border: 2px solid #4CAF50; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    .stProgress > div > div > div > div { background-color: #4CAF50; }
    .tip-box { background-color: #fff3e0; border-right: 10px solid #ff9800; padding: 20px; border-radius: 10px; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# الهيدر المطور
st.markdown("<h1 style='text-align: center;'>🌐 نظام المستشار الصحي الذكي 3.0</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>الذكاء الاصطناعي في خدمة صحتك</p>", unsafe_allow_html=True)

# 2. المدخلات الجانبية
with st.sidebar:
    st.header("👤 ملف البطل")
    name = st.text_input("اسمك:", "أحمد")
    goal = st.radio("هدفك:", ["تنشيف", "تضخيم", "لياقة عامة"])
    st.divider()
    weight = st.number_input("الوزن (كجم):", 30, 200, 75)
    height = st.number_input("الطول (سم):", 100, 250, 170)
    age = st.number_input("العمر:", 10, 100, 20)

# 3. لوحة التحكم اليومية
st.subheader("🛠️ نشاطك خلال الـ 24 ساعة الماضية")
c1, c2, c3, c4 = st.columns(4)
with c1: water = st.number_input("💧 أكواب الماء:", 0, 20, 8)
with c2: sleep = st.slider("😴 ساعات النوم:", 0, 12, 8)
with c3: phone = st.slider("📱 ساعات الموبايل:", 0, 16, 5)
with c4: steps = st.number_input("🚶 عدد الخطوات:", 0, 30000, 5000)

st.divider()

if st.button("🏁 تحليل النمط الصحي الشامل"):
    # حسابات ذكية
    bmi = weight / ((height/100)**2)
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    
    # حساب سكور جودة الحياة (Lifestyle Score)
    score = 0
    if 7 <= sleep <= 9: score += 25
    if water >= 8: score += 25
    if steps >= 7000: score += 25
    if phone <= 4: score += 25
    
    st.balloons()

    # 4. عرض النتائج (الأجزاء المتطورة)
    col_res1, col_res2 = st.columns([1, 2])

    with col_res1:
        st.markdown('<div class="score-box">', unsafe_allow_html=True)
        st.write("### تقييم يومك")
        st.title(f"{score}%")
        st.progress(score / 100)
        st.write("درجة التزامك بالعادات الصحية")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_res2:
        st.write(f"### 📋 تحليل البيانات يا {name}")
        m1, m2 = st.columns(2)
        m1.metric("مؤشر الكتلة", f"{bmi:.1f}")
        m2.metric("حرق جسمك الطبيعي", f"{int(bmr)} سعرة")
        
    st.divider()

    # 5. قسم الوجبات الذكي
    st.subheader("🥗 مقترحات غذائية لهدفك")
    meals = {
        "تنشيف": ["سلطة تونة بالخضار", "صدر دجاج مشوي مع 3 ملاعق أرز", "أومليت بياض بيض"],
        "تضخيم": ["مكرونة وايت صوص بالدجاج", "شوفان بالحليب والمكسرات", "لحم مشوي مع بطاطس مهروسة"],
        "لياقة عامة": ["سمك مشوي وسلطة خضراء", "عدس مع خبز أسمر", "زبادي يوناني بالفواكه"]
    }
    st.info(f"💡 وجبة مقترحة لك الآن: **{random.choice(meals[goal])}**")

    # 6. الرسم البياني للتوقعات
    st.write("### 📈 توقعات الوزن لشهر مايو 2026")
    days = list(range(1, 31))
    trend = [weight - (d * 0.1) if goal == "تنشيف" else weight + (d * 0.05) for d in days]
    st.line_chart(pd.DataFrame({"الوزن المتوقع": trend}, index=days))

    # 7. التحدي اليومي
    st.markdown('<div class="tip-box">', unsafe_allow_html=True)
    st.write("### 🎯 تحدي الـ 24 ساعة القادمة:")
    challenges = [
        "امشِ 15 دقيقة بعد الغداء مباشرة.",
        "امنع السكر تماماً في مشروباتك النهاردة.",
        "اشرب كوبين مية قبل كل وجبة.",
        "اقفل الموبايل قبل النوم بساعة كاملة."
    ]
    st.write(f"👉 **{random.choice(challenges)}**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.snow()