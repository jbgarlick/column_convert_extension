import streamlit as st

def app():
    col1, col2 = st.columns(2)
    with col1:
        convert_column = st.text_area('Convert column')
        convert = st.button('Convert')
        if convert:
            col_to_list = convert_column.splitlines()
            list_to_str = "','".join(col_to_list)
            final_for_query = "('" + list_to_str + "')"
            st.text_area('output',final_for_query)



if __name__ == "__main__":
    app()
