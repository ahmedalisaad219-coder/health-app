import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 1. إعدادات المنصة الأساسية
st.set_page_config(page_title="Health Student | منصة صحة الطالب", page_icon="🎓", layout="wide")

# 2. تصميم الواجهة (Custom CSS)
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; }
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 35px; border-radius: 15px; text-align: center; color: white; margin-bottom: 30px;
    }
    .section-card {
        background: white; padding: 25px; border-radius: 15px;
        border-top: 6px solid #3b82f6; box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .recommendation-box {
        background: #f0fdf4; border-right: 5px solid #22c55e;
        padding: 15px; border-radius: 10px; margin-top: 15px; font-size: 16px;
    }
    h3 { color: #1e40af; font-weight: 800; margin-bottom: 15px; }
    .stButton>button { background: #1e40af; color: white; border-radius: 8px; width: 100%; height: 45px; }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي للمنصة
st.markdown('<div class="main-header"><h1>🎓 Health Student</h1><p>نظام ذكي لتحليل العادات الصحية وتحسين أداء الطلاب</p></div>', unsafe_allow_html=True)

# 4. شريط البيانات الجانبي (Input)
with st.sidebar:
    st.header("👤 1. بيانات الطالب")
    student_id = st.text_input("Student ID (رقم الطالب):", placeholder="أدخل رقمك هنا...")
    age = st.number_input("العمر:", 15, 40, 20)
    
    st.write("---")
    st.header("🥗 5. قسم التغذية")
    meals_count = st.slider("عدد الوجبات في اليوم:", 1, 6, 3)
    fast_food = st.selectbox("الوجبات السريعة أسبوعياً:", ["نادراً", "1-2 مرة", "3+ مرات"])
    veggies = st.checkbox("أتناول خضار وفواكه يومياً")
    breakfast = st.checkbox("أهتم بوجبة الإفطار")
    
    st.write("---")
    # عداد المية (ميزة ابن البلد الأصلية)
    if 'water' not in st.session_state: st.session_state.water = 0
    st.write(f"💧 شربت {st.session_state.water} كوبايات مية")
    if st.button("➕ شربت كوباية"): st.session_state.water += 1

# 5. عرض المحتوى الرئيسي بعد إدخال الـ ID
if not student_id:
    st.warning("👈 من فضلك ابدأ بإدخال رقم الطالب في القائمة الجانبية لتفعيل التحليل.")
else:
    # الصف الأول: النوم والنشاط البدني
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("😴 2. قسم النوم")
        sleep_hours = st.number_input("ساعات النوم (ليلاً):", 3.0, 14.0, 7.5)
        sleep_quality = st.select_slider("جودة نومك:", options=["سيئة", "مقبولة", "جيدة", "ممتازة"])
        
        # رسم بياني للنوم
        sleep_fig = px.bar(
            x=["نومك الحالي", "المعدل المثالي"], 
            y=[sleep_hours, 8], 
            color=["نومك", "المثالي"],
            title="مقارنة ساعات النوم",
            labels={'x': '', 'y': 'الساعات'}
        )
        st.plotly_chart(sleep_fig, use_container_width=True)
        
        st.markdown('<div class="recommendation-box"><b>💡 توصيات النوم:</b><br>', unsafe_allow_html=True)
        if sleep_hours < 7: st.write("- ⚠️ نومك قليل؛ حاول تنام بدري لزيادة تركيزك الدراسي.")
        st.write("- 📱 قلل استخدام الموبايل قبل النوم بـ 30 دقيقة لتحسين جودة النوم.")
        st.markdown('</div></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("🏃 3. النشاط البدني")
        activity_days = st.slider("أيام الرياضة في الأسبوع:", 0, 7, 3)
        sitting_hours = st.number_input("ساعات الجلوس للدراسة:", 1, 16, 6)
        
        # رسم بياني للنشاط (Pie Chart)
        act_fig = px.pie(
            names=["جلوس", "حركة/نوم"], 
            values=[sitting_hours, 24-sitting_hours], 
            hole=0.5,
            title="توزيع نشاطك اليومي"
        )
        st.plotly_chart(act_fig, use_container_width=True)
        
        st.markdown('<div class="recommendation-box"><b>💡 توصيات النشاط:</b><br>', unsafe_allow_html=True)
        if activity_days < 3: st.write("- 🏃 مارس نشاط يومي أكثر؛ حتى المشي لمدة 20 دقيقة يكفي.")
        st.write("- 🚶 لكل ساعة جلوس، تحرك لمدة 5 دقائق لتنشيط الدورة الدموية.")
        st.markdown('</div></div>', unsafe_allow_html=True)

    # الصف الثاني: الموبايل والتغذية
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("📱 4. استخدام الموبايل")
        phone_hours = st.slider("ساعات الشاشة يومياً:", 1, 18, 5)
        st.write(f"تأثير الموبايل: {'عالي' if phone_hours > 6 else 'متوسط'}")
        
        # Line chart تخيلي لاستخدام الموبايل
        usage_data = pd.DataFrame({"الساعة": range(8, 24), "الاستخدام": np.random.randint(10, 60, 16)})
        fig_phone = px.line(usage_data, x="الساعة", y="الاستخدام", title="نمط استخدامك المتوقع (دقائق/ساعة)")
        st.plotly_chart(fig_phone, use_container_width=True)
        
        st.markdown('<div class="recommendation-box"><b>💡 توصيات تقليل الاستخدام:</b><br>', unsafe_allow_html=True)
        if phone_hours > 5: st.write("- 📉 قلل وقت الشاشة؛ حدد أوقاتاً معينة لتصفح السوشيال ميديا.")
        st.write("- 📵 ابعد الموبايل عن مكان المذاكرة تماماً لزيادة الإنتاجية.")
        st.markdown('</div></div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.subheader("🥗 5. تحليل التغذية")
        # حساب نقاط التغذية
        score = (meals_count * 15) + (25 if veggies else 0) + (30 if breakfast else 0)
        st.write(f"درجة جودة التغذية: {score}%")
        st.progress(score / 100)
        
        # Bar chart للتغذية
        diet_fig = px.bar(x=["نقاطك", "الهدف"], y=[score, 100], color=["أنت", "المثالي"], title="تقييم نظامك الغذائي")
        st.plotly_chart(diet_fig, use_container_width=True)

        st.markdown('<div class="recommendation-box"><b>💡 نصيحة التغذية:</b><br>', unsafe_allow_html=True)
        if not breakfast: st.write("- 🍳 الفطار هو أهم وجبة للطالب؛ بيدي طاقة للمخ.")
        if fast_food == "3+ مرات": st.write("- 🍔 قلل الوجبات السريعة؛ بتسبب خمول وتشتت.")
        st.markdown('</div></div>', unsafe_allow_html=True)

    # القسم الأخير: التوصية الشاملة
    st.write("---")
    st.subheader(f"📊 7. التقرير الختامي للطالب: {student_id}")
    
    total_health_score = (score + (sleep_hours*10) + (activity_days*10)) / 3
    
    if total_health_score > 70:
        st.success(f"استمر يا بطل! درجتك الصحية العامة هي {total_health_score:.1f}%. عاداتك تدعم تفوقك الدراسي.")
    else:
        st.warning(f"درجتك الصحية {total_health_score:.1f}%. تحتاج لتعديل بعض العادات (خاصة النوم والموبايل) لتحسين أدائك.")

    # ميزة إضافية: نصيحة الموسم (من الكود القديم)
    current_month = datetime.now().month
    season = "الشتاء" if current_month in [11,12,1,2] else "الصيف"
    st.info(f"❄️ نصيحة فصل {season}: اشرب سوائل دافئة وحافظ على نشاطك رغم البرد.")