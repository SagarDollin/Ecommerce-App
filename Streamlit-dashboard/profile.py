import streamlit as st
from streamlit_utils import card, wallet
from backend_interactions.user import get_user, get_token, get_balance, add_money

def render_profile():
    cols = st.columns(2)
    with cols[0]:
        token = get_token(username=st.session_state.username, password=st.session_state.password)
        st.session_state.token = token
        user = get_user(token=st.session_state.token)
        card(title=user["full_name"], img_url="https://cdn.britannica.com/50/182850-050-8B0F87B3/Robert-Downey-Jr-Iron-Man-film-Tony.jpg")

    with cols[1]:
        balance = get_balance(token=st.session_state.token, username=st.session_state.username)
        st.session_state.balance = balance
        wallet(title="Balance", balance=st.session_state.balance)

        button1 = st.button('Add money')
        if st.session_state.get('button') != True:

            st.session_state['button'] = button1 # Saved the state

        if st.session_state['button'] == True:

            amount = st.number_input(label="Enter amount", value=0)

            if st.button('Confirm'):

                wallet_receipt = add_money(token=st.session_state.token, username=st.session_state.username, amount=amount)
                st.success(f"New Balance: {wallet_receipt['balance']}")
                

            
        

            