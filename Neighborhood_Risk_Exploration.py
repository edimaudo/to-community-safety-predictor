from utils import * 
from data import *

st.title(APP_NAME)
st.header(NEIGHBORHOOD_HEADER)

st.write("""
         Highlights Socio-economic Metrics and Crime Risk trends for the selected neighborhood in Toronto.  
         """)


tab1, tab2 = st.tabs(["Socio-Ecomonic Metrics", "Crime Risk Trends"])



# Add LLM Here