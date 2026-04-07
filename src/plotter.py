import matplotlib.pyplot as plt
import seaborn as sns

class FinancialPlotter:
    def __init__(self, df):
        # I receive the final dataframe with all calculations and risk scores.
        self.df = df

    def plot_risk_distribution(self):
        # I create a bar chart to see the count of each risk level.
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df, x='risk_level', palette='viridis', order=['Low Risk', 'Medium Risk', 'High Risk'])
        plt.title('Distribution of Company Risk Levels')
        plt.show()

    def plot_profitability_trends(self):
        # I visualize net income trends over the years for each company.
        plt.figure(figsize=(12, 7))
        sns.lineplot(data=self.df, x='year', y='net_income', hue='company', marker='o')
        plt.title('Net Income Trends by Company')
        plt.grid(True)
        plt.show()
