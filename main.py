# main.py
import streamlit as st
import numpy as np #input functions from `input_str` are base on numpy




st.title('ttoptSDK with Streamlit')


try:
    def function_from_input(input_str):
        def f(X):
            return eval(input_str)
    
    def isclose(x, y, tol=1e-10):
        return abs(x - y) < tol
    input_str = "np.sin(X)"
    f = function_from_input(input_str)
    assert isclose(f(0), 0)
    assert isclose(f(np.pi/2), 1)

except ValueError:
    st.error("Input reading doesn't work")
    st.stop()