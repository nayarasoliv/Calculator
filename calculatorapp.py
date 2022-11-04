import streamlit as st
#import pandas
#import hashlib
#import statistics
#from PIL import Image
#from io import BytesIO
#import requests 
#import main

# st.title("") para TÍTULO
st.title ("Calculator")
#image = Image.open('Calculator.png') 

 #coletando dados
q = st.number_input("Quantos números serão informados?")
n1 = st.number_input("Número 1:")
n2 = st.number_input("Número 2:")
n3 = st.number_input("Número 3:")
n4 = st.number_input("Número 4:")
n5 = st.number_input("Número 5:")

operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Média"])
  
if operation == "Add":
    st.write(str(n1 + n2 + n3 + n4 + n5))
elif operation == "Subtract":
    st.write(str(n1 - n2 - n3 - n4 - n5))
elif operation == "Multiply":
    st.write(str(n1 * n2 * n3 * n4 * n5))
elif operation == "Média":
    st.write (str(n1 + n2 + n3 + n4 + n5)/(q))
else:
    st.write ("Selecione")
