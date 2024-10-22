import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# إعدادات التصميم
st.set_page_config(page_title="تطبيق تحليل البيانات", page_icon="📊", layout="wide")

# عنوان التطبيق
st.title("تطبيق تحليل البيانات")

# إضافة تنسيق CSS للكتابة بالعربية
st.markdown(
    """
    <style>
    body {
        direction: rtl;  /* جعل الكتابة من اليمين إلى اليسار */
        text-align: right; /* محاذاة النص إلى اليمين */
    }
    .reportview-container {
        background: #F5F5F5;
    }
    .stButton>button {
        background-color: #4CAF50; /* اللون الأخضر */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True
)

# تحميل ملف بيانات
uploaded_file = st.file_uploader("اختر ملف (CSV, Excel, JSON)", type=['csv', 'xlsx', 'json'])

if uploaded_file is not None:
    # تحديد نوع الملف وقراءة البيانات
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith('.json'):
        df = pd.read_json(uploaded_file)

    # عرض البيانات
    st.write("## البيانات المدخلة:")
    st.dataframe(df)

    # إحصائيات أساسية
    st.write("## الإحصائيات الأساسية:")
    st.write(df.describe())

    # رسم بياني باستخدام Seaborn
    st.subheader("رسم بياني باستخدام Seaborn")
    plt.figure(figsize=(10, 6))
    sns.histplot(df.select_dtypes(include=['number']), kde=True)
    st.pyplot(plt)

    # رسم بياني باستخدام Plotly
    st.subheader("رسم بياني باستخدام Plotly")
    if 'Date' in df.columns:
        fig = px.line(df, x='Date', y=df.select_dtypes(include=['number']).columns.tolist())
        st.plotly_chart(fig)

    # قائمة للأعمدة المتاحة للتحليل
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    selected_column = st.selectbox("اختر عمودًا لرسمه", numeric_columns)

    if selected_column:
        st.line_chart(df[selected_column])

    # خيارات لحفظ النتائج
    if st.button("احفظ البيانات المعدلة"):
        df.to_csv("modified_data.csv", index=False)
        st.success("تم حفظ البيانات المعدلة كـ modified_data.csv")
