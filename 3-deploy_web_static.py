#!/usr/bin/python3
"""
Full Deployment
Command:
    fab -f ./this_file_name deploy -i my_ssh_private_key -u ubuntu
"""
from fabric.api import *
from os.path import isfile
from datetime import datetime
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ['18.207.2.78', '54.162.43.21']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

# Compress depolyment package
recent_archive = do_pack()


def deploy(archive=recent_archive):
    """
    Create and distribute an archive to my web servers
    """

    # Compress archive
    try:
        if not isfile(archive):
            return False
    except Exception:
        return False

    # Deploy archive
    res = do_deploy(archive)
    return res
