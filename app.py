import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. إعدادات المنصة
st.set_page_config(page_title="Health Student | الموسوعة الذكية", page_icon="🎓", layout="wide")

# 2. تصميم CSS احترافي (لحل مشكلة الخطوط والألوان وعرض الأرقام)
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
    .slider-val {
        background: #2563eb; color: white; padding: 5px 15px; 
        border-radius: 10px; font-weight: bold; font-size: 22px;
    }
    .solution-box {
        background: #fff7ed; border-right: 6px solid #f97316;
        padding: 15px; border-radius: 10px; margin-top: 10px; color: #9a3412; font-weight: bold;
    }
    .water-msg {
        padding: 15px; border-radius: 12px; margin-top: 10px; 
        font-weight: bold; text-align: center; border: 1px solid rgba(0,0,0,0.1);
    }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية الشاملة لحلول مشاكل الطلاب</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية (عداد المياه الذكي - كما في الصورة 9372.jpg)
with st.sidebar:
    st.header("💧 عداد المياه اللحظي")
    if 'water_count' not in st.session_state: 
        st.session_state.water_count = 0
    
    st.subheader(f"كؤوس الماء: {st.session_state.water_count}")
    
    # منطق الرسائل المتغيرة بناءً على عدد الكؤوس
    if st.session_state.water_count <= 2:
        msg, bg, txt = "⚠️ تحذير: مستوى الترطيب منخفض!", "#fee2e2", "#991b1b"
    elif 3 <= st.session_state.water_count <= 5:
        msg, bg, txt = "🥤 بداية جيدة ولكن استمر!", "#fef3c7", "#92400e"
    elif 6 <= st.session_state.water_count <= 8:
        msg, bg, txt = "✨ رائع! أنت في منطقة الأمان.", "#dcfce7", "#166534"
    else:
        msg, bg, txt = "👑 بطل الترطيب! نشاطك في القمة.", "#e0f2fe", "#075985"

    st.markdown(f'<div class="water-msg" style="background-color: {bg}; color: {txt};">{msg}</div>', unsafe_allow_html=True)
    if st.button("🥤 سجل كوب مياه"):
        st.session_state.water_count += 1
        st.rerun()
    if st.button("🔄 تصفير العداد"):
        st.session_state.water_count = 0
        st.rerun()

# 5. منطقة تسجيل الدخول (لحل مشكلة الصورة e7850cf4)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    name_input = st.text_input("📝 اكتب اسمك هنا لفتح أقسام الموسوعة:", placeholder="مثلاً: أحمد محمود...")
    if name_input:
        if st.button("دخول للموسوعة 🚀"):
            st.session_state.logged_in = True
            st.session_state.user_name = name_input
            st.rerun()
    st.info("💡 بعد كتابة الاسم، اضغط على زر 'دخول للموسوعة' ليظهر لك المحتوى.")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. عرض المحتوى بعد الدخول
else:
    final_solutions = []
    u_name = st.session_state.user_name
    
    st.success(f"مرحباً بك يا {u_name}! يمكنك الآن التنقل بين الأقسام.")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🌙 النوم", "📱 التكنولوجيا", "🏃 الحركة", "🍎 التغذية", "🧠 النفسية", "📥 التقرير"])

    # --- تبويب النوم (حل مشكلة السلايدر والصورة b286d8a6) ---
    with tab1:
        st.markdown("### 😴 قسم حلول جودة النوم")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            s_hours = st.slider("ساعات نومك الفعلية:", 2, 12, 7, key="slp_sld")
            st.markdown(f"الساعات: <span class='slider-val'>{s_hours}</span>", unsafe_allow_html=True)
            st.write("---")
            st.write("**هل تواجه صعوبة في الاستيقاظ؟**")
            s_yes = st.checkbox("نعم (Yes)", key="s_y")
            s_no = st.checkbox("لا (No)", key="s_n")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if s_hours < 7:
                sol = "🛑 حل نقص النوم: نومك أقل من 8 ساعات. حاول النوم قبل 11 مساءً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if s_yes:
                sol = "🛑 حل خمول الاستيقاظ: تعرض لضوء الشمس فور الاستيقاظ لضبط ساعتك البيولوجية."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التكنولوجيا (حل مشكلة السلايدر - الصورة 9359.jpg) ---
    with tab2:
        st.markdown("### 📱 حلول إجهاد العين والتشتت")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            p_hours = st.slider("ساعات استخدام الهاتف يومياً:", 1, 16, 5, key="tch_sld")
            st.markdown(f"الساعات: <span class='slider-val'>{p_hours}</span>", unsafe_allow_html=True)
            st.write("---")
            st.write("**هل تعاني من جفاف العين أو ضبابية الرؤية؟**")
            eye_yes = st.checkbox("نعم (Yes)", key="e_y")
            eye_no = st.checkbox("لا (No)", key="e_n")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if eye_yes:
                sol = "🛑 حل إجهاد العين: طبق قاعدة 20-20-20 لراحة عينيك."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if p_hours > 6:
                sol = "🛑 حل الإدمان الرقمي: وقت الشاشة مرتفع جداً. استخدم نمط التركيز."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب الحركة ---
    with tab3:
        st.markdown("### 🏃 آلام الظهر والرقبة")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تشعر بألم في الرقبة بسبب المذاكرة؟**")
            back_yes = st.checkbox("نعم (Yes)", key="b_y")
            back_no = st.checkbox("لا (No)", key="b_n")
            sitting = st.number_input("ساعات الجلوس المتواصل:", 1, 10, 3)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if back_yes:
                sol = "🛑 حل آلام الرقبة: اجعل شاشة جهازك في مستوى عينك دائماً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التغذية ---
    with tab4:
        st.markdown("### 🍎 وقود الدماغ")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تعتمد على الوجبات السريعة؟**")
            food_yes = st.checkbox("نعم (Yes)", key="f_y")
            st.write("**هل تتناول سكريات بكثرة؟**")
            sug_yes = st.checkbox("نعم (Yes)", key="su_y")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if sug_yes:
                sol = "🛑 حل هبوط الطاقة: السكر يسبب خمولاً مفاجئاً. استبدله بالفاكهة أو المكسرات."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب الحالة النفسية ---
    with tab5:
        st.markdown("### 🧠 حلول التسويف")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تؤجل مهامك لآخر وقت؟**")
            proc_yes = st.checkbox("نعم (Yes)", key="p_y")
            stress = st.select_slider("مستوى القلق العام:", options=["هادئ", "متوتر", "منهار"])
            st.markdown(f"الحالة: <span class='slider-val'>{stress}</span>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if proc_yes:
                sol = "🛑 حل التسويف: استخدم تقنية بومودورو (25 دقيقة مذاكرة و 5 دقائق راحة)."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التقرير النهائي ---
    with tab6:
        st.markdown(f"## 📄 التقرير النهائي لـ: {u_name}")
        report = f"تقرير Health Student\nالاسم: {u_name}\nكؤوس الماء: {st.session_state.water_count}\n"
        report += "-------------------------------------------\n📌 الروشتة المخصصة:\n"
        for i, s in enumerate(final_solutions, 1): report += f"{i}. {s}\n"
        
        st.text_area("معاينة التقرير:", report, height=250)
        st.download_button("📥 تحميل التقرير", report, file_name=f"Report_{u_name}.txt")
        if st.button("🚪 تسجيل الخروج"):
            st.session_state.logged_in = False
            st.rerun()
        st.balloons()
