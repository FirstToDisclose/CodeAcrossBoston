from fabric.api import env, local, run, sudo, cd

# http://sysadminpy.com/sysadmin/2011/04/30/use-fabric-on-vagrant-instances/
def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']

    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]


def venv():
    with cd("/vagrant"):
        sudo("pip install virtualenv")
        run("virtualenv /home/vagrant/venv")
        run("/home/vagrant/venv/bin/pip install -r requirements.txt")

def manage(cmd):
    python = "/home/vagrant/venv/bin/python"
    with cd("/vagrant/firsttodisclose"):
        run('"%s" manage.py %s' % (python, cmd))

def server(port=8000):
    manage('runserver 0.0.0.0:%s' % port)

def migrate():
    manage('migrate')

def admin():
    local('open http://localhost:8000/admin/')
