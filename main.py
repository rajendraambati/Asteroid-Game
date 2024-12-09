import streamlit as st
from pathlib import Path

# Serve the HTML, CSS, and JavaScript
def render_game():
    # Read the HTML content
    html_content = Path("game.html").read_text()

    # Display the HTML content inside Streamlit
    st.components.v1.html(html_content, height=800)

# Streamlit page configuration
st.set_page_config(page_title="Asteroid Navigator", layout="wide")

# Add the title of the game
st.title("Asteroid Navigator")

# Render the game
render_game()
