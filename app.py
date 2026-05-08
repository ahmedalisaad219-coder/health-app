import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="AI Health Master Pro", page_icon="⚡", layout="wide")

# CSS متطور جداً (تصميم النيون الهادئ وتأثيرات حركية)
st.markdown("""
    <style>
    .stApp { background: #f0f2f6; }
    .main-header {
        background: linear-gradient(120deg, #1557ff 0%, #00d4ff 100%);
        padding: 50px; border-radius: 30px; color: white;
        text-align: center; margin-bottom: 40px;
        box-shadow: 0 20px 40px rgba(21, 87, 255, 0.2);
    }
    .status-card {
        background: white; border-radius: 20px; padding: 25px;
        border-bottom: 5px solid #1557ff;
        transition: transform 0.3s ease;
    }
    .status-card:hover { transform: translateY(-10px); }
    .badge {
        background: #ffd700; color: #000; padding: 5px 15px;
        border-radius: 50px; font-weight: bold; font-size: 14px;
    }
    .stNumberInput, .stTextInput { border-radius: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. الموسوعة المحدثة (داتا موسعة جداً)
ADVANCED_DB = {
    "نحافة": {
        "التحليل": "جسمك في حالة 'الأيض السريع'. نحتاج لإعادة هندسة الكتلة العضلية وتخزين الطاقة.",
        "سوبر_فود": ["زبدة اللوز", "الشوفان بالحليب كامل الدسم", "سمك السلمون", "البطاطا الحلوة"],
        "مشروبات": "عصير الأفوكادو بالعسل، سموزي البروتين الطبيعي.",
        "الخطة_الرياضية": "رفع أثقال (شدة عالية) مع تكرارات قليلة (6-8) لزيادة الضخامة.",
        "التحدي": "تحدي الـ 3000 سعرة حرارية يومياً.",
        "وسام": "🎖️ صانع العضلات الناشئ"
    },
    "مثالي": {
        "التحليل": "أنت في مرحلة 'الاستدامة الحيوية'. هدفنا هو تحسين الأداء الرياضي والوقاية الطويلة.",
        "سوبر_فود": ["بذور الشيا", "صدور الدجاج المشوية", "البروكلي", "التوت الأزرق"],
        "مشروبات": "الشاي الأخضر بالليمون، مياه الديتوكس بالنعناع.",
        "الخطة_الرياضية": "نظام الكروس فت أو السباحة لمدة ساعة 3 مرات أسبوعياً.",
        "التحدي": "تحدي المرونة واليوجا الصباحية.",
        "وسام": "💎 البطل المتوازن"
    },
    "زيادة وزن": {
        "التحليل": "الجسم في مرحلة 'المقاومة'. سنعمل على تنشيط الغدد المسؤولة عن الحرق وتقليل الالتهابات.",
        "سوبر_فود": ["البيض المسلوق", "السبانخ", "صدور الرومي", "الجوز (عين الجمل)"],
        "مشروبات": "القهوة السوداء (بدون سكر)، منقوع القرفة والزنجبيل.",
        "الخطة_الرياضية": "تمارين الـ HIIT لمدة 20 دقيقة يومياً + مشي سريع بعد الوجبات.",
        "التحدي": "تحدي الـ 10 آلاف خطوة وقطع السكر.",
        "وسام": "🔥 محارب الدهون"
    }
}

# 3. تصميم الواجهة (The High-Level UI)
st.markdown('<div class="main-header"><h1>🚀 AI Health Hub: Level Up</h1><p>مستشارك الذكي المعتمد على البيانات الضخمة</p></div>', unsafe_allow_html=True)

with st.expander("🛠️ إعدادات الحساب وتخصيص البيانات", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        user_name = st.text_input("👤 كود المستخدم:", value="بطل 2026")
        age = st.number_input("🎂 العمر:", 10, 100, 25)
    with col2:
        weight = st.number_input("⚖️ الوزن الحالي (كجم):", 30.0, 200.0, 70.0)
        height = st.number_input("📏 الطول (سم):", 100, 250, 175)
    with col3:
        goal = st.selectbox("🎯 الهدف الاستراتيجي:", ["تدمير الدهون", "بناء كتلة صلبة", "لياقة أبدية"])
        activity = st.select_slider("⚡ مستوى نشاطك:", options=["خامل", "متوسط", "نشط جداً"])

st.write("---")

# تفاعل إضافي: عادات اليوم
st.subheader("📊 مؤشرات الأداء اليومي")
c1, c2, c3, c4 = st.columns(4)
water = c1.number_input("💧 مياه (أكواب):", 0, 20, 8)
sleep = c2.number_input("😴 نوم (ساعات):", 0, 12, 8)
steps = c3.number_input("👣 خطوات اليوم:", 0, 30000, 5000)
stress = c4.slider("🧠 مستوى التوتر:", 1, 10, 5)

# 4. محرك التشغيل (Execution Engine)
if st.button("🔥 تفعيل التحليل الذكي الشامل"):
    with st.status("جاري الاتصال بقاعدة البيانات العملاقة...", expanded=True) as status_load:
        st.write("تحليل مؤشرات الجسم...")
        time.sleep(1)
        st.write("مطابقة البيانات مع الأهداف الاستراتيجية...")
        time.sleep(1)
        status_load.update(label="✅ اكتمل التحليل!", state="complete", expanded=False)

    bmi = weight / ((height/100)**2)
    if bmi < 18.5: status = "نحافة"
    elif bmi < 25: status = "مثالي"
    else: status = "زيادة وزن"
    
    data = ADVANCED_DB[status]
    
    # تفاعل بصري (حسب السكور)
    score = (water*5) + (sleep*5) + (steps/500) - (stress*2)
    if score > 70: st.balloons()
    else: st.toast("تقريرك جاهز، يمكنك تحسين نتائجك غداً!", icon="📈")

    # عرض النتائج بطريقة احترافية
    st.markdown(f"## 🏆 النتائج الاحترافية لـ {user_name}")
    
    r1, r2, r3, r4 = st.columns(4)
    r1.markdown(f'<div class="status-card"><h3>⚖️ BMI</h3><h2 style="color:#1557ff">{bmi:.1f}</h2><p>{status}</p></div>', unsafe_allow_html=True)
    r2.markdown(f'<div class="status-card"><h3>⭐ سكور</h3><h2 style="color:#10b981">{int(score)}%</h2><p>نقاط الصحة</p></div>', unsafe_allow_html=True)
    r3.markdown(f'<div class="status-card"><h3>🛡️ الوسام</h3><span class="badge">{data["وسام"]}</span></div>', unsafe_allow_html=True)
    r4.markdown(f'<div class="status-card"><h3>🔥 حرق</h3><h2 style="color:#f59e0b">{int(1.2 * (10*weight + 6.25*height))}</h2><p>BMR</p></div>', unsafe_allow_html=True)

    st.divider()

    col_info1, col_info2 = st.columns([1.5, 1])
    
    with col_info1:
        st.markdown(f"### 🧪 التحليل العلمي: {status}")
        st.info(data["التحليل"])
        
        st.markdown("### 📈 مسار التغير المتوقع (30 يوم)")
        days = list(range(1, 31))
        # معادلة رياضية ديناميكية للرسم البياني
        base_trend = [weight + (d * (0.1 if "بناء" in goal else -0.15 if "تدمير" in goal else 0.02)) for d in days]
        chart_df = pd.DataFrame({"الوزن المتوقع": base_trend}, index=days)
        st.line_chart(chart_df)

    with col_info2:
        st.markdown("### 🥗 قائمة الـ Super Food")
        for food in data["sوبر_فود"]:
            st.success(f"🔹 {food}")
        
        st.markdown("### 🥤 مشروبات الطاقة الطبيعية")
        st.warning(data["مشروبات"])
        
        st.markdown(f"### 🏋️ بروتوكول: {goal}")
        st.write(data["الخطة_الرياضية"])
        
        st.error(f"🚩 **التحدي الحالي:** {data['التحدي']}")

    st.snow()
else:
    st.info("💡 أدخل بياناتك في الأعلى للحصول على تحليل 'الليفل الأعلى'!")