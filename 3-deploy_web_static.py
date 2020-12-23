#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers, using the
function do_deploy"""
from fabric.api import put, run, env
from os.path import exists
from datetime import datetime

env.hosts = ["35.185.80.75", "35.231.48.2"]


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


def do_deploy(archive_path):
    """Function to distributes an archive to your web servers"""
    if exists(archive_path) is True:
        try:
            file_name = archive_path.split("/")[-1]
            file_name_without_ext = file_name.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, "/tmp/")
            run("mkdir -p {}{}/".format(path, file_name_without_ext))
            run("tar -xzf /tmp/{} -C {}{}/".format(file_name, path,
                                                   file_name_without_ext))
            run("rm /tmp/{}".format(file_name))
            run("mv {0}{1}/web_static/* {0}{1}/".format(path,
                                                        file_name_without_ext))
            run("rm -rf {}{}/web_static".format(path, file_name_without_ext))
            run("rm -rf /data/web_static/current")
            run("ln -s {}{}/ /data/web_static/current"
                .format(path, file_name_without_ext))
            return True
        except Exception:
            return False
    else:
        return False


def deploy():
    """Function to distributes an archive to your web servers"""
    path = do_pack()
    if path:
        return do_deploy(path)
    return False
