from app.cli import parse_args
from app.manager import ReportManager


def main():
    try:
        args = parse_args()
        report_manager = ReportManager()
        report = report_manager.generate_report(args.file, args.report)
        print(report)
    except Exception as exception:
        print(f"ERROR: {exception}")


if __name__ == "__main__":
    main()
