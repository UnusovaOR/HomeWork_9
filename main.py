#Лабораторная работа 10, вариант 13, студент Юнусова Оксана Руслановна, группа 2023-ФГиИБ-ПИ-1см
#Тесты программы по подсчету количества погибших детей по каждому пункту посадки (максимальный возраст от 1 до 18)

import matplotlib.pyplot as plt
import streamlit as st


def get_count(lines, age):
    c = 0
    q = 0
    s = 0
    for line in lines:
        lst = line.rstrip().split(',')
        if lst[1] == '0' and lst[6] != '' and float(lst[6]) < age:
            if lst[12][:-1] == 'C':
                c = c + 1
            elif lst[12][:-1] == 'Q':
                q = q + 1
            elif lst[12][:-1] == 'S':
                s = s + 1
    return c, q, s


st.text('Лабораторная работа 10, вариант 13, Юнусова Оксана Руслановна, 2023-ФГиИБ-ПИ-1см')
st.image('Titanic.png')
st.header('Данные пассажиров Титаника')
st.write('Для подсчета количества погибших детей по каждому пункту посадки, укажите максимальный возраст:')
max_age = st.slider('максимальный возраст', 1, 18)
with open('data.csv', 'r') as file:
    file_lines = file.readlines()
    c, q, s = get_count(file_lines, max_age)
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
