import os
import signal
import subprocess
import sys
import time


def kill_nudge(interval=0.4):
    while True:
        try:
            output = subprocess.check_output(
                ["pgrep", "-x", "Nudge"], text=True
            ).strip()

            pids = output.splitlines()
            for pid_str in pids:
                pid = int(pid_str)
                try:
                    os.kill(pid, signal.SIGTERM)
                    time.sleep(0.1)
                    os.kill(pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                except PermissionError:
                    pass

        except subprocess.CalledProcessError:
            pass
        except Exception:
            pass

        time.sleep(interval)


if __name__ == "__main__":
    try:
        kill_nudge()
    except KeyboardInterrupt:
        sys.exit(0)
