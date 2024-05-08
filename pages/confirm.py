import streamlit as st
from utilities import FirestoreWrapper

token = st.query_params.token
user = st.query_params.user

db = FirestoreWrapper().connect()
user_ref = db.collection("users").document(user)

if user_ref.get().to_dict()['is_confirmed']:
    st.warning("User account already confirmed. Please proceed to login by selecting `app` in navigation menu.")
else:
    try:

        if token == user_ref.get().to_dict()['confirmation_token']:
            user_ref.update({
                'is_confirmed': True
            })
        st.success("User registration successful! You can now login.")

    except:
        st.error("Registration failed. Please try again.")
