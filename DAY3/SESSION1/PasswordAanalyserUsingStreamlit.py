import streamlit as st
st.title("Password Checker")
st.write("Check your password strength")

def has_min_length(password,min_len=8):
    return len(password)>=min_len
def has_uppercase(password):
    for ch in password:
        if ch.isupper():
            return True
    return False
def has_lowercase(password):
    for ch in password:
        if ch.islower():
            return True
    return False
def has_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False
def has_special_char(password,special="!@#$%^&*"):
    for ch in password:
        if ch in special:
            return True
    return False
def analyse_password(password):
    strength=0
    failed=[]
    if has_min_length(password):
        strength+=1
    else:
        failed.append("minimum length required")
    if has_uppercase(password):
        strength+=1
    else:
        failed.append("required uppercase")
    if has_lowercase(password):
        strength+=1
    else:
        failed.append("required lowercase")
    if has_digit(password):
        strength+=1
    else:
        failed.append("required digit")    
    if has_special_char(password):
        strength+=1
    else:
        failed.append("required special characted")
    #label
    if strength<=2:
        flag="weak"
    if strength==3:
        flag="moderate"
    if strength==4:
        flag="strong"
    if strength==5:
        flag="very strong"        
    return flag,strength,failed

password=st.text_input("Enter the passowrd",type="password")

if st.button("analyse password"):
    if password=="":
        st.warning("please enter a passowrd")
    else:
        flag,strength,failed=analyse_password(password)
        st.subheader("Result after checking")
        st.success(f"strength {strength}/5")
        st.info(f"Flags:{flag}")
        if failed:
            st.error("failed checks")
            for i in failed:
                st.write(i)
            else:
                st.success("all checks pass")