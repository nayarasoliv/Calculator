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



operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide", "Média"])
  
  if operation == "Add":
    st.write(add(a, b))
  elif operation == "Subtract":
    st.write(sub(a, b))
  elif operation == "Multiply":
    st.write(mul(a, b))
  elif operation == "Divide":
    st.write(div(a, b))
   elif operation == "Média":
    st.write m = (n1 + n2 + n3 + n4 + n5)/q
  
  if __name__ == '__main__':
main()



