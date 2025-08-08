
from utils import *
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



with st.spinner("loading data in progress", show_time=True):
    # crime risk data
    df = load_data("data/Major_Crime_Indicators_Open_Data.xlsx")

    # wellbeing data
    wellbeing_culture = load_data("data/wellbeing-toronto-culture.xlsx")
    wellbeing_economics = load_data("data/wellbeing-toronto-economics.xlsx")
    wellbeing_environment = load_data("data/wellbeing-toronto-environment.xlsx")
    wellbeing_health = load_data("data/wellbeing-toronto-health.xlsx")
    wellbeing_transportation = load_data("data/wellbeing-toronto-transportation.xlsx")
    wellbeing_housing =  load_data("data/wellbeing-toronto-housing.xlsx")
    wellbeing_recreation =  load_data("data/wellbeing-toronto-recreation.xlsx")

    # neighborhood
    neighborhood = load_geojson("data/Neighbourhoods.geojson") #gpd.read_file('data/Neighbourhoods.geojson')
    neighborhood_improvement_area = load_data("data/neighbourhood-improvement-areas.xlsx")

# Data Information
YEAR =  df['OCC_YEAR'].unique()
YEAR  = YEAR.astype('int')
YEAR.sort()

MONTH = df['OCC_MONTH'].unique()
MONTH  = MONTH.astype('str')
MONTH = pd.DataFrame(MONTH,columns = ['Month'])
month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 
'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
MONTH = MONTH.sort_values('Month', key = lambda x : x.apply (lambda x : month_dict[x]))
MONTH = MONTH['Month'].values.tolist()

DAY_OF_WEEK = df['OCC_DOW'].unique()
DAY_OF_WEEK   = DAY_OF_WEEK.astype('str')
DAY_OF_WEEK = pd.DataFrame(DAY_OF_WEEK,columns = ['DOW'])
dow_dict = {'Monday':1,'Tuesday':2,'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}
DAY_OF_WEEK = DAY_OF_WEEK.sort_values('DOW', key = lambda x : x.apply (lambda x : dow_dict[x]))
DAY_OF_WEEK = DAY_OF_WEEK['DOW'].values.tolist()

HOUR=  df['OCC_HOUR'].unique()
HOUR  = HOUR.astype('int')
HOUR.sort()

DAY =  df['OCC_DAY'].unique()
DAY  = DAY.astype('int')
DAY.sort()

MCI_CATEGORY = df['MCI_CATEGORY'].unique()
MCI_CATEGORY  = MCI_CATEGORY.astype('str')
MCI_CATEGORY.sort()

NEIGHBORHOOD = df['NEIGHBOURHOOD_158'].unique()
NEIGHBORHOOD = NEIGHBORHOOD.astype('str')
NEIGHBORHOOD.sort()

PREMISES_TYPE = df['PREMISES_TYPE'].unique()
PREMISES_TYPE  = PREMISES_TYPE.astype('str')
PREMISES_TYPE.sort()
