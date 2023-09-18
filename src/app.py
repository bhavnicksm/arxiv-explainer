import streamlit as st
from utils import check_arxiv_url

st.set_page_config(
    page_title="Arxiv Xplainer",
    page_icon="👨‍🏫",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/bhavnicksm/arxiv-explainer',
        'Report a bug': "https://github.com/bhavnicksm/arxiv-explainer/issues",
        'About': "Arxiv Xplainer is a easy to use streamlit app designed to help answer questions from Arixiv papers."
    }
)

with st.sidebar:
    st.header("About")
    st.write("Arxiv Xplainer is a easy to use streamlit app designed to help answer questions from Arixiv papers. ")

    st.header("How to use")
    st.write("1. Enter your [OpenAI API Key](https://platform.openai.com/account/api-keys) in the space given below")
    st.write("2. Insert the links to the Arxiv Pages you want to ask questions about")
    st.write("3. Ask a question about the Arxiv documents")

    OPENAI_API_KEY = st.text_input("OpenAI API Key", placeholder='', 
                                    help="Can be generated from [OpenAI API Key](https://platform.openai.com/account/api-keys)")

st.image('assets/logo.png')

if OPENAI_API_KEY == '':
    st.warning("Please enter you OpenAI Key to proceed!")

if 'text_list' not in st.session_state:
    st.session_state.text_list = []

user_input = st.text_input("Add url below:")

if user_input:
   if check_arxiv_url(user_input):
    st.session_state.text_list.append(user_input)
   else:
      st.error("Not a valid arxiv link. Please enter a valid arxiv link only!")
   
for text in st.session_state.text_list:
    st.info(text)

cols = st.columns(5)
if cols[2].button("Refresh"):
    st.session_state.text_list.clear()




