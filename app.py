import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Meter by Saima Salar", page_icon="🌘", layout="centered")

# Custom CSS for centering elements
st.markdown("""
    <style>
        .main {text-align: center;}
        .stTextInput {width:60% !important; margin:auto;}
        .stButton {
            display: flex;
            justify-content: center;
        }
        .stButton button {
            width: 50%;
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
        }
        .stButton button:hover {
            background-color: #f33661;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.markdown("Enter your password below to check its security level.🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one digit.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one special character (!@#$%^&*).")

    # Display password strength results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Password Input
password = st.text_input("Enter your password:", type="password", help="Ensure your password is at least 8 characters long.🔐")

# Center the button using HTML
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter your password first.")
st.markdown("</div>", unsafe_allow_html=True)
