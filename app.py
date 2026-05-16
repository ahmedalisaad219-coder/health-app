import streamlit as st
from datetime import datetime

# 1. إعدادات المنصة
st.set_page_config(page_title="Health Student | الموسوعة الذكية", page_icon="🎓", layout="wide")

# 2. تصميم CSS احترافي وشامل
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
        padding: 10px; border-radius: 10px; text-align: center; font-weight: bold; margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. تهيئة Session State
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'water_count' not in st.session_state: st.session_state.water_count = 0

# 4. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية الشاملة لحلول مشاكل الطلاب</p></div>', unsafe_allow_html=True)

# 5. القائمة الجانبية (عداد المياه اللحظي)
with st.sidebar:
    st.header("💧 عداد المياه اللحظي")
    st.subheader(f"كؤوس الماء: {st.session_state.water_count}")
    
    # رسائل العداد المتغيرة
    if st.session_state.water_count <= 2:
        st.markdown('<div class="water-msg" style="background:#fee2e2; color:#991b1b;">⚠️ مستوى الترطيب منخفض!</div>', unsafe_allow_html=True)
    elif 3 <= st.session_state.water_count <= 5:
        st.markdown('<div class="water-msg" style="background:#fef3c7; color:#92400e;">🥤 استمر.. جسمك يحتاج المزيد!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="water-msg" style="background:#dcfce7; color:#166534;">👑 أحسنت! أنت في كامل نشاطك.</div>', unsafe_allow_html=True)
        
    if st.button("🥤 سجل كوب مياه"):
        st.session_state.water_count += 1
        st.rerun()
    if st.button("🔄 تصفير العداد"):
        st.session_state.water_count = 0
        st.rerun()

# 6. شاشة الدخول
if not st.session_state.logged_in:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📝 ابدأ بكتابة اسمك لفتح الموسوعة:")
    name_input = st.text_input("اسم الطالب:", placeholder="اكتب اسمك هنا...")
    if st.button("دخول للموسوعة 🚀"):
        if name_input.strip():
            st.session_state.logged_in = True
            st.session_state.user_name = name_input
            st.rerun()
        else:
            st.error("الرجاء كتابة الاسم أولاً!")
    st.markdown('</div>', unsafe_allow_html=True)

# 7. المحتوى الرئيسي بعد الدخول
else:
    final_solutions = []
    st.success(f"أهلاً بك يا {st.session_state.user_name}!")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌙 النوم", "📱 التكنولوجيا", "🏃 الحركة", "📥 التقرير"])

    # --- تبويب النوم ---
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        s_hours = st.slider("ساعات نومك الفعلية:", 2, 12, 7, key="sleep_slider")
        st.markdown(f"القيمة المختارة: <span class='slider-val'>{s_hours}</span>", unsafe_allow_html=True)
        st.write("---")
        st.write("**هل تواجه صعوبة في الاستيقاظ؟**")
        col1, col2 = st.columns(2)
        with col1:
            s_yes = st.checkbox("نعم (Yes)", key="s_y")
        with col2:
            s_no = st.checkbox("لا (No)", key="s_n")
        
        if s_hours < 7:
            sol = "🛑 حل نقص النوم: نم قبل الساعة 11 مساءً لتعويض احتياجك."
            st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
            final_solutions.append(sol)
        if s_yes:
            sol = "🛑 حل الاستيقاظ: تعرض لضوء الشمس فور استيقاظك."
            st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
            final_solutions.append(sol)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب التكنولوجيا ---
    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        p_hours = st.slider("ساعات استخدام الهاتف:", 1, 16, 5, key="tech_slider")
        st.markdown(f"الساعات: <span class='slider-val'>{p_hours}</span>", unsafe_allow_html=True)
        st.write("---")
        st.write("**هل تعاني من جفاف العين؟**")
        c1, c2 = st.columns(2)
        with c1:
            e_yes = st.checkbox("نعم (Yes)", key="e_y")
        with c2:
            e_no = st.checkbox("لا (No)", key="e_n")
            
        if e_yes:
            sol = "🛑 حل إجهاد العين: طبق قاعدة 20-20-20."
            st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
            final_solutions.append(sol)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب الحركة ---
    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**هل تشعر بألم في الرقبة؟**")
        back_col1, back_col2 = st.columns(2)
        with back_col1:
            b_yes = st.checkbox("نعم (Yes)", key="b_y")
        with back_col2:
            b_no = st.checkbox("لا (No)", key="b_n")
        
        if b_yes:
            sol = "🛑 حل آلام الرقبة: اضبط ارتفاع شاشتك ليكون في مستوى عينك."
            st.markdown(f'<div class="solution-box">{sol}</div>', unsafe_allow_html=True)
            final_solutions.append(sol)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب التقرير ---
    with tab4:
        st.markdown("### 📄 تقريرك الصحي")
        report = f"الاسم: {st.session_state.user_name}\nكؤوس الماء: {st.session_state.water_count}\n"
        report += "📌 التوصيات:\n" + ("\n".join(final_solutions) if final_solutions else "✅ عاداتك ممتازة!")
        st.text_area("ملخص الحالة:", report, height=200)
        st.download_button("📥 تحميل التقرير", report, file_name="Health_Report.txt")
        if st.button("🚪 تسجيل الخروج"):
            st.session_state.logged_in = False
            st.rerun()
        st.balloons()
