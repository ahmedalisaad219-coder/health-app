import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="AI Health Master v7", page_icon="🏆", layout="wide")

# تصميم CSS احترافي (ألوان فاتحة، وضوح تام، وتصميم Glassmorphism)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); }
    .hero { background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%); padding: 3rem; border-radius: 2rem; color: white; text-align: center; margin-bottom: 2rem; box-shadow: 0 15px 30px rgba(59,130,246,0.2); }
    .glass-card { background: rgba(255, 255, 255, 0.9); border-radius: 1.5rem; padding: 2rem; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid white; margin-bottom: 1.5rem; }
    .metric-value { font-size: 2rem; font-weight: 800; color: #1e40af; }
    .tip-box { background: #eff6ff; border-right: 5px solid #3b82f6; padding: 1rem; border-radius: 0.8rem; margin: 0.8rem 0; color: #1e3a8a; font-weight: 500; }
    .stButton>button { background: #1e40af; color: white !important; border-radius: 50px; padding: 0.8rem 2rem; font-size: 1.2rem; width: 100%; transition: 0.4s; border: none; }
    .stButton>button:hover { background: #2563eb; transform: scale(1.02); box-shadow: 0 10px 20px rgba(37,99,235,0.3); }
    </style>
    """, unsafe_allow_html=True)

# 2. الموسوعة الصحية الشاملة (Database)
HEALTH_MATRIX = {
    "نحافة": {
        "تحليل": "جسمك يحتاج لبروتوكول بناء عالي السعرات. التركيز الحالي على تحسين الامتصاص وبناء الألياف العضلية.",
        "تغذية": ["زد السعرات بـ 500 نقطة يومياً", "ركز على الدهون الصحية (مكسرات، أفوكادو)", "تناول وجبات غنية بالكربوهيدرات المعقدة"],
        "تمارين": "تمارين المقاومة (أوزان ثقيلة) 3-4 أيام أسبوعياً مع فترات راحة طويلة.",
        "نفسية": "قلل مسببات التوتر لأنها ترفع معدل الحرق اللاإرادي.",
        "تفاعل": "snow"
    },
    "مثالي": {
        "تحليل": "أنت في منطقة الكفاءة الحيوية القصوى. هدفنا هو الحفاظ على هذا التوازن وتطوير اللياقة القلبية.",
        "تغذية": ["نظام 40-30-30 (كارب-بروتين-دهون)", "حافظ على شرب 3-4 لتر ماء", "ركز على الأطعمة الغنية بمضادات الأكسدة"],
        "تمارين": "نظام الهجين (Hybrid Training)؛ يوم قوة ويوم كارديو عالي الكثافة.",
        "نفسية": "مارس التأمل الصباحي للحفاظ على صفاء الذهن والتركيز.",
        "تفاعل": "balloons"
    },
    "زيادة وزن": {
        "تحليل": "نحتاج لإعادة ضبط حساسية الأنسولين وتنشيط محركات حرق الدهون في الجسم.",
        "تغذية": ["امنع السكريات المضافة تماماً", "ابدأ وجبتك بالألياف والخضروات", "اتبع نظام الصيام المتقطع (16:8)"],
        "تمارين": "تمارين HIIT ونشاط حركي لا يقل عن 10 آلاف خطوة يومياً.",
        "نفسية": "النوم قبل الساعة 11 مساءً ضروري جداً لتنظيم هرمونات الحرق.",
        "تفاعل": "celebrate"
    }
}

# 3. واجهة التحكم (The Dashboard)
st.markdown('<div class="hero"><h1>🛡️ AI Health Master: البروتوكول النهائي</h1><p>نظام التحليل المتطور 2026 - الإصدار السابع</p></div>', unsafe_allow_html=True)

with st.container():
    st.markdown("### 📋 أدخل بيانات البروتوكول:")
    c1, c2, c3 = st.columns(3)
    with c1:
        name = st.text_input("👤 كود المستخدم (الاسم):", placeholder="اكتب اسمك...")
        age = st.number_input("🎂 العمر:", 10, 100, 25)
    with c2:
        weight = st.number_input("⚖️ الوزن الحالي (كجم):", 30, 200, 75)
        height = st.number_input("📏 الطول الكلي (سم):", 100, 250, 175)
    with c3:
        goal = st.selectbox("🎯 المسار الاستراتيجي:", ["تنشيف وحرق دهون", "بناء عضلات وضخامة", "تحسين الصحة العامة"])
        water = st.slider("💧 أكواب الماء:", 0, 20, 8)

st.markdown("---")
col_habits1, col_habits2 = st.columns(2)
with col_habits1: sleep = st.select_slider("😴 دورة النوم (ساعة):", options=list(range(13)), value=8)
with col_habits2: phone = st.select_slider("📱 إجهاد الشاشة (ساعة):", options=list(range(17)), value=5)

# 4. محرك التحليل والذكاء التفاعلي
if st.button("🚀 تشغيل محرك التحليل الشامل"):
    if not name:
        st.error("⚠️ يرجى إدخال اسم المستخدم لتشغيل النظام.")
    else:
        with st.spinner('جاري معالجة البيانات واستخراج النتائج من الموسوعة...'):
            time.sleep(1)
            
        bmi = weight / ((height/100)**2)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        # استدعاء البيانات بأمان لتجنب الـ KeyError
        data = HEALTH_MATRIX.get(status)
        
        # التفاعلات الذكية
        if data["تفاعل"] == "snow": st.snow()
        elif data["تفاعل"] == "balloons": st.balloons()
        else: 
            st.balloons()
            st.toast("🔥 تم تحقيق أقصى كفاءة للتقرير!", icon="✅")

        st.markdown(f"## 📊 التقرير التحليلي لـ {name}")
        
        # صف النتائج بالأرقام الكبيرة
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown(f'<div class="glass-card"><h3>⚖️ BMI</h3><p class="metric-value">{bmi:.1f}</p><p>{status}</p></div>', unsafe_allow_html=True)
        with r2: 
            score = (water*5) + (sleep*8) - (phone*4)
            st.markdown(f'<div class="glass-card"><h3>⭐ سكور</h3><p class="metric-value">{max(0, score)}%</p><p>كفاءة العادات</p></div>', unsafe_allow_html=True)
        with r3:
            bmr = (10 * weight) + (6.25 * height) - (5 * age)
            st.markdown(f'<div class="glass-card"><h3>🔥 BMR</h3><p class="metric-value">{int(bmr)}</p><p>سعرة/يوم</p></div>', unsafe_allow_html=True)
        with r4:
            st.markdown(f'<div class="glass-card"><h3>🛡️ الحالة</h3><p class="metric-value">نشط</p><p>بروتوكول فعال</p></div>', unsafe_allow_html=True)

        st.divider()

        # الداتا الموسوعية والرسوم البيانية
        res_col1, res_col2 = st.columns([1.3, 1])
        
        with res_col1:
            st.markdown(f'<div class="glass-card"><h3>🔬 التحليل البيولوجي</h3><p>{data["تحليل"]}</p></div>', unsafe_allow_html=True)
            st.markdown("### 📈 مسار التوقع لـ 30 يوم القادمة")
            days = list(range(1, 31))
            if "تنشيف" in goal: trend = [weight - (d * 0.15) for d in days]
            elif "بناء" in goal: trend = [weight + (d * 0.1) for d in days]
            else: trend = [weight + np.sin(d)*0.4 for d in days]
            
            st.line_chart(pd.DataFrame({"الوزن": trend}, index=days))

        with res_col2:
            st.markdown("### 🥗 الخطة الغذائية المقترحة")
            for tip in data["تغذية"]:
                st.markdown(f'<div class="tip-box">✅ {tip}</div>', unsafe_allow_html=True)
            
            st.markdown("### 🏋️ هندسة النشاط البدني")
            st.success(data["تمارين"])
            st.info(f"🧘 **نصيحة ذهبية:** {data['نفسية']}")

        st.snow()
else:
    st.info("👋 مرحباً بك في مستشارك الصحي الذكي. املأ بياناتك واضغط على الزر لإصدار التقرير.")