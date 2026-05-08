import streamlit as st
import pandas as pd
import numpy as np
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="المستشار الصحي الذكي 2026", page_icon="🌿", layout="wide")

# تصميم CSS (ألوان فاتحة، كلام واضح، تصميم عصري)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }
    .main-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .metric-box {
        background: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border-bottom: 4px solid #3b82f6;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    h1 { color: #1e293b; font-weight: 800; text-align: center; }
    h3 { color: #334155; }
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6 0%, #10b981 100%);
        color: white !important;
        border-radius: 50px;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(59,130,246,0.3); }
    </style>
    """, unsafe_allow_html=True)

# 2. الموسوعة الصحية الموسعة (بيانات ضخمة ومنظمة)
HEALTH_ENCYCLOPEDIA = {
    "خسارة دهون": {
        "التحليل": "هدفك هو حرق الدهون مع الحفاظ على العضلات. نحتاج لعجز سعرات ذكي.",
        "النظام_الغذائي": [
            "الصيام المتقطع (16 ساعة صيام، 8 ساعات أكل).",
            "زيادة حصة الألياف (نصف طبق سلطة في كل وجبة).",
            "استبدال الكربوهيدرات البسيطة بالمعقدة (كينوا، شوفان، فريك).",
            "شرب لتر مياه لكل 30 كجم من وزنك."
        ],
        "خطة_النشاط": "تمارين الكارديو (مشي سريع) قبل الفطار، وتمارين مقاومة خفيفة مساءً.",
        "نصيحة_ذهبية": "النوم قبل الساعة 11 مساءً يعزز حرق الدهون بنسبة 20%."
    },
    "بناء عضلات": {
        "التحليل": "هدفك هو بناء أنسجة عضلية قوية. نحتاج لفائض سعرات مدروس وبروتين كافٍ.",
        "النظام_الغذائي": [
            "تناول 1.6 جرام بروتين لكل كيلو من وزنك.",
            "وجبة كربوهيدرات سريعة قبل التمرين بـ 45 دقيقة (موز أو تمر).",
            "إضافة الدهون الصحية (أفوكادو، مكسرات) لزيادة الطاقة.",
            "توزيع الوجبات على 4-5 وجبات يومياً."
        ],
        "خطة_النشاط": "رفع أثقال بجدول (Push/Pull/Legs) مع راحة كافية للعضلات.",
        "نصيحة_ذهبية": "شرب المياه بين المجموعات التدريبية يحافظ على ضخ الدم للعضلات."
    },
    "صحة عامة": {
        "التحليل": "هدفك هو تحسين جودة الحياة والنشاط اليومي والوقاية من الأمراض.",
        "النظام_الغذائي": [
            "نظام 'طبق الأكل الصحي' (بروتين، نشويات، خضروات).",
            "تقليل السكر المضاف للمشروبات تدريجياً.",
            "تناول الفاكهة الموسمية كمصدر أساسي للفيتامينات.",
            "الحرص على تناول الأسماك مرتين أسبوعياً."
        ],
        "خطة_النشاط": "المشي لمدة 30 دقيقة يومياً مع تمارين إطالة (Stretch) صباحاً.",
        "نصيحة_ذهبية": "تجنب الجلوس المستمر لأكثر من ساعة؛ تحرك لمدة دقيقتين."
    }
}

# 3. واجهة المستخدم
st.markdown("<h1>🌿 AI Global Health Tracker</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center; color:#64748b;'>مستشارك الشخصي المطور لتحسين الأداء الحيوي</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        name = st.text_input("👤 اسم البطل")
        age = st.number_input("🎂 العمر", 10, 100, 20)
    with c2:
        weight = st.number_input("⚖️ الوزن (كجم)", 30, 200, 70)
        height = st.number_input("📏 الطول (سم)", 100, 250, 170)
    with c3:
        goal = st.selectbox("🎯 الهدف المرجو", ["خسارة دهون", "بناء عضلات", "صحة عامة"])
        water = st.slider("💧 أكواب الماء يومياً", 0, 20, 8)
    
    st.markdown("---")
    cc1, cc2 = st.columns(2)
    with cc1: sleep = st.select_slider("😴 ساعات النوم", options=list(range(0, 13)), value=8)
    with cc2: phone = st.select_slider("📱 ساعات الموبايل", options=list(range(0, 17)), value=5)
    st.markdown('</div>', unsafe_allow_html=True)

# 4. محرك التحليل
if st.button("🚀 إصدار التقرير التفاعلي الشامل"):
    if not name:
        st.error("يرجى كتابة الاسم لتفعيل التقرير.")
    else:
        bmi = weight / ((height/100)**2)
        st.balloons()
        
        # قسم النتائج بالألوان الواضحة
        st.markdown(f"### 📋 ملف تحليل: {name}")
        
        col_res1, col_res2, col_res3, col_res4 = st.columns(4)
        with col_res1:
            st.markdown(f'<div class="metric-box"><h3>⚖️ BMI</h3><h2>{bmi:.1f}</h2></div>', unsafe_allow_html=True)
        with col_res2:
            status = "نحافة" if bmi < 18.5 else "مثالي" if bmi < 25 else "زيادة وزن"
            st.markdown(f'<div class="metric-box"><h3>📊 الحالة</h3><h2>{status}</h2></div>', unsafe_allow_html=True)
        with col_res3:
            score = (water*5) + (sleep*8) - (phone*4)
            st.markdown(f'<div class="metric-box"><h3>⭐ سكور</h3><h2>{score}%</h2></div>', unsafe_allow_html=True)
        with col_res4:
            st.markdown(f'<div class="metric-box"><h3>🔥 حرق</h3><h2>{int(10*weight+6.25*height)}</h2></div>', unsafe_allow_html=True)

        st.divider()

        # الداتا التفاعلية (الرسوم والموسوعة)
        data_col1, data_col2 = st.columns([1.2, 1])
        
        with data_col1:
            st.markdown("### 📈 توقعات المسار (30 يوم القادمة)")
            days = list(range(1, 31))
            if "خسارة" in goal: trend = [weight - (d * 0.12) for d in days]
            elif "بناء" in goal: trend = [weight + (d * 0.08) for d in days]
            else: trend = [weight + np.sin(d)*0.3 for d in days]
            
            df = pd.DataFrame({"الوزن": trend}, index=days)
            st.line_chart(df)
            
        with data_col2:
            info = HEALTH_ENCYCLOPEDIA[goal]
            st.markdown(f"### 🥗 موسوعة التغذية لـ {goal}")
            st.info(info["التحليل"])
            for tip in info["النظام_الغذائي"]:
                st.write(f"✅ {tip}")

        st.divider()
        
        # إضافات تفاعلية أخيرة
        fin_c1, fin_c2 = st.columns(2)
        with fin_c1:
            st.success(f"🏋️ **البرنامج الرياضي:** {info['خطة_النشاط']}")
        with fin_c2:
            st.warning(f"💡 **نصيحة الموسوعة:** {info['نصيحة_ذهبية']}")
        
        st.snow()
else:
    st.info("👋 أهلاً بك يا بطل! املأ بياناتك واضغط على الزر بالأعلى للحصول على تقريرك الاحترافي.")