import sys

from app.cli import (
    _is_csv_file,
    parse_args,
)


def test__is_csv_file(valid_csv_path):
    assert _is_csv_file(valid_csv_path[0]) == valid_csv_path[0]


def test_parse_args(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["test_cli", "--file", "csv_file.csv", "--report", "performance"]
    )

    args = parse_args()

    assert args.file == ["csv_file.csv"]
    assert args.report == "performance"
