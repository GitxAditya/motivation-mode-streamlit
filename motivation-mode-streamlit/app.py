import streamlit as st
import random
import datetime

st.set_page_config(page_title="Motivation Mode", page_icon="⚡", layout="centered")

# ---------- Quotes ----------
QUOTES = [
    ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Do something today that your future self will thank you for.", "Unknown"),
    ("Everything you’ve ever wanted is on the other side of fear.", "George Addair"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
]

# ---------- Helper: pick quote ----------
def get_random_quote():
    return random.choice(QUOTES)

# ---------- Title / Date ----------
st.title("Motivation Mode")
today = datetime.date.today().strftime("%A, %d %B %Y")
st.caption(f"Today's date: {today}")

# ---------- Quote display ----------
if "quote" not in st.session_state:
    st.session_state.quote, st.session_state.author = get_random_quote()

if st.button("New Quote"):
    st.session_state.quote, st.session_state.author = get_random_quote()

st.markdown("---")
st.markdown("### Your Motivation")
st.markdown(f"> {st.session_state.quote}")
st.markdown(f"— *{st.session_state.author}*")
st.markdown("---")

# ---------- Audio (optional) ----------
st.markdown("### Background Audio (optional)")
uploaded_file = st.file_uploader("Upload audio file (mp3/wav/ogg)", type=["mp3", "wav", "ogg"])

if uploaded_file is not None:
    st.audio(uploaded_file)
else:
    st.info("No audio uploaded. Upload a file to play background music.")

