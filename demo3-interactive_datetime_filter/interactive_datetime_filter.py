import pandas as pd
import streamlit as st
import datetime
import re
import base64

def download_csv(name,df):
    
    csv = df.to_csv(index=False)
    base = base64.b64encode(csv.encode()).decode()
    file = (f'<a href="data:file/csv;base64,{base}" download="%s.csv">Download file</a>' % (name))
    
    return file

def df_filter(message,df):

        slider_1, slider_2 = st.slider('%s' % (message),0,len(df)-1,[0,len(df)-1],1)

        while len(str(df.iloc[slider_1][1]).replace('.0','')) < 4:
            df.iloc[slider_1,1] = '0' + str(df.iloc[slider_1][1]).replace('.0','')
            
        while len(str(df.iloc[slider_2][1]).replace('.0','')) < 4:
            df.iloc[slider_2,1] = '0' + str(df.iloc[slider_1][1]).replace('.0','')

        start_date = datetime.datetime.strptime(str(df.iloc[slider_1][0]).replace('.0','') + str(df.iloc[slider_1][1]).replace('.0',''),'%Y%m%d%H%M%S')
        start_date = start_date.strftime('%d %b %Y, %I:%M%p')
        
        end_date = datetime.datetime.strptime(str(df.iloc[slider_2][0]).replace('.0','') + str(df.iloc[slider_2][1]).replace('.0',''),'%Y%m%d%H%M%S')
        end_date = end_date.strftime('%d %b %Y, %I:%M%p')

        st.info('Start: **%s** End: **%s**' % (start_date,end_date))
        
        filtered_df = df.iloc[slider_1:slider_2+1][:].reset_index(drop=True)

        return filtered_df

if __name__ == '__main__':

    df = pd.read_csv('file_path')

    st.title('Datetime Filter')
    filtered_df = df_filter('Move sliders to filter dataframe',df)

    column_1, column_2 = st.beta_columns(2)

    with column_1:
        st.title('Data Frame')
        st.write(filtered_df)

    with column_2:
        st.title('Chart')
        st.line_chart(filtered_df['value'])

    st.markdown(download_csv('Filtered Data Frame',filtered_df),unsafe_allow_html=True)
    
