import streamlit as st
import pandas as pd
import numpy as np
import logic as l

df = pd.read_csv("titanic.csv", sep=",")

box_options = {"Шебурн":"S", "Квинстаун":"Q", "Саутгемптон":"C"}
box = st.selectbox("Выберите порт посадки:", box_options)

value_ebarked = box_options[box]

s = l.mean_fare(df, value_ebarked, True)
d = l.mean_fare(df, value_ebarked, False)
  
st.write(f"Средняя стоимость билетов выживших {s:0.2f}")
st.write(f"Средняя стоимость билетов погибших {d:0.2f}")