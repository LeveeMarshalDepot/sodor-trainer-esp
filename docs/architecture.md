# Architecture

```
sodor_trainer/
├── bootstrap.py        entry point (admin check + attach + HUD)
├── core/               config, injector, offsets
├── esp/                entity scanner + box renderer
├── godmode/            health / resource lock thread
├── teleport/           waypoints + warp writer
├── overlay/            tkinter HUD
└── utils/              hotkeys + logging
```

Data flows: `bootstrap` → `Injector.attach` → `SodorHud` drives
`EntityScanner` (read) and `HealthLock` / `Warp` (write). All offsets live in
`core/offsets.py` and are versioned per game build.