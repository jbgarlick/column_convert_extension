import streamlit as st
import pandas as pd
import numpy as np
import pgeocode as pg
import streamlit as st
import pandas as pd
import pymysql
import paramiko
import pandas as pd
from sshtunnel import SSHTunnelForwarder
from st_aggrid import AgGrid
from os.path import expanduser
from datetime import date, datetime, timedelta
import dateutil.relativedelta
import plotly.express as px
import altair as alt
from io import BytesIO
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials



def app():
    st.sidebar.image('VF Logo.jpeg')
    # CSS to inject contained in a string
    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

    # # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # VOX SQL Credentials
    mypkey = 'ssh-cert.pem'
    mysql_hostname = 'voxshipapivpc1read.ca3bp5ul1uqo.us-west-1.rds.amazonaws.com'
    mysql_username = 'jaredgarvox'
    mysql_password = '5=xzz/nTHJ'
    mysql_main_database = 'voxshipapi'
    sql_port = 3306
    ssh_host = '172.31.0.143'
    ssh_user = 'skylarvox'
    ssh_port = 22


    def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index=False).encode('utf-8')
    col1, col2 = st.columns(2)
    with col1:
        convert_column = st.text_area('Convert column')
        convert = st.button('Convert')
    with col2:
        if convert:
            col_to_list = convert_column.splitlines()
            list_to_str = "','".join(col_to_list)
            final_for_query = "('" + list_to_str + "')"
            st.text_area('output',final_for_query)
    input = st.text_area('Query Input')
    run_report = st.button('Run Report')
    if run_report:
        with SSHTunnelForwarder((ssh_host, ssh_port), ssh_username=ssh_user, ssh_pkey=mypkey,
                                    remote_bind_address=(mysql_hostname, sql_port)) as tunnel:
            conn = pymysql.connect(host='127.0.0.1', user=mysql_username, passwd=mysql_password, db=mysql_main_database, port=tunnel.local_bind_port)
            
            df = pd.read_sql_query(str(input), conn)
    
        st.download_button('Download Report', data = convert_df(df), file_name = 'export.csv')
        st.write('Num rows: ', len(df))
        st.dataframe(df)


if __name__ == "__main__":
    app()