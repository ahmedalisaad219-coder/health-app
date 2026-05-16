import streamlit as st

# 1. إعدادات الصفحة والتنسيق (CSS) لضمان ظهور كل شيء كما في الصور
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
        background: white; padding: 25px; border-radius: 15px;
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

# 2. إدارة الحالة (Session State)
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
    
    # رسالة تحفيزية بناءً على الماء
    if st.session_state.water < 5:
        st.warning("⚠️ اشرب مزيداً من الماء لتحسين تركيزك!")
    else:
        st.success("✅ أحسنت! ترطيب جسمك ممتاز.")

# 4. شاشة الدخول -
if not st.session_state.logged_in:
    st.markdown('<div class="main-header"><h1>🎓 Health Student Encyclopedia</h1><p>الموسوعة التفاعلية الشاملة لحلول مشاكل الطلاب</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("📝 ابدأ بكتابة اسمك لفتح الموسوعة والحلول:")
    name = st.text_input("اكتب اسمك هنا...", key="user_name_input")
    
    # إضافة زر الدخول لضمان تفعيل الصفحة
    if st.button("دخول للموسوعة 🚀"):
        if name.strip():
            st.session_state.logged_in = True
            st.session_state.u_name = name
            st.rerun()
        else:
            st.error("الرجاء إدخال الاسم أولاً!")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. محتوى الموسوعة (يظهر بعد الدخول فقط)
else:
    st.markdown(f'<div class="main-header"><h1>🎓 موسوعة الطالب: {st.session_state.u_name}</h1></div>', unsafe_allow_html=True)
    
    # التبويبات -
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌙 النوم والتركيز", "📱 التكنولوجيا", "🏃 الحركة والآلام", "🍎 التغذية", "📥 التقرير"])

    # --- تبويب النوم ---
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("ساعات نومك الفعلية")
        sleep_h = st.slider("حدد عدد ساعات نومك:", 2, 12, 7, key="sleep_s")
        st.markdown(f"القيمة المختارة: <span class='slider-val'>{sleep_h}</span>", unsafe_allow_html=True)
        
        st.write("---")
        st.write("**هل تواجه صعوبة في الاستيقاظ؟**")
        # حل مشكلة ظهور نعم ولا -
        c1, c2 = st.columns(2)
        with c1: s_yes = st.checkbox("نعم (Yes)", key="s_y")
        with c2: s_no = st.checkbox("لا (No)", key="s_n")

        # ظهور الحلول تلقائياً
        if sleep_h < 7:
            st.markdown('<div class="solution-box">🛑 حل نقص النوم: أنت تنام أقل من المعدل الصحي (8 ساعات). الحل: ابعد الأجهزة الإلكترونية قبل النوم بـ 30 دقيقة لتسريع الدخول في النوم العميق.</div>', unsafe_allow_html=True)
        if s_yes:
            st.markdown('<div class="solution-box">🛑 حل خمول الاستيقاظ: جرب تمرين "التنفس الصباحي" وتعرض لضوء الشمس فور الاستيقاظ لضبط ساعتك البيولوجية.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب التكنولوجيا ---
    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("إجهاد العين والتشتت")
        tech_h = st.slider("ساعات استخدام الهاتف يومياً:", 1, 16, 5, key="tech_s")
        st.markdown(f"الساعات: <span class='slider-val'>{tech_h}</span>", unsafe_allow_html=True)
        
        st.write("---")
        st.write("**هل تعاني من جفاف العين أو ضبابية الرؤية؟**")
        t1, t2 = st.columns(2)
        with t1: e_yes = st.checkbox("نعم (Yes)", key="e_y")
        with t2: e_no = st.checkbox("لا (No)", key="e_n")

        if e_yes:
            st.markdown('<div class="solution-box">🛑 حل إجهاد العين: طبق قاعدة (20-20-20)؛ كل 20 دقيقة مذاكرة، انظر لمسافة 20 قدم لمدة 20 ثانية لراحة عضلات العين.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب الحركة ---
    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("آلام الظهر والرقبة")
        st.write("**هل تشعر بألم في الرقبة بسبب وضعية المذاكرة؟**")
        b1, b2 = st.columns(2)
        with b1: b_yes = st.checkbox("نعم (Yes)", key="b_y")
        with b2: b_no = st.checkbox("لا (No)", key="b_n")
        
        if b_yes:
            st.markdown('<div class="solution-box">🛑 حل آلام الرقبة: ارفع الكتاب أو الحاسوب ليكون في مستوى عينك، وتجنب الانحناء للأمام لفترات طويلة.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- تبويب التقرير ---
    with tab4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("التقرير النهائي")
        if st.button("توليد التقرير المخصص 📄"):
            st.balloons()
            st.success(f"تم إعداد التقرير بنجاح يا {st.session_state.u_name}!")
        if st.button("🚪 تسجيل الخروج"):
            st.session_state.logged_in = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
