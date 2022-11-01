import streamlit
import pandas
import hashlib
import statistics
from PIL import Image
from io import BytesIO
import requests 

image = Image.open('Calculator.png') 


#list of positive integer numbers
data1 = [1, 3, 4, 5, 7, 9, 2]

x = statistics.mean(data1)

#printing the mean
print("Mean is :", x)
 
