# Security Policy

## Scope
`sodor-trainer-esp` attaches to the local process `WondersOfSodor.exe` via
`OpenProcess`. It does not phone home, does not modify game files on disk,
and does not interact with any anti-cheat or online service.

## Reporting
If you find a vulnerability (e.g. a code path that could be triggered
remotely, or a config loader that executes untrusted input), open a private
security advisory on GitHub or email `maintainer@sodor-trainer.dev`.

Please do **not** publish working exploits before a fix ships.

## Use at your own risk
Using a trainer with an account-bound game may violate the game's ToS.
The authors are not responsible for bans, save corruption, or bricked
saves. Back up `%LOCALAPPDATA%\WondersOfSodor\Saves` before use.