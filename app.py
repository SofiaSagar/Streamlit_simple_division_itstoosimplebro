import streamlit as st


st.write("""
# DIVISION OF TWO NUMBERS
""")
#Get Input

st.header('GIVE US SOME NUMBERS FOR FUN!')

def user_input_features():

    NUM1 = st.number_input("NUMERATOR")       #,min_value=0,max_value=20,step=1)
    NUM2 = st.number_input("DENOMINATOR",value=1) 
                                               #,min_value=0,max_value=20,step=1)
    if NUM2==0:
        st.write("OH!BY THE WAY DENOMINATOR CANT BE ZERO")
    
    result=NUM1/NUM2
    return result

df = user_input_features()    

st.write("THE RESULT OF YOUR DIVISION IS : ")
st.write(df)
