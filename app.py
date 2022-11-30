import numpy as np
import pandas as pd
import streamlit as st

def main():
  st.title("Multiplication")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Subtraction of 2 numbers using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  n1 = st.number_input("Number 1")
  n2 = st.number_input("Number 2")
  result = n1 * n2
  st.success('The output is {}'.format(result))
  if st.button("Made By"):
      st.text("Rushikesh Deshpande")
      st.text("22f1000845")

if __name__=='__main__':
  main()
