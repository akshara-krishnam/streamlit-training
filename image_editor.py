import streamlit as st
from PIL import Image
from PIL.ImageFilter import BLUR,SMOOTH,DETAIL

st.markdown("<h1 style='text-align :center;'> Image Editor </h1>", unsafe_allow_html=True)
st.markdown('---')
image = st.file_uploader("Upload your image", type=["jpg","png","jpeg"])
info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:

    img = Image.open(image)
    info.markdown("<h2 style='text-align :center;'> Information </h2>", unsafe_allow_html=True)
    size.markdown(f"<h6>Size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>", unsafe_allow_html=True)
    st.write(img)
    st.markdown("<h2 style='text-align :center;'> Resizing </h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)
    st.markdown("<h2 style='text-align :center;'> Rotation </h2>", unsafe_allow_html=True)
    degrees = st.number_input("Degrees",min_value=0, max_value=360)
    st.markdown("<h2 style='text-align :center;'> Filters </h2>", unsafe_allow_html=True)
    filter = st.selectbox("Filters", options=["None", "Blur", "Detail", "Smooth"])
    submit = st.button("Submit")
    if submit:
        edited = img.resize((width, height)).rotate(degrees)
        if filter != "None":
            if filter == "Blur":
                filtered_img = edited.filter(BLUR)
            elif filter == "Detail":
                filtered_img = edited.filter(DETAIL)
            elif filter == "Smooth":
                filtered_img = edited.filter(SMOOTH)
            st.write(filtered_img)
        else:
            st.write(edited)
        # img.filter()
