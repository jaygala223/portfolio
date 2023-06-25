import streamlit as st
from PIL import Image
import webbrowser

left, right = st.columns(2)

with left:
    st.title("Jay **Gala**")

    st.write("[Resume](https://drive.google.com/drive/folders/1jphVh04iyyQFjqodlwrbyoZjvfQnjAX9?usp=drive_link) \n[GitHub](https://www.github.com/jaygala223) \n[LinkedIn](https://www.linkedin.com/in/jaykishorgala)\n [Blog](https://galacodes.hashnode.dev/)")

    st.write("Hello reader. I'm a pre-final year Computer Science and Management student from [NMIMS University](https://www.nmims.edu/), Mumbai. I am working as a research intern at [IIT Patna](https://www.iitp.ac.in/), collaborating with [Dr. Sriparna Saha](https://www.iitp.ac.in/~sriparna/), where I am exploring computer vision applications for medical research using self-supervised and few shot learning techniques.")
             
    st.write("I was also part of the inaugral [Google ML Bootcamp India](https://rsvp.withgoogle.com/events/google-ml-bootcamp-india) in 2022 during which I got my **Deep Learning Specialization** from **Deeplearning.ai** and the **TensorFlow Developer Certification** from Google.")

    st.write("I am also passionate about open source and am a contributor in the [KerasCV](https://www.github.com/keras-team/keras-cv) library on GitHub")

st.write("My research interests lie in **Computer Vision, 3D Vision, Generative AI** and **Medical Imaging!**")


with right:
    # for adding some extra space
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.image("profile_pic.jpg", width=270, caption="Email: jaygala260@gmail.com")
    # st.caption("Email: jaygala260@gmail.com")
    # if st.button("Resume"):
    #     webbrowser.open("https://drive.google.com/drive/folders/1jphVh04iyyQFjqodlwrbyoZjvfQnjAX9?usp=drive_link")

    # if st.button("GitHub"):
    #     webbrowser.open("https://www.github.com/jaygala223")

    # if st.button("LinkedIn"):
    #     webbrowser.open("https://www.linkedin.com/in/jaykishorgala")
    
    # if st.button("Blog"):
    #     webbrowser.open("https://galacodes.hashnode.dev/")

    
st.header("news")

news_dict = {"June 2023": "Selected for the CVIT Summer School on AI with Focus on Computer Vision and Machine Learning at IIIT Hyderabad","Apr 2023":"Selected as a Fellow in the MLH Prep Fellowship of April 2023" ,"Feb 2023": "Paper accepted at the International Conference on Intelligent Computing and Networking", "Nov 2022":"Graduated from the Google ML Bootcamp 2022"}

st.write(news_dict)

st.header("publications")
st.divider()
st.write("**Identifying Suspicious Fishing Activity based on AIS Disabling Events**")
st.caption("by ***Anmaya Agarwal, Jay Gala and others.*** [Preprint](https://www.researchsquare.com/article/rs-2782178/v1)")
st.divider()
st.write("**A Review on Detecting Suspicious Fishing Activity**")
st.caption("by ***Anmaya Agarwal, Jay Gala and others.*** [PDF](https://drive.google.com/file/d/1Z56zgWp5y52GFK7uuOM7J89sp3S5Pqng/view?usp=drive_link)")
st.divider()