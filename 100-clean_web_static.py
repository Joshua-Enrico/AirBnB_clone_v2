#!/usr/bin/python3
"""
With Facric , creates a tgz archive
from web_static content folder
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.73.133.125', '52.201.252.232']


def local_clean(numer=0):
    """Locas Clean"""
    fd_list = local('ls -1t verions', capture=True)
    fd_list = fd_list.split('\n')
    num = int(number)
    if n in (0, 1):
        n = 1
    for i in fd_list[n:]:
        local('rm versions/' + i)


def remote_clean(numer=0):
    """Remote Clean"""
    fd_list = run('ls -1t /data/web_static/releases')
    fd_list = fd_list.split('\r\n')
    numb = int(number)
    if n in (0, 1):
        n = 1
    for i in fd_list[n:]:
        if i is 'test':
            continue
        run('rm -rf /data/web_static/releases/' + i)


def do_clean(number=0):
    """Fabric script that deletes aout of dates archives"""
    local_clean(number)
    remote_clean(number)
