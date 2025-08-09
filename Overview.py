from utils import * 
from data import *

st.title(APP_NAME)
st.header(OVERVIEW_HEADER)

st.write("""
         Highlights wellness and crime risk trends in the City of Toronto.  
         """)


tab1, tab2 = st.tabs(["Wellbeing Metrics", "Crime Risk Trends"])

with tab1:
    st.subheader("")

    st.metric("",0)

    st.markdown("<br><br>")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Total Crime by Year")
        crimes_data = df_filtered[['MCI_CATEGORY','OCC_YEAR']]
        crimes_data = crimes_data.groupby(['OCC_YEAR']).agg(Total_reviews = ('MCI_CATEGORY', 'count')).reset_index()
        crimes_data.columns = ['Year','Total']
        crimes_data.sort_values("Year", ascending=True)
        fig = px.bar(crimes_data, x="Year", y="Total")
        st.plotly_chart(fig)

        st.subheader("Crime Category by Month")
        crimes_data = df_filtered[['MCI_CATEGORY','OCC_MONTH']]
        crimes_data = crimes_data.groupby(['MCI_CATEGORY','OCC_MONTH']).agg(Total_reviews = ('MCI_CATEGORY', 'count')).reset_index()
        crimes_data.columns = ['MCI CATEGORY', 'Month','Total']
        month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 
        'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
        crimes_data = crimes_data.sort_values('Month', key = lambda x : x.apply (lambda x : month_dict[x]))
        fig = px.line(crimes_data, x="Month", y="Total",color='MCI CATEGORY')
        st.plotly_chart(fig)

        st.subheader("Crime Category by Day of Week")
        crimes_data = df_filtered[['MCI_CATEGORY','OCC_DOW']]
        dow_dict = {'Monday':1,'Tuesday':2,'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}
        crimes_data = crimes_data[crimes_data['OCC_DOW'].isin(dow_dict)]
        crimes_data = crimes_data.groupby(['MCI_CATEGORY','OCC_DOW']).agg(Total_reviews = ('MCI_CATEGORY', 'count')).reset_index()
        crimes_data.columns = ['MCI CATEGORY', 'Day of Week','Total']
        crimes_data = crimes_data.sort_values('Day of Week', key = lambda x : x.apply (lambda x : dow_dict[x]))
        fig = px.line(crimes_data, x="Day of Week", y="Total",color='MCI CATEGORY')
        st.plotly_chart(fig)





    

    with col2:
        st.subheader("Crime Category by Year")
        crimes_data = df_filtered[['MCI_CATEGORY','OCC_YEAR']]
        crimes_data = crimes_data.groupby(['MCI_CATEGORY','OCC_YEAR']).agg(Total_reviews = ('MCI_CATEGORY', 'count')).reset_index()
        crimes_data.columns = ['MCI CATEGORY', 'Year','Total']
        crimes_data.sort_values("Year", ascending=True)
        fig = px.line(crimes_data, x="Year", y="Total",color='MCI CATEGORY')
        st.plotly_chart(fig)

        st.subheader("Crime Category by Day of the Month")
        crimes_data = df_filtered[['MCI_CATEGORY','OCC_DAY']]
        crimes_data = crimes_data.groupby(['MCI_CATEGORY','OCC_DAY']).agg(Total_reviews = ('MCI_CATEGORY', 'count')).reset_index()
        crimes_data.columns = ['MCI CATEGORY', 'Day','Total']
        crimes_data.sort_values("Day", ascending=True)
        fig = px.line(crimes_data, x="Day", y="Total",color='MCI CATEGORY')
        st.plotly_chart(fig)

        st.subheader("Crime Category by by Hour")
        crimes_data = df_filtered[['MCI_CATEGORY','OCC_HOUR']]
        crimes_data = crimes_data.groupby(['MCI_CATEGORY','OCC_HOUR']).agg(Total_reviews = ('MCI_CATEGORY', 'count')).reset_index()
        crimes_data.columns = ['MCI CATEGORY', 'Hour','Total']
        crimes_data.sort_values("Hour", ascending=True)
        fig = px.line(crimes_data, x="Hour", y="Total",color='MCI CATEGORY')
        st.plotly_chart(fig)
