import ctypes
import sys
from pathlib import Path

from sodor_trainer.core.config import load_config
from sodor_trainer.core.injector import Injector
from sodor_trainer.overlay.hud import SodorHud


def ensure_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    cfg = load_config(Path("config/trainer.toml"))
    if cfg.require_admin and not ensure_admin():
        print("[!] run as administrator to attach to WondersOfSodor.exe")
        return 1

    inj = Injector(process=cfg.target_process)
    if not inj.attach():
        print(f"[!] could not attach to {cfg.target_process}")
        return 2

    hud = SodorHud(inj, cfg)
    hud.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())