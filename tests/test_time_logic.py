from src.stopwatch import Stopwatch

def test_stopwatch_reset():
    sw = Stopwatch()
    sw.start()
    sw.reset()
    assert sw.get_time() == 0
