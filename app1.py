import streamlit as st

st.set_page_config(page_title="QuickBite", page_icon="QB", layout="wide")

if "cart" not in st.session_state:
    st.session_state.cart = []

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');
* { box-sizing:border-box; }
.main { background:#ffffff; }
.block-container { padding-top:0 !important; }
.stApp { background:#ffffff; }
.hero { background:linear-gradient(160deg,#1a1a2e,#2d2d44); padding:52px 40px 40px; text-align:center; border-bottom:1px solid #e8e4de; }
.hero-badge { display:inline-block; border:1px solid rgba(200,169,110,.5); color:#c8a96e; font:500 10px/1 'Inter',sans-serif; letter-spacing:3px; text-transform:uppercase; padding:6px 16px; border-radius:2px; margin-bottom:20px; }
.hero-title { font:700 54px/1 'Cormorant Garamond',serif; color:#fff; margin:0 0 10px; }
.hero-title span { color:#c8a96e; }
.hero-subtitle { font:300 15px/1 'Inter',sans-serif; color:rgba(255,255,255,.55); letter-spacing:.5px; }
.section-title { font:700 28px/1 'Cormorant Garamond',serif; color:#1a1a2e; margin-bottom:4px; }
.section-sub { font:400 13px/1 'Inter',sans-serif; color:#999; margin-bottom:24px; }
.fancy-divider { height:1px; background:#c8a96e; margin:8px 0 28px; width:40px; }
.food-card { background:#fff; border-radius:6px; overflow:hidden; border:1px solid #e8e4de; transition:box-shadow .25s; margin-bottom:20px; }
.food-card:hover { box-shadow:0 8px 30px rgba(0,0,0,.08); }
.food-card-img { width:100%; height:175px; object-fit:cover; display:block; }
.food-card-body { padding:16px 18px 18px; }
.food-card-name { font:700 17px/1 'Cormorant Garamond',serif; color:#1a1a2e; margin:0 0 5px; }
.food-card-desc { font:400 12px/1.5 'Inter',sans-serif; color:#888; margin:0 0 14px; }
.food-card-footer { display:flex; align-items:center; justify-content:space-between; }
.food-price { font:600 16px/1 'Inter',sans-serif; color:#1a1a2e; }
.food-tag { background:#f5f0e8; color:#a07840; font:500 9px/1 'Inter',sans-serif; letter-spacing:1.5px; text-transform:uppercase; padding:4px 10px; border-radius:2px; }
.metric-card { background:#fff; border-radius:6px; padding:28px 24px; border:1px solid #e8e4de; text-align:center; }
.metric-value { font:700 38px/1 'Cormorant Garamond',serif; color:#1a1a2e; margin-bottom:6px; }
.metric-label { font:500 10px/1 'Inter',sans-serif; color:#aaa; letter-spacing:2px; text-transform:uppercase; }
.cart-item { background:#fff; border-radius:6px; padding:16px 20px; margin-bottom:10px; display:flex; align-items:center; justify-content:space-between; border:1px solid #e8e4de; }
.cart-item-name { font:700 15px/1 'Cormorant Garamond',serif; color:#1a1a2e; }
.cart-item-meta { font:400 12px/1 'Inter',sans-serif; color:#aaa; margin-top:3px; }
.cart-item-price { font:600 15px/1 'Inter',sans-serif; color:#1a1a2e; }
.total-box { background:#1a1a2e; border-radius:6px; padding:24px 28px; text-align:right; margin-top:16px; }
.total-label { font:500 10px/1 'Inter',sans-serif; color:rgba(255,255,255,.45); text-transform:uppercase; letter-spacing:2px; }
.total-amount { font:700 36px/1 'Cormorant Garamond',serif; color:#c8a96e; margin-top:6px; }
.info-pill { display:inline-block; background:#f5f0e8; color:#a07840; font:500 11px/1 'Inter',sans-serif; padding:6px 14px; border-radius:2px; margin:4px 6px 4px 0; }
.about-block { background:#fff; border-radius:6px; padding:28px 32px; border:1px solid #e8e4de; margin-bottom:16px; border-left:3px solid #c8a96e; }
.about-block h4 { font-family:'Cormorant Garamond',serif; font-size:19px; color:#1a1a2e; margin:0 0 10px; }
.about-block p { font:400 13px/1.8 'Inter',sans-serif; color:#555; margin:0; }
/* Force light theme on all main content widgets */
section[data-testid="stMain"], section[data-testid="stMain"] > div { background:#ffffff !important; }
section[data-testid="stMain"] label { color:#1a1a2e !important; font:500 12px/1 'Inter',sans-serif !important; }
section[data-testid="stMain"] p { color:#1a1a2e !important; }
section[data-testid="stMain"] input { background:#ffffff !important; color:#1a1a2e !important; border:1px solid #d0ccc5 !important; border-radius:4px !important; }
section[data-testid="stMain"] textarea { background:#ffffff !important; color:#1a1a2e !important; border:1px solid #d0ccc5 !important; border-radius:4px !important; }
section[data-testid="stMain"] div[data-baseweb="select"] > div { background:#ffffff !important; border:1px solid #d0ccc5 !important; }
section[data-testid="stMain"] div[data-baseweb="select"] div, section[data-testid="stMain"] div[data-baseweb="select"] span { color:#1a1a2e !important; background:#ffffff !important; }
div[data-baseweb="popover"] *, div[data-baseweb="menu"] * { background:#ffffff !important; color:#1a1a2e !important; }
section[data-testid="stMain"] .stNumberInput button { background:#f0eee8 !important; color:#1a1a2e !important; }
/* Radio: white background, dark text */
section[data-testid="stMain"] .stRadio > label { color:#1a1a2e !important; }
section[data-testid="stMain"] .stRadio > div { background:#ffffff !important; }
section[data-testid="stMain"] .stRadio label { background:#ffffff !important; color:#1a1a2e !important; font:400 13px/1.4 'Inter',sans-serif !important; }
section[data-testid="stMain"] .stRadio [data-testid="stMarkdownContainer"] p { color:#1a1a2e !important; font:400 13px/1 'Inter',sans-serif !important; }
.stFileUploader section { background:#f9f8f6 !important; border:1px dashed #c8a96e !important; border-radius:4px !important; }
.stFileUploader * { color:#1a1a2e !important; }
.stButton>button { background:#1a1a2e !important; color:#fff !important; border:none !important; border-radius:3px !important; font:500 13px/1 'Inter',sans-serif !important; padding:11px 28px !important; letter-spacing:.5px !important; transition:background .2s !important; }
.stButton>button:hover { background:#c8a96e !important; color:#fff !important; }
[data-testid="stSidebar"] { background:#1a1a2e !important; border-right:1px solid #252540; }
[data-testid="stSidebar"] * { color:rgba(255,255,255,.75) !important; font-family:'Inter',sans-serif !important; }
.sidebar-logo { font:700 22px/1 'Cormorant Garamond',serif; color:#c8a96e !important; text-align:center; padding:8px 0 22px; letter-spacing:1px; }
.cart-badge { background:#252540; border:1px solid #333360; color:rgba(255,255,255,.65) !important; font:500 11px/1 'Inter',sans-serif !important; border-radius:2px; padding:8px 14px; text-align:center; margin-top:8px; display:block; letter-spacing:.5px; }
</style>""", unsafe_allow_html=True)

# ── DATA ───────────────────────────────────────────────────────────────────────
menu = {
    "Burger":          {"price":120,"tag":"Bestseller","desc":"Juicy beef patty with fresh lettuce, tomato & special sauce",  "image":"https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop"},
    "Pizza":           {"price":250,"tag":"Popular",   "desc":"Crispy thin crust with mozzarella & your choice of toppings",  "image":"https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=400&h=300&fit=crop"},
    "Fried Chicken":   {"price":180,"tag":"Crispy",    "desc":"Golden crispy skin, tender and juicy on the inside",           "image":"https://images.unsplash.com/photo-1562967914-608f82629710?w=400&h=300&fit=crop"},
    "Fries":           {"price":90, "tag":"Side",      "desc":"Golden shoestring fries, seasoned to perfection",              "image":"https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400&h=300&fit=crop"},
    "Milk Tea":        {"price":110,"tag":"Drink",     "desc":"Creamy milk tea with chewy tapioca pearls",                    "image":"https://images.unsplash.com/photo-1499638673689-79a0b5115d87?w=400&h=300&fit=crop"},
    "Hotdog Sandwich": {"price":100,"tag":"Classic",   "desc":"Smoky hotdog in a soft bun with mustard & ketchup",            "image":"https://images.unsplash.com/photo-1612392062631-94b3e0f0f8b3?w=400&h=300&fit=crop"},
}

# ── HELPERS ────────────────────────────────────────────────────────────────────
def section(title, sub):
    st.markdown(f'<div style="height:32px"></div><div class="section-title">{title}</div><div class="section-sub">{sub}</div><div class="fancy-divider"></div>', unsafe_allow_html=True)

def food_card(name, item, price_suffix=""):
    st.markdown(f"""<div class="food-card">
        <img src="{item['image']}" class="food-card-img" alt="{name}"/>
        <div class="food-card-body">
            <div class="food-card-name">{name}</div>
            <div class="food-card-desc">{item['desc']}</div>
            <div class="food-card-footer">
                <div class="food-price">&#8369;{item['price']}{price_suffix}</div>
                <div class="food-tag">{item['tag']}</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

def total_box(label, amount):
    st.markdown(f'<div class="total-box"><div class="total-label">{label}</div><div class="total-amount">&#8369;{amount:,}</div></div>', unsafe_allow_html=True)

def grid_cards(items):
    cols = st.columns(3)
    for i, (name, item) in enumerate(items):
        with cols[i % 3]: food_card(name, item)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""<div class="hero">
    <div class="hero-badge">Est. 2026 &nbsp;&middot;&nbsp; Premium Dining</div>
    <div class="hero-title">Quick<span>Bite</span></div>
    <div class="hero-subtitle">Order freshly prepared meals, delivered to your door</div>
</div>""", unsafe_allow_html=True)

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
st.sidebar.markdown('<div class="sidebar-logo">QUICKBITE</div>', unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("", ["Dashboard", "Menu", "Order", "Cart", "Checkout", "About"])
st.sidebar.markdown("---")
n = len(st.session_state.cart)
st.sidebar.markdown(f'<div class="cart-badge">{n} item{"s" if n != 1 else ""} in cart</div>', unsafe_allow_html=True)

# ── PAGES ──────────────────────────────────────────────────────────────────────
if page == "Dashboard":
    section("Overview", "A summary of your current session")
    for col, val, lbl in zip(st.columns(3), [len(menu), n, "30 min"], ["Menu Items", "Cart Items", "Est. Delivery"]):
        col.markdown(f'<div class="metric-card"><div class="metric-value">{val}</div><div class="metric-label">{lbl}</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:28px"></div>', unsafe_allow_html=True)
    section("Featured Items", "Our most ordered selections")
    grid_cards([(k, menu[k]) for k in ["Burger", "Pizza", "Fried Chicken"]])
    st.info("Navigate to Menu to browse all items, or go to Order to place a new order.")

elif page == "Menu":
    section("Full Menu", "Freshly prepared with quality ingredients")
    grid_cards(list(menu.items()))

elif page == "Order":
    section("Place an Order", "Select your item and customize your preferences")
    col_form, col_preview = st.columns([3, 2])
    with col_form:
        name     = st.text_input("Customer Name")
        food     = st.selectbox("Select Item", list(menu.keys()))
        quantity = st.number_input("Quantity", 1, 10, 1)
        extras   = st.multiselect("Add-ons", ["Extra Cheese", "Spicy Sauce", "Large Drink", "Extra Rice"])
        spice    = st.radio("Spice Level", ["Mild", "Medium", "Hot"], horizontal=True)
        d, t = st.columns(2)
        with d: delivery_date = st.date_input("Delivery Date")
        with t: delivery_time = st.time_input("Delivery Time")
        notes = st.text_area("Special Instructions", placeholder="Allergies, preferences, or special requests")
        total = quantity * menu[food]["price"]
        if st.button("Add to Cart", use_container_width=True):
            st.session_state.cart.append({"Item": food, "Qty": quantity, "Total (P)": total})
            st.success(f"{food} x{quantity} has been added to your cart.")
    with col_preview:
        food_card(food, menu[food], " each")
        total_box("Order Total", quantity * menu[food]["price"])
        if extras:
            st.markdown("**Selected Add-ons:** " + "".join(f'<span class="info-pill">{e}</span>' for e in extras), unsafe_allow_html=True)

elif page == "Cart":
    section("Your Cart", "Review your items before proceeding to checkout")
    if not st.session_state.cart:
        st.markdown('<div style="text-align:center;padding:60px 20px"><div style="font:700 22px/1 \'Cormorant Garamond\',serif;color:#1a1a2e;margin-bottom:8px">Your cart is empty</div><div style="font:400 13px/1 \'Inter\',sans-serif;color:#aaa">Add items from the Order page to get started.</div></div>', unsafe_allow_html=True)
    else:
        for item in st.session_state.cart:
            st.markdown(f'<div class="cart-item"><div><div class="cart-item-name">{item["Item"]}</div><div class="cart-item-meta">Qty: {item["Qty"]}</div></div><div class="cart-item-price">&#8369;{item["Total (P)"]:,}</div></div>', unsafe_allow_html=True)
        total_box("Grand Total", sum(i["Total (P)"] for i in st.session_state.cart))
        st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)
        if st.button("Clear Cart"):
            st.session_state.cart = []; st.success("Cart has been cleared."); st.rerun()

elif page == "Checkout":
    section("Checkout", "Confirm your details to complete the order")
    col1, col2 = st.columns(2)
    with col1:
        address = st.text_input("Delivery Address")
        payment = st.selectbox("Payment Method", ["Cash on Delivery", "GCash", "Credit Card"])
        tip     = st.slider("Tip Amount (P)", 0, 200, 20)
        rating  = st.slider("Rate Your Experience", 1, 5, 5)
        receipt = st.file_uploader("Upload Payment Receipt", type=["png", "jpg", "pdf"])
    with col2:
        if st.session_state.cart:
            subtotal = sum(i["Total (P)"] for i in st.session_state.cart)
            rows = "".join(f'<div style="display:flex;justify-content:space-between;font:400 13px/1.6 \'Inter\',sans-serif;color:#555;margin-bottom:8px"><span>{i["Item"]} x{i["Qty"]}</span><span style="font-weight:600">&#8369;{i["Total (P)"]:,}</span></div>' for i in st.session_state.cart)
            st.markdown(f'<div style="background:#fff;border-radius:6px;padding:28px;border:1px solid #e8e4de"><div style="font:700 20px/1 \'Cormorant Garamond\',serif;color:#1a1a2e;margin-bottom:20px">Order Summary</div>{rows}<hr style="border:none;border-top:1px solid #f0eee8;margin:14px 0"><div style="display:flex;justify-content:space-between;font:400 12px/1 \'Inter\',sans-serif;color:#aaa;margin-bottom:8px"><span>Tip</span><span>&#8369;{tip}</span></div><div style="display:flex;justify-content:space-between;font:700 20px/1 \'Cormorant Garamond\',serif;color:#1a1a2e;margin-top:8px"><span>Total</span><span>&#8369;{subtotal+tip:,}</span></div></div>', unsafe_allow_html=True)
        else:
            st.info("Your cart is empty. Add items from the Order page first.")
    st.markdown('<div style="height:16px"></div>', unsafe_allow_html=True)
    if st.button("Confirm Order", use_container_width=True):
        if not st.session_state.cart: st.warning("Please add items to your cart before confirming.")
        elif not address: st.warning("Please enter a delivery address.")
        else:
            st.success("Your order has been placed. Estimated delivery time: 30 minutes.")
            st.balloons(); st.session_state.cart = []

elif page == "About":
    section("About QuickBite", "A professional digital food ordering system")
    for title, body in [
        ("What is QuickBite?", "QuickBite is a streamlined digital food ordering interface built with Streamlit. It demonstrates a complete ordering workflow — from menu browsing to checkout — with a clean, professional aesthetic."),
        ("Target Users", "Designed for customers seeking a fast, reliable digital ordering experience. Also serves as a prototype for restaurants or developers building web-based ordering systems."),
        ("Inputs Collected", "Customer name · Food item and quantity · Add-ons and spice preference · Delivery schedule · Delivery address · Payment method · Optional tip and receipt upload"),
        ("Outputs Displayed", "Illustrated menu with photos · Live order preview · Shopping cart summary · Grand total with tip · Order confirmation message"),
    ]:
        st.markdown(f'<div class="about-block"><h4>{title}</h4><p>{body}</p></div>', unsafe_allow_html=True)
