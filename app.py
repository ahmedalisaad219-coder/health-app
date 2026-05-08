import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Health Hub Ultra", page_icon="💊", layout="wide")

# 2. تصميم الواجهة (Light Professional)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    .main-title {
        background: #f8fafc; padding: 35px; border-radius: 20px;
        text-align: center; border-bottom: 6px solid #2563eb;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 30px;
    }
    .metric-box {
        background: white; padding: 20px; border-radius: 15px;
        border: 1px solid #e2e8f0; text-align: center;
    }
    .supp-card {
        background: #f0f9ff; padding: 15px; border-radius: 12px;
        border-right: 5px solid #0077b6; margin-bottom: 10px;
    }
    h1, h2, h3 { color: #1e3a8a !important; }
    .stButton>button {
        background: #2563eb; color: white !important; border-radius: 12px;
        height: 55px; font-weight: bold; width: 100%; border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 3. قاعدة البيانات الشاملة (وجبات + تمارين + مكملات)
MASTER_DATA = {
    "نحافة": {
        "تحليل": "تحتاج لزيادة الكتلة العضلية (Bulking).",
        "وجبات": ["إفطار: بيض وشوفان", "غداء: أرز ودجاج", "عشاء: مكرونة وتونة"],
        "تمارين": ["رفع أثقال ثقيلة", "تكرارات متوسطة (8-10)", "راحة طويلة"],
        "مكملات": [
            {"اسم": "Mass Gainer", "فوائد": "لزيادة السعرات والوزن بسرعة."},
            {"اسم": "Creatine Monohydrate", "فوائد": "لزيادة القوة البدنية وحجم العضلات."},
            {"اسم": "Multivitamins", "فوائد": "لتعزيز النشاط والحيوية."}
        ],
        "لون": "#3b82f6"
    },
    "مثالي": {
        "تحليل": "الحفاظ على الكتلة العضلية وتحسين التنشيف (Lean).",
        "وجبات": ["إفطار: زبادي وتوت", "غداء: سمك وسلطة", "عشاء: جبن قريش"],
        "تمارين": ["تمرين شامل للجسد", "كارديو مرتين أسبوعياً", "تحسين المرونة"],
        "مكملات": [
            {"اسم": "Whey Protein Isolate", "فوائد": "لبناء العضلات بدون دهون."},
            {"اسم": "Omega 3", "فوائد": "لصحة القلب والمفاصل."},
            {"اسم": "BCAA", "فوائد": "لسرعة الاستشفاء العضلي بعد التمرين."}
        ],
        "لون": "#fbbf24"
    },
    "زيادة وزن": {
        "تحليل": "حرق الدهون مع الحفاظ على العضلات (Shredding).",
        "وجبات": ["إفطار: بيض مسلوق وجرجير", "غداء: بروتين مشوي وخضار", "عشاء: زبادي بالليمون"],
        "تمارين": ["تمارين HIIT (عالية الكثافة)", "مشي سريع يومي", "رفع أثقال خفيفة"],
        "مكملات": [
            {"اسم": "L-Carnitine", "فوائد": "للمساعدة في تحويل الدهون لطاقة."},
            {"اسم": "Caffeine/Pre-workout", "فوائد": "لزيادة معدل الحرق والتركيز."},
            {"اسم": "Casein Protein", "فوائد": "بروتين بطيء الامتصاص للشعور بالشبع."}
        ],
        "لون": "#10b981"
    }
}

# 4. واجهة المستخدم
st.markdown('<div class="main-title"><h1>🛡️ AI Health Hub: Elite Edition</h1><p>نظام التحليل المتطور + دليل المكملات الذكي</p></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    name = st.text_input("👤 الاسم:")
with c2:
    weight = st.number_input("⚖️ الوزن (كجم):", 30.0, 200.0, 75.0)
with c3:
    height = st.number_input("📏 الطول (سم):", 100, 250, 175)

goal = st.selectbox("🎯 حدد هدفك بدقة:", ["ضخامة عضلية", "تنشيف دهون", "لياقة عامة"])

if st.button("🚀 تحليل البيانات واستعراض الدليل"):
    if not name:
        st.warning("يرجى إدخال اسمك")
    else:
        bmi = weight / ((height/100)**2)
        status = "نحافة" if bmi < 18.5 else "مثالي" if bmi < 25 else "زيادة وزن"
        data = MASTER_DATA[status]
        
        st.balloons()
        st.markdown(f"### 📑 التقرير الكامل للبطل: {name}")
        
        # كروت النتائج
        r1, r2, r3 = st.columns(3)
        r1.markdown(f'<div class="metric-box"><h3>BMI</h3><h2 style="color:{data["لون"]}">{bmi:.1f}</h2><p>{status}</p></div>', unsafe_allow_html=True)
        r2.markdown(f'<div class="metric-box"><h3>وزنك المثالي</h3><h2>{int(22 * ((height/100)**2))}</h2><p>كجم</p></div>', unsafe_allow_html=True)
        r3.markdown(f'<div class="metric-box"><h3>الحالة</h3><p>{data["تحليل"]}</p></div>', unsafe_allow_html=True)

        st.write("---")

        # الرسم البياني
        st.subheader("📈 توقعات تطور الوزن")
        change = 0.15 if "ضخامة" in goal else -0.18 if "تنشيف" in goal else 0.02
        y = weight + (np.arange(30) * change)
        st.line_chart(pd.DataFrame(y, columns=["الوزن"]), color=data["لون"])

        # توزيع البيانات الجديدة (الوجبات + التمارين + المكملات)
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.info("🍱 **خطة الوجبات**")
            for meal in data["وجبات"]:
                st.write(f"✅ {meal}")
                
        with col_res2:
            st.warning("💪 **الخطة التدريبية**")
            for exercise in data["تمارين"]:
                st.write(f"🔥 {exercise}")
                
        with col_res3:
            st.success("💊 **المكملات المقترحة**")
            for supp in data["مكملات"]:
                st.markdown(f"""
                <div class="supp-card">
                    <b>{supp['اسم']}</b><br>
                    <small>{supp['فوائد']}</small>
                </div>
                """, unsafe_allow_html=True)

else:
    st.info("👋 أدخل بياناتك لفتح 'دليل المكملات' والتقرير الشامل!")