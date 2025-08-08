from utils import * 
from data import *

st.title(APP_NAME)
st.header(OVERVIEW_HEADER)

with st.sidebar:
    year_options = st.multiselect('Year',YEAR,default=YEAR)
    month_options = st.multiselect('Month',MONTH,default=MONTH)
    dow_options = st.multiselect('Day of Week',DAY_OF_WEEK,default=DAY_OF_WEEK)
    mci_options = st.multiselect('Crime Type',MCI_CATEGORY,default=MCI_CATEGORY)
    premises_options = st.multiselect('Premises Type',PREMISES_TYPE,default =PREMISES_TYPE)


