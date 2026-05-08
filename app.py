import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Health Hub Pro", page_icon="🏆", layout="wide")

# 2. تصميم "الوضوح العالي" 
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    .main-title {
        background: white; padding: 35px; border-radius: 20px;
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

# 3. قاعدة البيانات (الوجبات والتمارين فقط)
MASTER_DATABASE = {
    "نحافة": {
        "تحليل": "هدفك هو 'الضخامة العضلية'. سنركز على زيادة السعرات من مصادر صحية لبناء الجسم.",
        "الافطار": "4 بيضات مسلوقة + رغيف خبز + زبدة فول سوداني + ثمرة موز.",
        "الغداء": "200جم بروتين + طبق أرز كبير + سلطة طحينة + بطاطس مشوية.",
        "العشاء": "علبة تونة + طبق مكرونة بالوايت صوص + كوب زبادي بالعسل.",
        "تمارين": ["يوم 1: صدر وتراي", "يوم 2: ضهر وباي", "يوم 3: راحة", "يوم 4: أرجل", "يوم 5: كتف وبطن"],
        "لون_الرسم": "#3b82f6"
    },
    "مثالي": {
        "تحليل": "أنت في منطقة الأمان. سنركز على نحت العضلات وتحسين اللياقة البدنية العامة.",
        "الافطار": "شوفان بالحليب والتوت + بيضة واحدة + شاي أخضر.",
        "الغداء": "سمك مشوي + 5 ملاعق أرز + طبق سلطة خضراء ضخم.",
        "العشاء": "جبن قريش بالزعتر + خيار + تفاحة.",
        "تمارين": ["3 أيام تمرين شامل (Full Body)", "يومين كارديو (جري/سباحة)", "يومين راحة"],
        "لون_الرسم": "#fbbf24"
    },
    "زيادة وزن": {
        "تحليل": "هدفك هو 'حرق الدهون'. سنعتمد على تقليل الكربوهيدرات لرفع معدل الحرق اليومي.",
        "الافطار": "3 بيضات مسلوقة + جرجير + قطعة جبن قريش + ربع رغيف.",
        "الغداء": "بروتين مشوي (لحم/دجاج) + خضار سوتيه مفتوح الكمية + سلطة خل تفاح.",
        "العشاء": "زبادي بالليمون + 2 خيار + كوب قرفة.",
        "تمارين": ["4 أيام كارديو عالي الكثافة (HIIT)", "يومين رفع أثقال خفيفة", "يوم مشي طويل"],
        "لون_الرسم": "#10b981"
    }
}

# 4. الواجهة الرئيسية
st.markdown('<div class="main-title"><h1>🏆 AI Health Master: Pro Edition</h1><p>نظام التحليل الصحي المتكامل (سعرات - تمارين - وجبات)</p></div>', unsafe_allow_html=True)

with st.container():
    st.markdown("### 📝 الملف الشخصي")
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

# 5. الحسابات والنتائج
if st.button("🏁 إصدار التقرير النهائي"):
    if not name:
        st.error("⚠️ يرجى إدخال الاسم!")
    else:
        # حساب الـ BMI
        bmi = weight / ((height/100)**2)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        info = MASTER_DATABASE[status]
        
        # حساب السعرات
        if gender == "ذكر":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        
        tdee = bmr * 1.375
        if "ضخامة" in goal_type: target_calories = tdee + 500
        elif "تنشيف" in goal_type: target_calories = tdee - 500
        else: target_calories = tdee

        st.balloons()
        st.markdown(f"## 📑 تقرير البطل: {name}")

        # كروت الأرقام
        r1, r2, r3, r4 = st.columns(4)
        r1.markdown(f'<div class="metric-box"><h3>BMI</h3><h2 style="color:{info["لون_الرسم"]}">{bmi:.1f}</h2><p>{status}</p></div>', unsafe_allow_html=True)
        r2.markdown(f'<div class="metric-box"><h3>السعرات/يوم</h3><h2 style="color:#2563eb">{int(target_calories)}</h2><p>هدف يومي</p></div>', unsafe_allow_html=True)
        r3.markdown(f'<div class="metric-box"><h3>الوزن المثالي</h3><h2 style="color:#10b981">{int(22 * ((height/100)**2))}</h2><p>كجم</p></div>', unsafe_allow_html=True)
        r4.markdown(f'<div class="metric-box"><h3>معدل الحرق</h3><h2 style="color:#f59e0b">{int(bmr)}</h2><p>BMR</p></div>', unsafe_allow_html=True)

        st.markdown("---")

        # الرسم البياني التفاعلي
        st.subheader(f"📈 مسار الوزن المتوقع لـ {goal_type}")
        days = np.arange(30)
        if "ضخامة" in goal_type:
            y = weight + (days * 0.12) + np.random.normal(0, 0.05, 30)
        elif "تنشيف" in goal_type:
            y = weight - (days * 0.15) + np.random.normal(0, 0.05, 30)
        else:
            y = weight + np.random.normal(0, 0.1, 30)
        
        df_chart = pd.DataFrame(y, index=days, columns=["الوزن"])
        st.line_chart(df_chart, color=info["لون_الرسم"])

        # الوجبات والتمارين
        st.markdown("### 🥗 الخطة التدريبية والغذائية")
        col_res1, col_res2 = st.columns([1.2, 0.8])
        
        with col_res1:
            st.success("**🍱 خطة الوجبات المقترحة**")
            st.write(f"🍳 **الإفطار:** {info['الافطار']}")
            st.write(f"🥘 **الغداء:** {info['الغداء']}")
            st.write(f"🥣 **العشاء:** {info['العشاء']}")
            st.info(f"🔬 **تحليل الحالة:** {info['تحليل']}")
            
        with col_res2:
            st.warning("**💪 جدول التمرين الأسبوعي**")
            for day in info['تمارين']:
                st.write(f"✅ {day}")
            st.write("---")
            st.write("💧 **نصيحة:** اشرب 3-4 لتر ماء يومياً.")

else:
    st.info("👋 أدخل بياناتك للحصول على التحليل النهائي بدون بدائل!")