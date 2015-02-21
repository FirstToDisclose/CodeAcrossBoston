# CodeAcrossBoston

Make sure you have fabric and vagrant installed

```
# Get the vagrant installer online
sudo pip install fabric
```

Then get going with:

```
# Install local settings for vagrant
cp firsttodisclose/firsttodisclose/local_settings.py.example firsttodisclose/firsttodisclose/local_settings.py

vagrant up
fab vagrant venv
fab vagrant manage:migrate
fab vagrant manage:createsuperuser
```

You can see the app running using the "server" fabric task:

```
fab vagrant server
```

In another window terminal you can launch the admin app with:

```
fab admin
```
