import streamlit as st
import pandas as pd
import numpy as np
import random

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="Ultra Health AI 2026", page_icon="🧬", layout="wide")

# تصميم CSS لليفل المحترفين (Dark Luxury Theme)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid #334155;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    .data-card {
        background: rgba(255, 255, 255, 0.05);
        border-right: 5px solid #10b981;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    h1, h2, h3 { color: #38bdf8 !important; }
    .stButton>button {
        background: linear-gradient(90deg, #0ea5e9 0%, #22c55e 100%);
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        height: 3em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة البيانات العملاقة (The Health Matrix)
HEALTH_MATRIX = {
    "نحافة": {
        "تحليل_عميق": "جسمك في حالة حرق مستمر (Hyper-metabolism). نحتاج لتحويل التركيز من حرق السعرات إلى بناء الألياف العضلية.",
        "خطة_التغذية": [
            "زيادة السعرات بمقدار 500 سعرة فوق المعدل الطبيعي.",
            "التركيز على الكربوهيدرات المعقدة (بطاطس، شوفان، أرز بني).",
            "إضافة حصة بروتين (30 جرام) في كل وجبة.",
            "استخدام الزيوت الصحية مثل زيت الزيتون وزبدة الفول السوداني."
        ],
        "البرنامج_الرياضي": "تدريبات القوة الثقيلة (Heavy Lifting) 3 مرات أسبوعياً بمدات راحة طويلة بين المجموعات.",
        "الصحة_النفسية": "تجنب التوتر الزائد لأنه يرفع الكورتيزول الذي يحرق العضلات."
    },
    "مثالي": {
        "تحليل_عميق": "أنت في منطقة التوازن الذهبي. هدفنا الآن هو (Body Recomposition) أي تحويل الدهون القليلة المتبقية إلى عضلات صافية.",
        "خطة_التغذية": [
            "تثبيت السعرات الحرارية مع زيادة جودة النوعية.",
            "الاعتماد على نظام 40% بروتين، 40% كربوهيدرات، 20% دهون.",
            "تناول وجبة غنية بالبروتين خلال 30 دقيقة بعد التمرين.",
            "استخدام الصيام المتقطع البسيط (12 ساعة) للحفاظ على نضارة البشرة."
        ],
        "البرنامج_الرياضي": "نظام الهجين (Hybrid): يومين قوة، يومين كارديو، ويوم مرونة (يوغا أو إطالات).",
        "الصحة_النفسية": "ركز على التأمل لتحسين الاتصال بين العقل والعضلات."
    },
    "زيادة وزن": {
        "تحليل_عميق": "الجسم يقوم بتخزين الطاقة الزائدة. نحتاج لإعادة ضبط حساسية الأنسولين وتنشيط محركات الحرق الطبيعية.",
        "خطة_التغذية": [
            "تقليل الكربوهيدرات إلى أقل من 100 جرام يومياً.",
            "البدء بنظام الصيام المتقطع (16/8).",
            "تناول الألياف (سلطات) كأول جزء في كل وجبة لتقليل امتصاص الدهون.",
            "شرب القهوة الخضراء أو الشاي الأخضر لزيادة معدل الأيض."
        ],
        "البرنامج_الرياضي": "تمارين عالية الكثافة (HIIT) لرفع نبض القلب، مع مشي يومي لا يقل عن 45 دقيقة.",
        "الصحة_النفسية": "النوم الكافي ضروري جداً؛ نقص النوم يمنع الجسم من حرق الدهون ليلاً."
    }
}

# 3. واجهة التحكم
st.markdown("<h1 style='text-align: center;'>🌌 Ultra Health AI Explorer</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #94a3b8;'>نظام الذكاء الاصطناعي المتكامل لتحليل وتطوير الأداء البشري</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("### 🛠️ مدخلات النظام المتقدمة")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        name = st.text_input("👤 كود المستخدم (الاسم):")
        age = st.number_input("🎂 العمر:", 10, 100, 25)
    with c2:
        weight = st.number_input("⚖️ الوزن الحالي:", 30, 200, 75)
        height = st.number_input("📏 الطول الكلي:", 100, 250, 175)
    with c3:
        water = st.number_input("💧 استهلاك المياه:", 0, 20, 8)
        sleep = st.slider("😴 دورة النوم (ساعة):", 0, 12, 7)
    with c4:
        phone = st.slider("📱 إجهاد الشاشة:", 0, 16, 5)
        goal = st.selectbox("🎯 المسار المطلوب:", ["حرق دهون", "بناء كتلة", "تحسين شامل"])

st.divider()

# 4. محرك التحليل والنتائج
if st.button("🏁 تشغيل محرك التحليل العميق"):
    if not name:
        st.warning("يرجى إدخال اسم المستخدم لتفعيل البروتوكول!")
    else:
        bmi = weight / ((height/100)**2)
        
        # تحديد الحالة بدقة
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        data = HEALTH_MATRIX[status]
        st.balloons()

        # عرض النتائج في لوحة التحكم
        st.markdown(f"## 📊 تقرير الأداء: {name}")
        
        # صف العدادات المتقدمة
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown(f'<div class="metric-card"><h3>⚖️ BMI</h3><h2>{bmi:.1f}</h2><p>{status}</p></div>', unsafe_allow_html=True)
        with r2: 
            h_score = (water*5) + (sleep*10) - (phone*5)
            st.markdown(f'<div class="metric-card"><h3>📈 Health Score</h3><h2>{h_score}%</h2><p>كفاءة العادات</p></div>', unsafe_allow_html=True)
        with r3:
            bmr = (10 * weight) + (6.25 * height) - (5 * age)
            st.markdown(f'<div class="metric-card"><h3>🔥 BMR</h3><h2>{int(bmr)}</h2><p>حرق السكون</p></div>', unsafe_allow_html=True)
        with r4:
            st.markdown(f'<div class="metric-card"><h3>🛡️ Status</h3><h2>Active</h2><p>جاهز للتطوير</p></div>', unsafe_allow_html=True)

        st.divider()

        # عرض الداتا الموسوعية
        col_data1, col_data2 = st.columns(2)
        with col_data1:
            st.markdown("### 🔬 التحليل البيولوجي")
            st.markdown(f'<div class="data-card">{data["تحليل_عميق"]}</div>', unsafe_allow_html=True)
            
            st.markdown("### 🥗 البروتوكول الغذائي")
            for tip in data["خطة_التغذية"]:
                st.write(f"🔹 {tip}")
        
        with col_data2:
            st.markdown("### 🏋️ هندسة النشاط البدني")
            st.info(data["البرنامج_الرياضي"])
            
            st.markdown("### 📈 مسار التوقع المستقبلي")
            days = list(range(1, 31))
            if "حرق" in goal: trend = [weight - (d * 0.12) for d in days]
            elif "بناء" in goal: trend = [weight + (d * 0.08) for d in days]
            else: trend = [weight + np.sin(d)*0.5 for d in days]
            
            st.line_chart(pd.DataFrame({"الوزن": trend}, index=days))

        st.divider()
        st.success(f"🧘 **توصية الصحة النفسية:** {data['الصحة_النفسية']}")
        st.snow()