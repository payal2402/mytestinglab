
from pages.DragDropPage import DragDrop
import pytest

@pytest.mark.sanity
def test_drag(driver):
    drag = DragDrop(driver)
    drag.drag_n_drop()
    assert True
