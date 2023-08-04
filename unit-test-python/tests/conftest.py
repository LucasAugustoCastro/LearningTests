from _pytest.monkeypatch import MonkeyPatch 
import pytest
@pytest.fixture(scope='session')
def monkeysession(request):
    """
    Fixture that provides a MonkeyPatch object to patch
    the flask.current_app object.
    """
    monkeypatch = MonkeyPatch()
    yield monkeypatch
    monkeypatch.undo()