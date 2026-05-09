import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 1. إعدادات المنصة (تجعل الموقع متوافق مع الموبايل والكمبيوتر)
st.set_page_config(page_title="Health Student | الموسوعة الذكية", page_icon="🎓", layout="wide")

# 2. تصميم CSS احترافي (تنسيق الألوان والبطاقات)
st.markdown("""
    <style>
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
        padding: 15px; border-radius: 10px; margin-top: 10px; color: #9a3412;
    }
    .success-box {
        background: #f0fdf4; border-right: 6px solid #22c55e;
        padding: 15px; border-radius: 10px; margin-top: 10px; color: #166534;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية الشاملة لحلول مشاكل الطلاب</p></div>', unsafe_allow_html=True)

# 4. إدخال الاسم (تم نقله هنا ليظهر فوراً على الموبايل)
name = st.text_input("📝 ابدأ بكتابة اسمك لفتح الموسوعة والحلول:", placeholder="اكتب اسمك هنا...")

if not name:
    st.info("👆 يرجى كتابة اسمك في الخانة أعلاه لتظهر لك أقسام الموسوعة والتقرير النهائي.")
    
    # إضافة لمسة تفاعلية في القائمة الجانبية حتى قبل كتابة الاسم
    with st.sidebar:
        st.header("💧 عداد المياه اللحظي")
        if 'water_count' not in st.session_state: st.session_state.water_count = 0
        st.subheader(f"كؤوس الماء: {st.session_state.water_count}")
        if st.button("🥤 سجل كوب مياه"):
            st.session_state.water_count += 1
            st.toast("ممتاز! الترطيب ينعش عقلك 💧")
else:
    # قائمة لتخزين كافة الحلول المقترحة للتقرير
    final_solutions = []

    # 5. التبويبات التفاعلية (Tabs)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌙 النوم والتركيز", 
        "📱 التكنولوجيا", 
        "🏃 الحركة والآلام", 
        "🍎 التغذية والدماغ", 
        "🧠 الحالة النفسية", 
        "📥 تحميل التقرير"
    ])

    # --- تبويب النوم ---
    with tab1:
        st.markdown("### 😴 قسم حلول جودة النوم")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            s_hours = st.slider("ساعات نومك الفعلية:", 2, 12, 7)
            s_difficulty = st.radio("هل تواجه صعوبة في الاستيقاظ؟", ["نعم، دائماً", "أحياناً", "لا، أصحو بنشاط"])
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if s_hours < 7:
                sol = "🛑 حل نقص النوم: نومك أقل من الاحتياج البيولوجي (8 ساعات). الحل هو النوم قبل 11 مساءً لتعويض هرمونات النمو والتركيز."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if s_difficulty == "نعم، دائماً":
                sol = "🛑 حل خمول الاستيقاظ: جسمك يمر بـ 'قصور ذاتي للنوم'. الحل هو التعرض لضوء الشمس فور الاستيقاظ لمدة 5 دقائق لضبط الساعة البيولوجية."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب التكنولوجيا ---
    with tab2:
        st.markdown("### 📱 حلول إجهاد العين والتشتت")
        col3, col4 = st.columns(2)
        with col3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            p_hours = st.slider("ساعات استخدام الهاتف يومياً:", 1, 16, 5)
            eye_dry = st.checkbox("هل تعاني من جفاف العين أو ضبابية الرؤية؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with col4:
            if eye_dry:
                sol = "🛑 حل إجهاد العين: طبق قاعدة 20-20-20 (كل 20 دقيقة مذاكرة، انظر لشيء بعيد 20 قدم لمدة 20 ثانية) واستخدم قطرة مرطبة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if p_hours > 6:
                sol = "🛑 حل الإدمان الرقمي: وقت الشاشة مرتفع جداً. الحل هو تفعيل 'نمط التركيز' وحذف تطبيقات السوشيال ميديا وقت الامتحانات."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب الحركة ---
    with tab3:
        st.markdown("### 🏃 حلول آلام الظهر والرقبة")
        col5, col6 = st.columns(2)
        with col5:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            back_p = st.radio("هل تشعر بألم في الرقبة بسبب المذاكرة؟", ["لا يوجد", "بسيط", "شديد"])
            sitting = st.number_input("ساعات الجلوس المتواصل:", 1, 10, 3)
            st.markdown('</div>', unsafe_allow_html=True)
        with col6:
            if back_p != "لا يوجد":
                sol = "🛑 حل آلام الرقبة: تأكد أن حافة اللابتوب العلوية في مستوى عينك. تجنب المذاكرة منحنياً فوق المكتب."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if sitting > 2:
                sol = "🛑 حل الجلوس الطويل: يسبب ركود الدم. الحل هو الوقوف وعمل تمارين إطالة بسيطة (Stretching) كل 45 دقيقة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب التغذية ---
    with tab4:
        st.markdown("### 🍎 وقود الدماغ والتركيز")
        col7, col8 = st.columns(2)
        with col7:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            fast_food = st.checkbox("هل تعتمد على الوجبات السريعة؟")
            sugar = st.toggle("هل تتناول سكريات بكثرة أثناء المذاكرة؟")
            st.markdown('</div>', unsafe_allow_html=True)
        with col8:
            if sugar:
                sol = "🛑 حل هبوط الطاقة: السكر يسبب (Sugar Crash) بعد ساعة. استبدله بالمكسرات أو زبدة الفول السوداني لطاقة مستدامة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if fast_food:
                sol = "🛑 حل الخمول الغذائي: الوجبات السريعة مليئة بالدهون التي تسبب النعاس. الحل هو التركيز على البروتين (بيض/تونة) لزيادة اليقظة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب الحالة النفسية ---
    with tab5:
        st.markdown("### 🧠 حلول التسويف والتوتر")
        col9, col10 = st.columns(2)
        with col9:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            procrast = st.radio("هل تؤجل مهامك لآخر وقت؟", ["دائماً", "أحياناً", "نادراً"])
            stress = st.select_slider("مستوى القلق العام:", options=["هادئ", "متوتر", "منهار"])
            st.markdown('</div>', unsafe_allow_html=True)
        with col10:
            if procrast == "دائماً":
                sol = "🛑 حل التسويف: استخدم تقنية 'بومودورو' (25 دقيقة مذاكرة - 5 دقائق راحة). ابدأ بأصعب مهمة في أول اليوم."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)
            if stress == "منهار":
                sol = "🛑 حل التوتر الشديد: جرب تمرين التنفس المربع (شهيق 4 - كتم 4 - زفير 4 - كتم 4) لتهدئة الجهاز العصبي فوراً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
                final_solutions.append(sol)

    # --- تبويب التقرير النهائي (تحميل PDF/Text) ---
    with tab6:
        st.markdown(f"## 📄 التقرير الصحي الشامل للطالب: {name}")
        st.write(f"تاريخ الإصدار: {datetime.now().strftime('%Y-%m-%d')}")
        
        # تجميع التقرير النهائي
        report_content = f"تقرير موسوعة Health Student\n"
        report_content += f"اسم الطالب: {name}\n"
        report_content += f"-------------------------------------------\n"
        report_content += f"• ساعات النوم: {s_hours} ساعة\n"
        report_content += f"• ساعات الهاتف: {p_hours} ساعة\n"
        report_content += f"• كؤوس الماء: {st.session_state.get('water_count', 0)}\n"
        report_content += f"-------------------------------------------\n"
        report_content += "📌 الروشتة المخصصة والحلول:\n\n"
        
        if not final_solutions:
            report_content += "✅ عاداتك رائعة جداً! استمر على هذا المنوال."
        else:
            for i, s in enumerate(final_solutions, 1):
                report_content += f"{i}. {s}\n\n"
        
        st.text_area("معاينة التقرير:", report_content, height=350)
        
        # زر التحميل التفاعلي
        st.download_button(
            label="📥 اضغط هنا لتحميل تقريرك كملف نصي (جاهز للطباعة)",
            data=report_content,
            file_name=f"Report_{name}.txt",
            mime="text/plain"
        )
        st.balloons()