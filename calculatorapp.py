import streamlit as st
#import pandas
#import hashlib
#import statistics
#from PIL import Image
#from io import BytesIO
#import requests 
#import main


def add(a, b):
  return a + b
def sub(a, b):
  return a - b
def mul(a, b):
  return a * b
def div(a, b):
  return a / b
def main():
  st.title("Calculator")
  st.write("Calculadora simples")
  a = st.number_input("Digite um número")
  b = st.number_input("Digite outro número")
  operation = st.selectbox("Selecione uma operação", ["Adição", "Subtração", "Mutiplicação", "Divisão","Média"])
  if operation == "Adição":
    st.write(add(a, b))
  elif operation == "Subtração":
    st.write(sub(a, b))
  elif operation == "Mutiplicação":
    st.write(mul(a, b))
  elif operation == "Divisão":
    st.write(div(a, b))
  elif operation == "Média":
    st.write(div(add(a, b), 2))
  else:
    st.write("llll")
if __name__ == '__main__':
  main()
