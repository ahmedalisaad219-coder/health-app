import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. إعدادات المنصة
st.set_page_config(page_title="مساعد ابن البلد الذكي", page_icon="💰", layout="wide")

# 2. التنسيق البصري (High Visibility & Clean Design)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    .header-box {
        background: #065f46; padding: 25px; border-radius: 15px;
        text-align: center; color: white; margin-bottom: 20px;
    }
    .budget-card {
        background: #f0fdf4; padding: 20px; border-radius: 15px;
        border: 2px solid #16a34a; margin-bottom: 20px;
    }
    .routine-card {
        background: #fff7ed; padding: 20px; border-radius: 15px;
        border: 2px solid #ea580c; margin-bottom: 20px;
    }
    .info-section {
        background: #f8fafc; padding: 20px; border-radius: 12px;
        border-right: 8px solid #065f46; margin-bottom: 15px;
    }
    h1, h2, h3 { font-weight: 900 !important; color: #064e3b; }
    p, b, li { font-size: 19px !important; line-height: 1.7; }
    .stButton>button { background: #065f46; color: white !important; font-weight: bold; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# 3. داتا الميزانية (أكلات اقتصادية)
BUDGET_MEALS = {
    "ميزانية بسيطة (أقل من 50 جنيه)": "كشري أصفر ببيض مسلوق، أو بصارة وعيش بلدي، أو فول بالزيت الحار وجبنة قريش.",
    "ميزانية متوسطة (50 - 150 جنيه)": "كبد وقوانص بالبصل وفلفل ألوان، أو مسقعة باللحمة المفرومة، أو سمك بلطي مشوي ورز صيادية.",
    "ميزانية مفتوحة (أكثر من 150 جنيه)": "صدور دجاج مشوية وخضار سوتيه، أو طاجن عكاوي بالفريك، أو لحمة مسلوقة وشوربة دافئة."
}

# 4. الروتين الصباحي حسب الحالة
ROUTINE_DATA = {
    "نحافة": "ابدأ يومك بـ 3 تمرات ومعلقة عسل أسود لتنشيط الدم وفتح الشهية.",
    "مثالي": "كوب ماء دافئ بقطرات ليمون ومعلقة عسل نحل صغيرة للمناعة والنشاط.",
    "زيادة وزن": "كوب ماء كبير مع معلقة خل تفاح صغيرة (لو معدتك سليمة) لرفع معدل الحرق."
}

# 5. واجهة المستخدم
st.markdown('<div class="header-box"><h1>🛡️ مساعد ابن البلد الذكي</h1><p>صحتك على قد جيبك.. وروتينك سر قوتك</p></div>', unsafe_allow_html=True)

# الجزء الأول: الميزانية والروتين (أول ما المستخدم يفتح)
col_top1, col_top2 = st.columns(2)

with col_top1:
    st.markdown('<div class="routine-card"><h3>☀️ روتينك الصباحي النهاردة</h3></div>', unsafe_allow_html=True)
    routine_status = st.selectbox("حدد حالتك للروتين:", ["زيادة وزن", "نحافة", "مثالي"])
    st.info(f"✨ **نصيحة الصباح:** {ROUTINE_DATA[routine_status]}")

with col_top2:
    st.markdown('<div class="budget-card"><h3>💰 رادار الميزانية (تاكل إيه بكام؟)</h3></div>', unsafe_allow_html=True)
    user_budget = st.selectbox("ميزانيتك النهاردة كام؟", list(BUDGET_MEALS.keys()))
    st.success(f"🥘 **اقتراح الأكلة:** {BUDGET_MEALS[user_budget]}")

st.write("---")

# الجزء الثاني: الموسوعة والمتابعة
with st.sidebar:
    st.header("👤 ملفك الشخصي")
    name = st.text_input("الاسم:")
    weight = st.number_input("الوزن (كجم):", 30, 200, 75)
    height = st.number_input("الطول (سم):", 100, 250, 175)
    
    st.write("---")
    # عداد المية (ثبتناه في الجنب عشان ميزحمش الصفحة)
    if 'water' not in st.session_state: st.session_state.water = 0
    st.write(f"💧 شربت {st.session_state.water} كوبايات مية")
    if st.button("➕ شربت كوباية"): st.session_state.water += 1

if st.button("🏁 إصدار التقرير الموسوعي"):
    if not name:
        st.error("يرجى كتابة الاسم")
    else:
        bmi = weight / ((height/100)**2)
        status = "نحافة" if bmi < 18.5 else "مثالي" if bmi < 25 else "زيادة وزن"
        
        st.markdown(f"## 📑 تقرير البطل: {name}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="info-section"><h3>⚖️ تحليل الجسم</h3><p>مؤشر الكتلة: <b>{bmi:.1f}</b><br>الحالة العامة: <b>{status}</b></p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="info-section"><h3>📈 مسار الوزن</h3>', unsafe_allow_html=True)
            st.line_chart(np.random.normal(weight, 0.3, 20))
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown(f"### 🥦 نصيحة الموسوعة لـ {status}")
        if status == "زيادة وزن":
            st.warning("ركز في الخضار المسلوق وابعد عن العيش الفينو والمقليات.")
        elif status == "نحافة":
            st.info("البروتين الشعبي (عدس وفول) مع السمن البلدي هيغير جسمك.")
        else:
            st.success("حافظ على المشي الصباحي وشرب المية بانتظام.")
else:
    st.info("👋 دخل بياناتك عشان نفتحلك الموسوعة والتقرير!")