import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 1. إعدادات المنصة
st.set_page_config(page_title="Health Student | الموسوعة الذكية", page_icon="🎓", layout="wide")

# 2. تصميم CSS احترافي
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    * { font-family: 'Tajawal', sans-serif; direction: rtl; }
    .stApp { background-color: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        padding: 40px; border-radius: 20px; text-align: center; color: white; margin-bottom: 25px;
    }
    .card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 20px;
        border-right: 8px solid #2563eb;
    }
    .solution-box {
        background: #fff7ed; border-right: 6px solid #f97316;
        padding: 15px; border-radius: 10px; margin-top: 10px; color: #9a3412; font-weight: bold;
    }
    .water-msg {
        padding: 15px; border-radius: 12px; margin-top: 10px; 
        font-weight: bold; text-align: center; border: 1px solid rgba(0,0,0,0.1);
    }
    /* تحسين شكل الـ checkbox ليناسب التصميم */
    .stCheckbox { margin-bottom: -15px; }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية الشاملة لحلول مشاكل الطلاب</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية (عداد المياه الذكي المعدل)
with st.sidebar:
    st.header("💧 عداد المياه اللحظي")
    if 'water_count' not in st.session_state: 
        st.session_state.water_count = 0
    
    st.subheader(f"كؤوس الماء: {st.session_state.water_count}")
    
    # منطق الرسائل المتغيرة بناءً على عدد الكؤوس
    if st.session_state.water_count <= 2:
        msg, bg, txt = "⚠️ تحذير: مستوى الترطيب منخفض جداً! اشرب الآن لزيادة تركيزك.", "#fee2e2", "#991b1b"
    elif 3 <= st.session_state.water_count <= 5:
        msg, bg, txt = "🥤 بداية جيدة ولكن غير كافية! جسمك يحتاج المزيد ليصل للأداء المثالي.", "#fef3c7", "#92400e"
    elif 6 <= st.session_state.water_count <= 8:
        msg, bg, txt = "✨ ممتاز! هذا هو المستوى المثالي لنشاط الخلايا العصبية.", "#dcfce7", "#166534"
    else:
        msg, bg, txt = "👑 بطل الترطيب! أنت الآن في قمة الصفاء الذهني والنشاط.", "#e0f2fe", "#075985"

    st.markdown(f'<div class="water-msg" style="background-color: {bg}; color: {txt};">{msg}</div>', unsafe_allow_html=True)
    
    if st.button("🥤 سجل كوب مياه"):
        st.session_state.water_count += 1
        st.rerun()
    
    if st.button("🔄 تصفير العداد"):
        st.session_state.water_count = 0
        st.rerun()

# 5. إدخال الاسم
name = st.text_input("📝 ابدأ بكتابة اسمك لفتح الموسوعة والحلول:", placeholder="اكتب اسمك هنا...")

if not name:
    st.warning("👆 يرجى كتابة اسمك في الخانة أعلاه لتظهر لك أقسام الموسوعة والتقرير النهائي.")
else:
    final_solutions = []

    # 6. التبويبات التفاعلية (Tabs)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌙 النوم والتركيز", "📱 التكنولوجيا", "🏃 الحركة والآلام", 
        "🍎 التغذية والدماغ", "🧠 الحالة النفسية", "📥 تحميل التقرير"
    ])

    # --- تبويب النوم ---
    with tab1:
        st.markdown("### 😴 قسم حلول جودة النوم")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            s_hours = st.slider("ساعات نومك الفعلية:", 2, 12, 7)
            st.write("---")
            st.write("**هل تواجه صعوبة في الاستيقاظ؟**")
            s_yes = st.checkbox("نعم (Yes)", key="sleep_y")
            s_no = st.checkbox("لا (No)", key="sleep_n")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if s_hours < 7:
                sol = "🛑 حل نقص النوم: نومك أقل من الاحتياج البيولوجي (8 ساعات). الحل هو النوم قبل 11 مساءً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if s_yes:
                sol = "🛑 حل خمول الاستيقاظ: تعرض لضوء الشمس فور الاستيقاظ لمدة 5 دقائق لضبط الساعة البيولوجية."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب التكنولوجيا ---
    with tab2:
        st.markdown("### 📱 حلول إجهاد العين والتشتت")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            p_hours = st.slider("ساعات استخدام الهاتف يومياً:", 1, 16, 5)
            st.write("---")
            st.write("**هل تعاني من جفاف العين أو ضبابية الرؤية؟**")
            eye_yes = st.checkbox("نعم (Yes)", key="eye_y")
            eye_no = st.checkbox("لا (No)", key="eye_n")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if eye_yes:
                sol = "🛑 حل إجهاد العين: طبق قاعدة 20-20-20 (كل 20 دقيقة مذاكرة، انظر لشيء بعيد 20 قدم لمدة 20 ثانية)."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if p_hours > 6:
                sol = "🛑 حل الإدمان الرقمي: وقت الشاشة مرتفع. الحل هو تفعيل 'نمط التركيز' وقت المذاكرة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب الحركة ---
    with tab3:
        st.markdown("### 🏃 حلول آلام الظهر والرقبة")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تشعر بألم في الرقبة بسبب المذاكرة؟**")
            back_yes = st.checkbox("نعم (Yes)", key="back_y")
            back_no = st.checkbox("لا (No)", key="back_n")
            st.write("---")
            sitting = st.number_input("ساعات الجلوس المتواصل:", 1, 10, 3)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if back_yes:
                sol = "🛑 حل آلام الرقبة: تأكد أن حافة اللابتوب العلوية في مستوى عينك. لا تذاكر منحنياً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if sitting > 2:
                sol = "🛑 حل الجلوس الطويل: يسبب ركود الدم. الحل هو الوقوف وعمل تمارين إطالة كل 45 دقيقة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب التغذية ---
    with tab4:
        st.markdown("### 🍎 وقود الدماغ والتركيز")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تعتمد على الوجبات السريعة؟**")
            food_yes = st.checkbox("نعم (Yes)", key="food_y")
            food_no = st.checkbox("لا (No)", key="food_n")
            st.write("---")
            st.write("**هل تتناول سكريات بكثرة أثناء المذاكرة؟**")
            sug_yes = st.checkbox("نعم (Yes)", key="sug_y")
            sug_no = st.checkbox("لا (No)", key="sug_n")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if sug_yes:
                sol = "🛑 حل هبوط الطاقة: السكر يسبب Sugar Crash. استبدله بالمكسرات لطاقة مستدامة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if food_yes:
                sol = "🛑 حل الخمول الغذائي: الوجبات السريعة تسبب النعاس. ركز على البروتين لزيادة اليقظة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب الحالة النفسية ---
    with tab5:
        st.markdown("### 🧠 حلول التسويف والتوتر")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تؤجل مهامك لآخر وقت؟**")
            proc_yes = st.checkbox("نعم (Yes)", key="proc_y")
            proc_no = st.checkbox("لا (No)", key="proc_n")
            st.write("---")
            stress = st.select_slider("مستوى القلق العام:", options=["هادئ", "متوتر", "منهار"])
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if proc_yes:
                sol = "🛑 حل التسويف: استخدم تقنية بومودورو (25-5) وابدأ بأصعب مهمة فوراً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if stress == "منهار":
                sol = "🛑 حل التوتر الشديد: جرب تمرين التنفس المربع (4-4-4-4) لتهدئة الأعصاب."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب التقرير النهائي ---
    with tab6:
        st.markdown(f"## 📄 التقرير الصحي الشامل للطالب: {name}")
        report_content = f"تقرير موسوعة Health Student\n"
        report_content += f"اسم الطالب: {name}\n"
        report_content += f"تاريخ الإصدار: {datetime.now().strftime('%Y-%m-%d')}\n"
        report_content += f"-------------------------------------------\n"
        report_content += f"• كؤوس الماء المسجلة: {st.session_state.water_count}\n"
        report_content += f"• ساعات النوم: {s_hours} ساعة\n"
        report_content += f"-------------------------------------------\n"
        report_content += "📌 الروشتة المخصصة والحلول:\n\n"
        
        if not final_solutions:
            report_content += "✅ عاداتك رائعة جداً! استمر على هذا المنوال يا بطل."
        else:
            for i, s in enumerate(final_solutions, 1):
                report_content += f"{i}. {s}\n\n"
        
        st.text_area("معاينة التقرير:", report_content, height=300)
        st.download_button("📥 تحميل التقرير كملف نصي", report_content, file_name=f"Health_Report_{name}.txt")
        st.balloons()
