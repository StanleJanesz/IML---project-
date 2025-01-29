
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('C:\\studia\\IML\\features.csv')


print(df.head())  
print(df.info())  
print(df.describe()) 


print(df.isnull().sum())


df = df.dropna()  
df = df.drop_duplicates()  


df['Gender'] = df['Gender'].astype('category') 
df['Class'] = df['Class'].astype('category') 


print(df[['Mean_R', 'Mean_G', 'Mean_B', 'Mean_Brightness', 'Mean_Saturation', 'Contrast']].describe())


df[['Mean_R', 'Mean_G', 'Mean_B', 'Mean_Brightness', 'Mean_Saturation', 'Contrast']].hist(bins=20, figsize=(12, 10))
plt.suptitle('Histograms of Numerical Features')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Mean_R', 'Mean_G', 'Mean_B', 'Mean_Brightness', 'Mean_Saturation', 'Contrast']])
plt.title('Boxplots of Numerical Features')
plt.show()


corr = df[['Mean_R', 'Mean_G', 'Mean_B', 'Mean_Brightness', 'Mean_Saturation', 'Contrast']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


sns.boxplot(x='Gender', y='Mean_R', data=df)
plt.title('Gender vs Mean Red')
plt.show()

sns.boxplot(x='Gender', y='Mean_G', data=df)
plt.title('Gender vs Mean Green')
plt.show()

sns.boxplot(x='Gender', y='Mean_B', data=df)
plt.title('Gender vs Mean Blue')
plt.show()

sns.boxplot(x='Class', y='Mean_R', data=df)
plt.title('Class vs Mean Red')
plt.show()

sns.boxplot(x='Class', y='Mean_G', data=df)
plt.title('Class vs Mean Green')
plt.show()

sns.boxplot(x='Class', y='Mean_B', data=df)
plt.title('Class vs Mean Blue')
plt.show()
