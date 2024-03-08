import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import os
import numpy as np

os.chdir(r"C:\Users\abdul\Downloads\PROJECTS\Recommendition system\Book_recommendation\pickle_files")

popular_books = pickle.load(open("popular_books.pkl","rb"))
data = pickle.load(open("data.pkl","rb"))
books = pickle.load(open("books.pkl","rb"))
similarity_score = pickle.load(open("similarity_score.pkl","rb"))



def recommend(book_name,n=5):
    try:
        index=np.where(data.index==book_name)[0][0]
        similar_item=sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:n+1]
        recc = []
        for i in similar_item:
            item = []
            temp_df = books[books["Book-Title"] == data.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values))
            item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values))
            item.extend(list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values))
            recc.append(item)
    except:
        recc = "Error"
    return recc


st.set_page_config(page_title="Recommendation System",layout="wide",)


st.title(":orange[Books Recommendation System]")

selected = option_menu(None, options=["Home", "Recommend",], 
icons=['house', 'person',], 
menu_icon="cast", default_index=0, orientation="horizontal",)


if selected =="Home":
    st.title("**:orange[Most Rated Top 20 Books]**")
    row1 = st.columns(4)
    row2 = st.columns(4)
 
    skills = popular_books.iloc[:8,:]
    for ind,(col, skill) in enumerate(zip(row1 + row2, skills)):
        tile = col.container()
        tile.write(f"**Top {ind+1} Book**")
        tile.image(image=skills.iloc[ind,5],caption=skills.iloc[ind,1],width=200)
    

    row1 = st.columns(4)
    row2 = st.columns(4)
    skills = popular_books.iloc[8:,:]
    for ind,(col, skill) in enumerate(zip(row1 + row2, skills)):
        tile = col.container()
        tile.write(f"**Top {ind+9} Book**")
        tile.image(image=skills.iloc[ind,5],caption=skills.iloc[ind,1],width=200,)

    row1 = st.columns(4)
    skills = popular_books.iloc[16:,:]
    for ind,(col, skill) in enumerate(zip(row1 , skills)):
        tile = col.container()
        tile.write(f"**Top {ind+17} Book**")
        tile.image(image=skills.iloc[ind,5],caption=skills.iloc[ind,1],width=200,)

    


if selected == "Recommend":
    st.title("Recommend Books")
    with st.container():
        col1,col2 =st.columns([8,2])
        with col1:
            title = st.text_input('**Book title**',placeholder="Enter Book Title")
        with col2:
            nbook = st.selectbox("Select N Books",np.arange(4,7),index=1)
    
    submit = st.button("Recommend Books Related",use_container_width=1)

    if submit:
        ans = recommend(title,n=nbook)
        if ans !="Error":
            st.success("Book Found")
            row1 = st.columns(int(nbook))
            for ind,(col, skill) in enumerate(zip(row1 , ans)):
                tile = col.container()
                tile.image(image=ans[ind][2],caption=ans[ind][0],width=200)
        else:
            st.error("No book Found ")








































