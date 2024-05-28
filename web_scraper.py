import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title="Web scraper", page_icon=":alien",layout='wide')
st.title("My Web Scraper Application")

with st.form("Search"):
    keyword = st.text_input("What images do you want to search?")
    submit = st.form_submit_button("Search")
# placeholder = st.empty()
# if submit:
if keyword:
    url = f"https://unsplash.com/s/photos/{keyword}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features="html.parser")
    rows = soup.find_all("div", class_="d95fI")
    col1, col2 = st.columns(2)
    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img", class_="ApbSI vkrMA")
            img_list = img["srcset"].split("?")
            anchor = figures[i].find("a", class_="Prxeh")
            # print(anchor["href"])
            if i == 0:
                col1.image(img_list[0])
                btn1 = col1.button("Download", key=f'{str(index)}_{str(i)}')
                if btn1:
                    # print((f"https://unsplash.com{anchor['href']}"))
                    webbrowser.open_new_tab(f"https://unsplash.com{anchor['href']}")
            else:
                col2.image(img_list[0])
                btn2 = col2.button("Download", key=f'{str(index)}_{str(i)}')
                if btn2:
                    # print((f"https://unsplash.com{anchor['href']}"))
                    webbrowser.open_new_tab(f"https://unsplash.com{anchor['href']}")
else:
    st.warning("Type your keyword to search for images!")

# div:d95fI = > fig => img:ApbSI vkrMA
