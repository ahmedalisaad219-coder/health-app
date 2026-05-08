import streamlit as st
import pandas as pd
import numpy as np
import random

# 1. إعدادات الصفحة - الصفحة بقت "عرض واسع" لشكل احترافي
st.set_page_config(page_title="المستشار الصحي المتكامل", page_icon="🏛️", layout="wide")

# تصميم الألوان والبطاقات (CSS)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .card { 
        background: white; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
        text-align: center; 
        border-top: 5px solid #2E7D32;
    }
    .info-box {
        background-color: #ffffff;
        border-right: 8px solid #4CAF50;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    h1 { color: #1B5E20; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة بيانات الموسوعة الضخمة (Data)
# ضفنا هنا تفاصيل أكتر بكتير عشان الردود متكونش مكررة
HEALTH_DB = {
    "نحافة": {
        "تحليل": "جسمك يحتاج لبناء كتلة عضلية وزيادة سعرات صحية.",
        "نصائح_غذائية": ["تناول البروتين (بيض، لحوم، بقوليات)", "أضف الدهون الصحية (زيت زيتون، مكسرات)", "تناول 5 وجبات صغيرة بدلاً من 3 كبيرة"],
        "جدول_تمارين": "تمارين المقاومة ورفع الأثقال (3 أيام أسبوعياً) مع تقليل الكارديو.",
        "تحدي": "تناول ملعقة عسل كبيرة مع 7 تمرات اليوم."
    },
    "مثالي": {
        "تحليل": "أنت في أفضل حالاتك الصحية! هدفنا هو الحفاظ على اللياقة.",
        "نصائح_غذائية": ["الحفاظ على توازن النشويات والبروتين", "تناول الخضروات الورقية يومياً", "تقليل الملح في الطعام"],
        "جدول_تمارين": "مزيج من المشي السريع (30 دقيقة) وتمارين السويدي.",
        "تحدي": "جرب تمرين 'البلانك' لمدة دقيقة كاملة اليوم."
    },
    "زيادة وزن": {
        "تحليل": "نحتاج لرفع معدل الحرق وتقليل السعرات الزائدة.",
        "نصائح_غذائية": ["امنع السكر الأبيض تماماً", "استبدل الخبز الأبيض بالأسود", "اشرب كوب ماء كبير قبل كل وجبة بـ 15 دقيقة"],
        "جدول_تمارين": "كارديو عالي الشدة (جري، سباحة، أو ركوب دراجة) 5 أيام أسبوعياً.",
        "تحدي": "امشِ 10 آلاف خطوة النهاردة."
    }
}

# 3. واجهة المستخدم (المدخلات بالأيقونات)
st.markdown("# 🏛️ الموسوعة الصحية الذكية الشاملة")
st.info("💡 **حكمة اليوم:** 'العقل السليم في الجسم السليم' - ابدأ الآن ولا تؤجل!")

st.divider()

col_in1, col_in2 = st.columns(2)
with col_in1:
    st.subheader("👤 البيانات الشخصية")
    name = st.text_input("اسم المستخدم:")
    age = st.number_input("🎂 العمر:", 10, 90, 20)
    height = st.number_input("📏 الطول (سم):", 100, 250, 170)
    gender = st.radio("🧬 النوع:", ["ذكر", "أنثى"], horizontal=True)

with col_in2:
    st.subheader("📊 القياسات اليومية")
    weight = st.number_input("⚖️ الوزن الحالي (كجم):", 30, 200, 75)
    water = st.number_input("💧 أكواب الماء:", 0, 20, 8)
    sleep = st.slider("😴 ساعات النوم:", 0, 12, 8)
    phone = st.slider("📱 استخدام الموبايل:", 0, 16, 5)

goal = st.selectbox("🎯 هدفك القادم:", ["تنشيف (حرق دهون)", "تضخيم (بناء عضلات)", "تحسين صحة عامة"])

st.divider()

# 4. معالجة البيانات والنتائج
if st.button("🚀 تحليل البيانات واستخراج الحلول من الموسوعة"):
    bmi = weight / ((height/100)**2)
    
    # تحديد الحالة بناءً على الـ BMI
    if bmi < 18.5: status = "نحافة"
    elif bmi < 25: status = "مثالي"
    else: status = "زيادة وزن"
    
    # سحب البيانات من الموسوعة
    res = HEALTH_DB[status]
    
    st.balloons()
    st.markdown(f"## 📋 التقرير الشامل للبطل {name}")

    # عرض العدادات (Metrics)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("كتلة الجسم", f"{bmi:.1f}", status)
    with c2: st.metric("النوم", f"{sleep} س", "ممتاز" if sleep >= 7 else "ناقص")
    with c3: st.metric("المياه", f"{water} كوب", "أحسنت" if water >= 8 else "زيدها")
    with c4: st.metric("الموبايل", f"{phone} س", "آمن" if phone <= 4 else "مجهد")

    # 5. عرض النصائح المجمعة في بطاقات
    st.divider()
    col_res1, col_res2 = st.columns(2)
    
    with col_res1:
        st.markdown(f'<div class="info-box"><h3>🥗 النظام الغذائي الموسوعي</h3>', unsafe_allow_html=True)
        for tip in res["نصائح_غذائية"]:
            st.write(f"✅ {tip}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_res2:
        st.markdown(f'<div class="info-box"><h3>🏋️ خطة التدريب الاحترافية</h3>', unsafe_allow_html=True)
        st.write(res["جدول_تمارين"])
        st.markdown('</div>', unsafe_allow_html=True)

    # 6. الرسم البياني للتوقعات (Data Visualization)
    st.write("### 📈 توقعات مسارك الصحي (30 يوم القادمة)")
    days = np.array(range(1, 31))
    if "تنشيف" in goal:
        trend = weight - (days * 0.12)
    elif "تضخيم" in goal:
        trend = weight + (days * 0.08)
    else:
        trend = [weight] * 30
    
    st.line_chart(pd.DataFrame({"الوزن المتوقع": trend}, index=days))

    # 7. التحدي اليومي العشوائي
    st.divider()
    st.warning(f"🎯 **تحدي الـ 24 ساعة الخاص بك:** {res['تحدي']}")
    
    # نصيحة عشوائية إضافية لزيادة الداتا
    extra = ["الجلوس الصحي يقلل آلام الظهر.", "الفاكهة أفضل بديل للسكريات.", "التنفس العميق يقلل التوتر."]
    st.success(f"🌟 **نصيحة إضافية:** {random.choice(extra)}")
    
    st.snow()