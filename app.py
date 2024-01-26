# streamlit run  "app.py"
import streamlit as st
import pandas as pd
import pickle as pkl
import joblib

cluster_0 = joblib.load("cluster_0.pkl")
cluster_1 = joblib.load("cluster_1.pkl")
cluster_2 = joblib.load("cluster_2.pkl")
cluster_3 = joblib.load("cluster_3.pkl")
mer_0 = joblib.load("mer_0.pkl")
mer_1 = joblib.load("mer_1.pkl")
mer_2 = joblib.load("mer_2.pkl")
mer_3 = joblib.load("mer_3.pkl")

st.title('Data Scientist Job Change Prediction')
st.image("https://i.ibb.co/wynpxvD/career-change.jpg")
df = pd.DataFrame({'What is Churn':['Churn is'],'What can we do':'you can do'})
st.write(df)


x = st.metric('Sales',2500,-12)

Trx_Rank = st.selectbox('What is Your Trx_Rank',([ 1,  2,  3,  4,  5]))

Points = st.slider('Enter Your Points', min_value=1, max_value=10000, value=10, step=1)
st.write('You Choose',Points)

Trx_Vlu = st.slider('Enter Your Trx_Vlu',min_value=1, max_value=10000, value=10, step=1)
st.write('You Choose',Trx_Vlu)

Trx_Age = st.slider('Enter Your Trx_Age', min_value=0, max_value=1000, value=10, step=1)
st.write('You Choose',Trx_Age)

Customer_Age = st.slider('Enter Your Customer_Age', min_value=0, max_value=1000, value=10, step=1)
st.write('You Choose',Customer_Age)

Category_In_English = st.radio('Category', ['Fashion', 'F&B', 'Health & Beauty', 'Grocery', 'Other','Electronics', 'Transportaion'])

Mer_Name = st.selectbox('company_size Type',['Shankar Traders', 'Agra Appliance Arena', 'Radha Emporium',
       'Mohan Brothers Mart', 'Jai Hind General Stores',
       'Rajasthan Handicrafts', 'Lucknow Leather World',
       'Pune Perfumes Paradise', 'Ranchi Rug Retail',
       'Faridabad Footwear Fair', 'Cuttack Curtain Corner',
       'Ganpati Enterprises', 'Gurgaon Gift Gallery',
       'Varanasi Silk House', 'Saraswati Fabrics',
       'Amritsar Auto Accessories', 'Vadodara Vegetables Villa',
       'Indore Instrument Inn', 'Madurai Music Mania',
       'Gwalior Garden Gear', 'Mumbai Fashion Hub',
       'Kanpur Kitchen Appliances', 'Thiruvananthapuram Toy Town',
       'Nashik Noodle Niche', 'Jamshedpur Jeans Junction',
       'Kochi Kitchenware Kingdom', "Bhubaneswar Baker's Boutique",
       'Delhi Electronics', 'Jodhpur Jewelry Junction',
       'Jaipur Pottery Emporium', 'Goa Grocery Galaxy',
       'Dehradun Dairy Delight', 'Krishna Textiles',
       'Ahmedabad Sweet Mart', 'Vijayawada Vegetable Village',
       'Gupta Saree Center', 'Bangalore Book House',
       'Nagpur Novelty Nook', 'Thane Tea Traders',
       'Guwahati Grocery Galleria', 'Punjabi Furniture Palace',
       'Mysuru Mobile Mart', 'Kolkata Carpets Corner',
       'Patna Paints Palace', 'Surat Stationery Studio',
       'Hyderabad Spices Bazaar', 'Udaipur Utensil Universe',
       'Coimbatore Cosmetics Castle', 'Chennai Gems and Jewels',
       'Bhopal Bedding Boutique', 'Shimla Shoe Shoppe',
       'Noida Novelty Nook', 'Raipur Rice Retail',
       'Trichy Tailoring Trends', 'Kollam Kitchenware Kingdom',
       'Rourkela Rice Retail'])

Recency = st.slider('Enter Your Recency',min_value=1, max_value=10000, value=100, step=1)
st.write('You Choose',Recency)

Frequency = st.slider('Enter Your Frequency',min_value=0, max_value=100, value=0, step=1)
st.write('You Choose',Frequency)

MonetaryValue = st.slider('Enter Your MonetaryValue',min_value=0, max_value=10000, value=0, step=1)
st.write('You Choose',MonetaryValue)

User_Id = st.number_input("Enter Your User_Id:", min_value=0, max_value=10000, step=1, value=50)

# Check if the user ID is in Cluster 0
if User_Id in cluster_0.index:
    Cluster = 0
    st.write(f'Cluster: {Cluster} ')
    st.info(' Based on our analysis it looks like you have made your last transaction a long time ago,and  have few purchases in total Please can you provide any problems you have . \n')
    st.write(f'Merchants Recomended :\n {mer_0} ')
    
elif User_Id in cluster_1.index:
    Cluster = 1
    st.write(f'Cluster: {Cluster} ')
    st.write(f'Merchants Recomended :\n {mer_1} ')
elif User_Id in cluster_2.index:
    Cluster = 2
    st.write(f'Cluster: {Cluster} ')
    st.write(f'Merchants Recomended: \n {mer_2} ')
elif User_Id in cluster_3.index:
    Cluster = 3
    st.write(f'Cluster: {Cluster} ')
    st.write(f'Merchants Recomended: \n {mer_3} ')
else:
    st.write(f'User: {User_Id} does not belong to any cluster')
    
image_path = "Plot.png"
  # Replace with the actual path to your image file
image = st.image(image_path, caption='Your Image Caption', use_column_width=True)

# You can use st.column to create columns and position the image in a specific column
col1, col2 = st.columns(2)

# Position the image in the first column
with col1:
    st.image(image_path, caption='Your Image Caption', use_column_width=True)

# Position other content in the second column
with col2:
    st.write("Some other content")



# enrolled_university = st.radio('Are There enrolled_university',('no_enrollment', 'Full time course','Part time course'))

# education_level = st.radio('Is There education_level',('Graduate', 'Masters', 'High School', 'Phd', 'Primary School'))

# major_discipline = st.selectbox('What is Your major_discipline Status',('STEM', 'Business Degree', 'Arts', 'Humanities', 'No Major',
#        'Other'))

# experience = st.slider('Enter Your experience',1,20)
# st.write('You Choose',experience)


# if company_size == '50-99':
#     st.write('You Choose',74.5)

# company_type = st.selectbox('company Type',('Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other',
#        'Public Sector', 'NGO'))

# last_new_job = st.selectbox(' last_new_job Type',('1', '>4', 'never', '4', '3', '2',))


# training_hours = st.slider('Enter Your training_hours',1,300)
# st.write('You Choose',training_hours)

# target = st.radio('Is There target',(0,1))

# data = pd.DataFrame({'city': [city],'city_development_index': [city_development_index],'gender': [gender],'relevent_experience': [relevent_experience],'enrolled_university':[enrolled_university],'education_level':[education_level],'major_discipline':[major_discipline],'experience':[experience],'company_size':[company_size],'company_type':[company_type],'last_new_job':[last_new_job],'training_hours':[training_hours]})

        
# data['last_new_job'] = data['last_new_job'].replace('>4','5').replace('never','0')
# data['last_new_job'] = pd.to_numeric(data['last_new_job'])
# data['company_size'] = data['company_size'].replace('50-99',(50+99)/2).replace('100-500',(100+500)/2).replace('10/49',(10+49)/2).replace('500-999',(999+500)/2).replace('1000-4999',(1000+4999)/2).replace('100-500',(100+500)/2).replace('5000-9999',(5000+9999)/2).replace('+10000',(10000)).replace('<10',9)
# data['city_numeric'] = pd.to_numeric(data['city'].str.split('_').str[1])

# data = pd.get_dummies(data=data, columns=['gender', 'relevent_experience','company_type','major_discipline','enrolled_university'])
                      



# education_dict = {'Primary School' : 0,
#                   'High School' : 1,
#                   'Graduate' : 2,
#                   'Masters' : 3,
#                   'Phd' : 4}
# # For Reversing the keys and vlues of the dictionary to retrive the encoded values using copmrehension for loop
# rev_education_dict = {value: key for key, value in education_dict.items()}
# data['education_level'] = data['education_level'].map(education_dict)
# data.drop(['city'],axis=1,inplace=True)


# col = ['city_development_index', 'education_level', 'experience',
#        'company_size', 'last_new_job', 'training_hours', 'gender_Female',
#        'gender_Male', 'gender_Other',
#        'relevent_experience_Has relevent experience',
#        'relevent_experience_No relevent experience', 'company_type_1',
#        'company_type_Early Stage Startup', 'company_type_Funded Startup',
#        'company_type_NGO', 'company_type_Other', 'company_type_Public Sector',
#        'company_type_Pvt Ltd', 'major_discipline_Arts',
#        'major_discipline_Business Degree', 'major_discipline_Humanities',
#        'major_discipline_No Major', 'major_discipline_Other',
#        'major_discipline_STEM', 'enrolled_university_Full time course',
#        'enrolled_university_Part time course',
#        'enrolled_university_no_enrollment']
# data = pd.get_dummies(data=data).reindex(columns=col,fill_value=0)


# st.write(data)

# model = pkl.load(open('Lmodel.pkl', 'rb'))

# churn_prop = model.predict_proba(data)[0][1] * 100
# st.markdown(f'## Probability of a Candidate to Take the Data Science Job is : {round(churn_prop, 2)} %')

# st.write(data['last_new_job'])
# st.write(data['company_size'])

# st.write(data)

# st.markdown(f'# Thanks For Using Our Application')
