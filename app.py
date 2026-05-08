import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="AI Health Expert 2026", page_icon="🧬", layout="wide")

# تصميم CSS (ألوان مريحة، كلام واضح جداً، وبطاقات عصرية)
st.markdown("""
    <style>
    .stApp { background: #fdfdfd; }
    .hero-section { background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); padding: 40px; border-radius: 20px; color: white; text-align: center; margin-bottom: 30px; }
    .glass-card { background: white; border-radius: 20px; padding: 25px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-left: 8px solid #3b82f6; margin-bottom: 20px; }
    .tip-box { background: #f0fdf4; border: 1px solid #bbf7d0; padding: 15px; border-radius: 12px; margin: 10px 0; color: #166534; }
    h1, h2, h3 { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stButton>button { background: #1e3a8a; color: white !important; border-radius: 50px; height: 50px; font-size: 18px; width: 100%; transition: 0.3s; }
    .stButton>button:hover { background: #3b82f6; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# 2. الموسوعة الضخمة (البيانات الشاملة)
DATABASE = {
    "نحافة": {
        "التحليل": "جسمك يحتاج لزيادة كثافة الأنسجة. أنت في مرحلة بناء القاعدة.",
        "التغذية": ["زد السعرات بنسبة 20% من مصادر بروتين صافية.", "تناول المكسرات وزيت الزيتون والأفوكادو يومياً.", "اجعل الوجبات 5 وجبات صغيرة لسهولة الهضم."],
        "التمارين": "تمارين القوة (رفع أثقال) بمدات راحة طويلة (90 ثانية) بين المجموعات.",
        "الصحة_النفسية": "مارس تمارين التنفس لتقليل التوتر الذي قد يحرق سعراتك بسرعة.",
        "التفاعل": "snow"
    },
    "مثالي": {
        "التحليل": "أنت في القمة! هدفنا الآن هو صقل التفاصيل وتحسين اللياقة القلبية.",
        "التغذية": ["حافظ على توازن الماكروز (بروتين 30%، كارب 40%، دهون 30%).", "استخدم الصيام المتقطع للحفاظ على حساسية الأنسولين.", "ركز على مضادات الأكسدة (التوت، الشاي الأخضر)."],
        "التمارين": "تمارين الـ Crossfit أو نظام الهجين (قوة + كارديو) 4 أيام أسبوعياً.",
        "الصحة_النفسية": "التأمل الصباحي لمدة 10 دقائق سيزيد من تركيزك في التمرين.",
        "التفاعل": "balloons"
    },
    "زيادة وزن": {
        "التحليل": "الجسم في حالة تخزين. سنقوم الآن بتشغيل محركات الحرق الطبيعية.",
        "التغذية": ["امنع السكريات المضافة والمشروبات الغازية تماماً.", "ابدأ وجبتك دائماً بالخضروات الورقية لتقليل الامتصاص.", "استبدل الأرز الأبيض بالبطاطس المسلوقة أو الكينوا."],
        "التمارين": "تمارين HIIT (عالية الكثافة) مع مشي سريع 10 آلاف خطوة يومياً.",
        "الصحة_النفسية": "النوم الكافي هو مفتاح حرق الدهون؛ نقص النوم يرفع هرمون الجوع.",
        "التفاعل": "celebrate"
    }
}

# 3. الهيكل الرئيسي للموقع
st.markdown('<div class="hero-section"><h1>🛡️ نظام المستشار الصحي الذكي المتكامل</h1><p>إصدار 2026 - تكنولوجيا تحليل الأداء البشري</p></div>', unsafe_allow_html=True)

# المدخلات المنظمة
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 👤 الملف الشخصي")
        name = st.text_input("اسم المستخدم:")
        age = st.number_input("العمر:", 10, 100, 25)
        gender = st.radio("النوع:", ["ذكر", "أنثى"], horizontal=True)
    with col2:
        st.markdown("### 📊 القياسات الحيوية")
        weight = st.number_input("الوزن الحالي (كجم):", 30, 200, 75)
        height = st.number_input("الطول الكلي (سم):", 100, 250, 175)
        goal = st.selectbox("🎯 المسار المختار:", ["تنشيف وحرق", "بناء وضخامة", "صحة واستدامة"])

st.markdown("---")
st.markdown("### 🌙 عاداتك خلال الـ 24 ساعة الماضية")
c1, c2, c3 = st.columns(3)
with c1: water = st.select_slider("💧 أكواب الماء:", options=list(range(21)), value=8)
with c2: sleep = st.select_slider("😴 ساعات النوم:", options=list(range(13)), value=7)
with c3: phone = st.select_slider("📱 استخدام الموبايل:", options=list(range(17)), value=5)

# 4. محرك التحليل الذكي
if st.button("🏁 بدء بروتوكول التحليل العميق"):
    if not name:
        st.error("⚠️ يرجى إدخال اسم المستخدم لتشغيل المحرك.")
    else:
        with st.spinner('جاري تحليل البيانات ومطابقتها مع الموسوعة...'):
            time.sleep(1.5) # محاكاة تفكير الذكاء الاصطناعي
            
        bmi = weight / ((height/100)**2)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        data = DATABASE[status]
        
        # التفاعلات المتغيرة (مش بالونات بس)
        if data["التفاعل"] == "snow": st.snow()
        elif data["التفاعل"] == "balloons": st.balloons()
        else: 
            st.balloons()
            st.toast("تهانينا! تقريرك جاهز الآن", icon="🔥")

        st.markdown(f"## 📊 التقرير الصحي الشامل لـ {name}")
        
        # العدادات التفاعلية
        r1, r2, r3, r4 = st.columns(4)
        r1.metric("كتلة الجسم", f"{bmi:.1f}", status)
        r2.metric("معدل الأيض", f"{int(10*weight+6.25*height-5*age)}", "سعرة")
        
        health_score = (water*5) + (sleep*8) - (phone*4)
        r3.metric("سكور العادات", f"{health_score}%", "جيد" if health_score > 60 else "ضعيف")
        r4.metric("الحالة", status)

        st.divider()

        # عرض الداتا الموسوعية بشكل شيك
        col_res1, col_res2 = st.columns([1.2, 1])
        
        with col_res1:
            st.markdown(f'<div class="glass-card"><h3>🔬 التحليل البيولوجي</h3><p>{data["تحليل"]}</p></div>', unsafe_allow_html=True)
            st.markdown("### 📈 مسار التوقع المستقبلي")
            days = list(range(1, 31))
            if "تنشيف" in goal: trend = [weight - (d * 0.15) for d in days]
            elif "بناء" in goal: trend = [weight + (d * 0.1) for d in days]
            else: trend = [weight + np.sin(d)*0.4 for d in days]
            st.line_chart(pd.DataFrame({"الوزن": trend}, index=days))

        with col_res2:
            st.markdown("### 🥗 الخطة الغذائية الموسوعية")
            for item in data["التغذية"]:
                st.markdown(f'<div class="tip-box">✅ {item}</div>', unsafe_allow_html=True)
            
            st.markdown("### 🏋️ التوصية الرياضية")
            st.success(data["الرياضة"])
            st.info(f"🧘 **نصيحة نفسية:** {data['الصحة_النفسية']}")

        st.divider()
        st.write(f"🎉 تم استخراج هذا التقرير بناءً على هدفك: **{goal}**. حافظ على الاستمرار!")
else:
    st.info("👋 مرحباً بك في نظامك الصحي. أدخل بياناتك بالأعلى واضغط على الزر لبدء الرحلة.")