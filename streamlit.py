import pandas as pd
import streamlit as st

A=st.sidebar.selectbox("select a column",["HOME","BOOKING PAGE"])
if A=="HOME":
    st.title("WELCOME TO THE RED BUS BOOKING SYSTEM")
    st.image("C:/Users/murkr/OneDrive/Desktop/imageredbus.jpg",width=100)
    st.video("https://youtu.be/eyAAUGhvZu8?si=Fz7h6tYBgUOAVxgS")
    if st.button("click"):
        st.write("SHOW THE DATABASE")
        st.dataframe(pd.read_csv("C:/Users/murkr/OneDrive/Desktop/RED_BUS/CLEANED_DATA.csv"))   
if A=="BOOKING PAGE":
    st.title("STATE AND PRICE")
    S=st.selectbox("list of states",["ANDRA_PRADESH","KERALA","GOA","UTTAR_PRADESH","CHANDIGARH","RAJASTHAN","BIHAR","HIMACHAL","JAMMU & KASHMIR","PUNJAB"])
    st.write(S)
    FARE=st.selectbox("PRICE",("100-500","501-1000","1001-1500","1500-2000","ABOVE 2000"))
    st.write(FARE)
