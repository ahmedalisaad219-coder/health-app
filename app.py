import streamlit as st

# 1. إعدادات الصفحة والألوان
st.set_page_config(page_title="المستشار الصحي الشامل", page_icon="✨", layout="wide")

# إضافة لمسة جمالية بالألوان (CSS)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 20px; width: 100%; }
    .report-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
    h1 { color: #2E7D32; text-align: center; }
    h3 { color: #1B5E20; }
    </style>
    """, unsafe_allow_html=True)

# 2. جملة تحفيزية في البداية
st.markdown("# 🌱 المستشار الصحي الذكي")
st.info("💡 **حكمة اليوم:** 'الصحة هي الثروة الحقيقية، وليس قطع الذهب والفضة.' - مهاتما غاندي")

st.divider()

# 3. إدخال البيانات في أقسام منظمة
with st.container():
    st.subheader("📝 أدخل بياناتك الشخصية")
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1:
        name = st.text_input("الاسم:")
        age = st.number_input("العمر:", 10, 100, 20)
    with col_in2:
        weight = st.number_input("الوزن (كجم):", 30, 200, 70)
    with col_in3:
        height = st.number_input("الطول (سم):", 100, 250, 170)

st.divider()

with st.container():
    st.subheader("⚙️ عاداتك اليومية")
    col_in4, col_in5, col_in6 = st.columns(3)
    with col_in4:
        phone_hours = st.select_slider("استخدام الموبايل (ساعة):", options=list(range(0, 17)), value=5)
    with col_in5:
        sleep_hours = st.select_slider("ساعات النوم (ساعة):", options=list(range(0, 13)), value=8)
    with col_in6:
        water_glasses = st.number_input("أكواب الماء يومياً:", 0, 20, 8)

# 4. زر إصدار التقرير
if st.button("🚀 استخراج التقرير الشامل"):
    bmi = weight / ((height/100)**2)
    st.balloons()
    
    st.markdown(f"## 📋 تقريرك الصحي يا كابتن {name}")
    
    # عرض النتائج في أيقونات منفصلة (Cards)
    col_res1, col_res2 = st.columns(2)
    
    with col_res1:
        # بطاقة الوزن
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        st.markdown("### ⚖️ تحليل الوزن (BMI)")
        if bmi < 18.5: st.warning(f"مؤشرك {bmi:.1f}: نحافة. تحتاج لغذاء غني بالبروتين.")
        elif bmi < 25: st.success(f"مؤشرك {bmi:.1f}: وزن مثالي! أنت بطل.")
        else: st.error(f"مؤشرك {bmi:.1f}: زيادة وزن. قلل السكريات وابدأ بالمشي.")
        st.markdown('</div>', unsafe_allow_html=True)

        # بطاقة النوم
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        st.markdown("### 😴 جودة النوم")
        if sleep_hours < 7: st.error(f"نومك ({sleep_hours} س) قليل! المخ يحتاج راحة ليركز في الدراسة.")
        else: st.success("نومك ممتاز! جسمك يتجدد الآن.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_res2:
        # بطاقة الماء
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        st.markdown("### 💧 ترطيب الجسم")
        if water_glasses < 8: st.info(f"شربت {water_glasses} أكواب فقط. الماء سر الذكاء ونضارة البشرة، اشرب أكثر!")
        else: st.success("ترطيب رائع! كليتاك تشكرانك.")
        st.markdown('</div>', unsafe_allow_html=True)

        # بطاقة الموبايل
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        st.markdown("### 📱 صحة العين والرقبة")
        if phone_hours > 4: st.warning(f"استخدام {phone_hours} ساعات يجهد عينك. اترك الهاتف واخرج للطبيعة!")
        else: st.success("استخدامك للموبايل ذكي ومنظم.")
        st.markdown('</div>', unsafe_allow_html=True)

    # 5. جملة تحفيزية في النهاية
    st.divider()
    st.success("🌟 **رسالة لك:** 'أنت اليوم أفضل مما كنت عليه بالأمس.. استمر في العناية بنفسك، فجسمك هو المكان الوحيد الذي ستعيش فيه للأبد!'")
    st.snow()