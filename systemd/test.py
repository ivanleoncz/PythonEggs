import subprocess


class status():
    """ Checks the status of a Systemd Unit (service) """

    def __init__(self, service):
        self.service = service

    def is_enabled(self):
        output = subprocess.check_output("systemctl status cron.service | grep enabled", shell=True)
        if "enabled" in str(output):
            return True
        else:
            return False


stat = status("cron.service")
print(stat.is_enabled())
