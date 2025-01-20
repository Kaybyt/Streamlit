import streamlit as st


# Mock database using a dictionary
db = {"Information1": {"name": "Abdul Kabir", "age": 30, "bvn": "000001100000"},
    "Information2": {"name": "Muhammed Jamiu", "age": 25, "bvn": "11111001111"}}

# Function to display user information
def display_user_info(user_info):
    st.write(f"name: {user_info['name']}")
    st.write(f"age: {user_info['age']}")
    st.write(f"bvn: {user_info['bvn']}")
    st.write("User information displayed successfully!")
    
# Function to register a new user
def register_user(bvn):
    st.write("BVN not found. Please register.")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0)
    if st.button("Register"):
        db[bvn] = {"name": name, "age": age, "bvn": bvn}
        st.success("Registration successful!")
        display_user_info(db[bvn])

# Streamlit app layout
st.title("BVN Checker and Registration")

bvn_input = st.text_input("Enter your BVN")

if st.button("Submit"):
    if bvn_input in db:
        st.success("BVN found! Retrieving user information...")
        display_user_info(db[bvn_input])
    else:
        register_user(bvn_input)
