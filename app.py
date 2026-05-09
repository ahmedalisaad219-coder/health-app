import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

# 1. إعدادات المنصة
st.set_page_config(page_title="Health Student | التفاعلية", page_icon="🚀", layout="wide")

# 2. تصميم CSS متطور للتفاعل
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 50px; border-radius: 20px; text-align: center; color: white; margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2);
    }
    .card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;
        transition: transform 0.3s; border-right: 8px solid #3b82f6;
    }
    .card:hover { transform: translateY(-5px); }
    .solution-box {
        background: #fff7ed; border-right: 6px solid #f97316;
        padding: 20px; border-radius: 12px; margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<div class="main-header"><h1>🎓 Health Student Interactive</h1><p>أول منصة تفاعلية ذكية لصحة وتركيز الطلاب</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية التفاعلية
with st.sidebar:
    st.header("👤 ملفك التفاعلي")
    student_name = st.text_input("اسمك بطل القصة:", placeholder="اكتب اسمك هنا...")
    
    if student_name:
        st.success(f"أهلاً يا {student_name}! جاهز للتحدي؟")
    
    st.write("---")
    # عداد المياه التفاعلي (مع رسائل تفاعلية)
    if 'water' not in st.session_state: st.session_state.water = 0
    
    st.subheader(f"💧 كوبايات المية: {st.session_state.water}")
    if st.button("🥤 سجل كوباية مية"):
        st.session_state.water += 1
        st.toast(f"عاش يا {student_name}! جسمك دلوقتي بيشكرك! ✨")
        if st.session_state.water == 8:
            st.balloons()
            st.toast("🏆 مبروك! وصلت للهدف المثالي للمية النهاردة!")

# 5. منطق التحقق
if not student_name:
    st.info("👋 مستنيين إيه؟ اكتب اسمك في الجنب عشان الموسوعة التفاعلية تفتح!")
else:
    # التبويبات التفاعلية
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌙 النوم", "📱 الموبايل", "🏃 الحركة", "🥗 التغذية", "📈 تقريرك الحقيقي"])

    # --- تبويب النوم ---
    with tab1:
        st.markdown('### 🌙 تحليل النوم الذكي')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            sleep_h = st.select_slider("كم ساعة نمت؟", options=list(range(2, 13)), value=7)
            feelings = st.radio("مودك إيه أول ما صحيت؟", ["مصدع ومكسل", "عايز أنام تاني", "فايق نص نص", "نشيط جداً"])
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            if sleep_h < 6:
                st.error("🚨 إنذار: مخك شغال بـ 50% من طاقته بس!")
                st.write("**الحل:** خد قيلولة (Nap) لمدة 20 دقيقة العصر، هتفرق جداً في تركيزك بالليل.")
            else:
                st.success("✅ رائع! عدد ساعات كافي لشحن خلايا الذاكرة.")

    # --- تبويب الموبايل ---
    with tab2:
        st.markdown('### 📱 تحدي وقت الشاشة')
        col3, col4 = st.columns(2)
        with col3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            screen_time = st.slider("ساعات الموبايل (ترفيه):", 1, 15, 4)
            app_type = st.selectbox("أكتر تطبيق سحلِك:", ["تيك توك (فيديوهات قصيرة)", "فيسبوك/إكس", "ألعاب أونلاين", "يوتيوب"])
            st.markdown('</div>', unsafe_allow_html=True)
        with col4:
            st.write("#### 🏥 الروشتة التفاعلية:")
            if app_type == "تيك توك (فيديوهات قصيرة)":
                st.warning("⚠️ الفيديوهات القصيرة بتبوظ 'هرمون الدوبامين' وبتخلي تركيزك في المذاكرة صعب.")
                st.write("**الحل:** حاول تذاكر بنظام (Deep Work) - اقفل الموبايل تماماً لمدة 50 دقيقة.")
            fig_p = px.pie(values=[screen_time, 24-screen_time], names=["موبايل", "حياة حقيقية"], hole=0.6)
            st.plotly_chart(fig_p, use_container_width=True)

    # --- تبويب الحركة ---
    with tab3:
        st.markdown('### 🏃 الرياضة وآلام المذاكرة')
        col5, col6 = st.columns(2)
        with col5:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            exercise = st.toggle("هل مارست أي رياضة النهاردة؟")
            if exercise:
                st.toast("بطل والله! 💪")
            back_pain = st.select_slider("مستوى وجع ظهرك:", options=["مرتاح", "شد بسيط", "وجع مزعج", "تعبان جداً"])
            st.markdown('</div>', unsafe_allow_html=True)
        with col6:
            if back_pain in ["وجع مزعج", "تعبان جداً"]:
                st.error("🆘 لازم تتحرك دلوقتي!")
                st.write("**تمرين تفاعلي:** قوم اقف، مِد إيدك للسقف لمدة 10 ثواني، ولف رقبتك ببطء. كرر ده كل ساعة.")

    # --- تبويب التغذية ---
    with tab4:
        st.markdown('### 🥗 وقود العقل')
        col7, col8 = st.columns(2)
        with col7:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            sugar = st.slider("معدل السكريات (حلويات/بيبسي):", 0, 10, 3)
            coffee = st.number_input("عدد أكواب القهوة/الشاي:", 0, 10, 2)
            st.markdown('</div>', unsafe_allow_html=True)
        with col8:
            if sugar > 5:
                st.error("📉 هتحس بخمول مفاجئ (Sugar Crash) بعد شوية.")
                st.write("**الحل:** اشرب كوباية مية كبيرة دلوقتي عشان تخفف تركيز السكر في دمك.")

    # --- التقرير النهائي التفاعلي ---
    with tab5:
        st.markdown(f"### 📊 ملخص يوم {student_name}")
        
        # حساب السكور النهائي
        score = 100
        if sleep_h < 7: score -= 20
        if screen_time > 5: score -= 20
        if st.session_state.water < 6: score -= 10
        
        c_score1, c_score2 = st.columns([1, 2])
        with c_score1:
            st.metric("درجتك الصحية اليوم", f"{score}%", f"{score-50}%")
        
        with c_score2:
            if score >= 80:
                st.balloons()
                st.success("أنت النهاردة 'سوبر طالب'! استمر يا بطل.")
            elif score >= 50:
                st.warning("أداء متوسط.. تقدر تخلي بكرة أحسن لو قللت الموبايل شوية.")
            else:
                st.snow()
                st.error("يوم صعب صحياً.. محتاجين نغير الخطة من بكرة وننام بدري.")

        st.write("---")
        st.button("📄 تحميل التقرير (قريباً)")