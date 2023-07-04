import streamlit as st
from backend_interactions.products import get_brands, search
from backend_interactions.transaction import transaction
from streamlit_utils import get_card



def render_product_catalogue():
    global Bought
    cols = st.columns([3/4, 1/4])
    with cols[1]:
        min_price = st.slider(label="Minimum price", min_value=1, max_value=500, value=10)
        max_price = st.slider(label="Maximum price", min_value=1, max_value=500, value=500)
        brands = get_brands(token=st.session_state.token)
        brand = st.selectbox("Select Brand", options=brands["brands"])
    with cols[0]:
        search_key = st.text_input("Search Product", value='')
        if min_price <= max_price:
            results = search(token=st.session_state.token, search_key=search_key, min_price=min_price, max_price=max_price, brand=brand)
            if not results:
                st.warning("No Results found!😔")
            else:    
                for key in results.keys():
                    product = results[key]
                    card = get_card(product=product)
                    st.markdown(card, unsafe_allow_html=True)
                    if st.button("Buy now", key=key, use_container_width=True):
                        transaction_receipt = transaction(username=st.session_state.username, product_id=product["id"], token=st.session_state.token, amount=product["price"])
                        if transaction_receipt == "Insufficient Balance" or transaction_receipt == "Something went wrong, refer to logs!":
                            st.warning(transaction_receipt) 
                        else:
                            st.success("Purchase complete. Click on Product Catalogue to refresh")
               
        else:
            st.warning("WARNING: Minimum price must be less than or equal to Maximum price!")
        
