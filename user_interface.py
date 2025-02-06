import streamlit as st
import numpy as np

def welcome_message():
    st.markdown(""" 
    🚀 AI Health Oracle -> Leveraging data-driven analytics 📊 for hyper-accurate diabetes risk predictions. ⚡ Feed in your metrics, and let our AI 🤖 deliver insights in real-time! 🔮 The Oracle predicts your health trajectory. Prepare for next-gen, data-powered wellness. 📈✨
    """)

def sidebar_info():
    with st.sidebar.expander("🔍 Dataset Information", expanded=False):
        st.markdown("""
        **Pima Indians Diabetes Dataset**  
        - **Source**: Pima Indian women, Arizona, USA.  
        - **Purpose**: Predict diabetes risk using health metrics.  

        **Key Features & Ranges**:  
        - **Glucose**: Plasma glucose (mg/dL).  
          - Normal: 70–100 mg/dL (fasting). Higher levels indicate higher risk. ⚡  
        - **BMI**: Body Mass Index.  
          - Healthy: 18.5–24.9. Obesity (>30) increases risk. 🏋️‍♂️  
        - **Age**: Age of the individual.  
          - Risk increases significantly after 45 years. 🧓  
        - **Pregnancies**: Number of pregnancies.  
          - Typically 0–10+ in this dataset. Affects insulin sensitivity. 🤰  
        - **Skin Thickness**: Triceps skinfold thickness (mm).  
          - Normal: 10–50 mm. Reflects body fat levels. 🔬  

        **Why It Matters**:  
        - Widely used for binary classification in healthcare.  
        - Strong feature correlations with diabetes outcomes.  
        - Preprocessed for missing values and normalization.  
        """)

    with st.sidebar.expander("💡 Health Insights & Prevention", expanded=False):
        st.markdown("""
        **Preventing Diabetes: Evidence-Based Strategies**  
        - **Diet**: Focus on whole foods 🍎🥦🌾, limit sugar 🍬.  
          - Daily sugar intake: <25g (WHO recommendation).  
        - **Exercise**: 150 mins/week (e.g., walking, cycling).  
          - Moderate activity: Brisk walking at 3–6 mph. 🏃‍♀️  
        - **Weight**: Maintain BMI <25.  
          - Even 5–10% weight loss reduces diabetes risk by 58%.⚖️  
        - **Monitoring**: Regular screenings (HbA1c, glucose).  
          - HbA1c: <5.7% = normal, 5.7–6.4% = prediabetes, ≥6.5% = diabetes. 🩺  
        - **Stress**: Manage with mindfulness 🧘‍♂️ or yoga.  
          - Chronic stress raises blood sugar levels.  

        **Proactive Steps**:  
        - High-risk groups (family history, obesity) should prioritize annual check-ups. 🔍  
        - Early lifestyle changes can delay/prevent diabetes onset. ⏳  
        - Always consult professionals before major changes. 👨‍⚕️  
        """)

    st.sidebar.subheader("🔗 Stay Connected with Us!")

    st.sidebar.markdown("""
    Stay updated with the latest health tips, features, and more.  
    Follow us on our social media platforms:
        
    - **Twitter**: [@Abhi__57](https://x.com/Abhi__57) 🐦 - Get quick updates and tips!
    - **LinkedIn**: [Abhishek Mishra](https://www.linkedin.com/in/abhishek-mishra-120799281/) 💼 - Let's connect professionally!
    - **GitHub**: [Abhishek08Mishra](https://github.com/Abhishek08Mishra) 🌟 - Explore projects and contribute!

    Feel free to reach out anytime!
    """)


def user_input():
    """Collecting user input via Streamlit and returning it as a NumPy array."""
    st.header("📝 Enter Your Health Metrics")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=100, value=24, step=1)
        glucose = st.number_input("Glucose Level (mg/dL)", min_value=70, max_value=200, value=100, step=1)
        bmi = st.number_input("BMI", min_value=15, max_value=50, value=25, step=1)
    with col2:
        skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20, step=1)
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=10, value=0, step=1)

    input_data = [[pregnancies, glucose, skin_thickness, bmi, age]]
    
    # Convert to NumPy array here to avoid errors in the main app file.
    return np.array(input_data)


# Footer Section
def add_footer():
    for _ in range(3):
        st.write("\n")
    
    st.markdown("---")
    st.write(f"Made with ❤️ by **Crazy Data Scientist** 🧠 | © 2025 My Crazy AI Doc: Diabetes Oracle App")

    st.write("**©️Copyright 2025. All rights reserved. Developed by Abhishek Mishra❤️‍🔥**")