import pytest

from app.factory import ReportStrategyFactory
from app.report_strategies import AbstractReportStrategy


def test_create(valid_report_type: str):
    strategy = ReportStrategyFactory.create(valid_report_type)

    assert isinstance(strategy, AbstractReportStrategy)


def test_invalid_report_type_exception(invalid_report_type: str):
    with pytest.raises(ValueError):
        ReportStrategyFactory.create(invalid_report_type)
