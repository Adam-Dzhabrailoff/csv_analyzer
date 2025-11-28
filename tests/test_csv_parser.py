from typing import TextIO

import pytest

from app.csv_parser import CSVParser
from app.exceptions import (
    EmptyFileCSVParserError,
    HeaderRowNotFoundCSVParserError,
    EmptyHeaderCSVParserError,
    InvalidRowCSVParserError,
    EmptyValueCSVParserError,
)


@pytest.mark.parametrize("csv_path", ["data/empty.csv"])
def test__is_csv_file_empty(csv_path: str):
    assert CSVParser._is_csv_file_empty(csv_path) is True


@pytest.mark.parametrize("invalid_csv_path", ["data/employees1.csv"])
def test__is_csv_file_empty_fail(invalid_csv_path: str):
    assert CSVParser._is_csv_file_empty(invalid_csv_path) is False




def test__is_csv_header_row_present(csv_file_with_header: TextIO):
    assert CSVParser._is_csv_header_row_present(csv_file_with_header) is True


def test__is_csv_header_row_present_fail(csv_file_with_no_header: TextIO):
    assert CSVParser._is_csv_header_row_present(csv_file_with_no_header) is False




@pytest.mark.parametrize("csv_header", ["performance"])
def test__is_csv_header_not_empty(csv_header: str):
    assert CSVParser._is_csv_header_not_empty(csv_header) is True


@pytest.mark.parametrize("invalid_csv_header", [" "])
def test__is_csv_header_not_empty_fail(invalid_csv_header: str):
    assert CSVParser._is_csv_header_not_empty(invalid_csv_header) is False




@pytest.mark.parametrize(
        "csv_headers, valid_csv_row",
        [
            (
                [
                    "name",
                    "position",
                    "completed_tasks",
                    "performance",
                    "skills",
                    "team",
                    "experience_years",
                ],
                {
                    "name": "David Chen",
                    "position": "Mobile Developer",
                    "completed_tasks": "36",
                    "performance": "4.6",
                    "skills": "Swift, Kotlin, React Native, iOS",
                    "team": "Mobile Team",
                    "experience_years": "3",
                },
            )
        ]
)
def test__is_csv_row_valid(
        csv_headers: list[str],
        valid_csv_row: dict[str, str]
):
    assert CSVParser._is_csv_row_valid(csv_headers, valid_csv_row) is True


@pytest.mark.parametrize(
        "csv_headers, invalid_csv_row",
        [
            (
                [
                    "name",
                    "position",
                    "completed_tasks",
                    "performance",
                    "skills",
                    "team",
                    "experience_years",
                ],
                {
                    "name": "David Chen",
                    "position": "Mobile Developer",
                    "completed_tasks": "36",
                    "performance": "4.6",
                    "skills": "Swift, Kotlin, React Native, iOS",
                    "team": "Mobile Team",
                },
            )
        ]
)
def test__is_csv_row_valid_fail(
        csv_headers: list[str],
        invalid_csv_row: dict[str, str]
):
    assert CSVParser._is_csv_row_valid(csv_headers, invalid_csv_row) is False




@pytest.mark.parametrize("valid_csv_value", ["Backend Developer"])
def test__is_csv_value_not_empty(valid_csv_value: str):
    assert CSVParser._is_csv_value_not_empty(valid_csv_value) is True


@pytest.mark.parametrize("invalid_csv_value", [" "])
def test__is_csv_value_not_empty_fail(invalid_csv_value: str):
    assert CSVParser._is_csv_value_not_empty(invalid_csv_value) is False




@pytest.mark.parametrize(
        "csv_header, csv_value, type", [
            ("name", "David Chen", str),
            ("position", "Mobile Developer", str),
            ("completed_tasks", "36", int),
            ("performance", "4.6", float),
            ("skills", "Swift, Kotlin, React Native, iOS", list),
            ("team", "Mobile Team", str),
            ("experience_years", "3", int),
        ]
)
def test__cast_csv_value_to_type(
        csv_header: str,
        csv_value: str,
        type: object,
):
    parsed_value = CSVParser._cast_csv_value_to_type(csv_header, csv_value)

    if isinstance(type, list):
        assert all(isinstance(sub_value, str) for sub_value in parsed_value) is True

    assert isinstance(parsed_value, type) is True




@pytest.mark.parametrize("valid_csv_paths",
        [
            ["data/employees1.csv"],
            ["data/employees1.csv", "data/employees2.csv"],
        ]
)
def test_parse_csv_by_row(valid_csv_paths):
    list(CSVParser.parse_csv_by_row(valid_csv_paths))


@pytest.mark.parametrize(
        "invalid_csv_files, raised_parser_exception",
        [
            (
                ["data/empty.csv"],
                EmptyFileCSVParserError,
            ),
            (
                ["data/no_header_row.csv"],
                HeaderRowNotFoundCSVParserError,
            ),
            (
                ["data/empty_header.csv"],
                EmptyHeaderCSVParserError,
            ),
            (
                ["data/invalid_row.csv"],
                InvalidRowCSVParserError,
            ),
            (
                ["data/empty_value.csv"],
                EmptyValueCSVParserError,
            ),
        ]
)
def test_parse_csv_by_row_exceptions(invalid_csv_files, raised_parser_exception):
    with pytest.raises(raised_parser_exception):
        list(CSVParser.parse_csv_by_row(invalid_csv_files))
