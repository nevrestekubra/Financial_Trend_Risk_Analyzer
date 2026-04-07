import sys
from loader import FinancialDataLoader
from analyzer import FinancialAnalyzer
from risk_engine import RiskEngine
from plotter import FinancialPlotter


def main():
    """
    The Entry Point of the application.
    Acts as the orchestrator for the data pipeline.
    """
    # Check for CLI arguments (Equivalent to argc < 2 in C++)
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path.csv>")
        return

    # Extract path from command line arguments (argv[1])
    file_path = sys.argv[1]

    try:
        # Step 1: Data Ingestion and Sanitization
        print(f"--- Loading: {file_path} ---")
        loader = FinancialDataLoader(file_path)
        df = loader.load_data()

        # Step 2: Financial Ratio Calculations
        print("--- Running Analysis ---")
        analyzer = FinancialAnalyzer(df)
        df = analyzer.run_analysis()

        # Step 3: Risk Scoring Logic
        print("--- Evaluating Risk Scores ---")
        engine = RiskEngine(df)
        df = engine.evaluate_risk()

        # Step 4: Data Visualization
        print("--- Generating Visuals ---")
        plotter = FinancialPlotter(df)

        # Displaying the results
        plotter.plot_risk_distribution()
        plotter.plot_profitability_trends()

        print("--- Pipeline Execution Successful ---")

        print("\n--- DETAILED RISK ANALYSIS ---")
        print(df[['company', 'year', 'risk_level']].to_string(index=False))

    except Exception as e:
        # Global exception handler to catch runtime errors
        print(f"Execution Error: {e}")


if __name__ == "__main__":
    # This block ensures the script runs only when executed directly,
    # not when imported as a module in another script.
    main()