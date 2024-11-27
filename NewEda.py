import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('C:\\studia\\IML\\featuresOld.csv')


print(data.head())



print(data.isnull().sum())


print(data.describe())


print(data.info())


import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(12, 8))


numerical_columns = [ "Mean_R", "Mean_Brightness",  "Contrast","Homogeneity","Edge_density"]


for i, col in enumerate(numerical_columns):
    plt.subplot(2, 3, i + 1)
    sns.histplot(data[col], kde=True, bins=20)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=data)
plt.title('Gender Distribution')
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='Person', data=data)
plt.title('Person Distribution')
plt.xticks(rotation=90)  
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='Script', data=data)
plt.title('Script Distribution')
plt.xticks(rotation=90)  
plt.show()

correlation_matrix = data[numerical_columns].corr()


plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.show()



plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 4, i + 1)
    sns.boxplot(x='Gender', y=col, data=data)
    plt.title(f'Gender vs {col}')
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 3, i + 1)
    sns.boxplot(x='Script', y=col, data=data)
    plt.title(f'Script vs {col}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 3, i + 1)
    sns.boxplot(x='AudioType', y=col, data=data)
    plt.title(f'AudioType vs {col}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 3, i + 1)
    sns.boxplot(x='IsTestSet', y=col, data=data)
    plt.title(f'IsTestSet vs {col}')
plt.tight_layout()
plt.show()



plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 3, i + 1)
    sns.boxplot(x='Class', y=col, data=data)
    plt.title(f'Class vs {col}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
for i, col in enumerate(numerical_columns):
    plt.subplot(2, 3, i + 1)
    sns.boxplot(x='Person', y=col, data=data)
    plt.title(f'Person vs {col}')
plt.tight_layout()
plt.show()

sns.pairplot(data[numerical_columns])
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='Person', hue='Gender', data=data)
plt.title('Person vs Gender Distribution')
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='Person', hue='IsTestSet', data=data)
plt.title('Person vs IsTestSet Distribution')
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='AudioType', hue='IsTestSet', data=data)
plt.title('AudioType   vs IsTestSet Distribution')
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='Person', hue='IsTestSet', data=data)
plt.title('Person vs IsTestSet Distribution')
plt.xticks(rotation=90)
plt.show()