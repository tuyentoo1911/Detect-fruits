import streamlit as st
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Load the saved model
@st.cache_resource
def load_model_cached():
    return load_model('vgg19_model.h5')

model = load_model_cached()

# Load CSS styles
st.markdown('<style>{}</style>'.format(open('static/styles.css').read()), unsafe_allow_html=True)


st.title('🍎 Fruit Classifier')

# Initialize session state for fruit statistics
if 'fruit_df' not in st.session_state:
    st.session_state.fruit_df = pd.DataFrame(columns=['Fruit', 'Count'])

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Upload an image")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"], key="file_uploader")
    
    if uploaded_file is not None:
        # Process uploaded image
        image_file = Image.open(uploaded_file)
        st.image(image_file, caption='Uploaded Image', use_column_width=True)

        # Prepare image for prediction
        img = np.array(image_file.resize((224, 224))) / 255.0
        img = np.expand_dims(img, axis=0)

        # Prediction
        with st.spinner('Analyzing the image...'):
            prediction = model.predict(img)

        fruit_classes = ['Apple', 'Banana', 'Grapes', 'Kiwi', 'Mango', 'Orange', 'Strawberry']
        predicted_class_index = np.argmax(prediction[0])
        predicted_class = fruit_classes[predicted_class_index]
        confidence = prediction[0][predicted_class_index] * 100

        # Update session state for fruit count
        if predicted_class in st.session_state.fruit_df['Fruit'].values:
            st.session_state.fruit_df.loc[st.session_state.fruit_df['Fruit'] == predicted_class, 'Count'] += 1
        else:
            new_row = pd.DataFrame({'Fruit': [predicted_class], 'Count': [1]})
            st.session_state.fruit_df = pd.concat([st.session_state.fruit_df, new_row], ignore_index=True)

        # Display prediction results
        with col2:
            st.markdown("### 🧠 AI Prediction")
            st.markdown(f"""
            <div class='prediction-box'>
                <h2 style='color: #4CAF50; margin-bottom: 10px;'>{predicted_class}</h2>
                <p>Confidence: <span style='color: #4CAF50; font-weight: bold;'>{confidence:.2f}%</span></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Fruit information
            fruit_info = {
                'Apple': "Rich in fiber, vitamins, and antioxidants. May help reduce the risk of heart disease and diabetes.",
                'Banana': "High in potassium and fiber. Supports heart health and aids digestion.",
                'Grapes': "Packed with antioxidants like resveratrol. May have anti-aging properties.",
                'Kiwi': "High in vitamin C and fiber. Supports immune function and digestive health.",
                'Mango': "Rich in vitamins A and C. Supports eye health and boosts the immune system.",
                'Orange': "Known for high vitamin C content. Supports immune function and skin health.",
                'Strawberry': "Low in calories, high in vitamin C and antioxidants. May help improve heart health."
            }

            st.markdown(f"""
            <div class='fruit-info-box'>
                <h4 style='color: #4CAF50; margin-bottom: 10px;'>🍏 More about {predicted_class}:</h4>
                <p>{fruit_info[predicted_class]}</p>
            </div>
            """, unsafe_allow_html=True)

            # Fun fact
            fruit_facts = {
                'Apple': "There are over 7,500 varieties of apples grown worldwide!",
                'Banana': "Bananas are berries, but strawberries aren't!",
                'Grapes': "It takes about 2.5 pounds of grapes to produce one bottle of wine.",
                'Kiwi': "Kiwifruit was renamed for marketing purposes.",
                'Mango': "Mangoes belong to the same family as cashews!",
                'Orange': "Orange trees can live for up to 100 years.",
                'Strawberry': "Strawberries are the only fruit with seeds on the outside!"
            }

            st.markdown(f"""
            <div class='fun-fact-box'>
                <h4 style='color: #4CAF50; margin-bottom: 10px;'>🎉 Fun Fruit Fact:</h4>
                <p>{fruit_facts[predicted_class]}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please upload an image to start the prediction.")

# Display fruit prediction statistics
if 'fruit_df' in st.session_state and not st.session_state.fruit_df.empty:
    st.markdown("### 📊 Fruit Prediction Statistics")

    fruit_emojis = {
        'Apple': '🍎',
        'Banana': '🍌',
        'Grapes': '🍇',
        'Kiwi': '🥝',
        'Mango': '🥭',
        'Orange': '🍊',
        'Strawberry': '🍓'
    }

    fig = go.Figure()

    for index, row in st.session_state.fruit_df.iterrows():
        fruit = row['Fruit']
        count = row['Count']
        emoji = fruit_emojis.get(fruit, '')

        fig.add_trace(go.Bar(
            x=[fruit],
            y=[count],
            name=fruit,
            text=[f"{fruit} {emoji}"],  
            textposition='outside',
            hoverinfo='text',
            hovertext=f"{fruit}: {count}",
            marker_color=['#4CAF50', '#FFC107', '#FF5733', '#3498DB', '#8E44AD', '#E67E22', '#16A085'][index % 7]
        ))

    fig.update_layout(
        title='Fruit Prediction Count',
        xaxis_title="Fruit Type",
        yaxis_title="Number of Predictions",
        showlegend=False,
        xaxis={'categoryorder': 'total descending'}
    )

    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("""
<div class='footer'>
    <p>Thank you for coming ❤️</p>
</div>
""", unsafe_allow_html=True)
