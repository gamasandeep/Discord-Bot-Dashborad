import streamlit as st
import pandas as pd

def app():
    # Giving a title 
    st.title('Discord Message Builder')
    # creating a form
    my_form=st.form(key='form-1')
    # creating input fields
    title=st.text_input('Title:')
    description=st.text_input('Description:')
    url=st.text_input('URL:')
    image_url=st.text_input('Image URL:')

    col1, col2 = st.columns(2)
    with col1:
        thumbnail=st.text_input('Thumbnail Icon URL:')

    with col2:
        colour = st.color_picker('Pick A Color', '#00f900')

    col3, col4, col5 = st.columns(3)

    with col3:
        authname=st.text_input('Author Name:')

    with col4:
        authlink=st.text_input('Author Link:')

    with col5:
        authurl=st.text_input('Author Icon URL:')

    col6, col7 = st.columns(2)

    with col6:
        fieldname=st.text_input('Field Name:')

    with col7:
        fieldvalue=st.text_input('Field Value:')

    footertext=st.text_input('Footer Text')

    submit=st.button('Submit')
    # creating a submit button
    if submit == True:
        data = {'title':[title],'description':[description],'url':[url],'image_url':[image_url], 'colour':[colour],'thumbnail':[thumbnail],'authname':[authname], 'authlink':[authlink], 'authurl':[authurl], 'fieldname':[fieldname], 'fieldvalue':[fieldvalue], 'inline':False, 'footertext':[footertext]}
        # Create the pandas DataFrame with column name is provided explicitly
        df = pd.DataFrame(data)
        # st.dataframe(df)
        df['colour'] = df['colour'].str.replace('#', '')
        df.to_csv("message.csv", encoding='utf-8', index=False)
