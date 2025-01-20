import streamlit as st

st.title('Currency Converter App')
st.write('This app converts the currency of one country to another currency')

sidebar = st.sidebar
sidebar.header("Our Current Exchange Rates 💸")
sidebar.subheader('Exchange Rates')
sidebar.write("""
            :blue['USD - NGN']: 1700\n
            ':blue[USD - CAD']: 1.43\n
            ':blue[NGN - USD']: 0.00064\n
            ':blue[NGN - CAD']: 0.00092\n
            ':blue[CAD - USD']: 0.70\n
            ':blue[CAD - NGN']: 1085.00
            
              """)
sidebar.divider()
sidebar.subheader('🎯 About')
sidebar.write('This app is a simple currency converter that converts the currency of one country to another currency')


# Currency Converter App
rate = {
    'USD - NGN': 1700,
    'USD - CAD': 1.43,
    'NGN - USD': 0.00064,
    'NGN - CAD': 0.00092,
    'CAD - USD': 0.70,
    'CAD - NGN': 1085.00
}

if 'result' not in st.session_state:
    st.session_state.result = 0
if 'amount2' not in st.session_state:
    st.session_state.amount = ''

col1, col2 = st.columns(2)

def convert_currency_top():
    pair = f"{currency_from} - {currency_destination}"
    if pair in rate:
        st.session_state.result = int(st.session_state.amount1) * rate[pair]

def convert_currency_bottom():
    pair = f"{currency_destination} - {currency_from}"
    if pair in rate:
        st.session_state.result = int(st.session_state.amount2) * rate[pair]        
   
    
with col1:
    currency_from = st.selectbox('Select source currency', ['USD', 'CAD', 'NGN'], key='currency_from')
    currency_destination = st.selectbox('Select destination currency', ['USD', 'CAD', 'NGN'], key='currency_destination')
with col2:
    amount1 = st.number_input('Enter amount to convert', key='amount1', on_change=convert_currency_top)
    amount2 = st.number_input('Enter amount to convert', key='amount2', on_change=convert_currency_bottom)
    st.write(st.session_state.result)
