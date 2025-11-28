from tabulate import tabulate

from app.factory import ReportStrategyFactory
from app.csv_parser import CSVParser


# A manager that acts as a context of report strategy
class ReportManager:
    def __init__(
            self,
    ):
        self._report_strategy_factory = ReportStrategyFactory
 

    # Generates report data and returns it in a tabular format
    def generate_report(
            self,
            csv_paths: list[str],
            report_type: str,
    ) -> str:
        report_strategy = self._report_strategy_factory.create(report_type)

        try:
            # Collects data according to the report strategy
            for parsed_row in CSVParser.parse_csv_by_row(csv_paths):
                report_strategy.collect(parsed_row)
        except Exception:
            raise

        # Aggregates on collected data according to the report strategy
        report_strategy.compute()

        # Summarizes collected data according to the report strategy
        headers, result_rows = report_strategy.summarize()

        report_table = tabulate(
            result_rows,
            headers=headers,
            floatfmt=".2f",
            showindex=range(1, len(result_rows) + 1)
        )

        return report_table
