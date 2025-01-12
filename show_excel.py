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
    
    # 获取 A 列数据并格式化显示
    for index, row in selected_df.iterrows():
        # A列数据用红色 <p> 标签显示
        a_column = f'<p style="color: red">{row[0]}</p>'
        
        # 其他列数据按 <p> 和 <br> 格式化显示
        other_columns = '<p>' + '<br>'.join([str(val) for val in row[1:]]) + '</p>'
        
        # 输出每一行
        st.markdown(a_column, unsafe_allow_html=True)
        st.markdown(other_columns + '<hr>', unsafe_allow_html=True)

