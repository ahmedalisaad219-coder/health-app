import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import numpy as np
from datetime import datetime

# 1. إعدادات الصفحة والستايل
st.set_page_config(page_title="AI Health Hub Pro", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #f0f2f6; }
    .main-header { background: #1e3a8a; padding: 25px; border-radius: 15px; color: white; text-align: center; margin-bottom: 25px; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# 2. قاعدة البيانات الداخلية (وحدنا الأسماء لمنع الـ KeyError)
DB = {
    "نحافة": {"تحليل": "تحتاج لزيادة السعرات الصحية.", "تفاعل": "snow"},
    "مثالي": {"تحليل": "وضعك ممتاز، حافظ على التوازن.", "تفاعل": "balloons"},
    "زيادة وزن": {"تحليل": "نحتاج لتنظيم الأكل وزيادة الحركة.", "تفاعل": "balloons"}
}

# 3. الواجهة الرئيسية
st.markdown('<div class="main-header"><h1>🚀 AI Health Master Pro</h1></div>', unsafe_allow_html=True)

# شريط جانبي للرابط
with st.sidebar:
    st.header("⚙️ الإعدادات")
    sheet_url = st.text_input("رابط جوجل شيت (اختياري):")

# مدخلات البيانات
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 الاسم:")
        weight = st.number_input("⚖️ الوزن (كجم):", 30.0, 200.0, 70.0)
    with col2:
        height = st.number_input("📏 الطول (سم):", 100, 250, 170)
        goal = st.selectbox("🎯 الهدف:", ["تنشيف", "ضخامة", "لياقة"])

# 4. محرك التحليل
if st.button("🏁 ابدأ التحليل"):
    if not name:
        st.error("يرجى إدخال الاسم أولاً")
    else:
        # حساب BMI
        bmi = weight / ((height/100)**2)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        # عرض النتائج (حل مشكلة AttributeError و KeyError)
        res = DB[status]
        if res["تفاعل"] == "snow":
            st.snow()
        else:
            st.balloons()
            
        st.markdown(f"### 📊 التقرير الخاص بك يا {name}")
        c1, c2 = st.columns(2)
        c1.metric("مؤشر الكتلة (BMI)", f"{bmi:.1f}", status)
        c2.info(f"🔬 **التحليل:** {res['تحليل']}")
        
        # الرسم البياني (بدون مكتبات خارجية معقدة لضمان التسطيب)
        st.write("### 📈 مسار الوزن المتوقع")
        diff = -0.1 if "تنشيف" in goal else 0.1 if "ضخامة" in goal else 0.01
        trend = [weight + (i * diff) for i in range(30)]
        st.line_chart(trend)

        # محاولة الاتصال بجوجل شيت (لو الرابط موجود)
        if sheet_url:
            try:
                conn = st.connection("gsheets", type=GSheetsConnection)
                st.sidebar.success("✅ متصل بالسحاب")
            except:
                st.sidebar.warning("⚠️ الرابط غير صحيح، سيعمل الموقع كنسخة زائر.")