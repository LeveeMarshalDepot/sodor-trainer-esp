"""Lightweight tkinter overlay used while the game runs in windowed mode."""
import tkinter as tk
import threading
import time

from sodor_trainer.core.config import TrainerConfig
from sodor_trainer.core.injector import Injector
from sodor_trainer.esp.entity_scanner import EntityScanner
from sodor_trainer.esp.box_renderer import BoxRenderer
from sodor_trainer.godmode.health_lock import HealthLock
from sodor_trainer.teleport.warp import Warp


class SodorHud:
    def __init__(self, inj: Injector, cfg: TrainerConfig) -> None:
        self.inj = inj
        self.cfg = cfg
        self.scanner = EntityScanner(inj)
        self.renderer = BoxRenderer()
        self.health = HealthLock(inj)
        self.warp = Warp(inj)

    def run(self) -> None:
        self.health.start()
        root = tk.Tk()
        root.title("Sodor Trainer — ESP / Godmode / Warp")
        root.attributes("-topmost", True)
        root.geometry("320x420+40+40")

        esp_var = tk.BooleanVar(value=self.cfg.esp_enabled)
        god_var = tk.BooleanVar(value=False)

        def toggle_god() -> None:
            self.health.enabled = god_var.get()

        tk.Checkbutton(root, text="ESP boxes", variable=esp_var).pack(anchor="w")
        tk.Checkbutton(root, text="Godmode (HP/coal/water)", variable=god_var,
                       command=toggle_god).pack(anchor="w")
        for key in ("tidmouth_sheds", "knapford_station", "gordon_hill"):
            tk.Button(root, text=f"Warp: {key}",
                      command=lambda k=key: self.warp.to_waypoint(k)).pack(fill="x")

        log = tk.Text(root, height=8)
        log.pack(fill="both", expand=True)

        def refresh() -> None:
            if esp_var.get():
                ents = self.scanner.scan()
                log.delete("1.0", "end")
                for e in ents[:12]:
                    log.insert("end", f"{e.name} @ ({e.x:.0f},{e.z:.0f}) hp={e.health:.0f}\n")
            root.after(250, refresh)

        refresh()
        try:
            root.mainloop()
        finally:
            self.health.stop()