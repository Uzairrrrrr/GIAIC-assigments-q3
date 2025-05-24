import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Global app state (for demo purpose, all in-memory)
if "KEY" not in st.session_state:
    st.session_state.KEY = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.KEY)
    st.session_state.stored_data = {}  # {"encrypted_text": {"encrypted_text": ..., "passkey": ...}}
    st.session_state.failed_attempts = 0
    st.session_state.locked = False
    st.session_state.admin_logged_in = False

cipher = st.session_state.cipher


# Utility: Hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()


# Encrypt text
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()


# Decrypt with passkey
def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)
    for data in st.session_state.stored_data.values():
        if data["encrypted_text"] == encrypted_text and data["passkey"] == hashed:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    st.session_state.failed_attempts += 1
    # Check if user should be locked after failed attempt
    if st.session_state.failed_attempts >= 3:
        st.session_state.locked = True
    return None


# UI Logic
st.title("🔒 Secure Data Encryption System")

# Check if user is locked out due to failed attempts
if st.session_state.failed_attempts >= 3:
    st.session_state.locked = True

# Show lockout screen if needed
if st.session_state.locked and not st.session_state.admin_logged_in:
    st.subheader("🔑 Account Locked - Admin Login Required")
    st.warning("🔒 Too many failed attempts. Please enter the master password to continue.")
    
    master_pass = st.text_input("Enter Master Password:", type="password", key="lockout_login")
    
    if st.button("🔓 Unlock Account"):
        if master_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.locked = False
            st.success("✅ Account unlocked!")
            st.rerun()
        else:
            st.error("❌ Incorrect master password.")
    
    # Don't show anything else when locked
    st.stop()

# Normal navigation
menu = ["Home", "Store Data", "Retrieve Data", "Admin Login"]
choice = st.sidebar.radio("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome!")
    st.write(
        "This tool allows you to **securely store and retrieve your data** using a secret passkey."
    )
    
    # Show some stats
    if st.session_state.stored_data:
        st.info(f"📊 Total encrypted entries stored: {len(st.session_state.stored_data)}")

elif choice == "Store Data":
    st.subheader("📂 Store Data")
    data = st.text_area("Enter data to encrypt:")
    passkey = st.text_input("Set a passkey to secure your data:", type="password")
    if st.button("🔐 Encrypt & Save"):
        if data and passkey:
            hashed = hash_passkey(passkey)
            encrypted = encrypt_data(data)
            st.session_state.stored_data[encrypted] = {
                "encrypted_text": encrypted,
                "passkey": hashed,
                "original_data": data  # Store for admin view
            }
            st.success("✅ Your data has been encrypted and stored.")
            st.code(encrypted, language="text")
        else:
            st.error("⚠️ Both fields are required.")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Data")
    encrypted = st.text_area("Enter your encrypted text:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("🔓 Decrypt"):
        if encrypted and passkey:
            decrypted = decrypt_data(encrypted, passkey)
            if decrypted:
                st.success("✅ Your decrypted data:")
                st.code(decrypted, language="text")
            else:
                remaining = 3 - st.session_state.failed_attempts
                if remaining > 0:
                    st.error(f"❌ Incorrect passkey. Attempts remaining: {remaining}")
                else:
                    st.error("❌ Too many failed attempts. Access locked!")
                    st.rerun()
        else:
            st.error("⚠️ Both fields are required.")

elif choice == "Admin Login":
    if not st.session_state.admin_logged_in:
        st.subheader("🔑 Admin Login")
        st.info("Access admin panel to view all stored data and system information.")
        
        admin_pass = st.text_input("Enter Admin Password:", type="password", key="admin_login")
        
        if st.button("🔐 Login as Admin"):
            if admin_pass == "admin123":
                st.session_state.admin_logged_in = True
                st.success("✅ Admin login successful!")
                st.rerun()
            else:
                st.error("❌ Incorrect admin password.")
    
    else:
        # Admin Panel
        st.subheader("👑 Admin Panel")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.success("🟢 Logged in as Administrator")
        with col2:
            if st.button("🚪 Logout"):
                st.session_state.admin_logged_in = False
                st.rerun()
        
        st.divider()
        
        # System Information
        st.subheader("📊 System Information")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Entries", len(st.session_state.stored_data))
        with col2:
            st.metric("Failed Attempts", st.session_state.failed_attempts)
        with col3:
            status = "🔒 Locked" if st.session_state.locked else "🔓 Active"
            st.metric("System Status", status)
        
        st.divider()
        
        # All Stored Data
        st.subheader("🗄️ All Stored Data")
        
        if st.session_state.stored_data:
            for i, (encrypted_key, data) in enumerate(st.session_state.stored_data.items(), 1):
                with st.expander(f"Entry #{i}"):
                    st.text("**Original Data:**")
                    st.code(data.get("original_data", "N/A"), language="text")
                    
                    st.text("**Encrypted Text:**")
                    st.code(data["encrypted_text"], language="text")
                    
                    st.text("**Passkey Hash:**")
                    st.code(data["passkey"], language="text")
        else:
            st.info("No data stored yet.")
        
        st.divider()
        
        # Admin Actions
        st.subheader("⚙️ Admin Actions")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 Reset Failed Attempts"):
                st.session_state.failed_attempts = 0
                st.session_state.locked = False
                st.success("Failed attempts reset!")
                st.rerun()
        
        with col2:
            if st.button("🗑️ Clear All Data"):
                st.session_state.stored_data = {}
                st.success("All data cleared!")
                st.rerun()