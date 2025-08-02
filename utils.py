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

"""
Dashboard Information
"""


APP_NAME = 'TO Neighborhood Risk Predictor'
ABOUT_HEADER = 'About'
NEIGHBORHOOD_HEADER = "Neighborhood Risk Exploration"
OVERVIEW_HEADER = 'Risk Overview'
PREDICTON_HEADER = 'Neighborhood Crime Risk Prediction'
APP_FILTERS = 'Filters'
NO_DATA_INFO = 'No data available to display based on the filters'

warnings.simplefilter(action='ignore', category=FutureWarning)
st.set_page_config(
    page_title=APP_NAME,
    page_icon="🌍",
    layout="wide"
)

"""
Load data
"""