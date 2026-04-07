import pandas as pd

class RiskEngine:
    def __init__(self, df):
        # I receive the enriched dataframe from the analyzer.
        self.df = df

    def evaluate_risk(self):
        # I apply my scoring logic to each row (axis=1 means row-by-row).
        self.df['risk_score'] = self.df.apply(self._calculate_row_risk, axis=1)

        # I categorize the numeric scores into readable risk levels.
        self.df['risk_level'] = self.df['risk_score'].apply(self._assign_risk_level)

        return self.df

    def _calculate_row_risk(self, row):
        # I start with a zero score for each row.
        score = 0

        # I add 2 points if debt ratio is dangerously high (> 70%).
        if row['debt_ratio'] > 0.70:
            score += 2

        # I add 3 points if the company has negative return on equity.
        if row['roe'] < 0:
            score += 3

        # I add 5 points if shareholders' equity is negative (insolvency).
        if row['shareholders_equity'] < 0:
            score += 5

        # I add 1 point if net income dropped by more than 10%.
        # I check for Not-Null because the first year is always NaN.
        if pd.notnull(row['net_income_growth']) and row['net_income_growth'] < -0.10:
            score += 1

        return score

    def _assign_risk_level(self, score):
        # I define risk categories based on the total score.
        if score >= 5:
            return "High Risk"
        elif score >= 2:
            return "Medium Risk"
        else:
            return "Low Risk"