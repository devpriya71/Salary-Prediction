import streamlit as st
import pickle
model=pickle.load(open("model.pkl",'rb'))
st.title("Salary Prediction App")
exp=st.number_input("enter Experience",min_value=0,max_value=50,value=1)
if st.button("Predict"):
    result=model.predict([[exp]])
    st.write(f'Predicted salary: {int(result[0])}')