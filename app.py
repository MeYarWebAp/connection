"""

"""
import itertools
import base64
import altair as alt
import copy
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st
import seaborn as sns
from fitter import Fitter, get_common_distributions, get_distributions
import pymc3 as pm
import matplotlib.pyplot as plt
from sklearn import preprocessing
#st.stop()
#import seaborn.apionly as sns
#%matplotlib inline
plt.style.use('bmh')
colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00','#CC79A7', '#56B4E9', '#009E73', '#F0E442', '#0072B2']
st.set_option('deprecation.showPyplotGlobalUse', False)
onedrive_link ="https://1drv.ms/x/s!AquyG0uXFObDgQXeo9qIu_prTFHx?e=1Behqf"
onedrive_link_h ="https://1drv.ms/x/s!AquyG0uXFObDgQrnt4QZ_YHZk1uB?e=FTqMBY"
@st.cache
def create_onedrive_directdownload (onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl


alt.renderers.set_embed_options(scaleFactor=2)


## Basic setup and app layout
st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called

crl_h=create_onedrive_directdownload (onedrive_link_h)
dataset_h=pd.read_excel(crl_h)
dataset_h.drop(dataset_h.columns[[0,1]], axis = 1, inplace = True)
#dataset_h.drop(dataset_h.columns[[0,1]], axis = 1, inplace = True)
st.write(dataset_h)
covidbook=dataset_h

ax = covidbook.groupby('Response Type')['Response Intensity'].size().plot(
    kind='bar', figsize=(12,3), title='Number of implementation per response', color=colors[0])
_ = ax.set_xlabel('Previous Sender')
_ = ax.set_ylabel('Number of messages')
_ = plt.xticks(rotation=45)
_ = ax.set_xlabel('Response code')
_ = ax.set_ylabel('Number of implementation')
_ = plt.xticks(rotation=45)
st.pyplot()
