import streamlit as st
from PIL import Image
import requests
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
def get_text_content(url):
    try:
        html = urlopen(url).read()
    except:
        pass
    soup = BeautifulSoup()
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text
from pymongo import MongoClient
MONGO_URL= 'mongodb+srv://projectvaluehub:KiYKX9PolLZNFCO3@projectvalhub.nbq6g.mongodb.net/projectValHubDB?retryWrites=true&w=majority'
cluster = MongoClient(MONGO_URL)
st.title("中文新聞")
image = Image.open('PVhub.png')
st.image(image, caption='Project Valuehub, Designed for New Generation Investors')
data_choices = ['價格追縱', '基本面分析', '新聞分析']
function = st.sidebar.selectbox("請選擇功能", data_choices)
def get_news_sources_INDEX(news_sources, index_choices):
    if news_sources == "經濟通":
        st.write("hi")
        if index == "深圳A股":
            st.write("Displaying 深圳A股")
            url = "https://www.etnet.com.hk/www/tc/stocks/ah.php"
        elif index == "港股":
            url = 'https://www.etnet.com.hk/www/tc/stocks/indexes_detail.php?subtype=hsi'
        else:
            url = 'https://www.etnet.com.hk/www/tc/stocks/realtime/top20.php'
        res = requests.get(url)
        st.write(res.text)
    elif news_sources == "HK01":
        st.header("HK01")
        url = ' https://rsshub.app/hk01/hot'
        res = requests.get(url)
        st.write(res.text)
    elif news_sources == "星島日報":
        st.header("星島日報")
        url = "https://rsshub.app/stheadline/std/realtime/即時"
        res = get_text_content(url)
        st.write(res.status)
    elif news_sources == "明報":
        st.header("明報")
        url = "https://rsshub.app/mingpao/ins/s00002"
        res = requests.get(url)
        text = res.text
        st.write(res.text.title())
        print(res)
    elif news_sources == "有線新聞":
        st.header("有線新聞")
        url = "https://rsshub.app/icable/international/plain/101800"
        res = requests.get(url)
        html = url.urlopen(url)
        st.write(res.text.title())
    else:
        # url = 'https://hk.finance.yahoo.com/news/%E5%8A%A0%E6%8B%BF%E5%A4%A7%E9%8B%B0%E7%A4%A6%E5%95%86-sigma-lithium-%E5%82%B3%E7%8D%B2-tesla-044002828.html'
        url = "https://rsshub.app/now/news/finance/507823"
        res = requests.get(url)
        print(res.text)
        st.write(res)
        st.write(res.text)

if function == '新聞分析':
    st.write("news source")
    st.sidebar.header("請選擇新聞來源: ")
    news_source_choice = ["請選擇新聞來源","星島日報", "明報", "彭博中文", "HK01", "經濟通", "有線新聞", "others"]
    news_sources = st.sidebar.selectbox("新聞來源", news_source_choice)
    endpoint_choices = ['個別股票走勢', '指數趨勢', '宏觀經濟']
    endpoint = st.sidebar.selectbox("新聞類別", endpoint_choices)
    if endpoint == '指數趨勢' or endpoint == '個別股票走勢':
        index_choices = ["港股", "深圳H股", "深圳A股", "國企指數", "恆生科技指數",]
        index = st.sidebar.selectbox("選擇指數", index_choices)
        get_news_sources_INDEX(news_sources, index_choices)