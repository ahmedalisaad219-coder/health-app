import streamlit as st

st.set_page_config(page_title="نظامي الصحي", page_icon="🏥")

st.title("🏥 المستشار الصحي الذكي")
st.write("أدخل بياناتك للحصول على الحلول الصحية")

name = st.text_input("الاسم:")
weight = st.number_input("الوزن (كجم):", value=70.0)
height = st.number_input("الطول (سم):", value=170.0)
phone_hours = st.number_input("ساعات استخدام الموبايل:", value=4.0)
workout_days = st.number_input("أيام الرياضة أسبوعياً:", value=2)

if st.button("عرض التقرير والعلاج"):
    bmi = weight / ((height/100)**2)
    st.subheader(f"📊 تقرير {name}")
    
    if bmi < 18.5:
        st.error(f"المؤشر {bmi:.1f}: نحافة. العلاج: زد البروتين والنشويات.")
    elif 18.5 <= bmi < 25:
        st.success(f"المؤشر {bmi:.1f}: مثالي. استمر!")
    else:
        st.warning(f"المؤشر {bmi:.1f}: زيادة وزن. العلاج: قلل السكر وامشِ أكثر.")

    if phone_hours > 5:
        st.info("📱 الحل للموبايل: قلل وقت الشاشة قبل النوم.")
    if workout_days < 3:
        st.info("🏃 الحل للنشاط: ابدأ بالمشي 20 دقيقة يومياً.")

    st.balloons()