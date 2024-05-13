# import time
import numpy as np
# import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# st.title("Hi! I am Streamlit Web Application")
# st.header("I am a header")
# st.subheader("Hi! I am your subheader")
# st.text("Hi! I am a text function and can be used in place of paragraph tag")
# st.markdown("**Hello Akshara!!** *You are the best!!* `streamlit is fun`")
# st.markdown("[Click here to visit my git profile](https://github.com/akshara-krishnam)")
# st.caption("This is a Caption??!!")
# # st.latex(r'''
# ...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
# ...     \sum_{k=0}^{n-1} ar^k =
# ...     a \left(\frac{1-r^{n}}{1-r}\right)
# ...     ''')
# json = {"RCB": "Virat,FAF,Maxi","CSK":"MSD"}
# st.json(json)
# code = """print("Hello World!")"""
# st.code(code)
# st.write("**Bold** using st.write")
# st.metric(label="RMSE", value="120ms⁻¹", delta="-20ms⁻¹")

# df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
# st.table(df)
# st.dataframe(df)
# st.image('image.jpg', caption="This is my image caption", width=500)
# st.audio()
# st.video()


# def change():
#     print(f"checkbox changed to {st.session_state.checker}")


# state = st.checkbox("Checkbox", value=True, on_change=change, key="checker")
# if state:
#     st.write("Hi! This is Akshara")
# else:
#     st.write("Text hidden!")

# radio = st.radio("In which country do you live?", options=["US", "India"])
# # st.button
# st.selectbox("Which is your favourite IPL team?", options=["RCB","CSK","MI"])
# st.write(st.multiselect("Which is your favourite IPL team?", options=["RCB","CSK","MI"]))

# st.header('Uploading files')
# st.markdown("---")
# image = st.file_uploader(label="Please upload an image", type='jpg')
# if image is not None:
#     st.image(image, width=500)

# st.slider("This is a slider",10,20)
# st.select_slider("This is a slider", options=[1,2,3,3.5,5])
# # st.text_input("Text input")
# # st.text_area("Text area")
# # st.date_input("Enter your start date")
# # st.time_input("set timer")
# bar = st.progress(0)
# for i in range(1,10):
#     bar.progress(i*10)
#     time.sleep(5)

# st.write("## User Registration")
# st.markdown('<h2 style="text-align: center;"> User Registration </h2>',
# unsafe_allow_html=True)
# # form = st.form("Form 1")
# # form.text_input("Text input")
# # form.form_submit_button("Submit")

# with st.form("Form 2", clear_on_submit=True):
#     col1, col2 = st.columns(2)
#     col1.text_input("Enter your First name")
#     col2.text_input("Enter your Last name")
#     st.text_input("Email address")
#     st.text_input("Password")
#     st.text_input("Confirm Password")
#     st.form_submit_button("Submit")

x = np.linspace(0, 10, 100)
opt = st.sidebar.radio("Select any graph type",
                       options=["line", "bar", "sin", "H Bar"])
if opt == "line":
    fig = plt.figure(figsize=[10, 5])
    plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
    plt.title(f"{opt} chart selected")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    st.write(fig)
