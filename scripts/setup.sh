echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list

apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

apt-get update -y

# Install postgres and setup database
apt-get install -y postgresql-9.4 postgresql-server-dev-9.4 python-dev python-pip

# Wait for postgres to spin up
sleep 3

sudo -u postgres psql -c "create user ftd encrypted password 'ftd'"
sudo -u postgres psql -c "create database firsttodisclose owner ftd"
