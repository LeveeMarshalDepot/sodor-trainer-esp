import threading
import time

from sodor_trainer.core import offsets
from sodor_trainer.core.injector import Injector


class HealthLock:
    """Freezes player HP and resource gauges at max while toggled on."""

    def __init__(self, inj: Injector, tick: float = 0.05) -> None:
        self.inj = inj
        self.tick = tick
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self.enabled = False

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=1.0)

    def _loop(self) -> None:
        while not self._stop.is_set():
            if self.enabled:
                self.inj.write_float(offsets.HEALTH, 100.0)
                self.inj.write_float(offsets.COAL, 9999.0)
                self.inj.write_float(offsets.WATER, 9999.0)
            time.sleep(self.tick)