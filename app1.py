import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="QuickBite Ordering App", page_icon="🍔", layout="wide")

# Sidebar
st.sidebar.title("🍔 QuickBite")
page = st.sidebar.radio("Navigation", ["Home", "Order Food", "Checkout", "About"])

theme = st.sidebar.color_picker("Choose Theme Color", "#FF4B4B")
st.sidebar.write("Welcome to QuickBite!")

# Menu Data
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fried Chicken": 180,
    "Fries": 90,
    "Milk Tea": 110,
    "Hotdog Sandwich": 100
}

# HOME PAGE
if page == "Home":

    st.title("🍔 QuickBite Food Ordering App")

    st.success("Order your favorite food easily!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Menu Items", "6")
    col2.metric("Average Delivery", "30 mins")
    col3.metric("Customer Rating", "4.8 ⭐")

    st.subheader("Popular Foods")

    st.progress(0.8)

    st.info("Use the sidebar to start ordering food.")

    with st.expander("View Available Menu"):
        df = pd.DataFrame(list(menu.items()), columns=["Food", "Price"])
        st.table(df)


# ORDER PAGE
elif page == "Order Food":

    st.title("🛒 Order Your Food")

    name = st.text_input("Customer Name")

    food = st.selectbox("Choose Food", list(menu.keys()))

    quantity = st.number_input("Quantity", 1, 10, 1)

    extras = st.multiselect(
        "Extras",
        ["Extra Cheese", "Spicy Sauce", "Large Drink", "Extra Rice"]
    )

    spice_level = st.radio(
        "Spice Level",
        ["Mild", "Medium", "Hot"]
    )

    delivery_date = st.date_input("Delivery Date")

    delivery_time = st.time_input("Delivery Time")

    instructions = st.text_area("Special Instructions")

    agree = st.checkbox("I confirm my order details")

    price = menu[food] * quantity

    st.subheader("Order Preview")
    st.write("Food:", food)
    st.write("Quantity:", quantity)
    st.write("Total Price: ₱", price)

    if st.button("Add to Cart"):
        st.success("Item added to cart!")


# CHECKOUT
elif page == "Checkout":

    st.title("💳 Checkout")

    payment = st.selectbox(
        "Payment Method",
        ["Cash on Delivery", "GCash", "Credit Card"]
    )

    tip = st.slider("Tip Amount (₱)", 0, 100, 10)

    rating = st.slider("Rate our app experience", 1, 5)

    receipt = st.file_uploader("Upload Proof of Payment")

    address = st.text_input("Delivery Address")

    color = st.color_picker("Choose packaging color 😄")

    if st.button("Place Order"):
        st.balloons()
        st.success("Your order has been placed successfully!")


# ABOUT PAGE
elif page == "About":

    st.title("ℹ About This App")

    st.subheader("What the App Does")
    st.write(
        """
        QuickBite is a simple food ordering application that allows users
        to browse menu items, select food, customize orders, and place
        delivery requests through an easy-to-use interface.
        """
    )

    st.subheader("Target Users")
    st.write(
        """
        The target users are students, office workers, and anyone who
        wants a quick and convenient way to order food online.
        """
    )

    st.subheader("Inputs Collected")
    st.write(
        """
        - Customer name  
        - Food selection  
        - Quantity  
        - Extras and preferences  
        - Delivery date and time  
        - Address  
        - Payment method  
        """
    )

    st.subheader("Outputs Displayed")
    st.write(
        """
        - Order preview  
        - Total price  
        - Order confirmation message  
        - Menu table and dashboard metrics  
        """
    )

    st.caption("Created using Streamlit for UI demonstration.")