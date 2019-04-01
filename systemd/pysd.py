""" Python Binding for Systemd, uses the output from native systemctl commands,
providing a programmable way of interacting with services, listing, verifying,
starting, stopping, enabling and disabling services.
"""
import json
import re
import subprocess


__author__ = "ivanleoncz"
__version__ = "1.0"


class Systemd():
    """ Main class for Systemd tasks. """

    def active_services(self, as_json=False):
        """ Verifies all activated services.

            as_json : boolean
                Activates JSON format for returning data.

            Returns:
                List of active services.
        """
        assert as_json is True or as_json is False, 'as_json => False or True'
        cmd = "systemctl list-units --type=service | grep 'active running'"
        output = subprocess.check_output(cmd, shell=True)
        output = output.decode('utf-8')
        output = re.sub(' +', ' ', output).split('\n')
        output = [s for s in output if s is not '']
        formatted_output = list()
        for srv in output:
            cols = srv.split(' ')
            service = {cols[1]: ' '.join(cols[4:])}
            formatted_output.append(service)
        if as_json:
            return json.dumps(formatted_output, indent=4)
        else:
            return formatted_output
        

    def enabled_services(self, as_json=False):
        """ Verifies all enabled services.

            as_json : boolean
                Activates JSON format for returning data.

            Returns:
                List of enabled services.
        """
        assert as_json is True or as_json is False, 'as_json => False or True'
        cmd = "systemctl list-unit-files --type=service | grep enabled"
        output = subprocess.check_output(cmd, shell=True)
        output = output.decode('utf-8')
        output = re.sub(' +', ' ', output).split('\n')
        output = [s for s in output if s is not '']
        formatted_output = [srv.split(' ')[0] for srv in output]
        if as_json:
            return json.dumps(formatted_output, indent=4)
        else:
            return formatted_output


    def is_enabled(self, service=None):
        """ Verifies if a service is enabled.

            service : string
                Service described as Systemd model (ex.: cron.service).

            Returns:
                True or False.
        """
        assert service != None, 'must provide a valid service (ex. cron.service)'
        cmd = "systemctl status {} | grep enabled".format(service)
        output = subprocess.check_output(cmd, shell=True)
        if "enabled" in str(output):
            return True
        else:
            return False


    def is_active(self, service=None):
        """ Verifies if a service is active.

            service : string
                Service described as Systemd model (ex.: cron.service).

            Returns:
                True or False.
        """
        assert service != None, 'must provide a valid service (ex. cron.service)'
        cmd = "systemctl status {} | grep active".format(service)
        output = subprocess.check_output(cmd, shell=True)
        if "active" in str(output):
            return True
        else:
            return False


