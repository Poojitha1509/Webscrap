import streamlit as st
import pandas as pd
import numpy as np
def explore(ide_ra,hush):
    if ide_ra and hush:
        col1, col2 = st.columns(2)

        with col1:
            st.header("AMAZON")
                
            for i in range(5):
                st.subheader(ide_ra[i][0])
                st.markdown("<style>.big-font {color:red;font-size:25px;} .d{font-size:20px;}</style>", unsafe_allow_html=True)
                st.markdown("<p class=\"big-font\">Price - "+ide_ra[i][1]+"</p>", unsafe_allow_html=True)
                st.markdown("<p class=\"d\">Rating - "+ide_ra[i][2]+"</p>", unsafe_allow_html=True)
                st.markdown("<p class=\"d\">Reviews Count - "+ide_ra[i][3]+" Ratings</p>", unsafe_allow_html=True)
                st.write("Click this [link]("+ide_ra[i][4]+") to visit product page.")
                                

        with col2:
            #st.subheader("FLIPKART")
            st.header("FLIPKART")
                    
            for i in range(5):
                if True:
                    st.subheader(ide_ra[i][0])
                    st.markdown("<style>.big-font {color:red;font-size:25px;} .d{font-size:20px;}</style>", unsafe_allow_html=True)
                    st.markdown("<p class=\"big-font\">Price - "+hush[i][0]+"</p>", unsafe_allow_html=True)
                    st.markdown("<p class=\"d\">Rating - "+hush[i][1]+" out of 5 stars</p>", unsafe_allow_html=True)
                    st.markdown("<p class=\"d\">Reviews Count - "+hush[i][2]+"</p>", unsafe_allow_html=True)
                    st.write("Click this [link]("+hush[i][3]+") to visit product page.")
    else:
        st.write("")
        
