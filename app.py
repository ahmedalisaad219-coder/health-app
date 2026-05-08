import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="المستشار الصحي الذكي", page_icon="🏆", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); text-align: center; margin-bottom: 15px; border-top: 5px solid #2E7D32; }
    h1 { color: #1B5E20; text-align: center; font-weight: bold; }
    .stButton>button { background: linear-gradient(45deg, #2E7D32, #4CAF50); color: white; font-weight: bold; border-radius: 25px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# البداية التحفيزية
st.markdown("# 🛡️ نظامك الصحي المتكامل")
st.markdown("<h4 style='text-align: center; color: #555;'>صناعة بطل: طريقك نحو حياة أفضل يبدأ من هنا</h4>", unsafe_allow_html=True)

st.divider()

# المدخلات المنظمة
col_in1, col_in2 = st.columns(2)

with col_in1:
    st.markdown("### 👤 البيانات الأساسية")
    name = st.text_input("ما هو اسمك يا بطل؟")
    age = st.number_input("🎂 عمرك الآن:", 10, 100, 20)
    gender = st.radio("🧬 الجنس:", ["ذكر", "أنثى"], horizontal=True)

with col_in2:
    st.markdown("### 📊 القياسات الحيوية")
    height = st.number_input("📏 طولك (سم):", 100, 250, 170)
    weight = st.number_input("⚖️ وزنك (كجم):", 30, 200, 75)
    activity = st.selectbox("🏃 مستوى نشاطك:", ["خامل (لا رياضة)", "نشاط خفيف", "نشاط متوسط", "رياضي جداً"])

st.divider()

st.markdown("### 🌙 العادات اليومية")
c1, c2, c3 = st.columns(3)
with c1: water = st.number_input("💧 أكواب الماء:", 0, 20, 8)
with c2: sleep = st.slider("😴 ساعات النوم:", 0, 12, 8)
with c3: phone = st.slider("📱 ساعات الموبايل:", 0, 16, 5)

if st.button("🚀 تحليل حالتي الصحية الآن"):
    bmi = weight / ((height/100)**2)
    
    # حساب السعرات الحرارية التقريبي (BMR)
    if gender == "ذكر":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
    st.balloons()
    st.markdown(f"## ✨ النتائج النهائية للبطل {name}")

    # عرض النتائج في بطاقات
    r1, r2, r3, r4 = st.columns(4)
    
    with r1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### ⚖️")
        st.write("**كتلة الجسم**")
        st.write(f"{bmi:.1f}")
        st.markdown('</div>', unsafe_allow_html=True)

    with r2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 🍎")
        st.write("**السعرات المطلوبة**")
        st.write(f"{int(bmr)} سعرة")
        st.markdown('</div>', unsafe_allow_html=True)

    with r3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 😴")
        st.write("**جودة النوم**")
        st.write("ممتاز" if sleep >= 7 else "ناقص")
        st.markdown('</div>', unsafe_allow_html=True)

    with r4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### 📱")
        st.write("**إجهاد العين**")
        st.write("منخفض" if phone <= 4 else "مرتفع")
        st.markdown('</div>', unsafe_allow_html=True)

    # النصيحة الذهبية
    st.divider()
    st.info(f"💡 **نصيحتك المخصصة:** يا {name}، جسمك يحتاج لحوالي {int(bmr)} سعرة حرارية ليعمل بكفاءة. حافظ على شرب الماء بانتظام وقلل ساعات الموبايل قبل النوم بـ 30 دقيقة لتحسين تركيزك.")
    st.snow()