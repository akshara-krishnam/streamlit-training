import os
import warnings
import pandas as pd
import streamlit as st
import plotly.express as px

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore Dashboard", page_icon=':bar_chart', layout='wide')

st.title(" :bar_chart: Sample Superstore EDA")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xls", "xlsx"])
if fl is not None:
    file_name = fl.name
    st.write(file_name)
    df = pd.read_excel(file_name)
else:
    os.chdir(r"/home/tiger04102/streamlit-training/")
    df = pd.read_excel('Sample - Superstore.xls')

col1, col2 = st.columns(2)
df["Order Date"] = pd.to_datetime(df["Order Date"])

#Getting min and max
start_date = df["Order Date"].min()
end_date = df["Order Date"].max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", start_date))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", end_date))

df = df[(df['Order Date']>=date1) & (df['Order Date']<=date2)].copy()

st.sidebar.header("Choose your filter: ")
region = st.sidebar.multiselect("Pick your region", df['Region'].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df['Region'].isin(region)]

state = st.sidebar.multiselect("Pick your state", df2['State'].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2['State'].isin(state)]

city = st.sidebar.multiselect("Pick your city", df3['City'].unique())
if not city:
    df4 = df3.copy()
else:
    df4 = df3[df3['City'].isin(city)]

filtered_df = df4.copy()
category_df = filtered_df.groupby(by =['Category'], as_index=False)["Sales"].sum()

with col1:
    st.subheader("Category wise sales")
    fig = px.bar(category_df, x="Category", y="Sales", text=['${:,.2f}'.format(x) for x in category_df["Sales"]],
                 template="seaborn")
    st.plotly_chart(fig, use_container_width=True, height=200)


with col2:
    st.subheader("Region wise sales")
    fig = px.pie(filtered_df, values="Sales", names = 'Region', hole=0.4)
    fig.update_traces(text = filtered_df['Region'], textposition = 'outside')
    st.plotly_chart(fig, use_container_width=True)

cl1, cl2 = st.columns(2)
with cl1:
    with st.expander("Category view data"):
        st.write(category_df.style.background_gradient(cmap="Blues"))
        csv = category_df.to_csv(index=False)
        st.download_button("Download Data", data=csv, file_name="Category.csv", mime='text/csv',
                           help = "Click here to download the data as csv file")

with cl2:
    with st.expander("Region view data"):
        region_df = filtered_df.groupby(by =['Region'], as_index=False)["Sales"].sum()
        st.write(region_df.style.background_gradient(cmap="Oranges"))
        csv = region_df.to_csv(index=False)
        st.download_button("Download Data", data=csv, file_name="Region.csv", mime='text/csv',
                           help = "Click here to download the data as csv file")

filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
st.subheader("Time Series Analysis")

linechart = pd.DataFrame(filtered_df.groupby(filtered_df['month_year'].dt.strftime("%Y :%b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x="month_year", y ="Sales", labels = {'Sales':'Amount'}, height=500, width=1000, template="gridon")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("Time Series view data"):
        st.write(linechart.style.background_gradient(cmap="Oranges"))
        csv = linechart.to_csv(index=False)
        st.download_button("Download Data", data=csv, file_name="TimeSeries.csv", mime='text/csv',
                           help = "Click here to download the data as csv file")

