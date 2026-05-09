import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 1. إعدادات المنصة
st.set_page_config(page_title="Health Student | حلول صحية ذكية", page_icon="🎓", layout="wide")

# 2. تصميم احترافي (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 40px; border-radius: 20px; text-align: center; color: white; margin-bottom: 30px;
    }
    .card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;
        border-bottom: 4px solid #3b82f6;
    }
    .solution-box {
        background: #fff7ed; border-right: 5px solid #ea580c;
        padding: 15px; border-radius: 8px; margin-top: 10px; color: #9a3412;
    }
    .success-box {
        background: #f0fdf4; border-right: 5px solid #22c55e;
        padding: 15px; border-radius: 8px; margin-top: 10px; color: #166534;
    }
    h3 { color: #1e293b; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Solutions</h1><p>تحليل العادات وتقديم حلول علمية مخصصة للطلاب</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar) - بسيطة جداً
with st.sidebar:
    st.header("👤 ملف الطالب")
    student_name = st.text_input("اسم الطالب:", placeholder="اكتب اسمك هنا...")
    age = st.number_input("العمر:", 15, 50, 20)
    st.write("---")
    st.info("قم بتعبئة الأقسام في اليمين للحصول على الحلول.")

# 5. منطق التحقق
if not student_name:
    st.warning("👋 أهلاً بك! من فضلك اكتب اسمك للبدء في تحليل عاداتك الصحية.")
else:
    # إنشاء التبويبات (Tabs)
    tab1, tab2, tab3, tab4 = st.tabs(["😴 النوم والتركيز", "📱 الموبايل والدراسة", "🏃 الرياضة والحركة", "🥗 التغذية والماء"])

    # --- القسم الأول: النوم ---
    with tab1:
        st.markdown('### 🌙 قسم النوم')
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            sleep_h = st.slider("كم ساعة نمت بالأمس؟", 2, 14, 7)
            trouble_sleeping = st.radio("هل تجد صعوبة في النوم فور دخولك السرير؟", ["نعم دائماً", "أحياناً", "لا، أنام بسرعة"])
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('**التحليل والحلول:**')
            if sleep_h < 7:
                st.markdown('<div class="solution-box"><b>🛑 المشكلة:</b> نقص حاد في النوم.<br><b>✅ الحل:</b> حاول تثبيت ميعاد للنوم يومياً، وقلل الكافيين بعد الساعة 5 مساءً.</div>', unsafe_allow_html=True)
            if trouble_sleeping == "نعم دائماً":
                st.markdown('<div class="solution-box"><b>🛑 المشكلة:</b> أرق البداية.<br><b>✅ الحل:</b> اترك الموبايل قبل النوم بـ 45 دقيقة، وجرب قراءة كتاب ورقي أو الاستماع لصوت هادئ.</div>', unsafe_allow_html=True)
            if sleep_h >= 7 and trouble_sleeping == "لا، أنام بسرعة":
                st.markdown('<div class="success-box">✅ نظام نومك مثالي، استمر على هذا المنوال لضمان تركيزك الدراسي.</div>', unsafe_allow_html=True)

    # --- القسم الثاني: الموبايل ---
    with tab2:
        st.markdown('### 📱 قسم الموبايل')
        cm1, cm2 = st.columns(2)
        with cm1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            phone_h = st.slider("ساعات استخدام الموبايل يومياً:", 1, 15, 5)
            study_phone = st.radio("هل تستخدم الموبايل أثناء المذاكرة؟", ["نعم، للتسلية", "للضرورة فقط", "لا ألمسه"])
            st.markdown('</div>', unsafe_allow_html=True)
        with cm2:
            st.markdown('**التحليل والحلول:**')
            if phone_h > 6:
                st.markdown('<div class="solution-box"><b>🛑 المشكلة:</b> وقت الشاشة مرتفع جداً.<br><b>✅ الحل:</b> فعل خاصية (Focus Mode) في موبايلك وحدد وقت لتطبيقات السوشيال ميديا.</div>', unsafe_allow_html=True)
            if study_phone == "نعم، للتسلية":
                st.markdown('<div class="solution-box"><b>🛑 المشكلة:</b> تشتت الانتباه.<br><b>✅ الحل:</b> استخدم تقنية (Pomodoro) - ذاكر 25 دقيقة وكافئ نفسك بـ 5 دقائق موبايل.</div>', unsafe_allow_html=True)

    # --- القسم الثالث: الرياضة ---
    with tab3:
        st.markdown('### 🏃 قسم الحركة')
        cp1, cp2 = st.columns(2)
        with cp1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            active_days = st.slider("أيام النشاط البدني أسبوعياً:", 0, 7, 2)
            stiff_neck = st.checkbox("هل تشعر بآلام في الرقبة أو الظهر بسبب الجلوس؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with cp2:
            st.markdown('**التحليل والحلول:**')
            if active_days < 3:
                st.markdown('<div class="solution-box"><b>🛑 المشكلة:</b> خمول بدني.<br><b>✅ الحل:</b> المشي لمدة 15 دقيقة فقط يومياً يحسن مزاجك وقدرتك على الحفظ.</div>', unsafe_allow_html=True)
            if stiff_neck:
                st.markdown('<div class="solution-box"><b>🛑 المشكلة:</b> إجهاد وضعية الجلوس.<br><b>✅ الحل:</b> تأكد من وضع الشاشة في مستوى عينك، وقم بعمل تمارين إطالة للرقبة كل ساعة.</div>', unsafe_allow_html=True)

    # --- القسم الرابع: التغذية ---
    with tab4:
        st.markdown('### 🥗 قسم التغذية')
        cf1, cf2 = st.columns(2)
        with cf1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            water = st.slider("أكواب الماء يومياً:", 0, 15, 6)
            junk_food = st.selectbox("كم مرة تأكل وجبات سريعة؟", ["نادراً", "مرتين أسبوعياً", "يومياً"])
            st.markdown('</div>', unsafe_allow_html=True)
        with cf2:
            st.markdown('**التحليل والحلول:**')
            if water < 8:
                st.markdown('<div class="solution-box"><b>🛑 المشكلة:</b> جفاف بسيط.<br><b>✅ الحل:</b> اشرب كوب ماء فور الاستيقاظ، واجعل زجاجة الماء أمامك دائماً أثناء المذاكرة.</div>', unsafe_allow_html=True)
            if junk_food != "نادراً":
                st.markdown('<div class="solution-box"><b>🛑 المشكلة:</b> طاقة غير مستقرة.<br><b>✅ الحل:</b> الوجبات السريعة تسبب خمولاً بعد ساعة؛ استبدلها بمكسرات أو فواكه أثناء المذاكرة.</div>', unsafe_allow_html=True)

    # التقرير الختامي
    st.write("---")
    st.markdown(f"### 📊 التقرير النهائي لـ {student_name}")
    st.info("بناءً على إجاباتك، قمنا بتوضيح الحلول المخصصة لك في كل قسم أعلاه. البدء بتغيير عادة واحدة فقط كفيل بتحسين مستواك الدراسي.")