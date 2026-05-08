import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Health Expert Pro", page_icon="🥗", layout="wide")

# 2. تصميم "الوضوح العالي" (Light & Professional)
st.markdown("""
    <style>
    /* خلفية فاتحة ومريحة */
    .stApp { background-color: #f8fafc; color: #1e293b; }
    
    /* الهيدر الرئيسي */
    .header-box {
        background: #ffffff; padding: 40px; border-radius: 20px;
        text-align: center; border-bottom: 5px solid #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 30px;
    }
    
    /* الكروت البيضاء الواضحة */
    .data-card {
        background: white; padding: 25px; border-radius: 15px;
        border: 1px solid #e2e8f0; margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* توضيح الخطوط */
    h1, h2, h3 { color: #0f172a !important; font-weight: 800 !important; }
    p, li { font-size: 18px !important; line-height: 1.6; color: #334155; }
    
    /* الأزرار */
    .stButton>button {
        background: #3b82f6; color: white !important; font-weight: bold;
        border-radius: 12px; height: 55px; width: 100%; border: none; font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الموسوعة العملاقة (Full Database)
# تم تحديث المسميات لضمان عدم حدوث KeyError
MASTER_DATA = {
    "نحافة": {
        "التحليل": "جسمك يحرق السعرات بسرعة عالية. الهدف هو 'تضخيم صحي' لزيادة الكتلة العضلية وليس الدهون فقط.",
        "وجبة_الافطار": "3 بيضات مسلوقة + رغيف خبز كامل + نصف أفوكادو + كوب عصير برتقال طبيعي.",
        "وجبة_الغداء": "صدر دجاج مشوي (200جم) + طبق كبير أرز بسمتي + سلطة بزيت الزيتون.",
        "وجبة_العشاء": "علبة تونة بالزيت + بطاطس مهروسة + كوب زبادي كامل الدسم مع عسل.",
        "سوبر_فود": ["المكسرات النيئة", "زبدة الفول السوداني", "التمر", "البطاطا الحلوة"],
        "نصيحة_نفسية": "لا تستعجل النتائج، بناء العضلات يحتاج استمرارية في الأكل التمرين.",
        "تفاعل": "snow"
    },
    "مثالي": {
        "التحليل": "أنت في أفضل حالاتك الصحية. الهدف الآن هو 'النحت' والحفاظ على مرونة الشرايين وكفاءة القلب.",
        "وجبة_الافطار": "أومليت بالخضروات + شريحة توست أسمر + كوب شاي أخضر.",
        "وجبة_الغداء": "سمك مشوي (أو تونة) + 5 ملاعق أرز + طبق سلطة خضراء عملاق.",
        "وجبة_العشاء": "جبن قريش بالزعتر وزيت الزيتون + خيار + زبادي لايت.",
        "سوبر_فود": ["بذور الشيا", "التوت", "السبانخ", "الجوز (عين الجمل)"],
        "نصيحة_نفسية": "التوازن هو سر الحياة، كافئ نفسك بوجبة تحبها مرة أسبوعياً.",
        "تفاعل": "balloons"
    },
    "زيادة وزن": {
        "التحليل": "الجسم لديه مخزون طاقة عالي. سنعتمد على 'تنشيط الأيض' وتحويل الجسم لحرق الدهون المخزنة.",
        "وجبة_الافطار": "2 بيضة مسلوقة (بدون صفار) + قطعة جبن قريش + جرجير وفلفل ألوان.",
        "وجبة_الغداء": "لحم أحمر مشوي أو مسلوق + خضار سوتيه (كوسة وفاصوليا) + سلطة مع خل تفاح.",
        "وجبة_العشاء": "زبادي بالليمون والقرفة + ثمرة فاكهة واحدة (تفاح أو كمثرى).",
        "سوبر_فود": ["البروكلي", "القهوة السوداء", "القرفة", "الشوفان بكمية قليلة"],
        "نصيحة_نفسية": "اشرب الماء بكثرة قبل الأكل، فهو يخدع المعدة ويقلل الشهية.",
        "تفاعل": "balloons"
    }
}

# 4. واجهة التطبيق (واضحة جداً)
st.markdown('<div class="header-box"><h1>🛡️ AI Health Expert Pro v15</h1><p>نظام التحليل الصحي عالي الوضوح والدقة</p></div>', unsafe_allow_html=True)

# المدخلات في حاويات منظمة
with st.container():
    st.markdown("### 📝 بياناتك الشخصية")
    c1, c2, c3 = st.columns(3)
    with c1:
        name = st.text_input("الاسم بالكامل:")
    with c2:
        weight = st.number_input("الوزن الحالي (كجم):", 30.0, 200.0, 70.0)
    with c3:
        height = st.number_input("الطول الحالي (سم):", 100, 250, 170)

# 5. زر التنفيذ
if st.button("🚀 إصدار التقرير الصحي الكامل"):
    if not name:
        st.error("⚠️ من فضلك اكتب الاسم أولاً!")
    else:
        # حساب الـ BMI
        bmi = weight / ((height/100)**2)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        # جلب الداتا الكاملة
        info = MASTER_DATA[status]
        
        # التفاعلات
        if info["تفاعل"] == "snow": st.snow()
        else: st.balloons()
        
        st.markdown(f"## 📊 التقرير التحليلي للبطل: {name}")
        
        # كروت النتائج الأساسية
        res1, res2, res3 = st.columns(3)
        with res1:
            st.markdown(f'<div class="data-card"><h3>📏 مؤشر الكتلة (BMI)</h3><h1 style="color:#2563eb">{bmi:.1f}</h1><p>الحالة: <b>{status}</b></p></div>', unsafe_allow_html=True)
        with res2:
            st.markdown(f'<div class="data-card"><h3>❤️ نصيحة نفسية</h3><p>{info["نصيحة_نفسية"]}</p></div>', unsafe_allow_html=True)
        with res3:
            st.markdown(f'<div class="data-card"><h3>🌟 سوبر فود</h3><p>{", ".join(info["سوبر_فود"])}</p></div>', unsafe_allow_html=True)
            
        st.markdown("---")
        
        # خطة الوجبات (الداتا الزائدة)
        st.markdown("### 🍱 خطة الوجبات اليومية المقترحة")
        meal_c1, meal_c2, meal_c3 = st.columns(3)
        meal_c1.info(f"**🍳 الإفطار:**\n\n{info['وجبة_الافطار']}")
        meal_c2.success(f"**🥘 الغداء:**\n\n{info['وجبة_غداء'] if 'وجبة_غداء' in info else info['وجبة_الغداء']}")
        meal_c3.warning(f"**🥣 العشاء:**\n\n{info['وجبة_العشاء']}")
        
        # الرسم البياني
        st.write("---")
        st.markdown("### 📈 توقعات مسار الوزن (الـ 30 يوم القادمة)")
        change = -0.12 if status == "زيادة وزن" else 0.1 if status == "نحافة" else 0.01
        trend = [weight + (i * change) for i in range(30)]
        st.line_chart(trend)
        
        st.markdown(f"**🔬 تحليل الخبير:** {info['التحليل']}")

else:
    st.info("👋 بانتظار بياناتك لتحويلها إلى تقرير طبي شامل!")