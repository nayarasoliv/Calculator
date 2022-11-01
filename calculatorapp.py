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

def main ():
 #coletando dados
q = st.number_input("Quantos números serão informados?")
n1 = st.number_input("Número 1:")
n2 = st.number_input("Número 2:")
n3 = st.number_input("Número 3:")
n4 = st.number_input("Número 4:")
n5 = st.number_input("Número 5:")

operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide", "Média"])
  
  if operation == "Add":
    st.write(add(n1, n2, n3, n4, n5))
  elif operation == "Subtract":
    st.write(sub(n1, n2, n3, n4, n5))
  elif operation == "Multiply":
    st.write(mul(n1, n2, n3, n4, n5))
  elif operation == "Divide":
    st.write(div(n1, n2, n3, n4, n5))
   elif operation == "Média":
    st.write (add(n1 + n2 + n3 + n4 + n5) div(q))
  
  if __name__ == '__main__':
main()



