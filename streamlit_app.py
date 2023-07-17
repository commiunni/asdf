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

    st.write(q = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
    st.write(r = 15)

    st.write(print(A, q))
    st.write(print(B, r))
    st.write(print(C, r * 2 * q))
    st.write(print(D, r * r * q))