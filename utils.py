"""
Libraries
"""
import streamlit as st
import pandas as pd
import datetime
import os, os.path
import warnings
import random
#import plotly.express as px
#import plotly.graph_objects as go
#import geopandas as gpd
#import folium
#from streamlit_folium import st_folium

import pickle
#from pycaret.classification import *
import datetime

"""
App Information
"""
APP_NAME = 'TO Crime Risk & Wellbeing Insights'
ABOUT_HEADER = 'About'
NEIGHBORHOOD_HEADER = "Neighborhood Crime Risk & Wellbeing"
OVERVIEW_HEADER = 'Crime Risk & Wellbeing Overview'
PREDICTON_HEADER = 'Neighborhood Crime Risk Prediction'
APP_FILTERS = 'Filters'
NO_DATA_INFO = 'No data available to display based on the filters'

warnings.simplefilter(action='ignore', category=FutureWarning)
st.set_page_config(
    page_title=APP_NAME,
    layout="wide"
)


wellbeing_link = "https://data.urbandatacentre.ca/organization/city-of-toronto-open-data?q=wellbeing&sort=score+desc%2C+metadata_modified+desc&page=3"


"""
Data
"""
# Load data
@st.cache_data
def load_data(DATA_URL):
    data = pd.read_excel(DATA_URL)
    return data

def load_geojson(DATA_URL):
    data = pd.read_json(DATA_URL)
    return data

# crime risk data
df = load_data("data/Major_Crime_Indicators_Open_Data.xlsx")

# wellbeing data
wellbeing_culture = load_data("data/wellbeing-toronto-culture.xlsx")
wellbeing_economics = load_data("data/wellbeing-toronto-economics.xlsx")
wellbeing_environment = load_data("data/wellbeing-toronto-environment.xlsx")
wellbeing_health = load_data("data/wellbeing-toronto-health.xlsx")
wellbeing_transportation = load_data("data/wellbeing-toronto-transportation.xlsx")
wellbeing_housing =  load_data("data/wellbeing-housing.xlsx")
wellbeing_recreation =  load_data("data/wellbeing-recreation.xlsx")

# neighborhood
neighborhood = load_geojson("data/Neighbourhoods.geojson")
neighborhood_improvement+area = load_data("data/neighbourhood-improvement-areas.xlsx")

month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 
'August':8, 'September':9, 'October':10, 'November':11, 'December':12}

dow_dict = {'Monday':1,'Tuesday':2,'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}