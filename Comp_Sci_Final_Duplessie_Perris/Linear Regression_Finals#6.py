import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LinearRegression

#Wouldn't let me sumbit code unless I commented the %matplotlib inline
#%matplotlib inline
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

cmap = mpl.colormaps.get_cmap("jet")

# Where to save the figures
PROJECT_ROOT_DIR = "."
FOLDER = "figures"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, FOLDER)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# Create 3D scatter plot with a line going through it
fig = plt.figure(figsize=[15, 15])
ax_list = []

for i in range(1, 5):
    ax = fig.add_subplot(2, 2, i, projection='3d')
    ax_list.append(ax)

# Scatter plot with labels
for ax in ax_list:
  np.random.seed(42)
x_data = np.random.rand(100) * 20
y_data = np.random.rand(100) * 20
z_data = 2 * x_data + 3 * y_data + np.random.randn(100) * 2  # Example linear relation with noise
ax.scatter3D(x_data, y_data, z_data, c=z_data, cmap=cmap)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Linear regression
model = LinearRegression()
model.fit(np.array([x_data, y_data]).T, z_data)
x_fit = np.linspace(min(x_data), max(x_data), 1000)
y_fit = np.linspace(min(y_data), max(y_data), 1000)
X_fit, Y_fit = np.meshgrid(x_fit, y_fit)
Z_fit = model.predict(np.array([X_fit.flatten(), Y_fit.flatten()]).T).reshape(X_fit.shape)

# Add best-fit curve to all subplots
for i, ax in enumerate(ax_list):
    ax.plot_surface(X_fit, Y_fit, Z_fit, cmap=cmap, alpha=0.5)
    ax.view_init(elev=20, azim=30 * i)  # Adjust the viewing angles

plt.tight_layout()
save_fig("data_scatter_with_regression")
plt.show()

# Display true model parameters
print("True Model Coefficients:", "ENTER YOUR VALUES")
print("True Model Intercept:", "ENTER YOUR VALUES")