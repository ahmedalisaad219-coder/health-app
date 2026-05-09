import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 1. إعدادات المنصة الأساسية
st.set_page_config(page_title="Health Student | المنصة المتكاملة", page_icon="🎓", layout="wide")

# 2. تصميم احترافي (CSS) لتنظيم الألوان والمساحات الواسعة
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e40af 100%);
        padding: 40px; border-radius: 20px; text-align: center; color: white; margin-bottom: 30px;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 20px; font-weight: bold; padding: 10px 25px; color: #1e40af;
    }
    .card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px;
        border-top: 5px solid #3b82f6;
    }
    .recommendation {
        background: #f0f9ff; border-right: 5px solid #0ea5e9;
        padding: 15px; border-radius: 8px; margin-top: 10px; color: #0369a1;
    }
    h2, h3 { color: #1e3a8a; }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي للمنصة
st.markdown('<div class="main-header"><h1>🎓 Health Student Dashboard</h1><p>النظام الشامل لتحليل العادات الصحية وتحسين أداء الطلاب</p></div>', unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar) لجمع البيانات الأساسية
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3429/3429433.png", width=100)
    st.header("👤 الملف الشخصي")
    student_name = st.text_input("اسم الطالب بالكامل:", placeholder="ادخل اسمك هنا...")
    university = st.text_input("الجامعة / الكلية:")
    level = st.selectbox("المستوى الدراسي:", ["سنة أولى", "سنة ثانية", "سنة ثالثة", "سنة رابعة", "خريج"])
    
    st.write("---")
    st.header("🥗 ملخص سريع")
    water_daily = st.number_input("أكواب الماء اليومية:", 0, 20, 8)
    if st.button("🔄 إعادة ضبط كل البيانات"):
        st.rerun()

# 5. منطق التحقق من الاسم لبدء العرض
if not student_name:
    st.warning("👋 أهلاً بك! من فضلك ابدأ بكتابة اسمك في القائمة الجانبية لفتح ملفك الصحي المترتب.")
else:
    # إنشاء التبويبات (Tabs) لتنظيم الموقع ومنع التداخل
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "😴 جودة النوم", 
        "📱 العادات الرقمية", 
        "🏃 النشاط البدني", 
        "🥗 التغذية والتركيز", 
        "📊 التقرير والتحليل"
    ])

    # --- القسم الأول: النوم ---
    with tab1:
        st.markdown('## 🌙 تحليل جودة النوم')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            sleep_hours = st.slider("عدد ساعات نومك الفعلية:", 2, 14, 8)
            bed_time = st.time_input("في أي ساعة تنام عادةً؟", datetime.strptime("23:00", "%H:%M"))
            wake_time = st.time_input("في أي ساعة تستيقظ؟", datetime.strptime("07:00", "%H:%M"))
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            fig_sleep = px.bar(
                x=["نومك", "المعدل المثالي"], 
                y=[sleep_hours, 8], 
                color=["أنت", "الهدف"],
                title="مقارنة ساعات النوم اليومية",
                labels={'x': '', 'y': 'ساعات النوم'}
            )
            st.plotly_chart(fig_sleep, use_container_width=True)
        
        st.markdown('<div class="recommendation"><b>💡 توصية النوم:</b><br>' + 
                   ("أحسنت! ساعات نومك كافية جداً للتحصيل الدراسي." if sleep_hours >= 7 else "انتبه! نقص النوم يقلل من قدرة عقلك على تخزين المعلومات الجديدة.") + '</div>', unsafe_allow_html=True)

    # --- القسم الثاني: استخدام الموبايل ---
    with tab2:
        st.markdown('## 📱 إدارة وقت الشاشة')
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            screen_time = st.slider("عدد ساعات استخدام الموبايل (ترفيه):", 1, 18, 5)
            apps = st.multiselect("أكثر التطبيقات التي تستهلك وقتك:", ["فيسبوك", "تيك توك", "يوتيوب", "ألعاب", "واتساب"])
            study_distraction = st.radio("هل يشتتك الموبايل أثناء المذاكرة؟", ["دائماً", "أحياناً", "نادراً"])
            st.markdown('</div>', unsafe_allow_html=True)
        with col_m2:
            fig_screen = px.pie(values=[screen_time, 24-screen_time], names=["وقت الشاشة", "بقية يومك"], hole=0.5, title="تأثير الموبايل على يومك")
            st.plotly_chart(fig_screen, use_container_width=True)

    # --- القسم الثالث: النشاط البدني ---
    with tab3:
        st.markdown('## 🏃 النشاط البدني والحركة')
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            active_days = st.slider("كم يوماً تمارس الرياضة أسبوعياً؟", 0, 7, 3)
            activity_type = st.selectbox("نوع النشاط المفضل:", ["مشي سريع", "جيم / قوى", "رياضة جماعية", "يوجا/تمطيط"])
            sitting_h = st.number_input("ساعات الجلوس للدراسة يومياً:", 1, 15, 6)
            st.markdown('</div>', unsafe_allow_html=True)
        with col_p2:
            # رسم بياني تخيلي للخطوات
            steps_data = pd.DataFrame({"اليوم": ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء"], "الخطوات": np.random.randint(3000, 10000, 5)})
            fig_steps = px.line(steps_data, x="اليوم", y="الخطوات", title="معدل نشاطك الأسبوعي المتوقع")
            st.plotly_chart(fig_steps, use_container_width=True)

    # --- القسم الرابع: التغذية والدراسة ---
    with tab4:
        st.markdown('## 🥗 التغذية والأداء الدراسي')
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            caffeine = st.slider("عدد أكواب المنبهات (قهوة/شاي):", 0, 10, 2)
            fast_food = st.selectbox("الوجبات السريعة أسبوعياً:", ["نادراً", "مرة واحدة", "2-3 مرات", "يومياً تقريباً"])
            fruits = st.checkbox("أتناول الفواكه والخضروات يومياً")
            breakfast = st.checkbox("أحرص على وجبة الإفطار قبل الدراسة")
            st.markdown('</div>', unsafe_allow_html=True)
        with col_f2:
            diet_points = (20 if water_daily >= 8 else 10) + (20 if fruits else 0) + (20 if breakfast else 0)
            st.write(f"### درجة التغذية الصحية: {diet_points}%")
            st.progress(diet_points / 100)
            st.info("💡 نصيحة: الإفطار والماء هما المحرك الأساسي لتركيزك في المحاضرات.")

    # --- القسم الخامس: التقرير النهائي وتحليل البيانات ---
    with tab5:
        st.markdown(f'## 📊 التحليل الشامل للطالب: {student_name}')
        st.write(f"**الجامعة:** {university} | **المستوى:** {level}")
        
        # عرض المقاييس الرئيسية بشكل احترافي
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("ساعات النوم", f"{sleep_hours} س", "جيد" if sleep_hours >= 7 else "قليل")
        with m2:
            st.metric("وقت الموبايل", f"{screen_time} س", "مرتفع" if screen_time > 6 else "مثالي", delta_color="inverse")
        with m3:
            st.metric("نقاط التغذية", f"{diet_points}%", f"{diet_points-50}%")

        st.write("---")
        
        # تحليل نهائي ذكي
        st.markdown("### 💡 التوصية الختامية المخصصة")
        if sleep_hours >= 7 and screen_time <= 5 and fruits:
            st.balloons()
            st.success(f"أنت طالب متميز يا {student_name}! نظامك الحالي يدعم صحتك النفسية والجسدية بشكل رائع. استمر في هذا المسار.")
        else:
            st.warning(f"يا {student_name}، هناك فرصة كبيرة لتحسين أدائك الدراسي. ابدأ بتقليل ساعات الموبايل ساعة واحدة فقط، وزد من ساعات نومك، وستلاحظ فرقاً كبيراً في قدرتك على الحفظ والاستيعاب.")
        
        # رسم بياني مجمع (Radar Chart - اختياري لو الداتا كترت)
        st.info(f"تاريخ إصدار التقرير: {datetime.now().strftime('%Y-%m-%d %H:%M')}")