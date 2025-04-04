import streamlit as st


about_me = st.Page(
    page= "views/about_me.py",
    title="About VGG19",
    icon= "❤️",
    default= True,
)
detect_fruits = st.Page(
    page= "views/detect_fruits.py",
    title="Fruits Classifier",
    icon= ":material/smart_toy:",
)
pg = st.navigation(
    {
        "Info": [about_me],
        "Project":[detect_fruits]
    }
)

st.logo("assets/key_logo.jpg")

st.sidebar.text("Made with by tt")
pg.run()