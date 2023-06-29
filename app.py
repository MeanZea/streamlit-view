import streamlit as st
view = [100,150,30] 
st.write('# Youtube view') #마크다운처럼 # 사용하면 크기 조절 됨
st.write('## raw') 
view
st.write('## bar chart') 
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview