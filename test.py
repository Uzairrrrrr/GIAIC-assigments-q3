import streamlit as st
import re
import random
import string

def check_password_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("🔐 Password Strength Meter")
    st.write("Check how secure your password is and get improvement tips!")

    password = st.text_input("Enter your password:", type="password")

    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🧠 Password Analysis")
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        for item in feedback:
            st.write(item)

    if st.button("🔄 Suggest a Strong Password"):
        suggested = generate_strong_password()
        st.info(f"💡 Suggested Password: `{suggested}`")

if __name__ == "__main__":
    main()
