import streamlit as st
from proj import finalfunc
from exp import explore
ide_ra,hush,res=0,0,0
st.set_page_config(layout="wide")
st.title("REAL TIME PRODUCT ANALYSIS USING WEB SCRAPING")
i=st.text_input(label='SEARCH HERE...')
if i:
    
    st.write("Searching for "+i)
    ide_ra,hush,res=finalfunc(i)
else:
    if ide_ra!=0:
        st.write(ide_ra[0][0])
    else:
        st.write("")
explore(ide_ra,hush)

