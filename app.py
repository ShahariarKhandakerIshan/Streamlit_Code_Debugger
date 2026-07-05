import streamlit as st
from api_calling import hint_generator,hint_solution,solution_provider
from PIL import Image

st.title("Code debugger",anchor = False)
st.markdown("Upload the image of your code error")
st.divider()

with st.sidebar:
    st.header("Controls")

    #image
    images = st.file_uploader(
        "Upload the photos of your code",
        type = ['jpg', 'jpeg', 'png'],
        accept_multiple_files = True
    )

    pil_images = []

    for img in images:
        pil_images.append(Image.open(img))
    
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded images")

            col = st.columns(len(images))

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
        
    selected_option = st.selectbox(
        "How you want to solve the problem",
        ("Hints", "Solution with code"),
        index = None
    )

    pressed = st.button("Debug Code", type = "primary")

if pressed:
    if not images:
        st.error("You must upload at least 1 image")
    if not selected_option:
        st.error("You must select a option")
    
    if images and selected_option:

        if selected_option == "Hints" :
            with st.container(border = True):
                st.subheader("The Issue")

                with st.spinner("AI is finding the issue"):
                    issue = hint_generator(pil_images)
                    st.markdown(issue) 
            
            with st.container(border = True):
                st.subheader("The solution")

                with st.spinner("Don't worry!! AI is here to provide the solution."):
                    issue = hint_solution(pil_images)
                    st.markdown(issue)

        else:
            with st.container(border = True):
                st.subheader("The Issue")

                with st.spinner("AI is finding the issue"):
                    issue = hint_generator(pil_images)
                    st.markdown(issue) 
            
            with st.container(border = True):
                st.subheader("The solution")

                with st.spinner("Don't worry!! AI is here to provide the solution."):
                    issue = solution_provider(pil_images)
                    st.markdown(issue)
