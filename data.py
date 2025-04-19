# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset

# Load the dataset (replace 'your_dataset.csv' with the path to your dataset)
try:
    df = pd.read_csv('your_dataset.csv')  # Example: use your actual dataset path here
    print("Dataset loaded successfully")
except FileNotFoundError:
    print("The dataset file was not found.")
    exit()

# Display the first few rows of the dataset to inspect
print(df.head())

# Explore the structure of the dataset
print(df.info())

# Check for missing values in the dataset
print("Missing Values:")
print(df.isnull().sum())

# Task 1: Clean the dataset

# Option 1: Drop rows with missing values
# df_cleaned = df.dropna()

# Option 2: Fill missing values with the mean (for numerical columns)
df_cleaned = df.fillna(df.mean())

# Verify the cleaned dataset (check for missing values again)
print("Missing Values After Cleaning:")
print(df_cleaned.isnull().sum())

# Task 2: Basic Data Analysis

# Compute basic statistics (mean, median, std, etc.)
print("Basic Statistics:")
print(df.describe())

# Group by a categorical column (example: species in Iris dataset)
if 'species' in df.columns:
    grouped = df.groupby('species').mean()
    print("Grouped Data by Species:")
    print(grouped)

# Task 3: Data Visualization

# Line Chart: Example of sales data over time (assuming dataset has a 'date' and 'sales' column)
if 'date' in df.columns and 'sales' in df.columns:
    df['date'] = pd.to_datetime(df['date'])  # Convert date to datetime format
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['sales'], label='Sales over Time')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    plt.grid(True)
    plt.show()

# Bar Chart: Example of average petal length by species (replace column names accordingly)
if 'species' in df.columns and 'petal_length' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.barplot(x='species', y='petal_length', data=df)
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length')
    plt.show()

# Histogram: Example of sepal length distribution (replace column names accordingly)
if 'sepal_length' in df.columns:
    plt.figure(figsize=(8, 6))
    plt.hist(df['sepal_length'], bins=20, edgecolor='black')
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Frequency')
    plt.show()

# Scatter Plot: Example of sepal length vs petal length
if 'sepal_length' in df.columns and 'petal_length' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal_length', y='petal_length', data=df)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.show()


