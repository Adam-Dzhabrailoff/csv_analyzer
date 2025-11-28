from app.report_strategies import (
    AbstractReportStrategy,
    AveragePerformanceReportStrategy
)

# A report strategy factory
class ReportStrategyFactory:
    # Each strategy corresponds to an report type
    _strategies = {
        "performance": AveragePerformanceReportStrategy
    }


    # Dynamically creates report strategy object
    @classmethod
    def create(
        cls,
        report_type: str,
    ) -> AbstractReportStrategy:
        try:
            return cls._strategies[report_type]()
        except KeyError:
            raise ValueError(f"The report type {report_type} is invalid")
