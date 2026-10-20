"""Helper: dumps candidate float offsets for the current game build."""
from sodor_trainer.core.injector import Injector
from sodor_trainer.core import offsets


def main() -> None:
    inj = Injector("WondersOfSodor.exe")
    if not inj.attach():
        raise SystemExit("attach failed")
    for name in dir(offsets):
        if name.isupper():
            print(f"{name:16s} 0x{getattr(offsets, name):08X}")


if __name__ == "__main__":
    main()