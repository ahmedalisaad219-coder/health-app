import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة الفاخرة
st.set_page_config(page_title="AI Health Hub Ultra", page_icon="🔥", layout="wide")

# 2. تصميم واجهة احترافية (Glassmorphism UI)
st.markdown("""
    <style>
    .stApp { background: #0f172a; color: white; }
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 50px; border-radius: 30px; text-align: center;
        margin-bottom: 30px; border: 1px solid rgba(255,255,255,0.1);
    }
    .stat-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px; border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: 0.3s;
    }
    .stat-card:hover { transform: translateY(-5px); border-color: #3b82f6; }
    .badge {
        background: #fbbf24; color: black; padding: 5px 15px;
        border-radius: 50px; font-weight: bold; font-size: 12px;
    }
    label { color: #cbd5e1 !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. الموسوعة الكاملة (داتا 100%)
DATABASE = {
    "نحافة": {
        "تحليل": "جسمك يحتاج لبناء كتلة عضلية وزيادة الكثافة الغذائية. أنت في مرحلة 'البناء الاستراتيجي'.",
        "سوبر_فود": ["زبدة الفول السوداني", "الموز والشوفان", "البيض الكامل", "المكسرات النيئة"],
        "الرياضة": "تمارين المقاومة (رفع أثقال) مع فترات راحة طويلة.",
        "تحدي": "إضافة وجبة إضافية غنية بالبروتين قبل النوم.",
        "وسام": "🎖️ صانع العضلات",
        "تفاعل": "snow"
    },
    "مثالي": {
        "تحليل": "أنت في منطقة التوازن الذهبي. هدفنا الآن هو صقل العضلات وزيادة المرونة والتحمل.",
        "سوبر_فود": ["بذور الشيا", "صدور الدجاج", "الخضروات الورقية", "التوت"],
        "الرياضة": "تدريبات شاملة (Cardio + Strength) 4 مرات أسبوعياً.",
        "تحدي": "تحدي 10 آلاف خطوة يومياً لمدة أسبوع.",
        "وسام": "💎 البطل المتوازن",
        "تفاعل": "balloons"
    },
    "زيادة وزن": {
        "تحليل": "الجسم في حالة تخزين طاقة زائدة. سنعمل على تحويل الجسم لـ 'ماكينة حرق دهون'.",
        "سوبر_فود": ["البروكلي والسبانخ", "التونة", "البيض المسلوق", "الجريب فروت"],
        "الرياضة": "تمارين عالية الكثافة (HIIT) مع مشي سريع يومياً.",
        "تحدي": "منع السكريات المضافة والمخبوزات البيضاء تماماً.",
        "وسام": "🔥 محارب الدهون",
        "تفاعل": "balloons"
    }
}

# 4. الواجهة الرئيسية
st.markdown('<div class="main-header"><h1>🚀 AI Health Tracker Ultra</h1><p>نظام تحليل الأداء البشري المطور - ليفل الاحتراف</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2964/2964514.png", width=100)
    st.title("لوحة التحكم")
    name = st.text_input("👤 اسم المستخدم:", placeholder="أدخل اسمك...")
    st.write("---")
    st.success("النسخة المتطورة تعمل بكفاءة ✅")

# إدخال البيانات في كروت
col_in1, col_in2 = st.columns(2)
with col_in1:
    st.markdown("### 📊 القياسات الحيوية")
    weight = st.number_input("الوزن (كجم):", 30.0, 200.0, 75.0)
    height = st.number_input("الطول (سم):", 100, 250, 175)
with col_in2:
    st.markdown("### 🎯 الأهداف والعادات")
    goal = st.selectbox("هدفك الرئيسي:", ["خسارة دهون", "بناء عضلات", "لياقة بدنية"])
    water = st.slider("شرب الماء (أكواب):", 0, 20, 8)

# 5. محرك التحليل والنتائج
if st.button("🏁 تفعيل التحليل العميق"):
    if not name:
        st.error("⚠️ يرجى إدخال اسمك أولاً لفتح التقرير!")
    else:
        bmi = weight / ((height/100)**2)
        status = "نحافة" if bmi < 18.5 else "مثالي" if bmi < 25 else "زيادة وزن"
        data = DATABASE[status]
        
        # التفاعلات
        if data["تفاعل"] == "snow": st.snow()
        else: st.balloons()
        
        st.markdown(f"## 🏆 تقرير الأداء الخاص بـ {name}")
        
        # صف النتائج (Cards)
        r1, r2, r3, r4 = st.columns(4)
        with r1:
            st.markdown(f'<div class="stat-card"><h3>⚖️ BMI</h3><h2 style="color:#3b82f6">{bmi:.1f}</h2><p>{status}</p></div>', unsafe_allow_html=True)
        with r2:
            score = (water * 10)
            st.markdown(f'<div class="stat-card"><h3>⭐ سكور</h3><h2 style="color:#10b981">{min(score, 100)}%</h2><p>نقاط الالتزام</p></div>', unsafe_allow_html=True)
        with r3:
            st.markdown(f'<div class="stat-card"><h3>🛡️ الوسام</h3><br><span class="badge">{data["وسام"]}</span></div>', unsafe_allow_html=True)
        with r4:
            bmr = 10 * weight + 6.25 * height - 5 * 25 # متوسط
            st.markdown(f'<div class="stat-card"><h3>🔥 الحرق</h3><h2 style="color:#f59e0b">{int(bmr)}</h2><p>سعرة حرارية</p></div>', unsafe_allow_html=True)

        st.markdown("---")
        
        # تفاصيل الموسوعة
        res_col1, res_col2 = st.columns([1.5, 1])
        with res_col1:
            st.markdown(f"### 🔬 التحليل العلمي العميق")
            st.info(data["تحليل"])
            st.markdown("### 📈 مسار التطور المتوقع (30 يوم)")
            change = -0.15 if "خسارة" in goal else 0.12 if "بناء" in goal else 0.02
            future = [weight + (i * change) for i in range(30)]
            st.line_chart(future)
            
        with res_col2:
            st.markdown("### 🥗 السوبر فود الموصى به")
            for food in data["سوبر_فود"]:
                st.success(f"🔹 {food}")
            st.markdown("### 🏋️ التوجيه الرياضي")
            st.warning(data["الرياضة"])
            st.error(f"🚩 تحدي الأسبوع: {data['تحدي']}")
else:
    st.info("👋 بانتظار إدخال بياناتك لإظهار القوة الكاملة للنظام!")