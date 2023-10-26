import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
# Import Seirs and DataFrame
from pandas import Series, DataFrame

class Solution:
    def __init__(self,filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)
    def a(self):
        return (self.df.head())
    def say(self):
        print ('The file is',self.filepath)
        print (self.project.head(1))
    def b(self):
    # Use isna and sum function to see if there are any null values in the data set.    
        return self.df.isna().sum()
    def c(self):
    # Use dropna function to remove the null vlaues
        return self.df.dropna()

    def task_one(self):
    #calculate the number of the type in different vendor
        chip_num = self.df.groupby(['Vendor','Type']).size()
    # Use matplotlib to visualize the results
        chip_num.plot.bar(title='Venders numbers of different types',figsize=(12,6))
        plt.xlabel('type')
        plt.ylabel('Numbers of types')
        return chip_num
    def task_two(self):
        # Create a barplot for 'Type' and 'Vendor' in one picture
        plt.figure(figsize=(12, 6))

        # Use catplot with kind='count' to create the barplot
        sb.catplot(data=self.df, x='Type', hue='Vendor', kind='count', palette='Set3', height=6, aspect=2)

        # Set labels and title
        plt.xlabel('Type')
        plt.ylabel('Count')
        plt.title('Barplot of Type and Vendor')

        # Show the plot
        plt.show()
    def task_three(self):
        plt.figure(figsize=(10,6))
        plt.plotbar(data=self.df, bins= 30, edgecolor='black')
        plt.title('Process Size and prequence')
        plt.xlabel('Process_Size')
        plt.ylabel('Freq')
        plt.grid(True)
        plt.show
    def task_five(self):
        # Create a scatter plot
        plt.figure(figsize=(10, 6))  # Set the figure size

        # Extract the data from your DataFrame
        x = self.df['Process_Size']
        y = self.df['Freq']

        # Create the scatter plot
        plt.scatter(x, y, marker='o', color='b', alpha=0.5)  # 'marker' sets the point style, 'color' sets the point color, 'alpha' sets transparency

        # Add labels and title
        plt.title('Scatter Plot of Process Size vs. Frequency')
        plt.xlabel('Process_Size')
        plt.ylabel('Frequency')

        # Display the plot
        plt.show()
    def task_six(self):
        # Set the style for the plot (optional)
        sb.set(style="whitegrid")

        # Create a scatter plot
        plt.figure(figsize=(10, 6))  # Set the figure size

        # Use Seaborn's scatterplot function
        sb.scatterplot(data=self.df, x="Process_Size", y="Freq", alpha=0.5)

        # Add labels and title
        plt.title('Scatter Plot of Process Size vs. Frequency')
        plt.xlabel('Process_Size')
        plt.ylabel('Frequency')

        # Display the plot
        plt.show()

    def task_seven(self):
        # Create a histogram for the "Transistors" column
        plt.figure(figsize=(10, 6))  # Set the figure size

        # Extract the data from your DataFrame
        transistors = self.df['Transistors']

        # Create the histogram
        plt.hist(transistors, bins=30, edgecolor='black', alpha=0.7, color='blue')

        # Add labels and title
        plt.title('Histogram of Transistors')
        plt.xlabel('Transistors')
        plt.ylabel('Frequency')

        # Display the plot
        plt.show()
    def task_eight(self):
        plt.figure(figsize=(12, 6))

        # Create a histogram for 'Transistors' and 'Freq' in one picture
        sb.histplot(data=self.df, x='Transistors', bins=30, kde=True, color='blue', label='Transistors')
        sb.histplot(data=self.df, x='Freq', bins=30, kde=True, color='green', label='Freq')

        # Set labels and title
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histograms of Transistors and Freq')

        # Add a legend
        plt.legend()

        # Show the plot
        plt.show()
    def task_nine(self):
        # Create a scatter plot
        plt.figure(figsize=(10, 6))  # Set the figure size

        # Extract the data from your DataFrame
        x = self.df['Die_Size']
        y = self.df['Freq']

        # Create the scatter plot
        plt.scatter(x, y, marker='o', color='b', alpha=0.5)  # 'marker' sets the point style, 'color' sets the point color, 'alpha' sets transparency

        # Add labels and title
        plt.title('Scatter Plot of Die Size vs. Frequency')
        plt.xlabel('Die_Size')
        plt.ylabel('Frequency')

        # Display the plot
        plt.show()
    def task_ten(self):
      # Set the style for the plot (optional)
        sb.set(style="whitegrid")

        # Create a scatter plot
        plt.figure(figsize=(10, 6))  # Set the figure size

        # Use Seaborn's scatterplot function
        sb.scatterplot(data=self.df, x="Die_Size", y="Freq", alpha=0.5)

        # Add labels and title
        plt.title('Scatter Plot of Die Size vs. Frequency')
        plt.xlabel('Die_Size')
        plt.ylabel('Frequency')

        # Display the plot
        plt.show()
    def task_d(self):
            # Create a bar plot for 'Process_Size' with numbers on the x-axis
            plt.figure(figsize=(12, 6))

            sb.barplot(data=self.df, x=self.df.index, y='Process_Size', palette='Set3')

            # Set labels and title
            plt.xlabel('Number')
            plt.ylabel('Process Size')
            plt.title('Bar Plot of Process Size')

            # Show the plot
            plt.show()
    def task_e(self):
            # Create a bar plot for 'Process_Size' with numbers on the x-axis
            plt.figure(figsize=(12, 6))

            sb.barplot(data=self.df, x=self.df.index, y='TDP', palette='Set3')

            # Set labels and title
            plt.xlabel('Number')
            plt.ylabel('TDB')
            plt.title('Bar Plot of TDB')

            # Show the plot
            plt.show()
    def task_f(self):
            # Create a bar plot for 'Process_Size' with numbers on the x-axis
            plt.figure(figsize=(12, 6))

            sb.barplot(data=self.df, x=self.df.index, y='Die_Size', palette='Set3')

            # Set labels and title
            plt.xlabel('Number')
            plt.ylabel('Die Size')
            plt.title('Bar Plot of DieSize')

            # Show the plot
            plt.show()
    def task_g(self):
            # Create a bar plot for 'Process_Size' with numbers on the x-axis
            plt.figure(figsize=(12, 6))

            sb.barplot(data=self.df, x=self.df.index, y='Transistors', palette='Set3')

            # Set labels and title
            plt.xlabel('Number')
            plt.ylabel('Transistors')
            plt.title('Bar Plot of Transistors')

            # Show the plot
            plt.show()
    def task_h(self):
            # Create a bar plot for 'Process_Size' with numbers on the x-axis
            plt.figure(figsize=(12, 6))

            sb.barplot(data=self.df, x=self.df.index, y='Freq', palette='Set3')

            # Set labels and title
            plt.xlabel('Number')
            plt.ylabel('Freq')
            plt.title('Bar Plot of Freq')

            # Show the plot
            plt.show()