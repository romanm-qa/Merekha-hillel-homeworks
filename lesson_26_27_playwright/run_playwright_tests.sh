#!/usr/bin/env bash

# Запуск Playwright UI-тестов с автоматическим сохранением скриншотов и трассировок при провале.

# Скрипт работает из любой директории — он сам определяет свой путь и переходит в корень репозитория.

# Определяем абсолютный путь к директории скрипта и переходим в корень репозитория

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT" || exit 1

pytest lesson_26_27_playwright/tests/ \
  --screenshot=only-on-failure \
  --tracing=retain-on-failure \
  --output=lesson_26_27_playwright/reports \
  "$@"
