import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_data():
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [23, 45, 56, 78]
    })
    sns.barplot(x='Category', y='Values', data=data)
    plt.title("Sample Bar Chart")
    plt.show()
visualize_data()
