import streamlit as st

# 1. إعدادات المنصة والتنسيق لضمان ثبات الواجهة
st.set_page_config(page_title="Health Student Encyclopedia", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    * { font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right; }
    .stApp { background-color: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        padding: 30px; border-radius: 20px; text-align: center; color: white; margin-bottom: 25px;
    }
    .card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); margin-bottom: 20px;
        border-right: 8px solid #2563eb;
    }
    .solution-box {
        background: #fff7ed; border-right: 6px solid #f97316;
        padding: 15px; border-radius: 10px; margin-top: 15px; color: #9a3412; font-weight: bold;
    }
    .slider-val {
        background: #2563eb; color: white; padding: 5px 15px; 
        border-radius: 10px; font-weight: bold; font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. إدارة الحالة (لضمان بقاء المستخدم مسجلاً)
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'water' not in st.session_state: st.session_state.water = 0

# 3. القائمة الجانبية (عداد المياه اللحظي) -
with st.sidebar:
    st.header("💧 عداد المياه اللحظي")
    st.subheader(f"كؤوس الماء: {st.session_state.water}")
    if st.button("🥤 سجل كوب مياه"):
        st.session_state.water += 1
        st.rerun()
    if st.button("🔄 تصفير"):
        st.session_state.water = 0
        st.rerun()

# 4. شاشة الدخول -
if not st.session_state.logged_in:
    st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية الشاملة لحلول مشاكل الطلاب</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    name = st.text_input("📝 اكتب اسمك هنا لفتح الموسوعة والحلول:", placeholder="مثال: أحمد محمود...")
    if st.button("دخول للموسوعة 🚀") and name:
        st.session_state.logged_in = True
        st.session_state.u_name = name
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 5. محتوى الموسوعة (التبويبات مرتبة ومنفصلة)
else:
    st.markdown(f'<div class="main-header"><h1>🎓 موسوعة {st.session_state.u_name} الصحية</h1></div>', unsafe_allow_html=True)
    
    # تعريف التبويبات بالكامل -
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌙 النوم والتركيز", "📱 التكنولوجيا", "🏃 الحركة والآلام", "🍎 التغذية والدماغ", "🧠 الحالة النفسية", "📥 التقرير النهائي"
    ])

    # --- تبويب النوم والتركيز ---
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        s_hours = st.slider("ساعات نومك الفعلية:", 2, 12, 7, key="sl_sleep")
        st.markdown(f"المختار: <span class='slider-val'>{s_hours}</span>", unsafe_allow_html=True)
        st.write("**هل تواجه صعوبة في الاستيقاظ؟**")
        c1, c2 = st.columns(2)
        with c1: s_yes = st.checkbox("نعم (Yes)", key="s_y") #
        with c2: s_no = st.checkbox("لا (No)", key="s_n")
        
        if s_hours < 7:
            st.markdown('<div class="solution-box">🛑 حل نقص النوم: نومك غير كافٍ (أقل من 8 ساعات). حاول النوم مبكراً لضمان تركيزك الدراسي غداً.</div>', unsafe_allow_html=True)
        if s_yes:
            st.markdown('<div class="solution-box">🛑 حل خمول الاستيقاظ: تعرض لضوء الشمس فور استيقاظك لضبط ساعتك البيولوجية فوراً.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب التكنولوجيا ---
    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        p_hours = st.slider("ساعات الموبايل يومياً:", 1, 16, 5, key="sl_tech")
        st.write("**هل تعاني من جفاف العين أو ضبابية الرؤية؟**")
        t1, t2 = st.columns(2)
        with t1: e_yes = st.checkbox("نعم (Yes)", key="e_y") #
        with t2: e_no = st.checkbox("لا (No)", key="e_n")
        
        if e_yes:
            st.markdown('<div class="solution-box">🛑 حل إجهاد العين: طبق قاعدة 20-20-20 (كل 20 دقيقة انظر لشيء بعيد لمسافة 20 قدم لمدة 20 ثانية).</div>', unsafe_allow_html=True)
        if p_hours > 6:
            st.markdown('<div class="solution-box">🛑 حل إدمان الشاشة: استهلاك مرتفع جداً؛ استخدم وضع الـ Focus لتقليل التشتت أثناء المذاكرة.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب الحركة والآلام ---
    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**هل تشعر بألم في الرقبة أو الظهر أثناء المذاكرة؟**")
        b1, b2 = st.columns(2)
        with b1: b_yes = st.checkbox("نعم (Yes)", key="b_y")
        with b2: b_no = st.checkbox("لا (No)", key="b_n")
        if b_yes:
            st.markdown('<div class="solution-box">🛑 حل آلام الرقبة: ارفع الكتاب أو اللابتوب ليكون في مستوى عينك تماماً، وتحرك 5 دقائق كل ساعة.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب التغذية والدماغ ---
    with tab4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**هل تتناول الوجبات السريعة أو المشروبات الغازية بكثرة؟**")
        f_yes = st.checkbox("نعم، غالباً", key="f_y")
        if f_yes:
            st.markdown('<div class="solution-box">🛑 نصيحة التغذية: السكريات تسبب خمولاً مفاجئاً. استبدلها بالمكسرات والفاكهة لطاقة تدوم أطول.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب الحالة النفسية ---
    with tab5:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**هل تشعر بالضغط أو التسويف المستمر؟**")
        p_yes = st.checkbox("نعم، أشعر بالتسويف", key="p_y")
        if p_yes:
            st.markdown('<div class="solution-box">🛑 حل التسويف: استخدم تقنية "بومودورو" (25 دقيقة مذاكرة تركيز، 5 دقائق راحة).</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب التقرير النهائي ---
    with tab6:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.header("📄 التقرير الصحي النهائي")
        st.write(f"الاسم: {st.session_state.u_name}")
        st.write(f"كؤوس الماء المسجلة: {st.session_state.water}")
        
        if st.button("توليد الروشتة المخصصة ✨"):
            st.balloons()
            st.success("تم إعداد تقريرك! يمكنك الآن مراجعة الحلول المقترحة أعلاه.")
        
        if st.button("🚪 تسجيل الخروج"):
            st.session_state.logged_in = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
