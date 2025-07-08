# -*- coding: utf-8 -*-
"""App for simple regression.ipynb


"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("📈 Simple Linear Regression Interactive Plot")
st.write("Created by Dr Jose Islas")
# Sample data
x_data= [5.0, 5.5, 6.0, 6.5, 7.0, 7.5]
true_slope = 2.5
true_intercept = 1.0
y_data = [150, 160, 170, 180, 190, 200]
st.dataframe(pd.DataFrame({'EPS': x_data, 'TeslaStockPrice': y_data}))



# Sidebar sliders for slope and intercept
#st.sidebar.header("🔧 Adjust Parameters")
#m = st.sidebar.slider("Slope $\hat{β}_1=$", min_value=-100.0, max_value=100.0, value=10.0, step=0.1)
#b = st.sidebar.slider("Intercept $\hat{β}_0=$", min_value=-500.0, max_value=500.0, value=0.0, step=0.1)


# Sidebar input for slope and intercept with numerical input as well
st.sidebar.header("🔧 Adjust Parameters")
m_input = st.sidebar.text_input("Enter Slope $\hat{β}_1$:", value="10.0")
b_input = st.sidebar.text_input("Enter Intercept $\hat{β}_0$:", value="0.0")

#try:
#    m = float(m_input)
#    b = float(b_input)
#except ValueError:
#    st.sidebar.error("Please enter valid numbers for Slope and Intercept.")
#    m = 10.0 # Default value if input is invalid
#    b = 0.0  # Default value if input is invalid




# Calculate predicted y values
#y_pred = m * x_data + b
y_pred = m * np.array(x_data) + b


# Plotting
fig, ax = plt.subplots()
ax.scatter(x_data, y_data, label="Data", color='blue')
ax.plot(x_data, y_pred, label=f"y = {m:.2f}x + {b:.2f}", color='red')
ax.set_xlabel("EPS")
ax.set_ylabel("Tesla Stock Price")
ax.legend()
ax.grid(True)

# Add lines for the axes crossing in black
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

st.pyplot(fig)

# Optional display of equation
st.markdown(f"### 📌 Current Line Equation: `Tesla Stock Price = {m:.2f} * EPS + ({b:.2f})`")
# Interpretation of intercept and slope
st.markdown("### 📊 Interpretation")
st.write(f"**Intercept = {b:.2f}:** This is the predicted Tesla Stock Price when the EPS (Earnings Per Share) is 0.")
st.write(f"**Slope = {m:.2f}:** This represents the estimated change in Tesla Stock Price for every one-unit increase in EPS.")
