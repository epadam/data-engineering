import streamlit as st

st.title('Data Engineering')
# change the process to how to build data pipeline on GKE

# Find a demo website for ELK, ETL
# Ex: A shopping site that track user operation and then can be analyzed to change the layout or use ML model to predict and recomannd the product or something
# EX2: Log that record the timing of the api or server status          
st.image('uber.png', caption='From Meet Michelangelo: Uber’s Machine Learning Platform', use_column_width=True)
st.write('This is one example of data pipeline from uber')

st.header('Data Pipeline for ETL')

st.subheader('0. Data pipeline tools')

st.write('Airflow, Luigi, Argo')



st.subheader('1. Data source and acquisition')

# A website that can generate fake data in the frontend/backend server, which is deployed in k8s 
st.write('Images upload, Videos, text, logs, csv from web, app, frontend, backend')

# You can track your server status, what is most used part in frontend
st.write('Tools include filebeat for log')

# Or pretend there are already some csv files and the frontend just show these csv files



st.subheader('2. Data Streaming')

# Kafka cluster in k8s take the csv files
st.write('kafka')

# Show pic of kafka deployment in GKE




st.subheader('3.Basic ETL Process')

# logstash process the csv files
st.write('Here you may need simple data processing using logstash, pandas, Spark')
# Show the processed csv files

st.subheader('4. Data lake/Data Warehouse')

# csv stored in elasticsearch or hadoop
st.write('Hadoop(HDFS), ElasticSearch, MongoDB Altas as data lake')
# show the link of the kibana 

# Load the data to database
st.write('After further ETL Process, Data can be loaded into Data warehouse like HBase, MongoDB, Canssandra, Snowflake')

st.subheader('5. Exploration Data Analysis')

st.write('Data in data lake/data warehouse is further used for analysis. Query with Spark SQL,Hive')

# using kibana to show the data
st.write('Visualization with Kibana/Grafana, it also has some ml functions')

st.write('EDA with pandas, Spark')

# Kubeflow read the csv and build ml model to predict it and show it on a frontend page of admin alert 
st.write('For Machine Learning using Kubeflow pipeline please check this streamlit app')

# Show the model training results
