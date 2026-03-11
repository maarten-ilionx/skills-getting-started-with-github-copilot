from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture
def client():
    """Provide a test client for API requests."""
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activity state before every test."""
    app_module.activities.clear()
    app_module.activities.update(deepcopy(INITIAL_ACTIVITIES))
    yield
