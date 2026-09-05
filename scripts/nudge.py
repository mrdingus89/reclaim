import os
import signal
import subprocess
import time


def kill_nudge(interval=0.2):
    try:
        while True:
            try:
                output = subprocess.check_output(
                    ["pgrep", "-x", "Nudge"], text=True
                ).strip()

                pids = output.splitlines()
                for pid_str in pids:
                    pid = int(pid_str)
                    print(f"NUDGE IS RUNNING!! PID: {pid}")

                    try:
                        os.kill(pid, signal.SIGTERM)
                        print(f"Terminated PID: {pid} (begone!)")
                    except ProcessLookupError:
                        print(f"PID {pid} already killed.")
                    except PermissionError:
                        print(
                            f"Permission denied run sudo"
                        )

            except subprocess.CalledProcessError:
                print("Nudge is not running")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nBeware of annoying update requests...")


if __name__ == "__main__":
    kill_nudge()
