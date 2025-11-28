import os
from typing import (
    Iterator,
    TextIO,
)

from csv import (
    DictReader,
    Sniffer,
)

from app.exceptions import (
    EmptyFileCSVParserError,
    HeaderRowNotFoundCSVParserError,
    EmptyHeaderCSVParserError,
    InvalidRowCSVParserError,
    EmptyValueCSVParserError,
)

# A csv parser
class CSVParser:
    _header_type_map = {
        "name": str,
        "position": str,
        "completed_tasks": int,
        "performance": float,
        "skills": lambda x: x.split(","),
        "team": str,
        "experience_years": int,
    }


    # Checks if a file is empty
    def _is_csv_file_empty(csv_path: str) -> bool:
        if not os.path.getsize(csv_path):
            return True
        
        return False


    # Checks if a csv file header row is present in a file
    def _is_csv_header_row_present(
            csv_file: TextIO,
    ) -> bool:
        sniffer = Sniffer()
        has_header_row = sniffer.has_header(csv_file.read(1024))
        csv_file.seek(0)

        return has_header_row


    # Checks if a csv file header is not empty
    def _is_csv_header_not_empty(
        csv_header: str,
    ) -> bool:
        return bool(csv_header.strip())


    # Checks if values in a csv file row is matching the number of headers
    def _is_csv_row_valid(
        csv_row: list[dict[str, str]],
        csv_headers: list[str],
    ) -> bool:
        return len(csv_row) == len(csv_headers)


    # Checks if a value in the csf file row is not empty
    def _is_csv_value_not_empty(
        csv_value: str,
    ) -> bool:
        return bool(csv_value.strip())


    # Converts a value to a type based on the header it belongs to
    @classmethod
    def _cast_csv_value_to_type(
            cls,
            csv_header: str,
            csv_value: str,
            csv_path: str = None
    ):
        try:
            return cls._header_type_map[csv_header](csv_value)
        except:
            raise ValueError(
                f"Invalid value for '{csv_header}' in {csv_path}: '{csv_value}'"
            )


    # A generator that returns a parsed row from a csv file
    @classmethod
    def parse_csv_by_row(
            cls,
            csv_paths: list[str],
    ) -> Iterator[dict[str, str]]:
        for csv_path in csv_paths:
            if cls._is_csv_file_empty(csv_path):
                raise EmptyFileCSVParserError(csv_path)

            with open(csv_path, mode="r", newline="") as csv_file:
                reader = DictReader(csv_file)

                if not cls._is_csv_header_row_present(csv_file):
                    raise HeaderRowNotFoundCSVParserError(csv_path)

                csv_headers = reader.fieldnames
                for csv_header in csv_headers:
                    if not cls._is_csv_header_not_empty(csv_header):
                        raise EmptyHeaderCSVParserError(csv_path)

                for csv_row in reader:
                    if not cls._is_csv_row_valid(csv_row, csv_headers):
                        raise InvalidRowCSVParserError(csv_path)

                    parsed_row = {}
                    for csv_header, csv_value in csv_row.items():
                        if not cls._is_csv_value_not_empty(csv_value):
                            raise EmptyValueCSVParserError(csv_path, csv_header)
                        
                        parsed_value = cls._cast_csv_value_to_type(
                            csv_header,
                            csv_value,
                            csv_path
                        )
                        parsed_row[csv_header] = parsed_value

                    yield parsed_row
