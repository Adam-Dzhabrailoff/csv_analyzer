from app.manager import ReportManager


def test_generate_report(
    valid_csv_path,
    valid_report_type,
    test_report_table,
):
    report_manager = ReportManager()
    report_table = report_manager.generate_report(
        valid_csv_path,
        valid_report_type
    )
    
    assert report_table == test_report_table
