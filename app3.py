import streamlit as st

database = {'Name: Abdul Kabir, BVN: 0123456789', 
            'Name: Muhammed Jamiu, BVN: 23456789012',
            'Name: James Tailor, BVN: 98765432109'}

st.title('BVN VALIDATOR')
st.write('This app validates the authenticity of a BVN number')
sidebar = st.sidebar
sidebar.header('BVN Validator')
sidebar.write('This app validates the authenticity of a BVN number')
sidebar.selectbox('Select BVN number', ['0123456789', '23456789012', '98765432109'])
sidebar.divider()
sidebar.subheader('🎯 About')
sidebar.write('This app is a simple BVN validator that validates the authenticity of a BVN number')
bvn = st.text_input('Enter BVN number')
validate_btn = st.button('Validate BVN')
if validate_btn:
    if len(bvn) == 11:
        st.success('BVN number is valid')
    else:
        st.error('BVN number is invalid')