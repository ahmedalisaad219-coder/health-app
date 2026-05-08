import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة الفخمة
st.set_page_config(page_title="AI Health Hub Pro MAX", page_icon="🏆", layout="wide")

# 2. تصميم "الوضوح الفائق" (Bright Luxury UI)
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; color: #1a1a1a; }
    .main-title {
        background: white; padding: 40px; border-radius: 20px;
        text-align: center; border-bottom: 6px solid #2563eb;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); margin-bottom: 30px;
    }
    .metric-box {
        background: white; padding: 25px; border-radius: 15px;
        border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
    }
    h1, h2, h3 { color: #1e3a8a !important; font-family: 'Segoe UI', sans-serif; }
    p, li, b { font-size: 18px !important; }
    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #3b82f6);
        color: white !important; border-radius: 15px; height: 60px;
        font-weight: bold; font-size: 22px; border: none; width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الموسوعة الغذائية والتدريبية (Mega Database)
MASTER_DATABASE = {
    "نحافة": {
        "تحليل": "هدفنا هو 'الضخامة العضلية'. سنقوم بزيادة كثافة الوجبات لرفع الوزن بشكل صحي.",
        "الافطار": "4 بيضات + 2 توست زبدة فول سوداني + موزة.",
        "الغداء": "200جم بروتين + طبق أرز كبير + سلطة طحينة + بطاطس مشوية.",
        "العشاء": "علبة تونة + طبق مكرونة بالوايت صوص + كوب زبادي بالعسل.",
        "بديل_ذكي": "يمكنك استبدال التونة بصدر دجاج أو جبن قريش بضعف الكمية.",
        "تمارين": ["يوم 1: صدر وتراي", "يوم 2: ضهر وباي", "يوم 3: راحة", "يوم 4: أرجل", "يوم 5: كتف وبطن"],
        "لون_الرسم": "#3b82f6" # أزرق للنمو
    },
    "مثالي": {
        "تحليل": "هدفنا 'النحت والتحمل'. سنركز على جودة البروتين والألياف للحفاظ على الرشاقة.",
        "الافطار": "شوفان بالحليب والتوت + بيضة واحدة + شاي أخضر.",
        "الغداء": "سمك مشوي + 5 ملاعق أرز + طبق سلطة خضراء ضخم.",
        "العشاء": "جبن قريش بالزعتر + خيار + تفاحة.",
        "بديل_ذكي": "يمكن استبدال الشوفان بزبادي يوناني مع مكسرات نيئة.",
        "تمارين": ["3 أيام تمرين شامل (Full Body)", "يومين كارديو (جري/سباحة)", "يومين راحة"],
        "لون_الرسم": "#fbbf24" # ذهبي للثبات
    },
    "زيادة وزن": {
        "تحليل": "هدفنا 'حرق الدهون'. سنعتمد على تقليل الكربوهيدرات وزيادة معدل الحرق اليومي.",
        "الافطار": "3 بيضات مسلوقة + جرجير + قطعة جبن قريش + ربع رغيف.",
        "الغداء": "بروتين مشوي (لحم/دجاج) + خضار سوتيه مفتوح الكمية + سلطة خل تفاح.",
        "العشاء": "زبادي بالليمون + 2 خيار + كوب قرفة.",
        "بديل_ذكي": "يمكن استبدال اللحم الأحمر بصدور الدجاج أو سمك الماكريل.",
        "تمارين": ["4 أيام كارديو عالي الكثافة (HIIT)", "يومين رفع أثقال خفيفة", "يوم مشي طويل"],
        "لون_الرسم": "#10b981" # أخضر للحرق
    }
}

# 4. واجهة المستخدم المدعمة بالمنطق الرياضي
st.markdown('<div class="main-title"><h1>🏆 AI Health Master: Infinite Edition</h1><p>نظام التحليل التفاعلي المتكامل (سعرات - تمارين - وجبات)</p></div>', unsafe_allow_html=True)

with st.container():
    st.markdown("### 📝 الملف الصحي")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        name = st.text_input("👤 الاسم:")
        age = st.number_input("🎂 العمر:", 10, 100, 25)
    with c2:
        weight = st.number_input("⚖️ الوزن (كجم):", 30.0, 200.0, 75.0)
    with c3:
        height = st.number_input("📏 الطول (سم):", 100, 250, 175)
    with c4:
        gender = st.selectbox("🚻 النوع:", ["ذكر", "أنثى"])
        goal_type = st.selectbox("🎯 الهدف:", ["تنشيف وحرق", "ضخامة وبناء", "لياقة وثبات"])

# 5. محرك الحسابات (BMR & TDEE)
if st.button("🏁 تحليل القوة القصوى"):
    if not name:
        st.error("⚠️ يرجى إدخال الاسم لفتح التقرير!")
    else:
        # حساب الـ BMI
        bmi = weight / ((height/100)**2)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        info = MASTER_DATABASE[status]
        
        # حساب السعرات (معادلة Mifflin-St Jeor)
        if gender == "ذكر":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        
        # تعديل السعرات حسب الهدف
        tdee = bmr * 1.375 # نشاط متوسط
        if "ضخامة" in goal_type: target_calories = tdee + 500
        elif "تنشيف" in goal_type: target_calories = tdee - 500
        else: target_calories = tdee

        st.balloons()
        st.markdown(f"## 📑 تقرير التحليل الشامل للبطل: {name}")

        # كروت الأرقام الملونة
        r1, r2, r3, r4 = st.columns(4)
        r1.markdown(f'<div class="metric-box"><h3>BMI</h3><h2 style="color:{info["لون_الرسم"]}">{bmi:.1f}</h2><p>{status}</p></div>', unsafe_allow_html=True)
        r2.markdown(f'<div class="metric-box"><h3>السعرات المطلوبة</h3><h2 style="color:#2563eb">{int(target_calories)}</h2><p>سعرة/يوم</p></div>', unsafe_allow_html=True)
        r3.markdown(f'<div class="metric-box"><h3>وزنك المثالي</h3><h2 style="color:#10b981">{int(22 * ((height/100)**2))}</h2><p>كجم تقريباً</p></div>', unsafe_allow_html=True)
        r4.markdown(f'<div class="metric-box"><h3>نسبة الحرق</h3><h2 style="color:#f59e0b">{int(bmr)}</h2><p>BMR الأساسي</p></div>', unsafe_allow_html=True)

        st.markdown("---")

        # الرسوم البيانية التفاعلية الملونة
        st.subheader(f"📈 مسار تطور الوزن المتوقع لـ {goal_type}")
        days = np.arange(30)
        if "ضخامة" in goal_type:
            y = weight + (days * 0.12) + np.random.normal(0, 0.05, 30)
        elif "تنشيف" in goal_type:
            y = weight - (days * 0.15) + np.random.normal(0, 0.05, 30)
        else:
            y = weight + np.random.normal(0, 0.1, 30)
        
        df_chart = pd.DataFrame(y, index=days, columns=["الوزن"])
        st.line_chart(df_chart, color=info["لون_الرسم"])

        # داتا الوجبات والتمارين (الضخامة المعلوماتية)
        st.markdown("### 🏋️ النظام التدريبي والغذائي المتكامل")
        tab1, tab2, tab3 = st.tabs(["🍎 خطة الوجبات", "💪 جدول التمرين", "🔄 البدائل الذكية"])
        
        with tab1:
            st.info(f"🔬 **التحليل:** {info['تحليل']}")
            c_m1, c_m2, c_m3 = st.columns(3)
            c_m1.success(f"**🍳 الإفطار:**\n\n{info['الافطار']}")
            c_m2.success(f"**🥘 الغداء:**\n\n{info['الغداء']}")
            c_m3.success(f"**🥣 العشاء:**\n\n{info['العشاء']}")
            
        with tab2:
            st.warning("⚠️ اتبع هذا الجدول لمدة 4 أسابيع للحصول على نتائج ملحوظة:")
            for day in info['تمارين']:
                st.write(f"✅ {day}")
                
        with tab3:
            st.help(f"**💡 نصيحة التبديل:** {info['بديل_ذكي']}")
            st.write("---")
            st.write("🚀 **تذكر:** الالتزام بالماء (3 لتر يومياً) يسرع النتائج بنسبة 40%!")

else:
    st.info("👋 بانتظار بياناتك لتحويلها إلى ذكاء اصطناعي صحي متكامل!")