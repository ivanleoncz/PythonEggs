import logging


def log_config():
    log_file = "/tmp/app.log"
    conf = logging.getLogger(__name__)
    conf.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]\t%(message)s')
    handler.setFormatter(formatter)
    conf.addHandler(handler)
    return conf

log = log_config()

program_start = "Program has started."
program_end = "Program has ended."

log.info("{0}".format(program_start))
print("Running actions!")
log.error("{0}".format(program_end))
