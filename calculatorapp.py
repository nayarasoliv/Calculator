import streamlit as st
import pandas
import hashlib
import statistics
from PIL import Image
from io import BytesIO
import requests 

# st.title("") para TÍTULO
st.title ("Calculator")

image = Image.open('Calculator.png') 

q = st.number_input("Quantos números serão informados?")
n1 = st.number_input("Número 1:")
n2 = st.number_input("Número 2:")
n3 = st.number_input("Número 3:")
n4 = st.number_input("Número 4:")
n5 = st.number_input("Número 5:")

return (n1 + n2 + n3 + n4 + n5)/q

#print("Média = " + str(m))



