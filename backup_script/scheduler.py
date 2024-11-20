"""
Модуль для управления периодическим выполнением бэкапов.

Использует фоновые потоки для выполнения бэкапов через заданный интервал времени.
"""

import time
from threading import Thread
from backup import perform_backup
import logging

def start_backup_scheduler(config):
    """
    Запускает планировщик бэкапов, выполняя их с заданной периодичностью.

    config -- Словарь с конфигурацией, содержащий:
        directories_to_backup (list) -- Список директорий для бэкапа.
        backup_destination (str) -- Путь к директории для сохранения бэкапов.
        backup_period (int) -- Интервал в секундах между бэкапами.
        
    Фоновый поток реализован при помощи ChatGPT 4o mini
    """
    source_dirs = config.get("directories_to_backup", [])
    destination_dir = config.get("backup_destination")
    period = config.get("backup_period", 3600)

    if not source_dirs or not destination_dir:
        raise ValueError("Не указаны исходные директории или директория назначения в конфигурации.")
    
    logging.info(f"Запуск планировщика бэкапов с периодом {period} секунд.")
    
    # Фоновый поток для планировщика
    def scheduler():
        while True:
            logging.info("Запуск процесса бэкапа.")
            perform_backup(source_dirs, destination_dir)
            logging.info(f"Ожидание {period} секунд до следующего бэкапа.")
            time.sleep(period)
    
    thread = Thread(target=scheduler, daemon=True)
    thread.start()

    try:
        while True:
            time.sleep(1)  # Главный поток ожидает, чтобы фоновый продолжал работать.
    except KeyboardInterrupt:
        logging.info("Остановка планировщика...")
