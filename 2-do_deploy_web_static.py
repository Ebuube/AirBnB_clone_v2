#!/usr/bin/python3
"""
Deploy archive to web servers
"""
from fabric.api import *
from os.path import isfile

env.hosts = ['18.207.2.78', '54.162.43.21']


def do_deploy(archive_path):
    """
    Deploy this archive to the specific web servers
    """
    if not isfile(archive_path):
        # print("File not found")
        return False

    # print("type: {} | val = {}".format(type(archive_path), archive_path))

    # Get name for unzipped file
    archive = archive_path.split(sep='/')[1]
    unzipped = archive.split(sep=".tgz")[0]
    deployable = "/data/web_static/releases/{}".format(unzipped)

    # Upload archive
    if run("mkdir --parents /tmp/").failed is True:
        return False

    if put(local_path=archive_path, remote_path="/tmp/").failed is True:
        return False

    # Uncompress archive

    cmd = "mkdir --parents {}".format(deployable)
    if run(cmd).failed is True:
        return False

    # Clean directory before decompression
    cmd = "rm --recursive --force {}/*".format(deployable)
    if run(cmd).failed is True:
        return False

    cmd = "tar -xzf /tmp/{} -C {}/".format(archive, deployable)
    # cmd = cmd.format(archive, deployable)
    if run(cmd).failed is True:
        return False

    # remove temporary file
    cmd = "rm --force /tmp/{}".format(archive)
    if run(cmd).failed is True:
        return False

    cmd = "mv -f {}/web_static/* {}".format(deployable, deployable)
    if run(cmd).failed is True:
        return False

    cmd = "rm -rf {}/web_static".format(deployable)
    if run(cmd).failed is True:
        return False

    # Relink deployed code
    if run("rm -rf /data/web_static/current").failed is True:
        return False

    cmd = "ln -sf {}/ /data/web_static/current".format(deployable)
    if run(cmd).failed is True:
        return False

    # Confirmation
    print("New version deployed!")
    return True
