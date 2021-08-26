#!/usr/bin/python3
"""
With Facric , creates a tgz archive
from web_static content folder
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.73.133.125', '52.201.252.232']


def local_clean(number=0):
    """Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean"""
    l = local('ls -1t versions', capture=True)
    l = l.split('\n')
    n = int(number)
    if n in (0, 1):
        n = 1
    print(len(l[n:]))
    for i in l[n:]:
        local('rm versions/' + i)


def remote_clean(number=0):
    """Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean"""
    l = run('ls -1t /data/web_static/releases')
    l = l.split('\r\n')
    print(l)
    n = int(number)
    if n in (0, 1):
        n = 1
    print(len(l[n:]))
    for i in l[n:]:
        if i is 'test':
            continue
        run('rm -rf /data/web_static/releases/' + i)


def do_clean(number=0):
    """Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean"""
    local_clean(number)
    remote_clean(number)
