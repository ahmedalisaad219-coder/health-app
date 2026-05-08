import streamlit as st
import pandas as pd
import numpy as np
import random

# 1. إعدادات الصفحة والتصميم
st.set_page_config(page_title="المستشار الصحي الذكي Pro", page_icon="🧪", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stMetric { background-color: white; padding: 15px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .card-pro { background: white; padding: 20px; border-radius: 20px; border-right: 10px solid #2E7D32; box-shadow: 0 10px 20px rgba(0,0,0,0.05); margin-bottom: 20px; }
    h1 { color: #1B5E20; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. الموسوعة الصحية الضخمة
HEALTH_DATABASE = {
    "نحافة": {
        "الحالة": "تحتاج بناء كتلة",
        "الأكل": ["وجبات عالية السعرات (مكسرات، عسل، بروتين)", "شرب العصائر الطبيعية بين الوجبات", "زيادة حصص النشويات الصحية"],
        "الرياضة": "تمارين المقاومة (رفع أثقال) 3-4 مرات أسبوعياً.",
        "نصيحة_سلوكية": "قلل الكافيين لأنه يسد الشهية."
    },
    "مثالي": {
        "الحالة": "وزن رائع ومثالي",
        "الأكل": ["توازن بين البروتين والخضروات", "تقليل السكريات المصنعة", "شرب 3 لتر ماء يومياً"],
        "الرياضة": "مزيج من اليوجا، المشي السريع، وتمارين القوة.",
        "نصيحة_سلوكية": "حافظ على مواعيد نوم ثابتة."
    },
    "زيادة وزن": {
        "الحالة": "نحتاج لحرق الدهون",
        "الأكل": ["الصيام المتقطع"، "منع الخبز الأبيض والحلويات", "زيادة الألياف والخضروات المسلوقة"],
        "الرياضة": "كارديو (جري أو سباحة) 45 دقيقة يومياً.",
        "نصيحة_سلوكية": "امشِ 10 دقائق بعد كل وجبة."
    }
}

# 3. الواجهة الأمامية
st.markdown("# 🧬 المستشار الصحي: نظام تحليل البيانات الذكي")
st.write("---")

col_in1, col_in2 = st.columns(2)
with col_in1:
    st.subheader("👤 بياناتك")
    name = st.text_input("الاسم:", "بطل مستقبلي")
    age = st.number_input("العمر:", 10, 100, 25)
    gender = st.radio("النوع:", ["ذكر", "أنثى"], horizontal=True)
    goal = st.selectbox("🎯 هدفك الحالي:", ["تنشيف (خسارة وزن)", "تضخيم (زيادة عضلات)", "تثبيت الوزن وتحسين الصحة"])

with col_in2:
    st.subheader("📏 القياسات")
    height = st.number_input("الطول (سم):", 100, 250, 170)
    weight = st.number_input("الوزن (كجم):", 30, 200, 75)
    water = st.number_input("💧 أكواب الماء:", 0, 20, 8)
    sleep = st.slider("😴 ساعات النوم:", 0, 12, 8)

st.write("---")

# 4. محرك التحليل والرسوم البيانية
if st.button("🚀 تحليل البيانات وإظهار التوقعات"):
    bmi = weight / ((height/100)**2)
    
    # اختيار الحالة
    if bmi < 18.5: status = "نحافة"
    elif bmi < 25: status = "مثالي"
    else: status = "زيادة وزن"
    
    res = HEALTH_DATABASE[status]
    st.balloons()

    # عرض النتائج في Metrics
    st.subheader(f"📊 لوحة تحكم {name}")
    m1, m2, m3 = st.columns(3)
    m1.metric("كتلة الجسم (BMI)", f"{bmi:.1f}", status)
    m2.metric("الحالة الصحية", status)
    m3.metric("جودة النوم", f"{sleep} س", "جيد" if sleep >= 7 else "تحتاج راحة")

    # 5. الرسم البياني الديناميكي (بيتغير بناءً على البيانات)
    st.write("### 📈 توقعات مسارك الصحي لـ 30 يوم القادمة")
    days = list(range(1, 31))
    
    # حساب المسار بناءً على الوزن الفعلي والهدف
    if "تنشيف" in goal:
        # يتوقع خسارة 150 جرام يومياً
        trend = [weight - (d * 0.15) for d in days]
        label = "خسارة وزن متوقعة"
    elif "تضخيم" in goal:
        # يتوقع زيادة 100 جرام عضل يومياً
        trend = [weight + (d * 0.1) for d in days]
        label = "زيادة عضلية متوقعة"
    else:
        # تذبذب بسيط حول الوزن الحالي
        trend = [weight + random.uniform(-0.5, 0.5) for _ in days]
        label = "استقرار الوزن"

    chart_df = pd.DataFrame({label: trend}, index=days)
    st.line_chart(chart_df)

    # 6. قاعدة البيانات الموسوعية (عرض الداتا)
    st.divider()
    col_res1, col_res2 = st.columns(2)
    
    with col_res1:
        st.markdown(f"""<div class="card-pro"><h3>🥗 خطة التغذية الموسوعية</h3>""", unsafe_allow_html=True)
        for meal in res["الأكل"]:
            st.write(f"🔹 {meal}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_res2:
        st.markdown(f"""<div class="card-pro"><h3>🏋️ التوصيات البدنية</h3>""", unsafe_allow_html=True)
        st.write(f"**التمارين:** {res['الرياضة']}")
        st.write(f"**نصيحة الخبير:** {res['نصيحة_سلوكية']}")
        st.markdown("</div>", unsafe_allow_html=True)

    # 7. التحدي اليومي العشوائي
    extra_tips = ["امشِ 15 دقيقة بعد الأكل.", "اشرب كوب ماء كل ساعة.", "توقف عن استخدام الموبايل قبل النوم بـ 30 دقيقة."]
    st.success(f"🎯 **تحدي اليوم:** {random.choice(extra_tips)}")
    st.snow()