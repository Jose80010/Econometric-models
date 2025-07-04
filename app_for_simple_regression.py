# -*- coding: utf-8 -*-
"""App for simple regression.ipynb


"""


import pandas as pd
import matplotlib.pyplot as plt
data = {'TeslaStockPrice': [150, 160, 170, 180, 190, 200],
        'EPS': [5.0, 5.5, 6.0, 6.5, 7.0, 7.5]}

df = pd.DataFrame(data)
x_data = df['EPS'].values
y_data = df['TeslaStockPrice'].values

#st.dataframe(df)
st.dataframe(pd.DataFrame(df)
# Sidebar sliders for slope and intercept
st.sidebar.header("🔧 Adjust Parameters")
m = st.sidebar.slider("Slope $\hat{β}_1=$", min_value=-100.0, max_value=100.0, value=10.0, step=0.1)
b = st.sidebar.slider("Intercept $\hat{β}_0=$", min_value=-500.0, max_value=500.0, value=0.0, step=0.1)

# Calculate predicted y values
y_pred = m * x_data + b

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
ax.legend()
ax.grid(True)

# Add lines for the axes crossing in black
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)




st.pyplot(fig)

# Optional display of equation
st.markdown(f"### 📌 Current Line Equation: `y = {m:.2f}x + ({b:.2f})`")
