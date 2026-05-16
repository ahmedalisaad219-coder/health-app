import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. إعدادات المنصة (متوافق مع جميع الشاشات)
st.set_page_config(page_title="Health Student | الموسوعة الذكية", page_icon="🎓", layout="wide")

# 2. تصميم CSS احترافي (تنسيق الخطوط، الألوان، وعرض الأرقام)
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
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px;
        border-right: 8px solid #2563eb;
    }
    .slider-container {
        display: flex; align-items: center; justify-content:建设; gap: 20px; margin-bottom: 10px;
    }
    .slider-val {
        background: #2563eb; color: white; padding: 5px 15px; 
        border-radius: 10px; font-weight: bold; font-size: 22px; min-width: 50px; text-align: center;
    }
    .solution-box {
        background: #fff7ed; border-right: 6px solid #f97316;
        padding: 15px; border-radius: 10px; margin-top: 10px; color: #9a3412; font-weight: bold;
    }
    .water-msg {
        padding: 15px; border-radius: 12px; margin-top: 10px; 
        font-weight: bold; text-align: center; border: 1px solid rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية الشاملة لحلول مشاكل الطلاب</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية (عداد المياه الذكي برسائل متغيرة)
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

# 5. إدخال الاسم لفتح الموقع
name = st.text_input("📝 ابدأ بكتابة اسمك لفتح الموسوعة والحلول:", placeholder="اكتب اسمك هنا...")

if not name:
    st.warning("👆 يرجى كتابة اسمك في الخانة أعلاه لتظهر لك أقسام الموسوعة والتقرير النهائي.")
else:
    final_solutions = []

    # 6. التبويبات التفاعلية (Tabs)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌙 النوم", "📱 التكنولوجيا", "🏃 الحركة", 
        "🍎 التغذية", "🧠 النفسية", "📥 التقرير"
    ])

    # --- تبويب النوم (حل مشكلة ظهور رقم السلايدر) ---
    with tab1:
        st.markdown("### 😴 قسم حلول جودة النوم")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            s_hours = st.slider("ساعات نومك الفعلية:", 2, 12, 7, key="sleep_slider")
            st.markdown(f"<div class='slider-container'><span>القيمة المختارة:</span><span class='slider-val'>{s_hours}</span></div>", unsafe_allow_html=True)
            st.write("---")
            st.write("**هل تواجه صعوبة في الاستيقاظ؟**")
            s_yes = st.checkbox("نعم (Yes)", key="s_y_check")
            s_no = st.checkbox("لا (No)", key="s_n_check")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if s_hours < 7:
                sol = "🛑 حل نقص النوم: نومك أقل من الاحتياج (8 ساعات). الحل هو النوم قبل 11 مساءً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if s_yes:
                sol = "🛑 حل خمول الاستيقاظ: تعرض لضوء الشمس فور الاستيقاظ لضبط الساعة البيولوجية."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التكنولوجيا (حل مشكلة ظهور رقم السلايدر) ---
    with tab2:
        st.markdown("### 📱 حلول إجهاد العين والتشتت")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            p_hours = st.slider("ساعات استخدام الهاتف يومياً:", 1, 16, 5, key="tech_slider")
            st.markdown(f"<div class='slider-container'><span>الساعات الحالية:</span><span class='slider-val'>{p_hours}</span></div>", unsafe_allow_html=True)
            st.write("---")
            st.write("**هل تعاني من جفاف العين أو ضبابية الرؤية؟**")
            eye_yes = st.checkbox("نعم (Yes)", key="e_y_check")
            eye_no = st.checkbox("لا (No)", key="e_n_check")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if eye_yes:
                sol = "🛑 حل إجهاد العين: طبق قاعدة 20-20-20 (انظر بعيداً 20 قدم كل 20 دقيقة)."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if p_hours > 6:
                sol = "🛑 حل الإدمان الرقمي: وقت الشاشة مرتفع جداً. استخدم نمط التركيز."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب الحركة ---
    with tab3:
        st.markdown("### 🏃 حلول آلام الظهر والرقبة")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تشعر بألم في الرقبة بسبب المذاكرة؟**")
            back_yes = st.checkbox("نعم (Yes)", key="b_y_check")
            back_no = st.checkbox("لا (No)", key="b_n_check")
            st.write("---")
            sitting = st.number_input("ساعات الجلوس المتواصل:", 1, 10, 3)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if back_yes:
                sol = "🛑 حل آلام الرقبة: تأكد أن حافة اللابتوب العلوية في مستوى عينك."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if sitting > 2:
                sol = "🛑 حل الجلوس الطويل: قف وقم بتمارين إطالة بسيطة كل 45 دقيقة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التغذية ---
    with tab4:
        st.markdown("### 🍎 وقود الدماغ والتركيز")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تعتمد على الوجبات السريعة؟**")
            food_yes = st.checkbox("نعم (Yes)", key="f_y_check")
            food_no = st.checkbox("لا (No)", key="f_n_check")
            st.write("---")
            st.write("**هل تتناول سكريات بكثرة أثناء المذاكرة؟**")
            sug_yes = st.checkbox("نعم (Yes)", key="su_y_check")
            sug_no = st.checkbox("لا (No)", key="su_n_check")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if sug_yes:
                sol = "🛑 حل هبوط الطاقة: السكر يسبب Sugar Crash. استبدله بالمكسرات."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if food_yes:
                sol = "🛑 حل الخمول الغذائي: البروتين يزيد اليقظة عكس الوجبات السريعة."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب الحالة النفسية ---
    with tab5:
        st.markdown("### 🧠 حلول التسويف والتوتر")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تؤجل مهامك لآخر وقت؟**")
            proc_yes = st.checkbox("نعم (Yes)", key="p_y_check")
            proc_no = st.checkbox("لا (No)", key="p_n_check")
            st.write("---")
            stress = st.select_slider("مستوى القلق العام:", options=["هادئ", "متوتر", "منهار"])
            st.markdown(f"<div class='slider-container'><span>الحالة:</span><span class='slider-val'>{stress}</span></div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if proc_yes:
                sol = "🛑 حل التسويف: استخدم تقنية بومودورو وابدأ بأصعب مهمة فوراً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if stress == "منهار":
                sol = "🛑 حل التوتر الشديد: جرب تمرين التنفس المربع لتهدئة الأعصاب."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التقرير النهائي ---
    with tab6:
        st.markdown(f"## 📄 التقرير الشامل للطالب: {name}")
        report_content = f"تقرير موسوعة Health Student\nالاسم: {name}\nكؤوس الماء: {st.session_state.water_count}\n"
        report_content += f"ساعات النوم: {s_hours}\nساعات الهاتف: {p_hours}\n"
        report_content += "-------------------------------------------\n📌 الروشتة والحلول:\n"
        for i, s in enumerate(final_solutions, 1): report_content += f"{i}. {s}\n"
        
        st.text_area("معاينة التقرير:", report_content, height=250)
        st.download_button("📥 تحميل التقرير كملف نصي", report_content, file_name=f"Report_{name}.txt")
        st.balloons()
