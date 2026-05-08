import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="AI Health Tracker", page_icon="💪")

# 2. قاموس البيانات الموحد (تم إصلاح المسميات لمنع KeyError)
HEALTH_DB = {
    "نحافة": {
        "تحليل": "وزنك أقل من الطبيعي، تحتاج لزيادة السعرات الصحية.",
        "نصيحة": "ركز على تناول الكربوهيدرات المعقدة والبروتين.",
        "اللون": "#3b82f6"
    },
    "مثالي": {
        "تحليل": "وزنك في النطاق الصحي المثالي، استمر على هذا المنوال!",
        "نصيحة": "حافظ على التوازن بين الغذاء والنشاط البدني.",
        "اللون": "#10b981"
    },
    "زيادة وزن": {
        "تحليل": "وزنك أعلى من النطاق المثالي، يفضل البدء بنظام غذائي.",
        "نصيحة": "قلل من السكريات المضافة وزد من شرب الماء والحركة.",
        "اللون": "#f59e0b"
    }
}

# 3. واجهة المستخدم (التصميم)
st.title("🛡️ المستشار الصحي الذكي")
st.write("أدخل بياناتك للحصول على تحليل فوري ومسار توقع للوزن.")

with st.form("health_form"):
    name = st.text_input("👤 الاسم:")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("⚖️ الوزن (كجم):", 30.0, 200.0, 70.0)
    with col2:
        height = st.number_input("📏 الطول (سم):", 100, 250, 170)
    
    goal = st.selectbox("🎯 هدفك:", ["خسارة وزن", "بناء عضلات", "صحة عامة"])
    submit = st.form_submit_button("إصدار التقرير")

# 4. محرك التحليل
if submit:
    if not name:
        st.warning("يرجى إدخال اسمك.")
    else:
        # حساب مؤشر كتلة الجسم BMI
        bmi = weight / ((height/100)**2)
        
        # تحديد الحالة (Logic)
        if bmi < 18.5: status = "نحافة"
        elif bmi < 25: status = "مثالي"
        else: status = "زيادة وزن"
        
        # جلب البيانات من القاموس (بدون KeyError)
        data = HEALTH_DB[status]
        
        # عرض النتائج
        st.balloons()
        st.success(f"أهلاً بك يا {name}! إليك تقريرك:")
        
        st.metric("مؤشر كتلة جسمك (BMI)", f"{bmi:.1f}", status)
        
        st.info(f"🔬 **التحليل:** {data['تحليل']}")
        st.warning(f"💡 **نصيحة الخبراء:** {data['نصيحة']}")
        
        # 5. رسم بياني بسيط (باستخدام مكتبة ستريمليت الأساسية فقط)
        st.subheader("📈 مسار الوزن المتوقع (30 يوم)")
        change = -0.15 if goal == "خسارة وزن" else 0.1 if goal == "بناء عضلات" else 0.02
        predictions = [weight + (i * change) for i in range(30)]
        st.line_chart(predictions)

else:
    st.info("قم بملء النموذج أعلاه واضغط على زر التقرير.")