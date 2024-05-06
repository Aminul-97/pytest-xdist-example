import pytest
import time

## Initializing 10 tests with intentional delay
@pytest.mark.parametrize("no_of_test", range(10))
def test_get_cat_fact_no_mock(no_of_test):
    """
    Running test with 1s delay.
    """
    time.sleep(1)



