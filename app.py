import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # مكتبة متطورة للرسومات

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="AI Health Hub", page_icon="💎", layout="wide")

# CSS متطور جداً لتغيير شكل الموقع بالكامل
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .main-title {
        color: #1e3a8a;
        font-size: 3rem !important;
        font-weight: 800;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        color: white !important;
        border: none;
        padding: 15px 30px;
        border-radius: 50px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر
st.markdown('<h1 class="main-title">🛡️ AI Health Hub v4.0</h1>', unsafe_allow_html=True)

# 3. إدخال البيانات بتصميم منظم
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input("👤 اسم المستخدم", placeholder="أدخل اسمك...")
        age = st.number_input("🎂 العمر", 10, 100, 20)
    with col2:
        height = st.number_input("📏 الطول (سم)", 100, 250, 170)
        weight = st.number_input("⚖️ الوزن (كجم)", 30, 200, 70)
    with col3:
        goal = st.selectbox("🎯 الهدف الاستراتيجي", ["خسارة دهون", "بناء عضلات", "صحة عامة"])
        gender = st.radio("🧬 النوع", ["ذكر", "أنثى"], horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### 📊 نمط الحياة اليومي")
c1, c2, c3 = st.columns(3)
with c1:
    water = st.select_slider("💧 شرب الماء (أكواب)", options=list(range(0, 21)), value=8)
with c2:
    sleep = st.select_slider("😴 ساعات النوم", options=list(range(0, 13)), value=7)
with c3:
    phone = st.select_slider("📱 استخدام الموبايل (ساعة)", options=list(range(0, 17)), value=5)

st.write("---")

# 4. محرك التحليل الذكي
if st.button("🚀 تحليل البيانات العميقة"):
    if not name:
        st.error("من فضلك أدخل اسمك لتخصيص التقرير!")
    else:
        bmi = weight / ((height/100)**2)
        st.balloons()
        
        # توزيع النتائج
        st.markdown(f"## 📋 التقرير الذكي لـ {name}")
        
        res_col1, res_col2 = st.columns([1, 1])
        
        with res_col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### ⚖️ الحالة البدنية")
            if bmi < 18.5: st.warning(f"مؤشر كتلة الجسم: {bmi:.1f} (نحافة)")
            elif bmi < 25: st.success(f"مؤشر كتلة الجسم: {bmi:.1f} (مثالي)")
            else: st.error(f"مؤشر كتلة الجسم: {bmi:.1f} (زيادة وزن)")
            
            # رسم بياني تفاعلي للوزن
            days = list(range(1, 31))
            if "خسارة" in goal: trend = [weight - (d * 0.1) for d in days]
            elif "بناء" in goal: trend = [weight + (d * 0.05) for d in days]
            else: trend = [weight] * 30
            
            df = pd.DataFrame({"اليوم": days, "الوزن المتوقع": trend})
            fig = px.line(df, x="اليوم", y="الوزن المتوقع", title="مسار التغير المتوقع")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with res_col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### 🧠 تحليل العادات")
            
            # رادار العادات (تقييم من 10)
            score = 0
            if 7 <= sleep <= 9: score += 30
            if water >= 8: score += 30
            if phone <= 4: score += 40
            
            st.write(f"**جودة نمط الحياة:** {score}%")
            st.progress(score / 100)
            
            st.markdown("---")
            st.markdown("### 🥗 التوصيات الذهبية")
            if score < 60:
                st.info("⚠️ تحتاج لتحسين عاداتك اليومية فوراً لزيادة طاقتك.")
            else:
                st.success("✅ أنت تتبع نمط حياة احترافي، استمر!")
                
            tips = {
                "خسارة دهون": "ركز على البروتين والألياف، وامشِ 10 آلاف خطوة.",
                "بناء عضلات": "ارفع أوزان ثقيلة ونم 8 ساعات على الأقل.",
                "صحة عامة": "نوع في أكلك واشرب مياه بانتظام."
            }
            st.write(f"**نصيحة الهدف:** {tips[goal]}")
            st.markdown('</div>', unsafe_allow_html=True)

        st.snow()
else:
    st.info("👋 مرحباً بك! املأ بياناتك في الأعلى واضغط على الزر للتحليل.")