import streamlit as st

# applying css to submit button
st.markdown(
    """
    <style>
    .stDownloadButton, div.stButton {text-align:center}
    .stDownloadButton button, div.stButton > button:first-child {
        background-color: #B6B6B6;
        color:white;
        height:40px;
        width: 120px;
        border:0px;
    }
    div.stButton > button:hover {
        background-color: blue;
        color:#ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.form(key = 'user_info'):
    st.write("")
    st.write("")

    # displaying logo and header
    col1, col2,col3 = st.columns((7,2,12))
    with col2:
        st.image("samooha_logo4.jpg", width=70,  use_column_width=False, output_format="auto",)
    with col3:
        st.header("**samooha**")

    # displaying title
    col4, col5,col6 = st.columns((3,8,2))
    with col5:
        st.subheader("Sign up using Snowflake account")
        st.write("")
        st.write("")
        st.write("")

    # displaying input fields
    col7, col8,col9 = st.columns((4,9,3))
    with col8:
        account = st.text_input("",placeholder="Account locator")
        username = st.text_input("", placeholder="Username")
        password = st.text_input("", placeholder="Password",type="password")

    st.write("")

    # displaying disclaimer
    col10, col11,col12 = st.columns((2,7,1))
    with col11:
        st.markdown("By signing up, I agree to the [**Terms of Service**](https://samooha.tech/) and [**Privacy Policy**](https://samooha.tech/).")

    st.write("")
        
    # displaying submit button
    submit_form = st.form_submit_button(label="**Sign up**")
    if submit_form:
            st.write(submit_form)
    
            if account and username and password:
                st.success(
                            f"Signup Successful!"
                        )
            else:
                st.warning("Please fill all the fields")

    st.write("")

    # displaying statement
    col13, col14,col15 = st.columns((4,7,4))
    with col14:
        st.markdown('<div style="text-align: center;">Note : You can later login to Samooha as a <b>Provider</b> or a <b>Consumer</b></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    st.write("")