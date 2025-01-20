import streamlit as st

# Mock database (dictionary)
db = {}

# Function to display user information
def display_user_info(bvn):
    if bvn in db:
        user_info = db[bvn]
        st.write("User Information:")
        st.write(f"Name: {user_info['name']}")
        st.write(f"Age: {user_info['age']}")
        st.write(f"BVN: {user_info['bvn']}")
    else:
        st.write("BVN not found. Please register.")

# Function to register a new user
def register_user():
    st.subheader("Register your information")

    # Collect user information
    name = st.text_input("Enter your full name")
    age = st.number_input("Enter your age", min_value=18)
    bvn = st.text_input("Enter your BVN", max_chars=11)
    
    # Ensure BVN is valid
    if len(bvn) == 11 and bvn.isdigit():
        if bvn not in db:
            # Add the user to the database
            db[bvn] = {"name": name, "age": age, "bvn": bvn}
            st.success("Registration successful! You can now log in with your BVN.")
        else:
            st.warning("This BVN is already registered.")
    else:
        st.error("Please enter a valid 11-digit BVN.")

# Streamlit app logic
def app():
    st.title("BVN Verification System")

    # Ask the user to input their BVN
    bvn_input = st.text_input("Enter your BVN to proceed:", max_chars=11)

    if bvn_input:
        # Check if the BVN exists in the mock database
        if bvn_input in db:
            display_user_info(bvn_input)
        else:
            st.warning("BVN not found in the database.")
            if st.button("Register"):
                register_user()

# Run the Streamlit app
if __name__ == "__main__":
    app()
