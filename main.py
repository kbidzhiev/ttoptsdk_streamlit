# main.py
import streamlit as st
import numpy as np #input functions from `input_str` are base on numpy
from ttoptSDK import optimize
import json


st.title('ttoptSDK with Streamlit')

def function_from_input(input_str):
    def f(X):
        return eval(input_str)
    return f 



user_input = st.text_input(
    "Input a function to evaluate: (e.f  'np.sum(np.abs(X * np.sin(X) + 0.1 * X), axis=1)' ",
    value="np.sum(np.abs(X * np.sin(X) + 0.1 * X), axis=1)")

d = st.text_input("dim", value = 3)
rank = st.text_input("rank", value = 4)

if user_input:
    f = function_from_input(user_input)

    d = int(d)
    rank = int(rank)
    lower_grid_bound = -10
    upper_grid_bound = 10
    p_grid_factor = 2
    q_grid_factor = 12
    n_evals = 2 * 1.E+3
    name = "myfunc"
    with_log = True
    x_opt_real=np.ones(d)
    y_opt_real=0.


    
    

if st.button('Optimize'):
    x, y, info = optimize(rank, d, f,
     lower_grid_bound, upper_grid_bound,
     p_grid_factor, q_grid_factor,
     n_evals,
     #name, with_log,
     #x_opt_real, y_opt_real,
     )
    st.write(f"Min value of the function is: {y}")


result_json = json.dumps(info)
# Add a download button
st.download_button(
    label="Download Result as JSON",
    data=result_json,
    file_name='result.json',
    mime='application/json'
)