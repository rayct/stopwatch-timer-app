import pytest
from stopwatch_timer_app.stopwatch import Stopwatch
from unittest.mock import patch

@pytest.fixture
def stopwatch():
    """Provides a fresh Stopwatch instance and a patched time.time function."""
    with patch("time.time") as mock_time:
        sw = Stopwatch()
        yield sw, mock_time  # returns both the stopwatch and the mock_time object

def test_stopwatch_start_pause(stopwatch):
    sw, mock_time = stopwatch
    mock_time.return_value = 1000
    sw.start()
    mock_time.return_value = 1001
    sw.pause()
    assert sw.get_time() == 1

def test_stopwatch_resume(stopwatch):
    sw, mock_time = stopwatch
    mock_time.return_value = 2000
    sw.start()
    mock_time.return_value = 2002
    sw.pause()
    mock_time.return_value = 2003
    sw.start()  # resume
    mock_time.return_value = 2005
    sw.pause()
    assert sw.get_time() == 4

def test_stopwatch_reset(stopwatch):
    sw, mock_time = stopwatch
    mock_time.return_value = 3000
    sw.start()
    mock_time.return_value = 3002
    sw.pause()
    sw.reset()
    assert sw.get_time() == 0

def test_stopwatch_multiple_starts(stopwatch):
    sw, mock_time = stopwatch
    mock_time.return_value = 4000
    sw.start()
    mock_time.return_value = 4001
    sw.start()
    mock_time.return_value = 4002
    sw.pause()
    assert sw.get_time() == 2

def test_stopwatch_lap_functionality(stopwatch):
    sw, mock_time = stopwatch
    mock_time.return_value = 5000
    sw.start()
    mock_time.return_value = 5002
    sw.lap()
    mock_time.return_value = 5005
    sw.lap()
    mock_time.return_value = 5006
    sw.pause()
    laps = sw.get_laps()
    assert laps == [2, 3]
    assert sw.get_time() == 6

def test_stopwatch_pause_without_start(stopwatch):
    sw, _ = stopwatch
    sw.pause()
    assert sw.get_time() == 0

def test_stopwatch_multiple_resets(stopwatch):
    sw, mock_time = stopwatch
    mock_time.return_value = 6000
    sw.start()
    mock_time.return_value = 6002
    sw.pause()
    sw.reset()
    sw.reset()
    assert sw.get_time() == 0

def test_stopwatch_laps_with_pause_resume(stopwatch):
    sw, mock_time = stopwatch
    mock_time.return_value = 7000
    sw.start()
    mock_time.return_value = 7002
    sw.lap()
    mock_time.return_value = 7003
    sw.pause()
    mock_time.return_value = 7005
    sw.start()
    mock_time.return_value = 7008
    sw.lap()
    mock_time.return_value = 7009
    sw.pause()
    laps = sw.get_laps()
    assert laps == [2, 4]
    assert sw.get_time() == 7
