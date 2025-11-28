from abc import (
    ABC,
    abstractmethod,
)
from collections import defaultdict


# A class that defines the way data is analyzed to produce a report
class AbstractReportStrategy(ABC):    
    @abstractmethod
    def collect(self):
        raise NotImplementedError


    @abstractmethod
    def compute(self):
        raise NotImplementedError


    @abstractmethod
    def summarize(self):
        raise NotImplementedError


class AveragePerformanceReportStrategy(AbstractReportStrategy):
    def __init__(self):
        self._collected_data = defaultdict(list)
        self._aggregated_data = {}


    # Collects data
    def collect(
            self,
            parsed_row: dict[str, str],
    ):
        position = parsed_row["position"]
        performance = parsed_row["performance"]
        self._collected_data[position].append(performance)


    # Aggregates on collected data
    def compute(
            self,
    ):
        for position, performance_values in self._collected_data.items():
            self._aggregated_data[position] = (
                sum(performance_values) / len(performance_values)
            )


    # Summarizes collected data
    def summarize(
            self,
    ):
        report_headers = ["position", "average_performance"]
        report_data = [[position, round(average_performance, 2)]
                       for position, average_performance
                       in self._aggregated_data.items()]
        report_data.sort(key=lambda x: x[1], reverse=True)

        return report_headers, report_data
