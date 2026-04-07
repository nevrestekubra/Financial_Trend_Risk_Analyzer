import pandas as pd
import os


class FinancialDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        # I only keep the columns necessary for my financial formulas.
        self.required_columns = [
            'company', 'year', 'total_revenue', 'net_income',
            'total_assets', 'total_liabilities', 'shareholders_equity', 'eps'
        ]

    def load_data(self):
        # I check if the file exists before attempting to read it.
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        df = pd.read_csv(self.file_path)
        return self._validate_and_clean(df)

    def _validate_and_clean(self, df):
        # I verify all required columns are present.
        missing_cols = [col for col in self.required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing columns: {missing_cols}")

        # I drop unnecessary columns to save memory.
        df = df[self.required_columns].copy()

        # I convert data to numeric, turning errors into NaNs.
        numeric_cols = self.required_columns[1:]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        initial_count = len(df)

        # I filter out negative or unrealistic years.
        df = df[df['year'] > 1800]

        # I ensure assets, revenue, and liabilities are non-negative.
        non_neg = ['total_revenue', 'total_assets', 'total_liabilities']
        for col in non_neg:
            df = df[df[col] >= 0]

        # I remove rows with missing critical identifiers.
        df.dropna(subset=['company', 'year', 'net_income'], inplace=True)

        # I notify if any invalid rows were removed.
        if len(df) < initial_count:
            print(f"I removed {initial_count - len(df)} invalid rows.")

        # I sort by company and year to prepare for growth analysis.
        df.sort_values(by=['company', 'year'], ascending=[True, True], inplace=True)

        return df.reset_index(drop=True)