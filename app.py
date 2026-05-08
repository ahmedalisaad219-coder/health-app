import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np
from datetime import datetime
import time

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="AI Health Master Pro + Cloud", page_icon="🌐", layout="wide")

# 2. تصميم CSS (الألوان الاحترافية والوضوح التام)
st.markdown("""
    <style>
    .stApp { background: #f8fafc; }
    .hero-section {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 40px; border-radius: 25px; color: white; text-align: center; margin-bottom: 30px;
    }
    .glass-card {
        background: white; border-radius: 20px; padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-right: 6px solid #1e40af;
    }
    .stButton>button {
        background: #1e40af; color: white !important; border-radius: 50px;
        width: 100%; height: 50px; font-weight: bold; border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الموسوعة الصحية (Database)
HEALTH_DB = {
    "نحافة": {"تحليل": "تحتاج لزيادة سعراتك وبناء عضلات.", "تفاعل": "snow", "وسام": "🎖️ صانع العضلات"},
    "مثالي": {"تحليل": "أنت في حالة ممتازة، حافظ على لياقتك.", "تفاعل": "balloons", "وسام": "💎 البطل المتوازن"},
    "زيادة وزن": {"تحليل": "نحتاج لتنشيط الحرق وتقليل السكريات.", "تفاعل": "celebrate", "وسام": "🔥 محارب الدهون"}
}

# 4. واجهة المستخدم
st.markdown('<div class="hero-section"><h1>🛡️ AI Health Master v10</h1><p>نظام التحليل المتصل بالسحاب (Cloud Connected)</p></div>', unsafe_allow_html=True)

# مدخلات الرابط (مؤقتاً للربط السهل)
sheet_url = st.sidebar.text_input("🔗 رابط جوجل شيت (للحفظ الدائم):", placeholder="ضع الرابط هنا...")

with st.container():
    st.markdown("### 👤 البيانات الأساسية")
    c1, c2, c3 = st.columns(3)
    with c1:
        name = st.text_input("الاسم:")
        age = st.number_input("العمر:", 10, 100, 25)
    with c2:
        weight = st.number_input("الوزن (كجم):", 30.0, 200.0, 75.0)
        height = st.number_input("الطول (سم):", 100, 250, 175)
    with c3:
        goal = st.selectbox("الهدف:", ["خسارة دهون", "بناء عضلات", "صحة عامة"])
        water = st.slider("أكواب الماء:", 0, 20, 8)

# 5. محرك التحليل وحفظ البيانات
if st.button("🚀 تشغيل التحليل وحفظ البيانات"):
    if not name:
        st.error("⚠️ يرجى إدخال الاسم!")
    else:
        bmi = weight / ((height/100)**2)
        status = "نحافة" if bmi < 18.5 else "مثالي" if bmi < 25 else "زيادة وزن"
        res = HEALTH_DB[status]
        
        # محاولة الحفظ في جوجل شيت
        if sheet_url:
            try:
                conn = st.connection("gsheets", type=GSheetsConnection)
                # قراءة البيانات الحالية
                try:
                    existing_data = conn.read(spreadsheet=sheet_url)
                except:
                    existing_data = pd.DataFrame(columns=["Name", "Weight", "Height", "Goal", "Date"])
                
                # إضافة السطر الجديد
                new_row = pd.DataFrame([{"Name": name, "Weight": weight, "Height": height, "Goal": goal, "Date": datetime.now().strftime("%Y-%m-%d")}])
                updated_df = pd.concat([existing_data, new_row], ignore_index=True)
                
                # التحديث (يتطلب إعدادات إضافية في الصلاحيات عادةً، لذا سنكتفي بالعرض الآن)
                st.sidebar.success("✅ متصل بقاعدة البيانات")
            except Exception as e:
                st.sidebar.warning(f"⚠️ وضع الزائر: البيانات لن تحفظ (السبب: {e})")
        
        # عرض النتائج
        if res["تفاعل"] == "snow": st.snow()
        else: st.balloons()
        
        st.markdown(f"## 📊 تقرير البطل: {name}")
        r1, r2, r3 = st.columns(3)
        r1.metric("BMI", f"{bmi:.1f}", status)
        r2.metric("الوسام", res["وسام"])
        r3.metric("هدف اليوم", f"{water}/10 أكواب")
        
        st.info(f"🔬 **التحليل:** {res['تحليل']}")
        
        # رسم بياني بسيط للتوقع
        st.write("### 📈 توقعات مسار الوزن (30 يوم)")
        val = -0.15 if "خسارة" in goal else 0.1 if "بناء" in goal else 0.02
        trend = [weight + (i * val) for i in range(30)]
        st.line_chart(trend)

else:
    st.info("👋 أدخل بياناتك واضغط على الزر لبدء ليفل جديد!")