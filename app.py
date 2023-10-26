import streamlit as st
import pandas as pd
import helper
import cv2
import os

st.set_page_config(layout='centered') ##centered, wide

WORKDIR = os.getcwd()

def main():
    st.title('running.... Invoice Checker !!')

    ## Pdf path
    pdf1, pdf2, pdf3 = st.columns(3)
    main_dir = pdf1.text_input("Enter Main Directory name")
    pdf_dir = os.path.join(WORKDIR, main_dir)
    datas = pdf2.text_input("Paste Excel Sheet name")
    path_pdf = pdf3.selectbox("SELECT PDFs", os.listdir(pdf_dir))
    path_pdf = os.path.join(pdf_dir, path_pdf)
    

    if path_pdf.endswith('.pdf'):
        helper.create_dir('out')
        helper.capture_pdf(path_pdf, 'out')

        imgs_path = os.listdir('out')
        img = st.selectbox('SELECT IMAGE', imgs_path)
        img_path = f"out/{img}"

        img = cv2.imread(img_path)
        st.image(img, use_column_width=True)
    else:
        raise("Pdf path not defined.")


    # Evaluating DataSheet
    data = pdf_dir.replace('Invoices/', datas)
    df = pd.read_excel(data)
    df.columns = df.iloc[0]
    df = df.drop(0)
    df = df.reset_index(drop=True)
    st.dataframe(df[df['Source - PDF Name'] == int(os.path.basename(path_pdf).split('.')[0])].dropna(axis=1),
                 use_container_width=True)

    if st.button("DELETE DATA"):
        helper.delete_dir('out')
        st.success("Data Erased Successfully...")


main()