"""
Libraries
"""
import streamlit as st
import pandas as pd
import datetime
import os, os.path
import warnings
import random
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import folium
#from streamlit_folium import st_folium
import pickle
from pycaret.classification import *
import datetime
import time

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


