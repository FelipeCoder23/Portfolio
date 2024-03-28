import streamlit as st
import requests
import time
import subprocess
import os
from io import BytesIO
import base64


output_directory = "/tmp"



if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Introduction'

st.markdown("""
<style>

    /* Main content area gradient background */
    .stApp {
        background-image: linear-gradient(to bottom, #000000, #000000);
    }


    /* Targeting the sidebar with data-testid attribute */
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #000000, #1B2631); /* Gradient from light green to dark grey */
    }
    /* Additional styling to ensure the gradient covers the whole sidebar */
    .stSidebar > div:first-child {
        background: linear-gradient(to bottom, #000000, #1B2631); /* Gradient from light green to dark grey */
    }


    /* Custom styles for buttons in the sidebar */
    .stButton>button {
        background-color: #FFFFFF; /* White */
        color: #000000; /* Black */
        border-radius: 10px;
        border: 1px solid #000000; /* Black border */
        padding: 10px 24px;
        margin-bottom: 10px; /* Add space between buttons */
    }


    /* Button styling */
    .css-1cpxqw2 {
        background-color: #FFFFFF; /* White */
        color: #000000; /* Black */
        border-radius: 10px;
        border: 1px solid #000000; /* Black border */
        padding: 10px 24px;
        margin-bottom: 10px; /* Add space between buttons */
    }

    /* Hover effect for buttons */
    .css-1cpxqw2:hover {
        background-color: #FFFFFF
; /* white */
    }

    /* Active button styling */
    .css-1cpxqw2:focus {
        background-color: #FFFFFF; /* Grey background for active button */
        border: 1px solid #4CAF50; /* Green border for active button */
    }
</style>
""", unsafe_allow_html=True)

# The HTML and CSS code for the button
github_repo_url = "https://github.com/FelipeCoder23/Fast_final"
github_chona = "https://github.com/ignaciogomenuka"
github_feli = "https://github.com/FelipeCoder23"
github_gus = "https://github.com/gpoliviero"

github_logo_base64 = "https://i.pinimg.com/564x/95/7c/4d/957c4dd9aa815cc1de2040cc1259589f.jpg"
button_html = f"""
<a href="{github_repo_url}" target="_blank" style="text-decoration: none;">
    <div style="
        margin: 1rem auto;
        padding: 0.5rem 1rem;
        background-color: #f6f8fa;
        border: 1px solid rgba(27,31,35,.15);
        border-radius: .5rem;
        box-shadow: rgba(27,31,35,.04) 0 1px 0 inset;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        color: #24292e;
        font-size: 1rem;
        font-weight: 500;">
        <img src="{github_logo_base64}" alt="GitHub Logo" style="height: 20px; margin-right: 0.5rem;"/>
        Go to Repo
    </div>
</a>
"""

# Sidebar navigation
st.sidebar.image('https://info.lewagon.com/hubfs/Mexico/Logo_Red%26White-1.png', width=200)
# Sidebar navigation
st.sidebar.title('⭐ Analyst in sport')

# Using session_state to control page navigation
if st.sidebar.button('⚽ Introduction'):
    st.session_state.current_page = 'Introduction'
if st.sidebar.button('📊 Upload & Analysis'):
    st.session_state.current_page = 'Upload & Analysis'
if st.sidebar.button('🚀 About us'):
    st.session_state.current_page = 'About us'

st.sidebar.markdown(button_html, unsafe_allow_html=True)

# Introduction page content
video_url= "videofinalfront.mp4"
if st.session_state.current_page == 'Introduction':
    st.title('Analyst in Sport')
    st.subheader('👋 Welcome!')
    st.write("""
        This app uses advanced computer vision to track handball matches and detect goal plays.
        Simply upload a video of a match, and the app will analyze it to return clips where goals are detected.
        Navigate to the 'Upload & Analysis' page to get started!

        Our system processes your video footage and, through our advanced machine learning algorithm, identifies instances
        of goals in handball games. This technology is adept at recognizing the precise moments when the referee signals a goal.
    """)
    st.video(video_url)
    st.subheader('🛠️ Tech Stack')
    st.write("\n" * 3)  # Adds three empty lines for spacing
    # Create four columns
    col1, col2, col3, col4 = st.columns(4)
    logo_width = 100
    # Display images in each column
    with col1:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png',  width=logo_width)

    with col2:
        st.image('https://assets-global.website-files.com/646dd1f1a3703e451ba81ecc/6500a996caa8af6dbea4ee0f_YV23%20Logo_Color.webp',  width=logo_width)

    with col3:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/PyTorch_logo_white.svg/640px-PyTorch_logo_white.svg.png',  width=logo_width)

    with col4:
        st.image('https://d7umqicpi7263.cloudfront.net/img/product/2f4886b5-307e-4dcc-b121-ae1d8b5614ad/66ea65ba-713d-4ca4-a4d3-23c726277157.png',  width=logo_width)

elif st.session_state.current_page == 'Upload & Analysis':
# Define the path to save the segments (preferably in a temporary directory)\
    st.title('Upload your match')
    st.write("""
        This app uses advanced computer vision to track handball matches and detect goal plays.
        Simply upload a video of a match, and the app will analyze it to return clips where goals are detected.
    """)
    output_directory = "/tmp"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)


    url = "http://127.0.0.1:8000/predict_video"
    uploaded_file = st.file_uploader("Upload a .mp4 file:", type="mp4")


    if st.button('Fetch Goals'):
        if uploaded_file is not None:

            progress_bar = st.progress(0)
            progress_message = st.empty()


            for i in range(100):

                progress_bar.progress(i + 1)


                progress_message.text(f'Processing... {i+1}%')


                time.sleep(0.05)

        # Display the video if a file has been uploaded
        if uploaded_file is not None:
            # Display the video
            st.video(uploaded_file)

            files = {'file': uploaded_file.getvalue()}
            response = requests.post(url, files=files)
            progress_message.text('Finishing up...')

            if response.ok:
                st.success('API called succesfully!')
                predictions = response.json().get('prediction', [])
                if predictions:
                    st.write('Detected Goals:')
                    for i, pred in enumerate(predictions):
                        # Asegúrate de que 'pred' es una cadena y contiene la información esperada
                        if isinstance(pred, str) and "gol:" in pred:
                            # Extrae el tiempo del gol del string
                            goal_time = pred.split(' ')[1]
                            st.write(f"{i+1}. Goal at {goal_time}")
                        else:
                            st.error(f"Unexpected format in predictions: {pred}")
                else:
                    st.info('No goals were detected.')
            else:
                st.error("Error in the API response.")

            # Limpieza
            progress_bar.empty()
            progress_message.empty()










elif st.session_state.current_page == 'About us':
    # Function to generate the button HTML
    def get_button_html(github_url):
        return f"""
        <a href="{github_url}" target="_blank" style="text-decoration: none;">
            <div style="
                margin: 1rem auto;
                padding: 0.5rem 1rem;
                background-color: #f6f8fa;
                border: 1px solid rgba(27,31,35,.15);
                border-radius: .5rem;
                box-shadow: rgba(27,31,35,.04) 0 1px 0 inset;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                color: #24292e;
                font-size: 1rem;
                font-weight: 500;">
                <img src="{github_logo_base64}" alt="GitHub Logo" style="height: 20px; margin-right: 0.5rem;"/>
                Github
            </div>
        </a>
        """

    from PIL import Image
    image = st.image('https://info.lewagon.com/hubfs/Mexico/Logo_Red%26White-1.png', width=200)
    st.title('About us')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('https://avatars.githubusercontent.com/u/103946112?v=4', width=200)  # Replace with the path to your image
        st.markdown("""
                     ## Ignacio Muñoz Gomeñuka

                     description
                    """)
        st.markdown(get_button_html(github_chona), unsafe_allow_html=True)

    with col2:
        st.image('https://avatars.githubusercontent.com/u/68247059?v=4', width=200)  # Replace with the path to your image
        st.markdown("""
                     ## Felipe Alvarez Diaz

                      description
                    """)
        st.markdown(get_button_html(github_feli), unsafe_allow_html=True)
    with col3:
        st.image('https://avatars.githubusercontent.com/u/100483669?v=4', width=200)  # Replace with the path to your image
        st.markdown("""
                     ## Gustavo Oliviero

                      description
                    """)
        st.markdown(get_button_html(github_gus), unsafe_allow_html=True)
