# Offset hunting cheatsheet

1. Launch Sodor in windowed mode.
2. Attach with `python scripts/dump_offsets.py` to verify the base.
3. Use Cheat Engine to scan for `float` coal / water values, then pointer-scan
   back to `PLAYER_BASE`.
4. Entity list is a flat array at `ENTITY_LIST` with stride `0x180`
   (see `core/offsets.py`). Dump 64 slots and eyeball for name strings.
5. Commit offset bumps as `offsets: <build date>` — never mix with feature PRs.