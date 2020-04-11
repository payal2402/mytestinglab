
import pytest

@pytest.mark.sanity
@pytest.mark.registration
@pytest.mark.xfail
def test_dummy():
    assert False