import streamlit as st
import pandas as pd

# 页面标题
st.title("上传并显示 Excel 文件内容")

# 文件上传控件，允许上传多个文件
uploaded_files = st.file_uploader("选择多个 Excel 文件", type=["xlsx"], accept_multiple_files=True)

if uploaded_files:
    # 创建一个字典来保存文件名和 DataFrame 对应关系
    file_dict = {}
    
    # 读取每个文件并保存
    for file in uploaded_files:
        df = pd.read_excel(file)
        file_dict[file.name] = df
    
    # 让用户选择哪个文件来显示
    file_choice = st.selectbox("选择一个文件来查看内容", list(file_dict.keys()))
    
    # 获取用户选择的 DataFrame
    selected_df = file_dict[file_choice]
    
    # 显示该文件的内容
    st.subheader(f"{file_choice} 的内容")
    
    # 处理每一行数据
    for index, row in selected_df.iterrows():
        # A列数据用红色 <p> 标签显示
        a_column = f'<p style="color: red">{row[0]}</p>'
        
        # 其他列数据处理，忽略空单元格
        other_columns = '<p>'
        for value in row[1:]:
            if pd.notna(value):  # 忽略 NaN 值
                other_columns += str(value) + '<br>'
        other_columns += '</p>'
        
        # 如果 A 列数据和其他列数据都不为空，则显示
        st.markdown(a_column, unsafe_allow_html=True)
        if other_columns != '<p></p>':  # 确保不显示空的 <p> 标签
            st.markdown(other_columns + '<hr>', unsafe_allow_html=True)

