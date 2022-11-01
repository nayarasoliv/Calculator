import streamlit as st
import pandas
import hashlib
import statistics
from PIL import Image
from io import BytesIO
import requests 

# st.title("") para TÍTULO
st.title("Calculator")

image = Image.open('Calculator.png') 

st.markdown("""

q = int(input("Quantos números serão informados?"))
n1 = int(input("Número 1:"))
n2 = int(input("Número 2:"))
n3 = int(input("Número 3:"))
n4 = int(input("Número 4:"))
n5 = int(input("Número 5:"))

m = (n1 + n2 + n3 + n4 + n5)/q

print("Média = " + str(m))
""")


