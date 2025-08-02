from utils import *

st.title(APP_NAME)
st.header(ABOUT_HEADER)

st.markdown(
    """
    Focusing on the theme - *Build with agentic AI challenge*, this project analyzes crime risk and wellbeing data in Toronto's neighborhoods.  
    It also enables the user to predict crime risk and using the data provide proactive steps for people to take. 
    It is built using [streamlit](https://streamlit.io/cloud) and [IBM Watson x](https://www.ibm.com/products/watsonx).  
    The data is from [Toronto Police](https://data.torontopolice.on.ca/datasets/TorontoPS::major-crime-indicators-open-data/about) and [City of Toronto](https://data.urbandatacentre.ca/organization/city-of-toronto-open-data?q=wellbeing&sort=score+desc%2C+metadata_modified+desc&page=1).
    """
)