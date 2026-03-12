from stopwatch_timer_app.stopwatch import Stopwatch
from unittest.mock import patch

def test_stopwatch_start_pause():
    sw = Stopwatch()
    with patch("time.time") as mock_time:
        mock_time.return_value = 1000
        sw.start()
        mock_time.return_value = 1001  # simulate 1 second elapsed
        sw.pause()
    
    assert sw.get_time() == 1

def test_stopwatch_resume():
    sw = Stopwatch()
    with patch("time.time") as mock_time:
        mock_time.return_value = 2000
        sw.start()
        mock_time.return_value = 2002
        sw.pause()
        mock_time.return_value = 2003
        sw.start()  # resume
        mock_time.return_value = 2005
        sw.pause()

    assert sw.get_time() == 4  # 2 + 2 seconds

def test_stopwatch_reset():
    sw = Stopwatch()
    with patch("time.time") as mock_time:
        mock_time.return_value = 3000
        sw.start()
        mock_time.return_value = 3002
        sw.pause()
        sw.reset()
    
    assert sw.get_time() == 0

def test_stopwatch_multiple_starts():
    sw = Stopwatch()
    with patch("time.time") as mock_time:
        mock_time.return_value = 4000
        sw.start()
        mock_time.return_value = 4001
        sw.start()  # starting while running should have no effect
        mock_time.return_value = 4002
        sw.pause()
    
    assert sw.get_time() == 2
