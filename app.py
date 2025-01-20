import streamlit as st


st.title("CURRENCY CONVERTER")
st.write("This app convert country currencies")

sidebar = st.sidebar
sidebar.header("Our Current Exchange Rate")
sidebar.write("""
    :blue['USD - NGN']:1700\n
    'CAD - NGN': 1.43\n
    'NGN - USD': 0.00064\n
    'NGN - CAD': 0.00092\n
    'CAD - USD': 0.70\n
    'CAD - NGN': 1085.00""")

sidebar.divider()
sidebar.subheader('🎯 About')
sidebar.write("This app is a simple currency converter that converts the currency of one country to another country")

# Currency Converter
rate = {'USD - NGN': 1700,
        'CAD - NGN': 1.43,
        'NGN - USD': 0.00064,
        'NGN - CAD': 0.00092,
        'CAD - USD': 0.70,
        'CAD - NGN': 1085.00}

result = 0

col1, col2 = st.columns(2)

with col1:
    currency_from = st.selectbox("Select source country", ['USD', 'CAD', 'NGN'], key='currency_from')
    amount = st.number_input("Enter amount to convert")


with col2:
    currency_destination = st.selectbox("Select destination country", ['USD', 'CAD', 'NGN'], key='currency_destination')
    convert_btn = st.button("Convert")
    if convert_btn:
        pair = f"{currency_from} - {currency_destination}"
        if pair in rate:
            result = amount * rate[pair]
            st.metric(label='Conversion Result', value=f'{result:,.2f}')
            #st.success(f":blue[{amount:,.2f}] {currency_from} is equal to orange:[{result:,.2f}] {currency_destination}")
        else:
            st.metric("Conversion Result", "Invalid currency pair")









