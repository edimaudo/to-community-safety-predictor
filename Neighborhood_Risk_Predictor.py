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


# Model information
model_data = df_filtered[['OCC_MONTH','OCC_DOW','OCC_HOUR','PREMISES_TYPE','Neighborhood','MCI_CATEGORY']]
# Categorize data
model_data["OCC_MONTH"] = model_data["OCC_MONTH"].astype('category')
model_data["OCC_DOW"] = model_data["OCC_DOW"].astype('category')
model_data["PREMISES_TYPE"] = model_data["PREMISES_TYPE"].astype('category')
model_data["Neighborhood"] = model_data["Neighborhood"].astype('category')
model_data["MCI_CATEGORY"] = model_data["MCI_CATEGORY"].astype('category')
model_data["OCC_MONTH_cat"] = model_data["OCC_MONTH"].cat.codes
model_data["OCC_DOW_cat"] = model_data["OCC_DOW"].cat.codes
model_data["PREMISES_TYPE_cat"] = model_data["PREMISES_TYPE"].cat.codes
model_data["Neighborhood_cat"] = model_data["Neighborhood"].cat.codes
model_data["MCI_CATEGORY_cat"] = model_data["MCI_CATEGORY"].cat.codes

model_info = model_data[(model_data.OCC_MONTH == month_options)]
model_info.reset_index(drop=True, inplace=True)
month = model_info['OCC_MONTH_cat'][0]

model_info = model_data[(model_data.OCC_DOW == dow_options)]
model_info.reset_index(drop=True, inplace=True)
dow = model_info['OCC_DOW_cat'][0]

model_info = model_data[(model_data.OCC_HOUR == hour_options)]
model_info.reset_index(drop=True, inplace=True)
hour = model_info['OCC_HOUR'][0]

model_info = model_data[(model_data.PREMISES_TYPE == premises_options)]
model_info.reset_index(drop=True, inplace=True)
premise = model_info['PREMISES_TYPE_cat'][0]

model_info = model_data[(model_data.Neighborhood == neighbourhood_options)]
model_info.reset_index(drop=True, inplace=True)
neighbourhood = model_info['Neighborhood_cat'][0]

if clicked:
    st.subheader("Prediction")
    info_df = pd.DataFrame(columns = ['OCC_MONTH_cat','OCC_DOW_cat','OCC_HOUR','PREMISES_TYPE_cat','Neighborhood_cat'],index = ['a'])
    info_df.loc['a'] = [month,dow,hour, premise, neighbourhood]
    # Load model
    saved_final_model = load_model('model/Final Model')
    # Prediction
    new_prediction = predict_model(saved_final_model, data=info_df)
    crime_category = new_prediction['Label'][0]
    if crime_category == 0:
        crime_output = 'Assault'
    elif crime_category == 1:
        crime_output = 'Auto Theft'
    elif crime_category == 2:
        crime_output = 'Break & Enter'
    elif crime_category == 3:
        crime_output = 'Robbery'
    else:
        crime_output = 'Theft Over'

    st.write("Based on the your selection")
    st.metric("The Predicted Crime Categroy is : ",crime_output)




st.subheader("Community Risk Insights + Actions")
## Add LLM here