import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 1. إعدادات المنصة
st.set_page_config(page_title="Health Student | الموسوعة الشاملة", page_icon="🎓", layout="wide")

# 2. تصميم CSS (واجهة عصرية وتفاعلية)
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        padding: 50px; border-radius: 20px; text-align: center; color: white; margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    .card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;
        border-right: 8px solid #2563eb;
    }
    .solution-box {
        background: #fff7ed; border-right: 6px solid #f97316;
        padding: 15px; border-radius: 10px; margin-top: 10px; color: #9a3412; font-size: 14px;
    }
    .success-box {
        background: #f0fdf4; border-right: 6px solid #22c55e;
        padding: 15px; border-radius: 10px; margin-top: 10px; color: #166534;
    }
    .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية لحلول مشاكل الطلاب الصحية والدراسية</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.header("👤 بيانات الطالب")
    name = st.text_input("الاسم بالكامل:", placeholder="اكتب اسمك هنا...")
    if 'water' not in st.session_state: st.session_state.water = 0
    
    st.write("---")
    st.subheader(f"💧 كوبايات المية: {st.session_state.water}")
    if st.button("🥤 سجل كوب مياه"):
        st.session_state.water += 1
        st.toast("بطل! الترطيب أساس التركيز.")
    
    st.write("---")
    st.info("قم بإنهاء جميع الأقسام لتحميل تقريرك النهائي.")

# 5. منطق الموسوعة والحلول
if not name:
    st.warning("⚠️ يرجى إدخال اسمك في القائمة الجانبية لفتح الموسوعة.")
else:
    # قائمة لتخزين الحلول للتقرير النهائي
    user_solutions = []

    tabs = st.tabs(["🌙 النوم والتركيز", "📱 التكنولوجيا", "🏃 الحركة والآلام", "🍎 التغذية والدماغ", "🧠 الحالة النفسية", "📥 التقرير النهائي"])

    # --- تبويب النوم ---
    with tabs[0]:
        st.subheader("🌙 قسم حلول النوم")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            s_hours = st.slider("ساعات نومك:", 2, 12, 7)
            s_quality = st.select_slider("جودة النوم:", ["سيئة", "متقطعة", "ممتازة"])
            coffee_late = st.toggle("شربت كافيين قبل النوم بـ 6 ساعات؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            if s_hours < 7:
                msg = "🛑 حل نقص النوم: المخ يحتاج دورات نوم كاملة لتثبيت المعلومات؛ حاول النوم 7 ساعات ونصف (5 دورات)."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)
            if s_quality == "متقطعة":
                msg = "🛑 حل النوم المتقطع: امنع الضوء الأزرق من الموبايل قبل النوم بـ 45 دقيقة لزيادة هرمون الميلاتونين."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)
            if coffee_late:
                msg = "🛑 حل الكافيين: الكافيين يغلق مستقبلات التعب؛ استبدله بـ 'بابونج' أو 'ينسون' في المساء."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)

    # --- تبويب التكنولوجيا ---
    with tabs[1]:
        st.subheader("📱 قسم حلول إجهاد الشاشات")
        c3, c4 = st.columns(2)
        with c3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            p_hours = st.slider("ساعات الموبايل (ترفيه):", 1, 16, 5)
            eye_pain = st.checkbox("بتحس بجفاف أو حرقان في عينك؟")
            st_distract = st.checkbox("الموبايل بيعطلك عن المذاكرة؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with c4:
            if eye_pain:
                msg = "🛑 حل إجهاد العين: طبق قاعدة (20-20-20)؛ كل 20 دقيقة انظر لمسافة بعيدة لمدة 20 ثانية."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)
            if p_hours > 6 or st_distract:
                msg = "🛑 حل التشتت الرقمي: استخدم تطبيقات (App Block) لقفل السوشيال ميديا وقت المذاكرة الجادة."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)

    # --- تبويب الحركة ---
    with tabs[2]:
        st.subheader("🏃 قسم حلول آلام الجسد")
        c5, c6 = st.columns(2)
        with c5:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            active_d = st.slider("أيام الرياضة أسبوعياً:", 0, 7, 2)
            back_p = st.radio("وجع الظهر والرقبة:", ["لا يوجد", "بسيط", "مزعج"])
            st.markdown('</div>', unsafe_allow_html=True)
        with c6:
            if active_d < 3:
                msg = "🛑 حل الخمول: قلة الحركة تقلل وصول الدم للمخ؛ اتمشى 15 دقيقة فقط يومياً لتجديد نشاطك."
                st.markdown(f'<div class="solution-card">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)
            if back_p != "لا يوجد":
                msg = "🛑 حل آلام الظهر: تأكد أن الشاشة في مستوى عينك، ولا تذاكر منبطحاً على السرير أبداً."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)

    # --- تبويب التغذية ---
    with tabs[3]:
        st.subheader("🍎 قسم حلول الغذاء والتركيز")
        c7, c8 = st.columns(2)
        with c7:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            junk_f = st.checkbox("بتعتمد على الوجبات السريعة كتير؟")
            sugar_high = st.toggle("بتاكل سكريات/حلويات كتير وأنت بتذاكر؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with c8:
            if junk_f:
                msg = "🛑 حل الوجبات السريعة: الدهون المشبعة تسبب خمولاً ذهنياً؛ استبدلها بوجبة منزلية غنية بالألياف."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)
            if sugar_high:
                msg = "🛑 حل السكر: السكر يرفع الطاقة ثم يسقطها (Sugar Crash)؛ ركز على المكسرات كوقود للمخ."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)

    # --- تبويب الحالة النفسية ---
    with tabs[4]:
        st.subheader("🧠 قسم حلول التسويف والقلق")
        c9, c10 = st.columns(2)
        with c9:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            procrastinate = st.checkbox("بتأجل المذاكرة للوقت الضايع؟")
            stress_level = st.select_slider("قلق الامتحانات:", options=["هادئ", "قلق", "توتر شديد"])
            st.markdown('</div>', unsafe_allow_html=True)
        with c10:
            if procrastinate:
                msg = "🛑 حل التسويف: استخدم قاعدة (الـ 5 دقائق)؛ ابدأ المذاكرة لمدة 5 دقائق فقط وسيكمل مخك الباقي."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)
            if stress_level == "توتر شديد":
                msg = "🛑 حل التوتر: جرب تمرين التنفس (Box Breathing) 4 ثواني شهيق - 4 كتم - 4 زفير."
                st.markdown(f'<div class="solution-box">{msg}</div>', unsafe_allow_html=True)
                user_solutions.append(msg)

    # --- تبويب التقرير النهائي ---
    with tabs[5]:
        st.markdown(f"## 📄 التقرير الصحي المتكامل للطالب: {name}")
        
        # تجميع نص التقرير
        full_report = f"تقرير موسوعة Health Student\n"
        full_report += f"الاسم: {name}\n"
        full_report += f"التاريخ: {datetime.now().strftime('%Y-%m-%d')}\n"
        full_report += "-------------------------------------------\n"
        full_report += f"- ساعات النوم: {s_hours} ساعة\n"
        full_report += f"- ساعات استخدام الموبايل: {p_hours} ساعة\n"
        full_report += f"- أكواب الماء المسجلة: {st.session_state.water}\n"
        full_report += "-------------------------------------------\n"
        full_report += "📌 الروشتة والحلول المقترحة لك:\n"
        
        if not user_solutions:
            full_report += "✅ عاداتك ممتازة، لا توجد مشاكل ملحوظة حالياً. استمر!"
        else:
            for i, s in enumerate(user_solutions, 1):
                full_report += f"{i}. {s}\n"
        
        # عرض التقرير في الموقع
        st.text_area("معاينة التقرير:", full_report, height=300)
        
        # زر التحميل
        st.download_button(
            label="📥 اضغط هنا لتحميل تقريرك (Text/PDF Ready)",
            data=full_report,
            file_name=f"Health_Report_{name}.txt",
            mime="text/plain"
        )
        st.balloons()