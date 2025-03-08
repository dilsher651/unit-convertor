import streamlit as st
import pandas as pd

# Custom CSS styling
st.markdown("""
<style>
.main {
    padding: 2rem;
    border-radius: 10px;
    background-color: #f0f2f6;
    transition: all 0.3s ease;
}
.main:hover {
    transform: scale(1.01);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.stButton button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    transition: all 0.2s ease;
}
.stButton button:hover {
    background-color: #ff6b6b;
    transform: translateY(-2px);
}
.result {
    font-size: 24px;
    font-weight: bold;
    color: #0066cc;
    padding: 1rem;
    border-radius: 5px;
    background-color: white;
    margin: 1rem 0;
    transition: all 0.3s ease;
}
.result:hover {
    transform: scale(1.02);
    box-shadow: 0 2px 6px rgba(0,102,204,0.2);
}
</style>
""", unsafe_allow_html=True)

# Title with emoji
st.title("Unit Converter 🔄")

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    input_value = st.number_input("Enter Value 📝", value=0.0)
    
with col2:
    # Dictionary of conversion categories and their units
    conversion_categories = {
        "Length 📏": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "Weight ⚖️": ["Kilograms", "Grams", "Pounds", "Ounces"],
        "Temperature 🌡️": ["Celsius", "Fahrenheit", "Kelvin"],
        "Time ⏰": ["Seconds", "Minutes", "Hours", "Days"]
    }
    
    # Category selection
    category = st.selectbox("Select Category", list(conversion_categories.keys()))
    
# Create two columns for from/to units
from_col, to_col = st.columns(2)

with from_col:
    from_unit = st.selectbox("From Unit", conversion_categories[category])
    
with to_col:
    to_unit = st.selectbox("To Unit", conversion_categories[category])

# Conversion functions
def convert_length(value, from_unit, to_unit):
    # Convert everything to meters first
    meters = {
        "Meters": value,
        "Kilometers": value * 1000,
        "Miles": value * 1609.34,
        "Feet": value * 0.3048,
        "Inches": value * 0.0254
    }
    # Convert from meters to desired unit
    conversion = {
        "Meters": meters[from_unit],
        "Kilometers": meters[from_unit] / 1000,
        "Miles": meters[from_unit] / 1609.34,
        "Feet": meters[from_unit] / 0.3048,
        "Inches": meters[from_unit] / 0.0254
    }
    return conversion[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Convert everything to grams first
    grams = {
        "Kilograms": value * 1000,
        "Grams": value,
        "Pounds": value * 453.592,
        "Ounces": value * 28.3495
    }
    # Convert from grams to desired unit
    conversion = {
        "Kilograms": grams[from_unit] / 1000,
        "Grams": grams[from_unit],
        "Pounds": grams[from_unit] / 453.592,
        "Ounces": grams[from_unit] / 28.3495
    }
    return conversion[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        if to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        if to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        if to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

def convert_time(value, from_unit, to_unit):
    # Convert everything to seconds first
    seconds = {
        "Seconds": value,
        "Minutes": value * 60,
        "Hours": value * 3600,
        "Days": value * 86400
    }
    # Convert from seconds to desired unit
    conversion = {
        "Seconds": seconds[from_unit],
        "Minutes": seconds[from_unit] / 60,
        "Hours": seconds[from_unit] / 3600,
        "Days": seconds[from_unit] / 86400
    }
    return conversion[to_unit]

# Convert button
if st.button("Convert! 🔄"):
    result = 0
    if category == "Length 📏":
        result = convert_length(input_value, from_unit, to_unit)
    elif category == "Weight ⚖️":
        result = convert_weight(input_value, from_unit, to_unit)
    elif category == "Temperature 🌡️":
        result = convert_temperature(input_value, from_unit, to_unit)
    elif category == "Time ⏰":
        result = convert_time(input_value, from_unit, to_unit)
    
    # Display result with styling
    st.markdown(f"""
    <div class="result">
        {input_value} {from_unit} = {result:.4f} {to_unit}
    </div>
    """, unsafe_allow_html=True)

# Add footer
st.markdown("---")
st.markdown("### Made with ❤️ using Streamlit")
