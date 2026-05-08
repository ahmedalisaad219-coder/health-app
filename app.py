import streamlit as st
import pandas as pd
import numpy as np
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="المستشار الصحي الخارق", page_icon="🧪", layout="wide")

# تصميم CSS لضمان الألوان والبطاقات
st.markdown("""
    <style>
    .main { background-color: #f0f4f8; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; margin-bottom: 15px; border-top: 5px solid #4CAF50; }
    h1 { color: #2E7D32; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# قاعدة بيانات الموسوعة
HEALTH_KNOWLEDGE = {
    "نحافة": {
        "نصيحة": "تحتاج لزيادة السعرات من مصادر صحية وبروتين عالي.",
        "وجبات": ["زبادي بالمكسرات والعسل", "شوفان بالحليب كامل الدسم", "مكرونة بالدجاج"],
        "تمارين": "رفع أثقال خفيفة لزيادة الكتلة العضلية."
    },
    "مثالي": {
        "نصيحة": "أنت في حالة ممتازة، ركز على الاستمرارية.",
        "وجبات": ["سمك مشوي وسلطة", "صدور دجاج وأرز بني", "فاكهة وزبادي"],
        "تمارين": "مزيج بين الكارديو وتمارين القوة."
    },
    "زيادة وزن": {
        "نصيحة": "نحتاج لتقليل النشويات وزيادة الحركة لحرق الدهون.",
        "وجبات": ["سلطة تونة", "شوربة خضار ودجاج", "بيض مسلوق وخضروات"],
        "تمارين": "مشي سريع أو جري لمدة 30-45 دقيقة يومياً."
    }
}

st.markdown("# 🛡️ المستشار الصحي الموسوعي الشامل")
st.success("💡 **'الصحة استثمار وليست مصاريف، استثمر في نفسك اليوم!'**")

# 2. المدخلات (كل اللي طلبته بالأيقونات)
st.divider()
col_in1, col_in2 = st.columns(2)
with col_in1:
    name = st.text_input("👤 الاسم الكريم:")
    age = st.number_input("🎂 العمر:", 10, 100, 20)
    height = st.number_input("📏 الطول (سم):", 100, 250, 170)
    gender = st.radio("🧬 النوع:", ["ذكر", "أنثى"], horizontal=True)

with col_in2:
    weight = st.number_input("⚖️ الوزن (كجم):", 30, 200, 75)
    water = st.number_input("💧 أكواب الماء يومياً:", 0, 20, 8)
    sleep = st.slider("😴 ساعات النوم:", 0, 12, 8)
    phone = st.slider("📱 ساعات الموبايل:", 0, 16, 5)

goal = st.selectbox("🎯 هدفك الأساسي:", ["تنشيف", "تضخيم", "تحسين صحة"])

# 3. زر التحليل
if st.button("🚀 إصدار التقرير الخارق"):
    bmi = weight / ((height/100)**2)
    # حساب السعرات (BMR)
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "ذكر" else -161)
    
    # تحديد الحالة للموسوعة
    if bmi < 18.5: status = "نحافة"
    elif bmi < 25: status = "مثالي"
    else: status = "زيادة وزن"
    
    data = HEALTH_KNOWLEDGE[status]
    st.balloons()
    
    # عرض النتائج في بطاقات (Cards)
    st.markdown(f"### 📋 نتائج البطل {name}")
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.markdown(f'<div class="card"><h3>⚖️</h3><p>كتلة الجسم</p><h4>{bmi:.1f}</h4><p>{status}</p></div>', unsafe_allow_html=True)
    with r2:
        st.markdown(f'<div class="card"><h3>🔥</h3><p>حرق السعرات</p><h4>{int(bmr)}</h4><p>سعرة/يوم</p></div>', unsafe_allow_html=True)
    with r3:
        st.markdown(f'<div class="card"><h3>😴</h3><p>النوم</p><h4>{"كافٍ" if sleep >= 7 else "قليل"}</h4></div>', unsafe_allow_html=True)
    with r4:
        st.markdown(f'<div class="card"><h3>📱</h3><p>الموبايل</p><h4>{"آمن" if phone <= 4 else "مرهق"}</h4></div>', unsafe_allow_html=True)

    # 4. الموسوعة (الأكل والتمارين)
    st.divider()
    st.subheader("📖 من الموسوعة الصحية المخصصة لك:")
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        st.info(f"🥗 **قائمة الطعام المقترحة:**\n\n" + "\n".join([f"- {m}" for m in data["وجبات"]]))
    with c_m2:
        st.warning(f"🏋️ **خطة النشاط البدني:**\n\n{data['تمارين']}")

    # 5. الرسم البياني (توقعات المستقبل)
    st.write("### 📈 توقعات تغير الوزن خلال 30 يوم")
    days = np.array(range(1, 31))
    trend = weight - (days * 0.1) if goal == "تنشيف" else weight + (days * 0.05) if goal == "تضخيم" else [weight]*30
    st.line_chart(pd.DataFrame({"الوزن": trend}, index=days))

    # 6. التحدي اليومي ونصيحة الموسوعة (تم تصحيح الخطأ هنا)
    st.divider()
    extra_tips = ["شرب الماء الدافئ صباحاً يحسن الهضم.", "المشي 10 دقائق بعد الأكل يقلل السكر.", "النوم المبكر يبني العضلات."]
    st.success(f"💡 **نصيحة الموسوعة العشوائية:** {random.choice(extra_tips)}")
    
    challenges = ["امشِ 20 دقيقة الآن", "امنع السكر اليوم", "اشرب لتر ماء إضافي"]
    st.error(f"🎯 **تحدي الـ 24 ساعة:** {random.choice(challenges)}")
    
    st.snow()