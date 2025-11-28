class EmptyFileCSVParserError(Exception):
    def __init__(self, csv_path: str):
        self.message = f"The csv file is empty: {csv_path}"
        super().__init__(self.message)


class HeaderRowNotFoundCSVParserError(Exception):
    def __init__(self, csv_path: str):
        self.message = f"Could not find the header row in" \
                        f" the csv file: {csv_path}"
        super().__init__(self.message)


class EmptyHeaderCSVParserError(Exception):
    def __init__(self, csv_path: str):
        self.message = f"Found an empty header in the csv file: {csv_path}"
        super().__init__(self.message)


class InvalidRowCSVParserError(Exception):
    def __init__(self, csv_path: str):
        self.message = f"The number of values in every row must match" \
                        f" the number of headers: {csv_path}"
        super().__init__(self.message)


class EmptyValueCSVParserError(Exception):
    def __init__(self, csv_path: str, csv_header):
        self.message = f"Found an empty value for '{csv_header}' header in" \
                        f" the csv file: {csv_path}"
        super().__init__(self.message)
