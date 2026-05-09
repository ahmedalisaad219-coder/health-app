import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 1. إعدادات المنصة الأساسية
st.set_page_config(page_title="Health Student | الموسوعة الصحية الشاملة", page_icon="🎓", layout="wide")

# 2. تصميم احترافي متقدم (Custom CSS)
st.markdown("""
    <style>
    /* تنسيق الخلفية والعناصر العامة */
    .stApp { background-color: #f1f5f9; }
    
    /* رأس الصفحة */
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #2563eb 100%);
        padding: 50px; border-radius: 20px; text-align: center; color: white; 
        margin-bottom: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    /* تنسيق الكروت (الأقسام) */
    .card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;
        border-right: 7px solid #2563eb;
    }
    
    /* صناديق الحلول (الروشتة) */
    .solution-box {
        background: #fff7ed; border-right: 6px solid #f97316;
        padding: 20px; border-radius: 12px; margin-top: 15px;
        color: #9a3412; font-size: 15px; line-height: 1.6;
    }
    
    /* صناديق النجاح (الحالات الجيدة) */
    .success-box {
        background: #f0fdf4; border-right: 6px solid #22c55e;
        padding: 20px; border-radius: 12px; margin-top: 15px;
        color: #166534;
    }

    /* تنسيق التبويبات */
    .stTabs [data-baseweb="tab"] {
        font-size: 18px; font-weight: bold; padding: 12px 30px;
    }
    
    h2, h3 { color: #1e3a8a; }
    </style>
""", unsafe_allow_html=True)

# 3. واجهة المستخدم الرئيسية
st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>موسوعة الحلول الذكية - مرجعك الأول لصحة جسدية وعقلية أفضل أثناء الدراسة</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية (بيانات الطالب)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3048/3048122.png", width=100)
    st.header("👤 بيانات الطالب")
    student_name = st.text_input("اسم الطالب:", placeholder="اكتب اسمك هنا...")
    age = st.number_input("العمر:", 15, 50, 20)
    st.write("---")
    st.markdown("### 📊 حالة الموسوعة")
    st.info("النظام جاهز لتحليل بياناتك وتقديم الحلول الموسوعية.")
    if st.button("🔄 تصفير البيانات"):
        st.rerun()

# 5. منطق الموسوعة والتحليل
if not student_name:
    st.warning("👈 يرجى إدخال اسمك في القائمة الجانبية لتفعيل موسوعة الحلول الخاصة بك.")
else:
    # إنشاء التبويبات الخمسة الأساسية
    tabs = st.tabs([
        "🌙 النوم واليقظة", 
        "📱 التكنولوجيا والعين", 
        "🏃 الحركة والآلام", 
        "🍎 الغذاء والدماغ", 
        "🧠 الحالة النفسية والتسويف"
    ])

    # --- تبويب (1): النوم ---
    with tabs[0]:
        st.markdown('## 🌙 موسوعة حلول النوم والتركيز')
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            sleep_h = st.slider("كم ساعة تنام يومياً؟", 2, 12, 7)
            sleep_quality = st.select_slider("كيف تصف جودة نومك؟", options=["سيئة", "متقطعة", "جيدة", "عميقة جداً"])
            coffee_late = st.checkbox("هل تشرب قهوة أو منبهات بعد الساعة 6 مساءً؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.write("### 🏥 الروشتة البرمجية للنوم:")
            if sleep_h < 7:
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: الحرمان الإدراكي.</b><br><b>الحل:</b> المخ يحتاج 7 ساعات كحد أدنى لتنظيف الخلايا من السموم (Beta-amyloid). حاول النوم قبل منتصف الليل لضبط ساعتك البيولوجية.</div>', unsafe_allow_html=True)
            if coffee_late:
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: حصار الأدينوزين.</b><br><b>الحل:</b> الكافيين يغلق مستقبلات التعب في مخك لكن التعب لا يختفي. توقف عن المنبهات قبل موعد نومك بـ 8 ساعات على الأقل.</div>', unsafe_allow_html=True)
            if sleep_h >= 7 and not coffee_late:
                st.markdown('<div class="success-box">✅ نظام نومك يدعم الذاكرة الطويلة المدى بشكل ممتاز. استمر!</div>', unsafe_allow_html=True)

    # --- تبويب (2): الموبايل والعين ---
    with tabs[1]:
        st.markdown('## 📱 موسوعة التكنولوجيا وإجهاد العين')
        c3, c4 = st.columns(2)
        with c3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            screen_time = st.slider("ساعات استخدام الموبايل (غير الدراسة):", 1, 16, 5)
            eye_dryness = st.checkbox("هل تعاني من جفاف العين أو صداع بعد المذاكرة؟")
            dark_mode = st.checkbox("هل تستخدم وضع " + "Dark Mode" + " دائماً؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with c4:
            st.write("### 🏥 حلول الإجهاد الرقمي:")
            if eye_dryness:
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: متلازمة الرؤية الكمبيوترية.</b><br><b>الحل:</b> طبق قاعدة 20-20-20. كل 20 دقيقة، انظر لمكان بعيد (6 أمتار) لمدة 20 ثانية لتريح عضلات العين.</div>', unsafe_allow_html=True)
            if screen_time > 6:
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: تشتت الانتباه الرقمي.</b><br><b>الحل:</b> وقتك يضيع في التمرير اللانهائي. جرب مسح تطبيقات التواصل وإعادة تحميلها في العطلة فقط.</div>', unsafe_allow_html=True)

    # --- تبويب (3): الحركة والآلام ---
    with tabs[2]:
        st.markdown('## 🏃 موسوعة الحركة وآلام الجلوس')
        c5, c6 = st.columns(2)
        with c5:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            sitting_h = st.number_input("كم ساعة تجلس للمذاكرة يومياً؟", 1, 15, 6)
            back_pain = st.radio("هل تشعر بألم في الظهر أو الرقبة؟", ["لا يوجد", "ألم بسيط", "ألم شديد"])
            st.markdown('</div>', unsafe_allow_html=True)
        with c6:
            st.write("### 🏥 حلول آلام الهيكل العظمي:")
            if back_pain != "لا يوجد":
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: الضغط الفقري.</b><br><b>الحل:</b> لا تذاكر أبداً وأنت مستلقٍ على السرير. استخدم كرسياً بمسند للظهر، واجعل حافة الشاشة العلوية في مستوى عينك تماماً.</div>', unsafe_allow_html=True)
            if sitting_h > 4:
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: الركود الدموي.</b><br><b>الحل:</b> قف وتحرك لمدة 5 دقائق كل ساعة مذاكرة. هذا يضخ الأكسجين مجدداً لدماغك ويرفع استيعابك بنسبة 20%.</div>', unsafe_allow_html=True)

    # --- تبويب (4): التغذية والدماغ ---
    with tabs[3]:
        st.markdown('## 🍎 موسوعة الغذاء والتركيز الذهني')
        c7, c8 = st.columns(2)
        with c7:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            water_h = st.slider("كم كوب ماء تشرب؟", 0, 15, 6)
            sugar_intake = st.select_slider("معدل تناول السكريات والحلويات:", options=["منخفض", "متوسط", "عالي جداً"])
            breakfast = st.checkbox("هل تأكل وجبة إفطار غنية بالبروتين؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with c8:
            st.write("### 🏥 حلول التغذية العقلية:")
            if water_h < 8:
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: جفاف خلايا الدماغ.</b><br><b>الحل:</b> الجفاف بنسبة 2% فقط يسبب تشتت الانتباه. اشرب لتر ماء إضافي أثناء المذاكرة.</div>', unsafe_allow_html=True)
            if sugar_intake == "عالي جداً":
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: ضبابية الدماغ (Brain Fog).</b><br><b>الحل:</b> السكر يرفع طاقتك لحظياً ثم ينهار سكر الدم فتفقد تركيزك. استبدل الحلوى بالمكسرات أو الفاكهة.</div>', unsafe_allow_html=True)

    # --- تبويب (5): الحالة النفسية ---
    with tabs[4]:
        st.markdown('## 🧠 موسوعة الحلول النفسية والتسويف')
        c9, c10 = st.columns(2)
        with c9:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            procrastination = st.radio("هل تؤجل المذاكرة حتى اللحظة الأخيرة؟", ["دائماً", "أحياناً", "أبدأ مبكراً"])
            exam_stress = st.select_slider("مستوى قلقك من الامتحانات:", options=["هادئ", "متوتر قليلاً", "رعب شديد"])
            st.markdown('</div>', unsafe_allow_html=True)
        with c10:
            st.write("### 🏥 حلول الإنتاجية والهدوء:")
            if procrastination == "دائماً":
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: خوف البداية (التسويف).</b><br><b>الحل:</b> استخدم "قاعدة الخمس دقائق". ابدأ المذاكرة لمدة 5 دقائق فقط، وعقلك سيكمل المهمة تلقائياً بعد كسر حاجز البداية.</div>', unsafe_allow_html=True)
            if exam_stress == "رعب شديد":
                st.markdown('<div class="solution-box"><b>🚨 مشكلة: فرط نشاط اللوزة الدماغية (Amydala).</b><br><b>الحل:</b> جرب الكتابة التعبيرية. اكتب كل مخاوفك على ورقة لمدة 10 دقائق قبل المذاكرة لتفريغ شحنة التوتر من مخك.</div>', unsafe_allow_html=True)

    # التقرير الختامي
    st.write("---")
    st.markdown(f"### 🏁 الملخص الموسوعي لـ {student_name}")
    st.info("هذه الموسوعة ليست مجرد أرقام، بل هي دليل عملي لتغيير حياتك. اتبع 'الحلول' المكتوبة بالأعلى وستلاحظ تحسناً جذرياً في صحتك ومعدلك الدراسي.")