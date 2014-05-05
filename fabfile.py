from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

def remote():
    env.hosts = ['faithcommunitychurchonline.org']
    env.user = prompt('Username: ')
    env.deploy_dir = '~/public_html/'
    env.repo = 'https://github.com/NathanRSmith/FCCWebsite.git'
    env.branch = 'gh-pages'

def deploy():
    with settings(warn_only=True):
        if run("test -d %s" % env.deploy_dir).failed:
            run("git clone -b %s %s %s" % (env.branch, env.repo, env.deploy_dir))
    with cd(env.deploy_dir):
        run('git pull')