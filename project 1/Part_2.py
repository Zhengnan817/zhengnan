import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
# Import Seirs and DataFrame
from pandas import Series, DataFrame

class Solution:
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