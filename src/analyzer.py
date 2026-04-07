import pandas as pd


class FinancialAnalyzer:
    """
    I designed this class to take the clean data and calculate 
    financial performance metrics like ROA, ROE, and growth rates.
    """

    def __init__(self, df):
        # I receive the cleaned dataframe from the loader as input
        self.df = df

    def run_analysis(self):
        """I am the main controller. I call each calculation step in the correct order."""
        self._calculate_ratios()
        self._calculate_growth()

        # I return the enriched dataframe containing new calculated columns
        return self.df

    def _calculate_ratios(self):
        """I calculate the fundamental financial health ratios."""

        # ROA (Return on Assets): Net Income / Total Assets
        # I measure how much profit a company generates for every $1 of assets it owns.
        self.df['roa'] = self.df['net_income'] / self.df['total_assets']

        # ROE (Return on Equity): Net Income / Shareholders Equity
        # I measure the profit generated compared to the money invested by shareholders.
        self.df['roe'] = self.df['net_income'] / self.df['shareholders_equity']

        # Debt Ratio: Total Liabilities / Total Assets
        # I check what percentage of the company's assets are financed by debt.
        self.df['debt_ratio'] = self.df['total_liabilities'] / self.df['total_assets']

    def _calculate_growth(self):
        """I calculate year-over-year (YoY) growth for income and revenue."""

        # Engineering Note: I MUST group by company before calculating growth.
        # Otherwise, the system might try to compare Apple's 2022 with Microsoft's 2021.
        grouped = self.df.groupby('company')


        self.df['net_income_growth'] = grouped['net_income'].pct_change()
        self.df['revenue_growth'] = grouped['total_revenue'].pct_change()
        self.df['eps_growth'] = grouped['eps'].pct_change()