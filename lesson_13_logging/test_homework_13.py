from pathlib import Path
from homework_13 import log_event

LOG_FILE = Path(__file__).parent / "login_system.log"


def test_log_event_success():
    LOG_FILE.write_text("")

    log_event("user1", "success")

    with open(LOG_FILE, "r") as file:
        log_text = file.read()

    assert "Username: user1" in log_text
    assert "Status: success" in log_text


def test_log_event_expired():
    LOG_FILE.write_text("")

    log_event("user2", "expired")

    with open(LOG_FILE, "r") as file:
        log_text = file.read()

    assert "Username: user2" in log_text
    assert "Status: expired" in log_text


def test_log_event_failed():
    LOG_FILE.write_text("")

    log_event("user3", "failed")

    with open(LOG_FILE, "r") as file:
        log_text = file.read()

    assert "Username: user3" in log_text
    assert "Status: failed" in log_text
