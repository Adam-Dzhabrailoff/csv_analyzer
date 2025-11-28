import pytest

from app.report_strategies import AveragePerformanceReportStrategy


class TestAveragePerformanceReportStrateg:
    @pytest.mark.parametrize(
            "parsed_row, collected_data",
            [
                (
                    {
                        "name": "Elena Popova",
                        "position": "Backend Developer",
                        "completed_tasks": 43,
                        "performance": 4.8,
                        "skills": ["Java", "Spring Boot", "MySQL", "Redis"],
                        "team": "API Team",
                        "experience_years": 4
                    },
                    {
                        "Backend Developer": [4.8]
                    },
                ),
            ]
    )
    def test_collect(self, parsed_row, collected_data):
        strategy = AveragePerformanceReportStrategy()
        
        strategy.collect(parsed_row)

        assert strategy._collected_data == collected_data


    @pytest.mark.parametrize(
            "parsed_rows, aggregated_data",
            [
                (
                    [
                        {
                            "name": "Elena Popova",
                            "position": "Backend Developer",
                            "completed_tasks": 43,
                            "performance": 4.8,
                            "skills": ["Java", "Spring Boot", "MySQL", "Redis"],
                            "team": "API Team",
                            "experience_years": 4
                        },
                        {
                            "name": "Tom Anderson",
                            "position": "Backend Developer",
                            "completed_tasks": 49,
                            "performance": 4.9,
                            "skills": ["Go", "Microservices", "gRPC", "PostgreSQL"],
                            "team": "API Team",
                            "experience_years": 7
                        },
                    ],
                    {
                        "Backend Developer": 4.85
                    }
                )
            ]

    )
    def test_compute(self, parsed_rows, aggregated_data):
        strategy = AveragePerformanceReportStrategy()

        for parsed_row in parsed_rows:
            strategy.collect(parsed_row)
        strategy.compute()

        assert strategy._aggregated_data == aggregated_data


    @pytest.mark.parametrize(
            "aggregated_data, test_report_headers, test_report_data",
            [
                (
                    {
                        "Mobile Developer": 4.6,
                        "Backend Developer": 4.85,
                        "DevOps Engineer": 4.7,
                        "Frontend Developer": 4.6,
                        "Data Engineer": 4.7,
                        "QA Engineer": 4.5,
                        "Data Scientist": 4.7
                    },
                    ["position", "average_performance"],
                    [
                        ["Backend Developer", 4.85],
                        ["DevOps Engineer", 4.7],
                        ["Data Engineer", 4.7],
                        ["Data Scientist", 4.7],
                        ["Mobile Developer", 4.6],
                        ["Frontend Developer", 4.6],
                        ["QA Engineer", 4.5],
                    ]
                )
            ]
    )
    def test_summarize(self, aggregated_data, test_report_headers, test_report_data):
        strategy = AveragePerformanceReportStrategy()
        strategy._aggregated_data = aggregated_data

        report_headers, report_data = strategy.summarize()

        assert report_headers == test_report_headers
        assert report_data == test_report_data
