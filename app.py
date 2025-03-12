import streamlit as st
import openai

# Set OpenAI API Key (Replace with your actual key)
openai.api_key = "your-api-key-here"

def get_outfit_suggestion(body_type, occasion, budget, colors):
    prompt = f"Suggest a fashionable outfit for a {body_type} person going to a {occasion} event. Budget is {budget}. Preferred colors: {colors}."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a fashion stylist."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"].strip()

# Streamlit UI
st.title("AI Fashion Assistant 👗👕")

body_type = st.selectbox("Select your body type:", ["Slim", "Athletic", "Plus-size", "Average"])
occasion = st.selectbox("Select the occasion:", ["Casual", "Party", "Wedding", "Office", "Date Night"])
budget = st.selectbox("Select budget range:", ["Under ₹1000", "₹1000-₹5000", "₹5000-₹10000", "₹10000+"])
colors = st.text_input("Preferred colors (comma-separated):")

if st.button("Get Outfit Suggestion"):
    suggestion = get_outfit_suggestion(body_type, occasion, budget, colors)
    st.write("### Suggested Outfit:")
    st.write(suggestion)
