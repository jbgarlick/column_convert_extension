import streamlit as st

def app():
    col1, col2, col3 = st.columns(3)
    with col1:
        convert_column = st.text_area('Convert column')
        no_str = st.checkbox('Check here if you don\'t want quotations around each item')
        convert = st.button('Convert')
        if convert and not no_str:
            col_to_list = convert_column.splitlines()
            list_to_str = "','".join(col_to_list)
            final_for_query = "('" + list_to_str + "')"
            st.text_area('output',final_for_query)
        if convert and no_str:
            col_to_list = convert_column.splitlines()
            list_to_str = ",".join(col_to_list)
            final_for_query = "(" + list_to_str + ")"
            st.text_area('output',final_for_query)



if __name__ == "__main__":
    app()
