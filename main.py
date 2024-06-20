import streamlit as st
import pandas as pd
import numpy as np

st.title('My first Deploy DL model')
st.header('Header là đây chứ đâu')
st.text('Đây là text')
st.markdown('Mark down đây **anh em ơi**')
st.text('Còn dưới đây là latex')
st.latex(r"""
    a + b = 3
    """)
st.markdown(12345)
st.code("""
    def(hello):
        print("Hello word")
    """, language='python')
st.text('Hiển thị luôn cả chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
