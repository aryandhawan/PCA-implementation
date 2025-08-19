import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [2.5, 2.4, 1.0],
    [0.5, 0.7, 0.6],
    [2.2, 2.9, 0.9],
    [1.9, 2.2, 1.3],
    [3.1, 3.0, 1.0]
])

# always gotta center the data first so that the data is not biased at all this should be done for all columns separately
def center_data(data):
        mean_vector=data.mean(axis=0)
        centered_vector=data-mean_vector
        return centered_vector

# now it's time to calculate covariance matrix for the same

covariance_matrix=np.cov(center_data(data),rowvar=False)


# now it's time to find the eigenvalues of the covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

sorted_indices = eigenvalues.argsort()[::-1]
# print("Top 2 eigenvalues:", eigenvalues[sorted_indices[:2]])
# print("Indices of top 2 components:", sorted_indices[:2])



# select top 2 eigen vectors to project on

k=2

projection_matrix=eigenvectors[:,sorted_indices[:k]]

# projecting onto PCA axis

x_proejcted=center_data(data).dot(projection_matrix)

print(x_proejcted)

# visualisation for PCA

import matplotlib.pyplot as plt

# Your projected data (5 samples, 2 components)
X_projected = [[ 0.44527954,  0.20106725],
               [-2.20399016,  0.06577795],
               [ 0.56024754, -0.35346475],
               [-0.08959421, -0.1030011 ],
               [ 1.28805729,  0.18962066]]

# Separate the two components for plotting
x = [point[0] for point in X_projected]
y = [point for point in X_projected]

# Create scatter plot
plt.scatter(x, y, color='blue')

# Add titles and labels
plt.title('PCA Projected Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

# Show grid for easier interpretation
plt.grid(True)

# Display the plot
plt.show()
