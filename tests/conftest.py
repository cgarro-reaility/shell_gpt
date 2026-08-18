import os

import pytest


@pytest.fixture(autouse=True)
def mock_os_name(monkeypatch):
    monkeypatch.setattr(os, "name", "test")

from unittest.mock import patch

@pytest.fixture(autouse=True)
def mock_memory():
    with patch("sgpt.memory.get_relevant_memories", return_value=[]) as mock:
        yield mock
