from utils import *
from data import *
from config import *

st.title(APP_NAME)
st.header(PREDICTON_HEADER)

with st.sidebar:
    month_options = st.selectbox('Month',MONTH)
    dow_options = st.selectbox('Day of Week',DAY_OF_WEEK)
    hour_options = st.selectbox('Hour',HOUR)
    premises_options = st.selectbox('Premises Type',PREMISES_TYPE)
    neighbourhood_options = st.selectbox('Neighborhood',NEIGHBORHOOD)
    clicked = st.button("Run Prediction")

st.subheader("Prediction")

st.subheader("Community Risk Insights + Actions")
## Add LLM here