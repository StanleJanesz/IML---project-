import pandas as pd

# Load the CSV file
data = pd.read_csv('C:\\studia\\IML\\features.csv')

# Check the first few rows of the data
print(data.head())


# Check for missing values
print(data.isnull().sum())

# Get basic statistics of numerical features
print(data.describe())

# Check data types and structure
print(data.info())


import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plot
plt.figure(figsize=(12, 8))

# Plot histograms for each numerical feature
numerical_columns = [ "Mean_R", "Mean_G", "Mean_B", "Mean_Brightness", "Mean_Saturation", "Contrast"]

# Plotting individual histograms
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 4, i + 1)
    sns.histplot(data[col], kde=True, bins=20)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()


# Plot the distribution of 'Gender'
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=data)
plt.title('Gender Distribution')
plt.show()

# Plot the distribution of 'Person'
plt.figure(figsize=(12, 6))
sns.countplot(x='Person', data=data)
plt.title('Person Distribution')
plt.xticks(rotation=90)  # Rotate x-axis labels if there are many unique persons
plt.show()

# Plot the distribution of 'Script'
plt.figure(figsize=(12, 6))
sns.countplot(x='Script', data=data)
plt.title('Script Distribution')
plt.xticks(rotation=90)  # Rotate x-axis labels if there are many unique persons
plt.show()
# Compute the correlation matrix
correlation_matrix = data[numerical_columns].corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.show()


# Box plots for 'Gender' vs numerical features
plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 4, i + 1)
    sns.boxplot(x='Gender', y=col, data=data)
    plt.title(f'Gender vs {col}')
plt.tight_layout()
plt.show()

# Box plots for 'Script' vs numerical features
plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 4, i + 1)
    sns.boxplot(x='Script', y=col, data=data)
    plt.title(f'Script vs {col}')
plt.tight_layout()
plt.show()

# Box plots for 'AudioType' vs numerical features
plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 4, i + 1)
    sns.boxplot(x='AudioType', y=col, data=data)
    plt.title(f'AudioType vs {col}')
plt.tight_layout()
plt.show()

# Box plots for 'IsTestSet' vs numerical features
plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 4, i + 1)
    sns.boxplot(x='IsTestSet', y=col, data=data)
    plt.title(f'IsTestSet vs {col}')
plt.tight_layout()
plt.show()


# Box plots for 'Class' vs numerical features
plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 4, i + 1)
    sns.boxplot(x='Class', y=col, data=data)
    plt.title(f'Class vs {col}')
plt.tight_layout()
plt.show()


# Box plots for 'Person' vs numerical features
plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 4, i + 1)
    sns.boxplot(x='Person', y=col, data=data)
    plt.title(f'Person vs {col}')
plt.tight_layout()
plt.show()

# Pairplot for numerical features
sns.pairplot(data[numerical_columns])
plt.show()


# Countplot of Person vs Gender
plt.figure(figsize=(12, 6))
sns.countplot(x='Person', hue='Gender', data=data)
plt.title('Person vs Gender Distribution')
plt.xticks(rotation=90)
plt.show()

# Countplot of Person vs IsTestSet
plt.figure(figsize=(12, 6))
sns.countplot(x='Person', hue='IsTestSet', data=data)
plt.title('Person vs IsTestSet Distribution')
plt.xticks(rotation=90)
plt.show()

# Countplot of Person vs Gender
plt.figure(figsize=(12, 6))
sns.countplot(x='AudioType', hue='IsTestSet', data=data)
plt.title('AudioType vs IsTestSet Distribution')
plt.xticks(rotation=90)
plt.show()

# Countplot of Person vs Gender
plt.figure(figsize=(12, 6))
sns.countplot(x='Person', hue='IsTestSet', data=data)
plt.title('Person vs IsTestSet Distribution')
plt.xticks(rotation=90)
plt.show()