import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. إعدادات المنصة لضمان التوافق مع الموبايل والكمبيوتر
st.set_page_config(page_title="Health Student | الموسوعة الذكية", page_icon="🎓", layout="wide")

# 2. تصميم CSS احترافي (تنسيق العناوين، البطاقات، وأرقام السلايدر)
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
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px;
        border-right: 8px solid #2563eb;
    }
    .slider-val {
        background: #2563eb; color: white; padding: 5px 15px; 
        border-radius: 10px; font-weight: bold; font-size: 22px; display: inline-block;
    }
    .solution-box {
        background: #fff7ed; border-right: 6px solid #f97316;
        padding: 15px; border-radius: 10px; margin-top: 10px; color: #9a3412; font-weight: bold;
    }
    .water-msg {
        padding: 15px; border-radius: 12px; margin-top: 10px; 
        font-weight: bold; text-align: center; border: 1px solid rgba(0,0,0,0.1);
    }
    /* تنسيق زر الدخول ليكون واضحاً */
    .stButton>button { width: 100%; border-radius: 12px; height: 50px; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

# 3. تهيئة حالة الجلسة (Session State) لضمان عدم ضياع البيانات
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'water_count' not in st.session_state:
    st.session_state.water_count = 0

# 4. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية الشاملة لحلول مشاكل الطلاب</p></div>', unsafe_allow_html=True)

# 5. القائمة الجانبية (عداد المياه اللحظي - متاح دائماً بعد الدخول)
if st.session_state.logged_in:
    with st.sidebar:
        st.header("💧 عداد المياه اللحظي")
        st.subheader(f"كؤوس الماء: {st.session_state.water_count}")
        
        # منطق الرسائل المتغيرة بناءً على عدد الكؤوس
        count = st.session_state.water_count
        if count <= 2:
            msg, bg, txt = "⚠️ تحذير: مستوى الترطيب منخفض جداً!", "#fee2e2", "#991b1b"
        elif 3 <= count <= 5:
            msg, bg, txt = "🥤 بداية جيدة ولكن غير كافية!", "#fef3c7", "#92400e"
        elif 6 <= count <= 8:
            msg, bg, txt = "✨ ممتاز! هذا هو المستوى المثالي.", "#dcfce7", "#166534"
        else:
            msg, bg, txt = "👑 بطل الترطيب! أنت في قمة النشاط.", "#e0f2fe", "#075985"

        st.markdown(f'<div class="water-msg" style="background-color: {bg}; color: {txt};">{msg}</div>', unsafe_allow_html=True)
        if st.button("🥤 سجل كوب مياه"):
            st.session_state.water_count += 1
            st.rerun()
        if st.button("🔄 تصفير العداد"):
            st.session_state.water_count = 0
            st.rerun()

# 6. شاشة الدخول (باستخدام Form لضمان ظهور الزرار فوراً)
if not st.session_state.logged_in:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📝 ابدأ بكتابة اسمك لفتح الموسوعة:")
    with st.form("login_form"):
        name_input = st.text_input("اسم الطالب:", placeholder="اكتب اسمك هنا...")
        submit = st.form_submit_button("دخول للموسوعة 🚀")
        if submit:
            if name_input.strip() != "":
                st.session_state.logged_in = True
                st.session_state.user_name = name_input
                st.rerun()
            else:
                st.error("الرجاء كتابة الاسم أولاً!")
    st.markdown('</div>', unsafe_allow_html=True)

# 7. عرض محتوى الموسوعة بعد الدخول
else:
    u_name = st.session_state.user_name
    final_solutions = []
    
    st.success(f"مرحباً بك يا {u_name}! تم تفعيل الموسوعة والحلول.")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌙 النوم", "📱 التكنولوجيا", "🏃 الحركة", "🍎 التغذية", "🧠 النفسية", "📥 التقرير"
    ])

    # --- تبويب النوم ---
    with tab1:
        st.markdown("### 😴 حلول جودة النوم")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            s_hours = st.slider("ساعات نومك الفعلية:", 2, 12, 7, key="s_hours")
            st.markdown(f"القيمة المختارة: <span class='slider-val'>{s_hours}</span>", unsafe_allow_html=True)
            st.write("---")
            st.write("**هل تواجه صعوبة في الاستيقاظ؟**")
            s_y = st.checkbox("نعم (Yes)", key="s_y")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if s_hours < 7:
                sol = "🛑 حل نقص النوم: نومك أقل من الاحتياج. نم قبل 11 مساءً."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if s_y:
                sol = "🛑 حل خمول الاستيقاظ: تعرض لضوء الشمس فور استيقاظك."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التكنولوجيا ---
    with tab2:
        st.markdown("### 📱 حلول إجهاد العين")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            p_hours = st.slider("ساعات الهاتف يومياً:", 1, 16, 5, key="p_hours")
            st.markdown(f"القيمة المختارة: <span class='slider-val'>{p_hours}</span>", unsafe_allow_html=True)
            st.write("---")
            st.write("**هل تعاني من جفاف العين؟**")
            e_y = st.checkbox("نعم (Yes)", key="e_y")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if e_y:
                sol = "🛑 حل إجهاد العين: طبق قاعدة 20-20-20 لراحة عينيك."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)
            if p_hours > 6:
                sol = "🛑 حل التشتت: وقت الشاشة مرتفع. استخدم نمط التركيز."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب الحركة ---
    with tab3:
        st.markdown("### 🏃 حلول آلام الجسم")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تشعر بألم في الرقبة؟**")
            b_y = st.checkbox("نعم (Yes)", key="b_y")
            st.write("---")
            sitting = st.number_input("ساعات الجلوس المتواصل:", 1, 10, 3)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if b_y:
                sol = "🛑 حل آلام الرقبة: اضبط ارتفاع شاشتك ليكون في مستوى العين."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التغذية ---
    with tab4:
        st.markdown("### 🍎 وقود الدماغ")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write("**هل تتناول سكريات بكثرة؟**")
            su_y = st.checkbox("نعم (Yes)", key="su_y")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if su_y:
                sol = "🛑 حل الطاقة: استبدل السكر بالمكسرات لتجنب الخمول المفاجئ."
                st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True); final_solutions.append(sol)

    # --- تبويب التقرير ---
    with tab6:
        st.markdown(f"## 📄 التقرير الشامل: {u_name}")
        report = f"تقرير موسوعة Health Student\nالاسم: {u_name}\nكؤوس الماء: {st.session_state.water_count}\n"
        report += "-------------------------------------------\n📌 الروشتة المخصصة:\n"
        if final_solutions:
            for i, s in enumerate(final_solutions, 1): report += f"{i}. {s}\n"
        else:
            report += "✅ عاداتك رائعة جداً! استمر."
        
        st.text_area("معاينة التقرير:", report, height=250)
        st.download_button("📥 تحميل التقرير", report, file_name=f"Report_{u_name}.txt")
        if st.button("🚪 تسجيل الخروج"):
            st.session_state.logged_in = False
            st.rerun()
        st.balloons()
