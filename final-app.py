import time  # to simulate a real time data, time loop
from urllib.request import urlopen
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import json
from pandas import json_normalize
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import plotly.express as px
from os import path
from PIL import Image
import matplotlib.pyplot as plt
import os


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.

st.set_page_config(
    page_title="Discord Server Dashboard",
    page_icon="✅",
    layout="wide",
)
# dashboard title
st.markdown("<h1 style='text-align: center;'>Real-Time Discord Server Dashboard</h1>", unsafe_allow_html=True)


with open('Data.json') as f:
    user_mes = json.load(f)

with open('Cache.json') as g:
    user_num = json.load(g)

guilds = tuple(user_num.keys())

option = st.selectbox(
     'Please select one of the following servers',
     guilds)

# url = "http://127.0.0.1:5000"
# response = urlopen(url)
# data_json = json.loads(response.read())
# df = json_normalize(data_json[option]) 
df = json_normalize(user_mes[option])
online = df.filter(like='Online_')
online.columns = online.columns.str.replace("Online_Members.", "")
online = online.T
online[0] = online[0].str.replace("Total Online: ", "")
online.reset_index(inplace=True)
online = online.rename({'index': 'Time', 0: 'Total_Online_Users'}, axis=1)
online['Total_Online_Users'] = online['Total_Online_Users'].astype(int)


words_num = df.filter(like='Word_Frequency.')
words_num.columns = words_num.columns.str.replace("Word_Frequency.", "")
words_num = words_num.T
words_num.reset_index(inplace=True)
words_num = words_num.rename({'index': 'Words', 0: 'Words Frequency'}, axis=1)
words_num['Words Frequency'] = words_num['Words Frequency'].astype(int)

def cleanTxt(text):
 text = re.sub('@[A-Za-z0–9]+', '', str(text))
 text = re.sub('#', '', str(text)) 
 text = re.sub('_', '', str(text)) 
 text = re.sub('RT[\s]+', '', str(text))
 text = re.sub('https?:\/\/\S+', '', str(text))
 text = re.sub('[0-9]', '', str(text))
 text = re.sub('[^\w\s]','', str(text)) 
 words = text.lower().split()     
 stops = set(stopwords.words("english"))     
 meaningful_words = [w for w in words if not w in stops]      
 return (" ".join(meaningful_words))
words_num['Words'] = words_num['Words'].apply(cleanTxt)
nan_value = float("NaN")
words_num.replace("", nan_value, inplace=True)
words_num.dropna(subset = ["Words"], inplace=True)
words_num.reset_index(drop=True, inplace=True)




words_freq = px.scatter(words_num, y=words_num['Words Frequency'],size=words_num['Words Frequency'], color=words_num['Words'],hover_name=words_num['Words'], size_max=80)
words_freq.update_xaxes(showgrid=False)
words_freq.update_layout(showlegend=False)
words_freq.update_xaxes(visible=False)
# words_freq.show()

time1 = px.area(online, x=online['Time'], y=online['Total_Online_Users'])
# time1.show()
# time1 = px.line(online, x=online['Time'], y=online['Total_Online_Users'])
# time1.show()
# Add range slider
time1.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1D",
                     step="day",
                     stepmode="backward"),
                dict(count=6,
                     label="1M",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="6M",
                     step="month",
                     stepmode="todate"),
                dict(count=1,
                     label="1Y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

# time1.show()


channels = df.filter(like='Channels.')
channels.columns = channels.columns.str.replace("Channels.", "")
channels = channels.T
channels.reset_index(inplace=True)
channels = channels.rename({'index': 'Channels', 0: 'Total-Messages'}, axis=1)
# channels


import plotly.express as px
messages = px.bar(channels, x=channels['Channels'], y=channels['Total-Messages'])
# messages.show()

df = df.iloc[:, : 8]

df['Most Active Channel'] = df['Most Active Channel'].astype(str)
df['Most Active Channel'] = df['Most Active Channel'].str.replace("[", "")
df['Most Active Channel'] = df['Most Active Channel'].str.replace("]", "")
df['Most Active Channel'] = df['Most Active Channel'].str.replace("'", "")
df['Most Active Channel'] = df['Most Active Channel'].str.replace("'", "")
most_active_channel = str(df['Most Active Channel'])
most_active_channel = re.sub('[0-9]', '', str(df['Most Active Channel']))
sep = '\n'
most_active_channel = most_active_channel.split(sep, 1)[0]
most_active_channel.strip()
# most_active_user = str(df['Most Active Users'])
df['Most Active Users'] = df['Most Active Users'].astype(str)
df['Most Active Users'] = df['Most Active Users'].str.replace("[", "")
df['Most Active Users'] = df['Most Active Users'].str.replace("]", "")
df['Most Active Users'] = df['Most Active Users'].str.replace("'", "")
df['Most Active Users'] = df['Most Active Users'].str.replace("'", "")
most_active_user = re.sub('[0-9]', '', str(df['Most Active Users']))
most_active_user = re.sub('#', '', str(most_active_user))
sep = '\n'
most_active_user = most_active_user.split(sep, 1)[0]
sep = ','
most_active_user = most_active_user.split(sep, 1)[0]
most_active_user.strip()


# for seconds in range(200):
# url1="http://127.0.0.1:8000"
# response1 = urlopen(url1)
# data_json1 = json.loads(response1.read())
# df1 = json_normalize(data_json1[option])
df1 = json_normalize(user_num[option])
df1["Words"] = df1["Words"].astype(str)
df1["Words"] = df1["Words"].str.replace("[", "")
df1["Words"] = df1["Words"].str.replace("]", "")
df1["Words"] = df1["Words"].str.replace("'", "")
df1["Words"] = df1["Words"].str.replace("'", "")
words = df1["Words"]
words = pd.DataFrame({'Index':words.index, 'words':words.values})

def cleanTxt(text):
 text = re.sub('@[A-Za-z0–9]+', '', str(text))
 text = re.sub('#', '', str(text)) 
 text = re.sub('_', '', str(text)) 
 text = re.sub('RT[\s]+', '', str(text))
 text = re.sub('https?:\/\/\S+', '', str(text))
 text = re.sub('[0-9]', '', str(text))
 text = re.sub('[^\w\s]','', str(text)) 
 words = text.lower().split()     
 stops = set(stopwords.words("english"))     
 meaningful_words = [w for w in words if not w in stops]      
 return (" ".join(meaningful_words))
words['words'] = words['words'].apply(cleanTxt)

df1.drop('Words', axis=1, inplace=True)
df1.columns = df1.columns.str.replace("Users.", " ")
users = df1.T
users.reset_index(inplace=True)
users = users.rename({'index': 'Users', 0: 'Total_Messages'}, axis=1)
# users
#     time.sleep(1)
    # users


users = px.pie(df, values=users['Total_Messages'], names=users['Users'])
# users.show()


# !pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
allWords = ' '.join([twts for twts in words['words']])
discord_mask = np.array(Image.open(path.join(d, "discord.png")))

print(discord_mask)

wordCloud = WordCloud(background_color="black", max_words=2000, mask=discord_mask, contour_width=1, contour_color='steelblue',margin=0,scale=1.1).generate(allWords)

# plt.imshow(wordCloud, interpolation="bilinear")
# plt.axis('off')
# plt.show()
# plt.savefig('Plotly-World_Cloud.png')
fig, ax = plt.subplots(figsize = (8, 5))
ax.imshow(wordCloud, interpolation = "bilinear")
plt.axis('off')
plt.close()






placeholder = st.empty()
with placeholder.container():
    st.title("")
    st.title("")
    st.title("")
# create three columns
    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="Total Channels ⏳",
        value=int(df['Total Channels']),
    #     delta=round(df['Total Channels']) - 10,
    )

    kpi2.metric(
        label="Total Messages ✉️",

        value=int(df['Total Messages']),
    #     delta=-10 + df['Total Messages'],
    )

    kpi3.metric(
        label="Total Users 👥",

        value=int(df['Total Users']),
    #     delta=round(df['Total Users']) - 10,
    )
    
    kpi4.metric(
        label="Most Active Channel 🫶",

        value=str(most_active_channel),
    #     delta=round(df['Total Users']) - 10,
    )
    
    kpi5.metric(
    label="Most Active Users 🔥",

    value=str(most_active_user),
    #     delta=round(df['Total Users']) - 10,
    )
    
    st.title("")
    st.title("")
    fig_col1, fig_col2 = st.columns(2)

    with fig_col1:
        st.markdown("<h3 style='text-align: center;'>Total Messages From Users</h3>", unsafe_allow_html=True)
        st.plotly_chart(users, use_container_width=True)

    with fig_col2:
        st.markdown("<h3 style='text-align: center;'>Total Messages In Channels</h3>", unsafe_allow_html=True)
        st.plotly_chart(messages, use_container_width=True)
    
#     st.title("")
#     st.title("")

#     fig_col3, fig_col4 = st.columns(2)

#     with fig_col3:
#         st.markdown("<h3 style='text-align: center;'>Online Users</h3>", unsafe_allow_html=True)
#         st.plotly_chart(time1, use_container_width=True)

#     with fig_col4:
#         st.markdown("<h3 style='text-align: center;'>Recurring Words</h3>", unsafe_allow_html=True)
#         st.plotly_chart(words_freq, use_container_width=True)

 
    st.markdown("<h3 style='text-align: center;'>Online Users</h3>", unsafe_allow_html=True)
    st.plotly_chart(time1, use_container_width=True)

#     st.title("")
#     st.title("")
    st.markdown("<h3 style='text-align: center;'>Recurring Words</h3>", unsafe_allow_html=True)
    st.plotly_chart(words_freq, use_container_width=True)
    fig_col3, fig_col4, fig_col5 = st.columns(3)
    with fig_col4:
        st.markdown("<h3 style='text-align: center;'>Recurring Words</h3>", unsafe_allow_html=True)
        st.pyplot(fig, use_container_width=True)

