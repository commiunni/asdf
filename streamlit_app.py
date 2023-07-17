import streamlit as st
import math

msg = "Hello World!!!"
st.write(msg)  # 문자열 직접 넣어도 됨 (streamlit -> print?)

# 터미널(git bash, cmd) : pip install streamlit (ctrl + `)

st.write(math.pi)



with st.echo():
import streamlit as st

radius = st.number_input("반지름")
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

circumference = 2 * pi * radius
area = pi * radius * radius

st.write("원주율 :", pi)
st.write("반지름 :", radius)
st.write("원의 둘레 :", circumference)
st.write("원의 넓이 :", area)
