import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="AI Health Master Pro", page_icon="⚡", layout="wide")

# تصميم CSS احترافي (ألوان مريحة وخطوط واضحة)
st.markdown("""
    <style>
    .stApp { background: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 40px; border-radius: 25px; color: white;
        text-align: center; margin-bottom: 30px;
    }
    .status-card {
        background: white; border-radius: 20px; padding: 25px;
        border-bottom: 5px solid #1e40af; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .badge {
        background: #fbbf24; color: #000; padding: 6px 16px;
        border-radius: 50px; font-weight: bold; font-size: 14px;
    }
    h1, h2, h3 { color: #1e293b; }
    </style>
    """, unsafe_allow_html=True)

# 2. الموسوعة الصحية العملاقة (بيانات تم تدقيقها برمجياً)
HEALTH_DB = {
    "نحافة": {
        "تحليل": "جسمك يحتاج لزيادة كثافة الأنسجة السليمة. التركيز الحالي هو بناء الكتلة العضلية.",
        "سوبر_فود": ["زبدة الفول السوداني", "الشوفان والموز", "سمك السلمون", "المكسرات النيئة"],
        "الرياضة": "تمارين القوة (رفع أثقال) 3 مرات أسبوعياً مع راحة كافية.",
        "تحدي": "تناول 5 وجبات غنية بالبروتين يومياً.",
        "وسام": "🎖️ صانع العضلات",
        "تفاعل": "snow"
    },
    "مثالي": {
        "تحليل": "أنت في منطقة التوازن الحيوي. هدفنا هو صقل اللياقة والحفاظ على حيوية الأعضاء.",
        "سوبر_فود": ["بذور الشيا", "الخضروات الورقية", "التوت الأزرق", "صدور الدجاج"],
        "الرياضة": "نظام هجين (كارديو + قوة) 4 مرات أسبوعياً.",
        "تحدي": "تحدي المرونة واليوجا الصباحية.",
        "وسام": "💎 البطل المتوازن",
        "تفاعل": "balloons"
    },
    "زيادة وزن": {
        "تحليل": "الجسم في حالة تخزين طاقة زائدة. سنعمل على تنشيط الحرق وإعادة توازن الهرمونات.",
        "سوبر_فود": ["البيض المسلوق", "السبانخ والبروكلي", "التونة", "الجوز"],
        "الرياضة": "تمارين HIIT ونشاط حركي يومي (10 آلاف خطوة).",
        "تحدي": "قطع السكريات المضافة والمشروبات الغازية.",
        "وسام": "🔥 محارب الدهون",
        "تفاعل": "celebrate"
    }
}

# 3. الواجهة الرئيسية
st.markdown('<div class="main-header"><h1>🚀 المستشار الصحي الذكي Pro</h1><p>نظام تحليل الأداء البشري المطور 2026</p></div>', unsafe_allow_html=True)

with st.container():
    st.markdown("### 🛠️ إعدادات الملف الشخصي")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input("👤 الاسم:", placeholder="اكتب اسمك...")
        age = st.number_input("🎂 العمر:", 10, 100, 25)
    with col2:
        weight = st.number_input("⚖️ الوزن (كجم):", 30.0, 200.0, 75.0)
        height = st.number_input("📏 الطول (سم):", 100, 250, 175)
    with col3:
        goal = st.selectbox("🎯 الهدف الاستراتيجي:", ["خسارة دهون", "بناء عضلات", "صحة عامة"])
        water = st.slider("💧 أكواب الماء:", 0, 20, 8)

st.markdown("---")
c_h1, c_h2 = st.columns(2)
with c_h1: sleep = st.select_slider("😴 ساعات النوم:", options=list(range(13)), value=8)
with c_h2: phone = st.select_slider("📱 استخدام الموبايل:", options=list(range(17)), value=5)

# 4. محرك التشغيل
if st.button("🏁 تفعيل التحليل العميق"):
    if not name:
        st.error("⚠️ يرجى إدخال اسمك أولاً!")
    else:
        with st.status("جاري معالجة البيانات...", expanded=False):
            time.sleep(1)
            
        bmi = weight / ((height/100)**2)
        status = "نحافة" if bmi < 18.5 else "مثالي" if bmi < 25 else "زيادة وزن"
        data = HEALTH_DB[status]
        
        # التفاعلات
        if data["تفاعل"] == "snow": st.snow()
        elif data["تفاعل"] == "balloons": st.balloons()
        else: 
            st.balloons()
            st.toast("تقريرك الاحترافي جاهز!", icon="✅")

        st.markdown(f"## 🏆 تقرير الأداء لـ {name}")
        
        # صف النتائج
        r1, r2, r3, r4 = st.columns(4)
        r1.markdown(f'<div class="status-card"><h3>⚖️ BMI</h3><h2 style="color:#1e40af">{bmi:.1f}</h2><p>{status}</p></div>', unsafe_allow_html=True)
        
        score = (water*5) + (sleep*8) - (phone*4)
        r2.markdown(f'<div class="status-card"><h3>⭐ سكور</h3><h2 style="color:#10b981">{max(0, int(score))}%</h2><p>نقاط الصحة</p></div>', unsafe_allow_html=True)
        r3.markdown(f'<div class="status-card"><h3>🛡️ الوسام</h3><span class="badge">{data["وسام"]}</span></div>', unsafe_allow_html=True)
        r4.markdown(f'<div class="status-card"><h3>🔥 الحرق</h3><h2 style="color:#f59e0b">{int(10*weight + 6.25*height)}</h2><p>BMR</p></div>', unsafe_allow_html=True)

        st.divider()

        res_col1, res_col2 = st.columns([1.5, 1])
        with res_col1:
            st.info(f"🔬 **التحليل العلمي:** {data['تحليل']}")
            st.markdown("### 📈 مسار الوزن المتوقع (30 يوم)")
            days = list(range(1, 31))
            val = -0.15 if "خسارة" in goal else 0.1 if "بناء" in goal else 0.02
            trend = [weight + (d * val) for d in days]
            st.line_chart(pd.DataFrame({"الوزن": trend}, index=days))

        with res_col2:
            st.markdown("### 🥗 قائمة الـ Super Food")
            for food in data["سوبر_فود"]:
                st.success(f"🔹 {food}")
            st.markdown(f"### 🏋️ الخطة الرياضية")
            st.warning(data["الرياضة"])
            st.error(f"🚩 **تحدي الأسبوع:** {data['تحدي']}")
else:
    st.info("👋 املأ بياناتك واضغط على الزر لبدء ليفل جديد من الصحة!")