#Лабораторная работа 9, вариант 13, студент Юнусова Оксана Руслановна, группа 2023-ФГиИБ-ПИ-1см
#Подсчитать количество погибших детей по каждому пункту посадки, указав максимальный возраст (число от 1 до 18)

import matplotlib.pyplot as plt
import streamlit as st

st.text('Лабораторная работа 9, вариант 13, Юнусова Оксана Руслановна, 2023-ФГиИБ-ПИ-1см')
st.image('Titanic.png')
st.header('Данные пассажиров Титаника')
st.write('Для подсчета количества погибших детей по каждому пункту посадки, укажите максимальный возраст:')
max_age = st.slider('максимальный возраст',1,18)

c = 0
q = 0
s = 0
with open('data.csv', 'r') as file:
    for line in file:
        lst = line.rstrip().split(',')
        if lst[1] == '0' and lst[6] != '' and float(lst[6]) < max_age:
            if lst[12][:-1] == 'C':
                c = c + 1
            elif lst[12][:-1] == 'Q':
                q = q + 1
            elif lst[12][:-1] == 'S':
                s = s + 1

embarked = ['Шербур', 'Квинстаун', 'Саутгемптон']
count = [c, q, s]
data = {'пункт посадки': embarked, 'количество': count}
st.table(data)
fig = plt.figure(figsize=(8, 3))
plt.bar(embarked, count)
plt.xlabel('пункт посадки')
plt.ylabel('количество')
plt.title(f'количество погибших детей в возрасте до {max_age} лет')
st.pyplot(fig)
