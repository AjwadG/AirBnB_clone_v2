#!/usr/bin/python3
""" deploy_web_static module """
from fabric.api import *
from os.path import exists, isdir
from datetime import datetime
env.hosts = ['100.26.215.136', '100.26.20.75']
env.warn_only = True


def do_deploy(archive_path):
    """deply filr to server

    Args:
        archive_path: path of the file.
    Returns:
        False if fail or filr not exists otherwise True.
    """
    if not exists(archive_path):
        return False

    sPath = archive_path.replace("versions", "/tmp")
    r = put(archive_path, "/tmp/")
    if r.failed:
        return False
    fName = sPath.split('/')[-1].split('.')[0]
    fPath = "/data/web_static/releases/{}".format(fName)
    r = run("mkdir -p {}".format(fPath))
    if r.failed:
        return False
    r = run("tar -xzf {} -C {}/".format(sPath, fPath))
    if r.failed:
        return False
    r = run("rm {}".format(sPath))
    if r.failed:
        return False
    sPath = fPath
    r = run("mv {}/web_static/* /data/web_static/releases/{}/".
            format(sPath, fName))
    if r.failed:
        return False
    r = run("rm -rf {}/web_static".format(sPath))
    if r.failed:
        return False
    r = run("rm -rf /data/web_static/current")
    if r.failed:
        return False
    r = run("ln -s {}/ /data/web_static/current".format(fPath))
    if r.failed:
        return False
    return True


@runs_once
def do_pack():
    """crates a tar file of content of web_static"""
    n = datetime.now()
    stamp = "{}{}{}{}{}{}".format(n.year, n.month, n.day,
                                  n.hour, n.minute, n.second)
    if not isdir("versions"):
        local("mkdir versions")
    path = "versions/web_static_{}.tgz".format(stamp)

    code = local("tar -cvzf {} web_static".format(path)).succeeded

    if code:
        return (path)
    else:
        return None


def deploy():
    """
        deploy joins do_deploy and do_pack tohether

        Returns:
            False if path in None
            return the return of  do_deploy
    """
    path = do_pack()
    if path is None:
        return False
    res = do_deploy(path)
    return res
