import streamlit as st

col1,col2=st.columns(2, gap="small",vertical_alignment="center")
with col1:
    st.image("./assets/VGG19.webp",width=230)
with col2:
    st.title("VGG19", anchor=False)
    st.write(
        "The VGG19 CNN model was created by a research group at the University of Oxford, part of the Visual Geometry Group (VGG), led by scientists K. Simonyan and A. Zisserman."
    )
st.write("\n")
st.subheader("Architecture:",anchor=False)
st.write(
    """
    - Fixed size of (224 * 224) RGB image was given as input to this network which means that the matrix was of shape (224,224,3).
    - The only preprocessing that was done is that they subtracted the mean RGB value from each pixel, computed over the whole training set.
    - Used kernels of (3 * 3) size with a stride size of 1 pixel, this enabled them to cover the whole notion of the image.
    - Spatial padding was used to preserve the spatial resolution of the image.
    - Max pooling was performed over a 2 * 2 pixel windows with sride 2.
    - This was followed by Rectified linear unit(ReLu) to introduce non-linearity to make the model classify better and to improve 
      computational time as the previous models used tanh or sigmoid functions this proved much better than those.
    - Implemented three fully connected layers from which the first two were of size 4096 and after that,a layer with 1000 channels
      for 1000-way ILSVRC classification and the final layer is a softmax function.
    """
)
