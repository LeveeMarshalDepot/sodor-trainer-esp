# Contributing to sodor-trainer-esp

Thanks for helping improve the Thomas & Friends: Wonders of Sodor Trainer!

## Ground rules
- This project is for **educational and offline single-player modding only**.
- Do not submit offsets for online / multiplayer builds.
- Keep PRs focused: one feature (ESP, godmode, warp, overlay) per PR.

## Local setup
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m sodor_trainer.bootstrap
```

## Updating offsets
When Sodor ships a patch, run `scripts/dump_offsets.py` and update
`sodor_trainer/core/offsets.py` in a dedicated PR titled
`offsets: <game build date>`.

## Code style
- Python 3.11+, type hints on public functions.
- Keep the `sodor_trainer/` package tree intact — no stray scripts.