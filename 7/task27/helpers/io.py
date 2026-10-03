import logging


def logger(name="app", logfile="app.log", level=logging.INFO):
    """
    Создаёт и возвращает настроенный логгер.
    Вывод идёт в файл и в консоль.
    """
    log = logging.getLogger(name)
    log.setLevel(level)

    # Защита от дублирования обработчиков
    if not log.handlers:
        fh = logging.FileHandler(logfile, encoding="utf-8")
        ch = logging.StreamHandler()

        fmt = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)

        log.addHandler(fh)
        log.addHandler(ch)

    return log
