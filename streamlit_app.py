import streamlit as st
import math

msg = "Hello World!!!"
st.write(msg)  # 문자열 직접 넣어도 됨 (streamlit -> print?)

# 터미널(git bash, cmd) : pip install streamlit (ctrl + `)

st.write(math.pi)



with st.echo():
    radius = st.number_input("반지름")
    A = '원주율 : '
    B = '반지름 : '
    C = '원의 둘레 : '
    D = '원의 넓이 : '

    q = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    r = 15

    print(A, q)
    print(B, r)
    print(C, r * 2 * q)
    print(D, r * r * q)