#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """Function to generates a .tgz archive """
    try:
        date_of_file = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        name_of_file = "versions/web_static_{}.tgz".format(date_of_file)
        local("tar -cvzf {} web_static".format(name_of_file))
        return name_of_file
    except Exception:
        return None
