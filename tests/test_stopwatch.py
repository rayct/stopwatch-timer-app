from stopwatch_timer_app.stopwatch import Stopwatch
import time


def test_stopwatch_start_pause():

    sw = Stopwatch()

    sw.start()
    time.sleep(1)
    sw.pause()

    assert sw.get_time() >= 1
