import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Meter by Saima Salar", page_icon="🌘", layout="centered")
#custome css
st.markdown(""""
<style>
    .main {text-align: center;}
    .stTextInput {width:60% !important; margin:auto;}
    .stButton button {width:50%, background-color: #f63366 color: white; font-size: 18px;}
    .stButton button:hover {background-color: #f33661;}
</style>
""", unsafe_allow_html=True)

#page title and description
st.title("🔐 Password Strength Generator")
st.markdown(" Enter your password below to check its security level.🔍")

# function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 # increase score by 1
    else:
        feedback.append("❌Password must be at least 8 characters long.")
        
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1 # increase score by 1
        else:
            feedback.append("❌Password must contain both uppercase and lowercase letters.")
        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌Password must contain at least one digit.")
        if re.search(r"[!@#$%^&*]", password):
            score += 1
        else:
            feedback.append("❌Password must contain at least one special character.")

            #display password strength results
            if score == 4:
                st.success("✅**Strong Password**Your password is secure.")
            elif score == 3:
                st.info("⚠️** moderate Password** - Consider improving secuity by adding more feature.")
            else:
                st.error("❌**Weak Password**Follow the suggestion below to strength it.")


            #feedback
            if feedback:
                with st.expander("🔍 **Improve yoy password"):
                    for i, item in feedback:
                        st.write(item)
                        password = st.text_input("Enter your password:", type="password" , help="Ensure your password is at least 8 characters long.🔐")

    #Button Working
    if st.button("Check Password Strength"):
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter your password first.") #show warning message if no password is entered

    
