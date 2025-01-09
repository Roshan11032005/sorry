import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set up the page layout
st.set_page_config(page_title="Apology to Junior", page_icon="💖", layout="wide")

# Load a Lottie animation
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Beautiful animation for apology
apology_animation = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_vfcbaz.json")

# Page Title
st.title("🌟 Dear Junior, I'm So Sorry 🌟")
st.markdown(
    """
    **Junior,**

    I just wanted to say **I'm truly sorry** for anything I might have done that hurt you. 
    You mean so much to me, and I value our friendship more than words can ever express. 
    I've missed you a lot, and life hasn't been the same without you. 💕
    """
)

# Display animation
if apology_animation:
    st_lottie(apology_animation, height=400, key="apology")

# Add heartfelt quotes
st.write("### 🌸 Some Words from My Heart 🌸")
quotes = [
    "Friendship is delicate as glass; once broken, it can be fixed but there will always be cracks. Please help me fix it. ❤️",
    "True friends are never apart, maybe in distance but never in heart. I've missed you so much, Junior. 💕",
    "A simple sorry can save a relationship that took years to build. Junior, I'm sorry and I hope we can mend things. 🙏",
]

for quote in quotes:
    st.markdown(f"- *{quote}*")

# Add a sweet apology button
if st.button("💌 Junior, Please Forgive Me 💌"):
    st.balloons()
    st.success("Thank you, Junior, for being the wonderful person you are. I've missed you so much, and I promise to always cherish our friendship. ❤️")
