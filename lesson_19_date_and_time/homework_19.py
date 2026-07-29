import logging
from datetime import datetime

logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(levelname)s: %(message)s",
    filemode="w",
)

KEY = "TSTFEED0300|7E3E|0400"


def analyze_heartbeat(log_file_path: str) -> str:
    filtered_log = []

    with open(log_file_path, "r") as log_file:
        for line in log_file:
            if KEY in line:
                filtered_log.append(line)

    heartbeat_times = []

    for line in filtered_log:
        timestamp_position = line.find("Timestamp ")
        time_string = line[
            timestamp_position + len("Timestamp "):
            timestamp_position + len("Timestamp ") + 8
        ]

        heartbeat_time = datetime.strptime(time_string, "%H:%M:%S")
        heartbeat_times.append(heartbeat_time)

    for index in range(len(heartbeat_times) - 1):
        current_time = heartbeat_times[index]
        next_time = heartbeat_times[index + 1]

        heartbeat_difference = current_time - next_time
        heartbeat_seconds = heartbeat_difference.total_seconds()

        if 31 < heartbeat_seconds < 33:
            logging.warning(
                f"Heartbeat at {current_time.strftime('%H:%M:%S')} "
                f"was delayed by {heartbeat_seconds:.0f} seconds"
            )
        elif heartbeat_seconds >= 33:
            logging.error(
                f"Heartbeat at {current_time.strftime('%H:%M:%S')} "
                f"was delayed by {heartbeat_seconds:.0f} seconds"
            )

    return "hb_test.log"


analyze_heartbeat("hblog.txt")
