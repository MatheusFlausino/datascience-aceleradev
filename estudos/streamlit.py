import streamlit as st
import pandas as pd
import time

def main():
    st.title('Estudo de componentes')
    st.title('Title')
    st.header('Heades')
    st.subheader('Sub Heades')
    st.markdown('Markdown')
    st.text('Text')

    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })

    st.markdown('Write DataFrame')
    st.write(df)

    st.markdown('Checkbox')
    if st.checkbox('Show Chart dataframe'):
        st.markdown('Linear Chart DataFrame')
        st.line_chart(df)

    st.markdown('Select')
    option = st.selectbox( 'Select a number', df['first column'])
    'Selected: ', option

if __name__ == '__main__':
    main()