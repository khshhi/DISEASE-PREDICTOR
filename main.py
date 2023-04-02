import streamlit as st
import pandas as pd
import numpy as np
import pickle

Heart_disease=pickle.load(open('heart.sav','rb'))
Stone_disease=pickle.load(open('kidney.sav','rb'))
data=pd.read_csv("Health_data.csv")
data1=pd.read_csv("kindey.csv")

#navigation
nav=st.sidebar.radio("Main Memu",["Home","Heart Disease","Kidney Stone"])

#Home
if nav=="Home":
    st.title("Disease Predictor")
    st.write("This is just the homepage")
    st.write("A well-functioning healthcare system is critical to the economy and the well-being of humanity.\nA disease predictor, often known as a virtual doctor, may accurately predict a patient's sickness without the need for human involvement.")
    st.image("Disease.jpg")
    
    #show table
    if st.checkbox("Show Table for heart disease"):
         st.table(data)
    
    #show table
    if st.checkbox("Show Table for kidney disease"):
         st.table(data1)     
    

#Heart Disease    
if nav=="Heart Disease":
    st.title("Heart disease predictor")
    col1,col2,col3,col4 = st.columns(4)
    

    with col1: 
        Age=st.text_input("Enter your Age")

    with col2:
        RestingBP=st.text_input("Enter your Blood Pressure")

    with col3:
        Cholesterol=st.text_input("Enter your Cholestrol Level")

    with col4:
        FastingBS=st.text_input("Enter your Blood Sugar level ")

    with col1:
        MaxHR=st.text_input("Enter your Maximum Heart Rate")

    with col2:
        Oldpeak=st.text_input("Enter ST depression induced by exercise relative to rest")

    with col3:
        Sex=st.radio("Enter your Gender",["Male","Female"])
        if Sex=='Male':
            Sex_M=1
            Sex_F=0
        if Sex=="Female":
            Sex_M=0
            Sex_F=1

    with col4:    
        ChestPainType=st.radio("Enter the Chest PAin Type",["ASY","NAP","ATA","TA"])
        if ChestPainType=='ASY':
            
            ChestPainType_ASY=1
            ChestPainType_NAP=0
            ChestPainType_ATA=0
            ChestPainType_TA=0
        if ChestPainType=='NAP':
            ChestPainType_ASY=0
            ChestPainType_NAP=1
            ChestPainType_ATA=0
            ChestPainType_TA=0
        if ChestPainType=='ATA':
            ChestPainType_ASY=0
            ChestPainType_NAP=0
            ChestPainType_ATA=1
            ChestPainType_TA=0
        if ChestPainType=='TA':
            ChestPainType_ASY=0
            ChestPainType_NAP=0  
            ChestPainType_ATA=0
            ChestPainType_TA=1 
    with col1:      
        ST_Slope=st.radio("Enter the ST slope",["Down","UP","Flat"])
        if ST_Slope=='Down':
            ST_Slope_Down=1
            ST_Slope_Up=0
            ST_Slope_Flat=0
        if ST_Slope=='Up':
            ST_Slope_Down=0
            ST_Slope_Up=1
            ST_Slope_Flat=0
        if ST_Slope=="Flat":
            ST_Slope_Down=0
            ST_Slope_Up=0
            ST_Slope_Flat=1
    with col2:
        ExerciseAngina=st.radio("ExerciseAngina( pain in the chest that comes on with exercise, stress, or other things that make the heart work harder)",["Yes","No"])	
   	
        if ExerciseAngina=='Yes':
            ExerciseAngina_Y=1
            ExerciseAngina_N=0
        if ExerciseAngina=='No':
            ExerciseAngina_Y=0
            ExerciseAngina_N=1
    
    with col3:
        RestingECG=st.radio("Enter Rating of ECG",["LVH","Normal","ST"])

        if RestingECG=='LVH':
            RestingECG_LVH=1
            RestingECG_Normal=0
            RestingECG_ST=0
        if RestingECG=="Normal":
            RestingECG_LVH=0
            RestingECG_Normal=1
            RestingECG_ST=0
        if RestingECG=="ST":
            RestingECG_LVH=0
            RestingECG_Normal=0
            RestingECG_ST=1
    
    heart_diag=''
    if st.button("Test Result"):
        heart_pred=Heart_disease.predict([[Age,RestingBP,Cholesterol,FastingBS,MaxHR,Oldpeak,Sex_F,Sex_M,ChestPainType_ASY,ChestPainType_ATA,ChestPainType_NAP,ChestPainType_TA,ST_Slope_Down,ST_Slope_Flat,ST_Slope_Up,ExerciseAngina_N,ExerciseAngina_Y,RestingECG_LVH,RestingECG_Normal,RestingECG_ST]])
        if(heart_pred[0] == 1):
            heart_diag = "heart disease found "
        else:
            heart_diag = "no heart disease"

    st.success(heart_diag)   


#Stone disease         
if nav=="Kidney Stone":
    st.title("Kidney Stone Predictor")  
    

    col1,col2=st.columns(2)

    with col1:
       gravity=st.text_input("Enter the gravity")
    with col2:   
       ph=st.text_input("Ente the ph")
    with col1:   
       osmo=st.text_input("Enter the osmo")
    with col2:   
       cond=st.text_input("Enter the cond data")
    with col1:   
       urea=st.text_input("Enter the urea data")
    with col2:   
       calc=st.text_input("Enter the calculated amount")
    
    result=''
    if st.button('Kidney stone result'):
         Stone_pred=Stone_disease.predict([[gravity,ph,osmo,cond,urea,calc]])
         if(Stone_pred[0]==1):
             result="Person has A kidney stone"
         else:
             result="Person does not have the disease"    
    st.success(result)