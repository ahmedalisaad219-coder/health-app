import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Health Master Interactive", page_icon="📈", layout="wide")

# 2. تصميم "الوضوح العالي" مع لمسات تفاعلية
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #000000; }
    .header-style {
        background: #f0f9ff; padding: 30px; border-radius: 15px;
        text-align: center; border: 2px solid #3b82f6; margin-bottom: 25px;
    }
    .card-white {
        background: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;
        margin-bottom: 15px;
    }
    h1, h2, h3 { color: #1e3a8a !important; font-weight: bold; }
    p, b, span { font-size: 19px !important; }
    </style>
""", unsafe_allow_html=True)

# 3. قاعدة البيانات الضخمة (الموسوعة الشاملة)
DATABASE = {
    "نحافة": {
        "تحليل": "جسمك يحرق الطاقة بسرعة فائقة. نحتاج لخطة 'فائض سعرات' لبناء العضلات.",
        "الافطار": "4 بيضات + رغيف خبز + زبدة فول سوداني + ثمرة موز.",
        "الغداء": "200جم لحم أو دجاج + طبق أرز كبير + سلطة طحينة.",
        "العشاء": "بطاطس مهروسة + علبة تونة + كوب زبادي كامل الدسم مع عسل.",
        "الممنوعات": "تجنب شرب الماء وسط الأكل، وتجنب الوجبات السريعة الضارة.",
        "المسموحات": "المكسرات، التمر، العسل، العصائر الطبيعية، الزيوت الصحية.",
        "تفاعل": "snow"
    },
    "مثالي": {
        "تحليل": "أنت في منطقة الأمان. هدفنا هو تحسين كفاءة القلب ونحت العضلات.",
        "الافطار": "3 ملاعق فول بزيت زيتون + بيضة + نصف رغيف + خيار.",
        "الغداء": "سمك مشوي أو صدور دجاج + 6 ملاعق أرز + سلطة خضراء متنوعة.",
        "العشاء": "جبن قريش + ثمرة تفاح + كوب زبادي لايت.",
        "الممنوعات": "تجنب الإفراط في الملح والسكر للحفاظ على ضغط الدم.",
        "المسموحات": "الفواكه الموسمية، الشاي الأخضر، الشوفان، الأسماك.",
        "تفاعل": "balloons"
    },
    "زيادة وزن": {
        "تحليل": "الجسم يخزن الدهون. سنستخدم استراتيجية 'عجز السعرات' لتحويل الدهون لطاقة.",
        "الافطار": "2 بيضة مسلوقة + قطعة جبن قريش + جرجير وفلفل ألوان.",
        "الغداء": "بروتين مشوي (دجاج/لحم/سمك) + طبق خضار سوتيه كبير + ربع رغيف فقط.",
        "العشاء": "علبة زبادي بالليمون + 2 خيار.",
        "الممنوعات": "تجنب الخبز الأبيض، السكر، المقليات، والمشروبات الغازية تماماً.",
        "المسموحات": "القهوة السوداء، القرفة، الزنجبيل، الخضروات الورقية بكثرة.",
        "تفاعل": "balloons"
    }
}

# 4. واجهة المستخدم
st.markdown('<div class="header-style"><h1>🛡️ AI Health Master Pro v16</h1><p>نظام التحليل التفاعلي - ليفل الاحتراف الأقصى</p></div>', unsafe_allow_html=True)

with st.container():
    st.markdown("### 📝 بياناتك الحيوية")
    c1, c2, c3 = st.columns(3)
    with c1:
        name = st.text_input("👤 اسمك الكامل:")
    with c2:
        weight = st.number_input("⚖️ الوزن الحالي (كجم):", 30.0, 200.0, 75.0)
    with c3:
        height = st.number_input("📏 الطول (سم):", 100, 250, 175)

    goal = st.radio("🎯 اختر هدفك الحالي (سيؤثر على الرسم البياني):", ["ضخامة عضلية (زيادة)", "تنشيف دهون (نقصان)", "لياقة بدنية (ثبات)"], horizontal=True)

# 5. محرك التقرير والرسم البياني المتحرك
if st.button("🏁 إصدار التقرير التفاعلي"):
    if not name:
        st.error("⚠️ يرجى إدخال الاسم!")
    else:
        # حساب الـ BMI
        bmi = weight / ((height/100)**2)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        info = DATABASE[status]
        
        # التفاعلات البصرية
        if info["تفاعل"] == "snow": st.snow()
        else: st.balloons()
        
        st.success(f"أهلاً بك يا {name}. تم إصدار تقريرك بناءً على هدف: {goal}")
        
        # كروت النتائج
        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown(f'<div class="card-white"><h3>📊 مؤشر الكتلة (BMI)</h3><h1 style="color:#2563eb">{bmi:.1f}</h1><p>الحالة: <b>{status}</b></p></div>', unsafe_allow_html=True)
        with r2:
            st.markdown(f'<div class="card-white"><h3>🚫 الممنوعات</h3><p style="color:#dc2626">{info["الممنوعات"]}</p></div>', unsafe_allow_html=True)
        with r3:
            st.markdown(f'<div class="card-white"><h3>✅ المسموحات</h3><p style="color:#16a34a">{info["المسموحات"]}</p></div>', unsafe_allow_html=True)

        # الرسم البياني التفاعلي (المتحرك بناءً على الهدف)
        st.markdown("---")
        st.subheader(f"📈 توقعات مسار الوزن لـ {goal} (30 يوم)")
        
        # منطق تحريك الرسم البياني
        days = np.arange(30)
        if "ضخامة" in goal:
            # الخط بيطلع لفوق
            trend_data = weight + (days * 0.15) + np.random.normal(0, 0.1, 30)
        elif "تنشيف" in goal:
            # الخط بينزل لتحت
            trend_data = weight - (days * 0.18) + np.random.normal(0, 0.1, 30)
        else:
            # الخط بيتحرك بالعرض (ثبات)
            trend_data = weight + np.random.normal(0, 0.2, 30)
            
        chart_df = pd.DataFrame({"الوزن المتوقع": trend_data}, index=days)
        st.line_chart(chart_df)

        # تفاصيل النظام الغذائي
        st.markdown("### 🥘 نظام الوجبات اليومي المخصص")
        m1, m2, m3 = st.columns(3)
        m1.info(f"**🍳 الإفطار:**\n\n{info['الافطار']}")
        m2.success(f"**🥘 الغداء:**\n\n{info['الغداء']}")
        m3.warning(f"**🥣 العشاء:**\n\n{info['العشاء']}")
        
        st.markdown(f"**🔬 تحليل الخبراء:** {info['تحليل']}")
else:
    st.info("👋 بانتظار بياناتك لتحويل الموقع إلى لوحة تحكم تفاعلية!")