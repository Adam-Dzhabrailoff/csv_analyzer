import argparse


# Checks if a file is a csv file.
def _is_csv_file(file_path: str) -> str:
    if not file_path.endswith(".csv"):
        raise argparse.ArgumentTypeError(
            f"Invalid file extension for '{file_path}'. Expected '.csv'"
        )

    return file_path


# Parses command-line arguments
def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        type=_is_csv_file,
        nargs="+",
        required=True,
    )

    parser.add_argument(
        "--report",
        type=str,
        choices=["performance"],
        required=True,
    )

    return parser.parse_args()
