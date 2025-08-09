
from utils import *
wellbeing_link = "https://data.urbandatacentre.ca/organization/city-of-toronto-open-data?q=wellbeing&sort=score+desc%2C+metadata_modified+desc&page=3"

# Add orchestration here

"""
Data
"""
# Load data
@st.cache_data
def load_data(DATA_URL,DATA_TYPE):
    if DATA_TYPE == 'xlsx':
        data = pd.read_excel(DATA_URL)
    elif DATA_TYPE == 'geojson':
        data = pd.read_json(DATA_URL)
    return data


# crime risk data
df = load_data("data/Major_Crime_Indicators_Open_Data.xlsx",'xlsx')
df_filtered = df[(df['OCC_YEAR'] >= 2014) & (df['OCC_YEAR'] <= 2025)]

# wellbeing data
wellbeing_culture = load_data("data/wellbeing-toronto-culture.xlsx",'xlsx')
wellbeing_economics = load_data("data/wellbeing-toronto-economics.xlsx",'xlsx')
wellbeing_environment = load_data("data/wellbeing-toronto-environment.xlsx",'xlsx')
wellbeing_health = load_data("data/wellbeing-toronto-health.xlsx",'xlsx')
wellbeing_transportation = load_data("data/wellbeing-toronto-transportation.xlsx",'xlsx')
wellbeing_housing =  load_data("data/wellbeing-toronto-housing.xlsx",'xlsx')
wellbeing_recreation =  load_data("data/wellbeing-toronto-recreation.xlsx",'xlsx')

# neighborhood
neighborhood_improvement_area = load_data("data/neighbourhood-improvement-areas.xlsx",'xlsx')
neighborhood = load_data("data/Neighbourhoods.xlsx","xlsx")


# Data Information
YEAR = (
    df.loc[(df['OCC_YEAR'] >= 2014) & (df['OCC_YEAR'] <= 2025), 'OCC_YEAR']
      .unique()
)
YEAR = YEAR.astype(int)
YEAR.sort()

month_dict = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}

MONTH = (
    pd.DataFrame({'Month': df['OCC_MONTH'].dropna().unique()})  # remove NaN here
    .assign(order=lambda d: d['Month'].str.strip().map(month_dict))
    .dropna(subset=['order'])  # also removes anything not in month_dict
    .sort_values('order')
    ['Month'].tolist()
)


dow_dict = {
    'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
    'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7
}

DAY_OF_WEEK = (
    pd.Series(df['OCC_DOW'].dropna().unique())
      .str.strip()                      # remove extra spaces
      .str.title()                      # normalize capitalization
      .drop_duplicates()
      .sort_values(key=lambda x: x.map(dow_dict))
      .tolist()
)


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

 