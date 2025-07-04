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

st.header("📚 Interpretation")

st.write("### Intercept ($\hat{β}_0$) Interpretation:")
if b > 0:
    st.write(f"When EPS is 0, the model predicts a Tesla Stock Price of approximately **{b:.2f}**.  However, interpreting the intercept in isolation can be misleading, especially if 0 is outside the range of observed EPS values.")
elif b < 0:
    st.write(f"When EPS is 0, the model predicts a Tesla Stock Price of approximately **{b:.2f}**.  A negative intercept might not be meaningful in this context, as stock prices are typically non-negative. It's important to consider if 0 is within the range of your data.")
else:
    st.write("When EPS is 0, the model predicts a Tesla Stock Price of approximately **0.00**. This suggests that without any EPS, the stock price is predicted to be zero, which might not be a realistic scenario.")


st.write("### Slope ($\hat{β}_1$) Interpretation:")
if m > 0:
    st.write(f"For every one-unit increase in EPS, the model predicts an increase in the Tesla Stock Price of approximately **{m:.2f}**.")
elif m < 0:
    st.write(f"For every one-unit increase in EPS, the model predicts a decrease in the Tesla Stock Price of approximately **{m:.2f}**.")
else:
    st.write("The slope is **0.00**. This means the model predicts no change in Tesla Stock Price for a one-unit increase in EPS.")




# Sidebar sliders for slope and intercept
st.sidebar.header("🔧 Adjust Parameters")
m = st.sidebar.slider("Slope $\hat{β}_1=$", min_value=-100.0, max_value=100.0, value=10.0, step=0.1)
b = st.sidebar.slider("Intercept $\hat{β}_0=$", min_value=-500.0, max_value=500.0, value=0.0, step=0.1)

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
