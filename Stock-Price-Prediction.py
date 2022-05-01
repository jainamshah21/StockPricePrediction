#Stock-Price-Prediction

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_qp1q7mct.json")
#https://assets8.lottiefiles.com/packages/lf20_qp1q7mct.json
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_DataSet = Image.open("images/DataSet.png")
img_Code = Image.open("images/Code-ss.png")
img_OriginalGraph = Image.open("images/Original-Graph.png")
img_PredictedGraph = Image.open("images/Predicted-Graph.png")
img_PredictedGraph2 = Image.open("images/Predicted-Graph2.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am jainam :wave:")
    st.title("Stock Price Prediction")
    

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Stock price prediction using python and LSTM :
            - i analyze the data and Filter usefull data.
            - Then make the LSTM model for prediction of Stock.
            - Create the graph for visualization  of data.
            

            Warning : This is not the actual data for real life stock prediction , this is use only for Study perpose.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_DataSet)
    with text_column:
        st.subheader("This is our data set of microsoft")
        st.write(
            """
            Here we use Microsoft data set for analyze the data and use of LSTM model to predict the Stock!
          
            """
        )
     
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Code)
    with text_column:
        st.subheader("This is our code for train the model")
        st.write(
            """
            we use this code for train the data using LSDM and make decition maker model
            """
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_OriginalGraph)
    with text_column:
        st.subheader("This is our original graph for Microsoft dataset")
        #st.write(
         #   """
          #  we use this code for train the data using LSDM and make decition maker model
           # """
        #)

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_PredictedGraph)
    with text_column:
        st.subheader("This is our Predited graph(Latest Time) for Microsoft dataset")
         st.write(
            """
            we can see that next 20 days prediction graph.
            in this we predicted the price of the stock will go down in 20th day.
            """
         )  
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_PredictedGraph2)
    with text_column:
        st.subheader("This is our Predited graph for Microsoft dataset")
        st.write(
            """
            For more Graph and Proper code , Click Below Link
            """
        )
        st.write("[Click Here](https://github.com/jainamshah21/StockPricePrediction.git)")      
      
    
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/jdsh21022001@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

 
