#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers, using the
function do_deploy"""
from fabric.api import put, run, env

env.hosts = [35.185.80.75, 35.231.48.2]


def do_deploy(archive_path):
    """Function to distributes an archive to your web servers"""
    try:
        put(archive_path, "/tmp/")
        file_name = frase.split("/")[-1]
        file_name_without_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        run("mkdir -p {}{}/".format(path, file_name_without_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_name, path,
                                               file_name_without_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path,
                                                    file_name_without_ext))
        run("rm -rf {}{}/web_static".format(path, file_name_without_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/\
             current".format(path, file_name_without_ext))
        return True
    except Exception:
        return False
