import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="AI Health Master Ultra", page_icon="🧬", layout="wide")

# 2. تصميم الألوان والتفاعل (Dark Neon Theme)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .main-header {
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
        padding: 40px; border-radius: 25px; text-align: center; margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,114,255,0.3);
    }
    .info-card {
        background: #1c2128; border-radius: 20px; padding: 25px;
        border: 1px solid #30363d; margin-bottom: 20px;
        transition: 0.3s ease;
    }
    .info-card:hover { border-color: #00c6ff; transform: translateY(-5px); }
    h1, h2, h3 { font-family: 'Segoe UI', sans-serif; }
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white !important; border-radius: 50px; border: none;
        height: 55px; font-weight: bold; width: 100%; font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الموسوعة الشاملة (داتا مضاعفة 200%)
# تم إصلاح المسميات تماماً لتجنب أي KeyError
HEALTH_ENCYCLOPEDIA = {
    "نحافة": {
        "تحليل": "جسمك يحتاج لزيادة الكثافة العضلية. معدل الأيض لديك مرتفع حالياً.",
        "سوبر_فود": ["زبدة الفول السوداني", "الأفوكادو", "الشوفان بالمكسرات", "البيض الكامل", "اللحوم الحمراء"],
        "البرنامج": "تمارين المقاومة بأوزان ثقيلة + 5 وجبات غنية بالبروتين.",
        "نصيحة_ذهبية": "لا تشرب الماء قبل الوجبات مباشرة لتترك مساحة للطعام.",
        "تفاعل": "snow"
    },
    "مثالي": {
        "تحليل": "أنت في 'النطاق الذهبي'. هدفنا الآن هو الحفاظ على نسبة الدهون المنخفضة وزيادة اللياقة.",
        "سوبر_فود": ["بذور الشيا", "الأسماك الدهنية", "الخضروات الورقية", "التوت الأزرق", "الزبادي اليوناني"],
        "البرنامج": "دمج تمارين الكارديو مع رفع الأثقال (Crossfit) لزيادة قوة التحمل.",
        "نصيحة_ذهبية": "النوم لمدة 8 ساعات هو مفتاحك للحفاظ على هذا الوزن المثالي.",
        "تفاعل": "balloons"
    },
    "زيادة وزن": {
        "تحليل": "الجسم في حالة تخزين طاقة. سنقوم بإعادة برمجة الحرق لديك من خلال 'الصيام المتقطع'.",
        "سوبر_فود": ["البروكلي", "خل التفاح (مخفف)", "القرفة", "صدور الدجاج", "الجريب فروت"],
        "البرنامج": "تمارين عالية الكثافة (HIIT) + مشي سريع لمدة 45 دقيقة يومياً.",
        "نصيحة_ذهبية": "ابدأ وجبتك دائماً بالسلطة ثم البروتين، واترك الكربوهيدرات للنهاية.",
        "تفاعل": "balloons"
    }
}

# 4. واجهة المستخدم
st.markdown('<div class="main-header"><h1>🧬 AI Health Master: Ultra Edition</h1><p>نظام التحليل المتطور بالألوان والتفاعل الشامل</p></div>', unsafe_allow_html=True)

with st.container():
    st.markdown("### 👤 الملف الشخصي")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input("اسم المستخدم:")
    with col2:
        weight = st.number_input("الوزن الحالي (كجم):", 30.0, 200.0, 75.0)
    with col3:
        height = st.number_input("الطول الحالي (سم):", 100, 250, 175)

    st.write("---")
    goal = st.select_slider("🎯 حدد مستوى طموحك:", ["تحسين بسيط", "تغيير شامل", "تحول جذري"])

# 5. محرك التقرير
if st.button("🏁 استخراج التقرير الشامل"):
    if not name:
        st.error("يرجى إدخال الاسم لفتح التقرير!")
    else:
        # حساب الـ BMI
        bmi = weight / ((height/100)**2)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        # جلب الداتا الكاملة
        data = HEALTH_ENCYCLOPEDIA[status]
        
        # التفاعلات البصرية
        if data["تفاعل"] == "snow": st.snow()
        else: st.balloons()
        
        st.markdown(f"## 🏆 النتائج الخاصة بالبطل: {name}")
        
        # كروت النتائج
        res_c1, res_c2, res_c3 = st.columns(3)
        with res_c1:
            st.markdown(f'<div class="info-card"><h3 style="color:#00c6ff">📊 مؤشر الكتلة</h3><h2>{bmi:.1f}</h2><p>{status}</p></div>', unsafe_allow_html=True)
        with res_c2:
            st.markdown(f'<div class="info-card"><h3 style="color:#00ff88">🥗 أهم سوبر فود</h3><p>{" - ".join(data["سوبر_فود"][:3])}</p></div>', unsafe_allow_html=True)
        with res_c3:
            st.markdown(f'<div class="info-card"><h3 style="color:#ffcc00">💡 نصيحة اليوم</h3><p>{data["نصيحة_ذهبية"]}</p></div>', unsafe_allow_html=True)
            
        # الداتا العميقة
        st.info(f"🔬 **التحليل العميق:** {data['تحليل']}")
        
        col_final1, col_final2 = st.columns([1.5, 1])
        with col_final1:
            st.markdown("### 📈 توقعات مسار الوزن (الخطة القادمة)")
            change = -0.2 if status == "زيادة وزن" else 0.15 if status == "نحافة" else 0.02
            trend = [weight + (i * change) for i in range(30)]
            st.line_chart(trend)
            
        with col_final2:
            st.markdown("### 🏋️ البرنامج الرياضي")
            st.warning(data["البرنامج"])
            st.markdown("### 🍱 قائمة الطعام المقترحة")
            for item in data["سوبر_فود"]:
                st.write(f"✅ {item}")
else:
    st.info("👋 بانتظار إدخال بياناتك لإبهارك بالتحليل الجديد!")