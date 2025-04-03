import streamlit as st
import numpy as np
from model_operation import load_model, preprocess_input, predict_diabetes
from user_interface import welcome_message, sidebar_info, user_input, add_footer

st.set_page_config(
    page_title="AI Doc: Diabetes Oracle",
    page_icon="🧠💡",
    layout="wide"
)

st.title("🧠 AI Doc: Diabetes Oracle")
st.subheader("🚀 Welcome to AI Health Oracle 2.0: Your Personal Diabetes Predictor 🔮")
st.subheader("Where Data Science Meets Health 🚨💻")

def main():

    welcome_message()

    model, scaler = load_model()

    if model is None or scaler is None:
        st.error("Failed to load the model or scaler. Please check the logs.")
        return

    sidebar_info()

    input_data = user_input()

    if st.button("Predict"):
        try:
            scaled_input = preprocess_input(np.array(input_data), scaler)

            prediction = predict_diabetes(model, scaled_input)

            if prediction == 1:
                st.error("Prediction: Diabetic 🚨")
                st.markdown("""
                **Uh-oh, Sugar Alert!** 🚨  
                Your stats are waving a red flag for diabetes risk. But hey, catching it early is half the battle!  

                **What's Up?**  
                - Glucose or BMI might be throwing shade. 🔴  
                - Age, lifestyle, or other sneaky factors could be in play.  

                **Game Plan**:  
                - **Doctor Time**: Get tested (HbA1c, fasting glucose). 🩺  
                - **Small Wins**:  
                - Shed 5-10% weight = ~60% lower risk. ⚖️  
                - Walk 30 mins/day = instant health boost. 🚶‍♀️  
                - Sugar? Keep it under 25g/day. 🍬→🍎  

                **You've Got This!** Tiny steps = big wins. 💪  
                """)

            else:
                st.success("Prediction: Non-Diabetic ✅")
                st.balloons()
                st.markdown("""
                **High-Five! You're Crushing It!** 🎉  
                Your stats say you're in the clear—low diabetes risk. Keep slaying those healthy habits!  

                **Why It's Lit**:  
                - Glucose, BMI, and more = all in the green zone. 🌟  
                - You're basically a diabetes-fighting superhero. 🦸‍♂️  

                **Stay Awesome**:  
                - **Check-Ups**: Keep tabs on your health. 📊  
                - **Pro Tips**:  
                - Eat the rainbow (veggies > junk). 🥦🍟  
                - Move it! 150 mins/week = magic. 🏃‍♂️  
                - Chill out—mindfulness or hobbies = win. 🧘‍♂️🎨  

                **Keep Shining!** You're a health rockstar. ✨  
                """)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

    add_footer()

if __name__ == "__main__":
    main()