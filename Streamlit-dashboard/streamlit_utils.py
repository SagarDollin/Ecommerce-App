import streamlit as st
from streamlit_elements import elements, mui, html, sync

def card(title, img_url):
    with elements("profile"):
                
        with mui.Card(key="profile", sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            
            mui.CardHeader(
                title=title,
                avatar=mui.Avatar(title[0], sx={"bgcolor": "#ffa31a"}),
                # action=mui.IconButton(mui.icon.MoreVert),
            )

            mui.CardMedia(
                component="img",
                image=img_url,
                alt="Paella dish",
                height=150
            )

            with mui.CardContent(sx={"flex": 1}):
                mui.Button("Edit Profile", variant="contained", sx={"borderRadius":5, "textTransform": "none", "margin":0.5})

def wallet(title, balance):
    with elements("wallet"):
                
        with mui.Card(key="wallet", sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            
            mui.CardHeader(
                title="Balance",
            )
            mui.CardHeader(
                title=f"$ {balance}",
            )

            # with mui.CardContent(sx={"flex": 1}):
            #     mui.Button("Add money", variant="contained", sx={"borderRadius":5, "textTransform": "none", "margin":0.5})

def get_card(product):
    header =  '''
    <html>
    <head>
    <style>
    .card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    max-width: 400px;
    margin: auto;
    text-align: center;
    font-family: arial;
    }

    .price {
    color: grey;
    font-size: 22px;
    }

    </style>
    </head>'''
    
    body = f'''
    <body>


    <div class="card">
    <img src="https://images-cdn.ubuy.co.in/6351094d27bc4630df6c57e3-adidas-men-39-s-freak-carbon-cleats.jpg" alt="{product["brand"]}" style="width:100%;height:50%">
    <h5>{product["name"]}</h5>
    <b class="price">$ {product["price"]}</b>
    <p>{product["Description"]}</p>
    <p>STOCK : {product["stocks"]}  DATE: {product["date of manufacture"]}</p>
    </div>

    </body>
    </html>
    '''
    return header+body

import streamlit as st
# import streamlit as st

def row_spaces(num_rows=5):
    for i in range(num_rows):
        st.markdown(" ")

def middle_heading(heading="Streamlit Heading"):
    cols = st.columns(3)
    with cols[1]:
        st.header(heading)

def custom_text(color, size, font, text):
    display_text = f'<b style="font-family:{font}; color:{color}; font-size: {size}px;">{text}</b>'
    st.markdown(display_text, unsafe_allow_html=True)

def draw_line():
    st.markdown("""---""")

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def download_csv(df, file_name="data.csv", label="Download"):
    

    csv = convert_df(df)