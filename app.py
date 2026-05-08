import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="مدربك الصحي الذكي", page_icon="🌟", layout="wide")

# إضافة لمسة جمالية وتنسيق الألوان
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTextInput, .stNumberInput, .stSlider {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 5px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 15px;
    }
    h1 { color: #2E7D32; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

# 2. جملة تحفيزية في البداية
st.markdown("# 🌱 المستشار الصحي الذكي")
st.success("✨ **'صحتك هي أغلى ما تملك، ابدأ العناية بها اليوم!'**")

st.divider()

# 3. إدخال البيانات مع الأيقونات التوضيحية
st.subheader("📋 من فضلك أدخل بياناتك:")

col_in1, col_in2 = st.columns(2)

with col_in1:
    name = st.text_input("👤 الاسم الكريم:")
    age = st.number_input("🎂 العمر (بالسنوات):", 10, 100, 20)
    height = st.number_input("📏 الطول (سم):", 100, 250, 170)

with col_in2:
    weight = st.number_input("⚖️ الوزن (كجم):", 30, 200, 70)
    water = st.number_input("💧 كم كوب ماء تشرب يومياً؟", 0, 20, 8)
    sleep = st.select_slider("😴 عدد ساعات نومك:", options=list(range(0, 13)), value=8)

phone = st.slider("📱 ساعات استخدام الموبايل:", 0, 16, 5)

st.divider()

# 4. زر التقرير
if st.button("🚀 اضغط هنا للحصول على نصيحتك"):
    bmi = weight / ((height/100)**2)
    st.balloons()
    
    st.markdown(f"### 📋 التقرير الصحي للبطل: {name}")
    
    # عرض النتائج في شكل أيقونات كبيرة (Cards)
    res1, res2, res3 = st.columns(3)
    
    with res1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### ⚖️")
        st.write("**حالة الوزن**")
        if bmi < 18.5: st.warning("نحافة")
        elif bmi < 25: st.success("مثالي")
        else: st.error("زيادة وزن")
        st.markdown('</div>', unsafe_allow_html=True)

    with res2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 😴")
        st.write("**جودة النوم**")
        if sleep < 7: st.error("نوم قليل")
        else: st.success("نوم كافي")
        st.markdown('</div>', unsafe_allow_html=True)

    with res3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 💧")
        st.write("**شرب الماء**")
        if water < 8: st.info("تحتاج مزيد")
        else: st.success("ممتاز")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### 📱")
    st.write("**صحة العين (الموبايل)**")
    if phone > 5: st.warning("استخدام مفرط - ارح عينك")
    else: st.success("استخدام معتدل")
    st.markdown('</div>', unsafe_allow_html=True)

    # 5. جملة تحفيزية في النهاية
    st.divider()
    st.info("💪 **'تذكر دائماً: البدايات الصغيرة تصنع نتائج كبيرة!'**")
    st.snow()