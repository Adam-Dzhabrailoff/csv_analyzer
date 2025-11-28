import pytest

from tabulate import tabulate


# ==========
# test_csv_parser.py, test_manager.py and test_cli.py fixtures
# ==========
@pytest.fixture()
def valid_csv_path():
    return ["data/employees1.csv"]


@pytest.fixture()
def csv_file_with_header():
    try:
        csv_path = "data/employees1.csv"
        csv_file = open(csv_path, mode="r", newline="")
        yield csv_file
    finally:
        csv_file.close()


@pytest.fixture()
def csv_file_with_no_header():
    try:
        csv_path = "data/no_header_row.csv"
        csv_file = open(csv_path, mode="r", newline="")
        yield csv_file
    finally:
        csv_file.close()
# ==========


# ==========
# test_factory.py and test_manager.py fixtures
# ==========
@pytest.fixture()
def valid_report_type():
    return "performance"


@pytest.fixture()
def invalid_report_type():
    return "invalid_report_type"


@pytest.fixture()
def test_report_table():
    headers = ["position", "average_performance"]
    tabular_data = [
        ["Mobile Developer", 4.6],
        ["Backend Developer", 4.85],
        ["DevOps Engineer", 4.7],
        ["Frontend Developer", 4.6],
        ["Data Engineer", 4.7],
        ["QA Engineer", 4.5],
        ["Data Scientist", 4.7],
    ]
    tabular_data.sort(key=lambda x: x[1], reverse=True)

    report_table = tabulate(
        tabular_data,
        headers=headers,
        floatfmt=".2f",
        showindex=range(1, len(tabular_data) + 1),
    )

    return report_table
# =========
