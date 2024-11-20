import json
import logging
from scheduler import start_backup_scheduler
from pathlib import Path

def setup_logging(log_level):
    """
    Настраивает глобальное логирование для проекта.

    log_level -- Уровень логирования в текстовом формате ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").
    """
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Некорректный уровень логирования: {log_level}")
    
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def main():
    config_path = Path("config.json")
    if not config_path.is_file():
        raise FileNotFoundError("Файл config.json не найден. Убедитесь, что он существует.")
    
    with config_path.open("r", encoding="utf-8") as file:
        config = json.load(file)
    
    # Настройка логирования
    log_level = config.get("log_level", "INFO")
    setup_logging(log_level)

    logging.info("Запуск программы.")
    
    # Запуск планировщика бэкапов
    start_backup_scheduler(config)

if __name__ == "__main__":
    main()
