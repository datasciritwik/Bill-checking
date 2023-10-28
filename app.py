import streamlit as st
import pandas as pd
import helper
import cv2
import os

st.set_page_config(layout='wide') ##centered, wide

WORKDIR = os.getcwd()

def main():
    st.title('running.... Invoice Checker !!')

    ## Pdf path
    pdf1, pdf2, pdf3 = st.columns(3)
    main_dir = pdf1.text_input("Enter Main Directory name")
    pdf_dir = os.path.join(WORKDIR, main_dir)
    datas = pdf2.text_input("Paste Excel Sheet name")
    path_pdf = pdf3.selectbox("LIST OF SELECTED PDFs", os.listdir(pdf_dir))
    path_pdf = st.number_input('YOU SELECTED', int(path_pdf.split('.')[0]))
    path_pdf = f"{(path_pdf)}.pdf"
    st.write('YOU SELECTED', f"{(path_pdf.split('.')[0])}.pdf")
    # st.write(f"{pdf_dir}")
    path_pdf = os.path.join(pdf_dir, path_pdf)
    
    # Evaluating DataSheet
    if datas is not None:
        data = pdf_dir.replace('Invoices/', datas)
        df = pd.read_excel(data)
        df.columns = df.iloc[0]
        df = df.drop(0)
        df = df.reset_index(drop=True)
        st.dataframe(df[df['Source - PDF Name'] == int(os.path.basename(path_pdf).split('.')[0])].dropna(axis=1).style,
                    use_container_width=True)

    if path_pdf.endswith('.pdf'):
        helper.create_dir('out')
        num = helper.capture_pdf(path_pdf, 'out')
        st.write(f'Total Number of pages {num}')
        imgs_path = os.listdir('out')
        img = st.selectbox('SELECT IMAGE', imgs_path[::-1])
        img_path = f"out/{img}"
        # st.write(f"{(imgs_path[::-1][-1])}")
        if num == 2:
            col1, col2 = st.columns(2)
            img1 = cv2.imread(f"out/{imgs_path[::-1][1]}")
            img2 = cv2.imread(f"out/{imgs_path[::-1][0]}")
            col1.image(img1, use_column_width=True, caption=f"out/{imgs_path[::-1][1]}")
            col2.image(img2, use_column_width=True, caption=f"out/{imgs_path[::-1][0]}")
            
        elif num == 3:
            col1, col2, col3 = st.columns(3)

            img1 = cv2.imread(f"out/{imgs_path[::-1][2]}")
            img2 = cv2.imread(f"out/{imgs_path[::-1][1]}")
            img3 = cv2.imread(f"out/{imgs_path[::-1][0]}")

            col1.image(img1, use_column_width=True, caption=f"out/{imgs_path[::-1][2]}")
            col2.image(img2, use_column_width=True, caption=f"out/{imgs_path[::-1][1]}")
            col3.image(img3, use_column_width=True, caption=f"out/{imgs_path[::-1][0]}")

        elif num == 4:
            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            img1 = cv2.imread(f"out/{imgs_path[::-1][3]}")
            img2 = cv2.imread(f"out/{imgs_path[::-1][2]}")
            img3 = cv2.imread(f"out/{imgs_path[::-1][1]}")
            img4 = cv2.imread(f"out/{imgs_path[::-1][0]}")

            col1.image(img1, use_column_width=True, caption=f"out/{imgs_path[::-1][3]}")
            col2.image(img2, use_column_width=True, caption=f"out/{imgs_path[::-1][2]}")
            col3.image(img3, use_column_width=True, caption=f"out/{imgs_path[::-1][1]}")
            col4.image(img4, use_column_width=True, caption=f"out/{imgs_path[::-1][0]}")

        else:
            img = cv2.imread(img_path)
            st.image(img, use_column_width=True)
    else:
        raise("Pdf path not defined.")

    if st.button("DELETE DATA"):
        helper.delete_dir('out')
        st.success("Data Erased Successfully...")


main()