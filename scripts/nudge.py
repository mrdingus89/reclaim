import os
import signal
import subprocess
import sys
import time

def kill_nudge(interval=1.0):
    while True:
        try:
            output = subprocess.check_output(
                ["pgrep", "-x", "Nudge"], text=True
            ).strip()

            pids = output.splitlines()
            for pid_str in pids:
                pid = int(pid_str)
                print(f"NUDGE DETECTED! Terminating PID: {pid}", flush=True)

                try:
                    os.kill(pid, signal.SIGTERM)
                    time.sleep(0.1)
                    
                    os.kill(pid, signal.SIGKILL)
                except ProcessLookupError:
                    print(f"PID {pid} successfully eliminated.", flush=True)
                except PermissionError:
                    print(f"Permission denied killing PID {pid}. Daemon must run as root.", flush=True)

        except subprocess.CalledProcessError:
       
            pass
        except Exception as e:
            print(f"Unexpected error: {e}", flush=True)

        time.sleep(interval)


if __name__ == "__main__":
    try:
        kill_nudge()
    except KeyboardInterrupt:
        sys.exit(0)
