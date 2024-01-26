import streamlit as st
import pandas as pd
import pickle as pkl
import joblib

# Load models and data
cluster_0 = joblib.load("cluster_0.pkl")
cluster_1 = joblib.load("cluster_1.pkl")
cluster_2 = joblib.load("cluster_2.pkl")
cluster_3 = joblib.load("cluster_3.pkl")
mer_0 = joblib.load("mer_0.pkl")
mer_1 = joblib.load("mer_1.pkl")
mer_2 = joblib.load("mer_2.pkl")
mer_3 = joblib.load("mer_3.pkl")
ID = joblib.load("ID.pkl")
data = joblib.load("data.pkl")


# Main title and image
st.title('Customer Segmentation analysis')
st.image("https://i.ibb.co/wynpxvD/career-change.jpg")


# User inputs on the left side
with st.sidebar:

    User_Id = st.number_input("Enter Your User_Id:", min_value=0, max_value=10000, step=1, value=50)
    # Check if the user ID is in the DataFrame
    if User_Id in data['User_Id'].values:
        st.sidebar.title('User Data')
        user_data = data[data['User_Id'] == User_Id].squeeze()
        st.sidebar.write(f'Trx_Rank: {user_data["Trx_Rank"]}')
        st.sidebar.write(f'Points: {user_data["Points"]}')
        st.sidebar.write(f'Trx_Vlu : {user_data["Trx_Vlu"]}')
        st.sidebar.write(f'Customer_Age: {user_data["Customer_Age"]}')
        st.sidebar.write(f'Trx_Age : {user_data["Trx_Age"]}')
        st.sidebar.write(f'Category In English : {user_data["Category In English"]}')
        st.sidebar.write(f'Mer_Name : {user_data["Mer_Name"]}')
        st.sidebar.write(f'Recency: {user_data["Recency"]}')
        st.sidebar.write(f'Frequency : {user_data["Frequency"]}')
        st.sidebar.write(f'MonetaryValue: {user_data["MonetaryValue"]}')
#         st.sidebar.write(f'User_Id: {User_Id}')
#         st.sidebar.write(f'Points: {data["Points"]}')




    # Add checkbox widget
agree = st.checkbox(f'I am sure that my user ID is {User_Id} ')

if st.button('Submit'):
        # Perform action based on widget inputs
    if agree:
        
        image_path = "Plot.png"
      # Replace with the actual path to your image file
        image = st.image(image_path, caption='Cluster Distrubution Analysis', use_column_width=True)
        # Check if the user ID is in Cluster 0
        if User_Id in cluster_0.index:
                Cluster = 0
                st.write(f'Cluster: {Cluster} ')
                st.info(' Based on our analysis it looks like you have made your last transaction a long time ago,and  have few purchases in total Please can you provide any problems you have . \n')
                st.write(f'Merchants Recomended :\n {mer_0} ')

        elif User_Id in cluster_1.index:
            Cluster = 1
            st.write(f'Cluster: {Cluster} ')
            st.info(' Based on our analysis it looks like you have transacted recently and have a lower purchase frequency, with a low amount of monetary spending Please can you provide any problems you have . \n')
            st.write(f'Merchants Recomended :\n {mer_1} ')
        elif User_Id in cluster_2.index:
            Cluster = 2
            st.write(f'Cluster: {Cluster} ')
            st.info(' Based on our analysis it looks like you have made your last transaction a while ago and who made frequent and large purchases in the past We thank you and wish you the best to go . \n')
            st.write(f'Merchants Recomended: \n {mer_2} ')
        elif User_Id in cluster_3.index:
            Cluster = 3
            st.write(f'Cluster: {Cluster} ')
            st.info(' Based on our analysis it looks like you are the most frequent customers with the highest monetary spending amount and transact most recently We thank you and wish you the best to go . \n')
            st.write(f'Merchants Recomended: \n {mer_3} ')
        else:
            st.write(f'User: {User_Id} does not belong to any cluster')
        
    else:
        st.warning('Please confirm your User_ID')
