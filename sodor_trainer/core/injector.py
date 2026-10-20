import ctypes
from ctypes import wintypes

PROCESS_ALL_ACCESS = 0x1F0FFF
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)


class Injector:
    """Attaches to the Wonders of Sodor process and exposes r/w handles."""

    def __init__(self, process: str) -> None:
        self.process = process
        self.pid: int | None = None
        self.handle: int | None = None

    def attach(self) -> bool:
        pid = self._find_pid(self.process)
        if pid is None:
            return False
        self.pid = pid
        self.handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        return bool(self.handle)

    @staticmethod
    def _find_pid(name: str) -> int | None:
        import subprocess
        try:
            out = subprocess.check_output(
                ["tasklist", "/FI", f"IMAGENAME eq {name}", "/FO", "CSV", "/NH"],
                text=True, creationflags=0x08000000,
            )
        except Exception:
            return None
        parts = out.strip().split(",")
        if len(parts) >= 2 and parts[0].strip('"').lower() == name.lower():
            return int(parts[1].strip('"'))
        return None

    def read_float(self, address: int) -> float:
        buf = ctypes.c_float()
        kernel32.ReadProcessMemory(self.handle, wintypes.LPCVOID(address),
                                   ctypes.byref(buf), 4, None)
        return buf.value

    def write_float(self, address: int, value: float) -> None:
        buf = ctypes.c_float(value)
        kernel32.WriteProcessMemory(self.handle, wintypes.LPVOID(address),
                                    ctypes.byref(buf), 4, None)