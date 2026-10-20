import ctypes


VK_MAP = {
    "F7": 0x76,
    "F8": 0x77,
    "F9": 0x78,
    "F10": 0x79,
    "INSERT": 0x2D,
    "DELETE": 0x2E,
}


def is_pressed(name: str) -> bool:
    vk = VK_MAP.get(name.upper())
    if vk is None:
        return False
    return ctypes.windll.user32.GetAsyncKeyState(vk) & 0x8000 != 0