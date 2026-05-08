import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Health Master v14", page_icon="⚡", layout="wide")

# 2. إرجاع التصميم الاحترافي (CSS) - بدون مكتبات خارجية
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 30px; border-radius: 20px; color: white; text-align: center; margin-bottom: 25px;
    }
    .result-card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-right: 10px solid #1e3a8a;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الموسوعة الشاملة (حل مشكلة KeyError اللي ظهرت قبل كدة)
HEALTH_GUIDE = {
    "نحافة": {
        "تحليل": "مؤشر كتلة جسمك منخفض. نحتاج للتركيز على الأطعمة الغنية بالطاقة.",
        "نصيحة": "تناول 5 وجبات صغيرة يومياً وركز على المكسرات وزيت الزيتون والبروتين.",
        "أيقونة": "❄️"
    },
    "مثالي": {
        "تحليل": "أنت في النطاق الصحي المثالي. استمر في الحفاظ على هذا الإنجاز!",
        "نصيحة": "التنويع في الخضروات الورقية وممارسة الرياضة سيضمن استمرارك.",
        "أيقونة": "🎈"
    },
    "زيادة وزن": {
        "تحليل": "هناك زيادة بسيطة في الكتلة. تنظيم السعرات هو الحل الأمثل.",
        "نصيحة": "استبدل العصائر بالماء، وحاول المشي 30 دقيقة يومياً.",
        "أيقونة": "🔥"
    }
}

# 4. واجهة المستخدم
st.markdown('<div class="main-header"><h1>🛡️ AI Health Master Pro</h1><p>النسخة المستقرة فائقة الأداء</p></div>', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 اسم البطل:")
        weight = st.number_input("⚖️ الوزن الحالي (كجم):", 30.0, 200.0, 75.0)
    with col2:
        height = st.number_input("📏 الطول (سم):", 100, 250, 175)
        goal = st.selectbox("🎯 هدفك القادم:", ["تنشيف دهون", "ضخامة عضلية", "تحسين لياقة"])

# 5. محرك التحليل (Logic)
if st.button("🚀 تحليل البيانات وإصدار التقرير"):
    if not name:
        st.warning("من فضلك اكتب اسمك أولاً!")
    else:
        # الحسابات
        bmi = weight / ((height/100)**2)
        
        # التصنيف
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        # استدعاء البيانات بأمان (حل KeyError)
        res = HEALTH_GUIDE[status]
        
        # الاحتفالات
        if status == "نحافة": st.snow()
        else: st.balloons()
        
        # عرض النتائج في كروت شيك
        st.markdown(f'<div class="result-card"><h3>📊 تقرير البطل: {name}</h3>', unsafe_allow_html=True)
        
        r1, r2, r3 = st.columns(3)
        r1.metric("مؤشر الكتلة (BMI)", f"{bmi:.1f}", status)
        r2.write(f"🔬 **التحليل:** {res['تحليل']}")
        r3.write(f"💡 **النصيحة:** {res['نصيحة']}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # الرسم البياني (آمن جداً)
        st.write("---")
        st.subheader("📈 توقعات مسار وزنك في 30 يوم")
        change_rate = -0.12 if "تنشيف" in goal else 0.1 if "ضخامة" in goal else 0.02
        future_weights = [weight + (i * change_rate) for i in range(30)]
        st.line_chart(future_weights)