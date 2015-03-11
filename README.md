# Overview

This project is about enabling idea flow by making it easy to disclose, find, use and improve inventions and other innovations.  
* Project Information at: [http://www.FirstToDisclose.info](http://www.FirstToDisclose.info) 
* Current Prototype: [http://www.FirstToDisclose.net](http://www.FirstToDisclose.net) 

* For More Information, See: the [project background site](http://firsttodisclose.info) and the [MIT project page](https://law.mit.edu/FirstToDisclose)

This project is intended to enable people to publicly share their inventions without risking that another person will later get a patent that excludes open, public free use of the invention.  But the basic idea can also work very well for sharing other types of inventions and other innovations that are less heavy-weight than a patent-track invention but are also valuable and important.  For instance, groups like Code for America and university researchers can use this service to disclose and share open source projects in  way that can be discovered and used and improved by others.  

By leveraging OAuth 2 and innovative identity protocols like OpenID Connect this project also aims to make the experience of sharing information simplified and streamlined.  For instance, people can more quickly agree to relevant terms and conditions without needing to enter their names and emails again so long as they have an active session.  These "federated" approaches also easily enable users to authorize access to protected resources as part of their disclosures such as files in their dropbox accounts, or evernote or other districtured apps and services.  Most important, these approaches promote sharing of ideas and other data by ensuring clear and definitie and continuous user-centred permission management.  

# Technical Documentation


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

# System 

## Routes 

- / 
- /auth
- /agreements
- /disclosure 
- /tag
- /search

## Developement 

http://localhost:8123/tag/
http://localhost:8123/search/
http://localhost:8123/agreements/
http://localhost:8123/disclosure/

Background Slides
'''
<iframe src="https://docs.google.com/presentation/d/1wtlH0Cad8yWDb-c8qC6_NxvyxKkOdcNuKIN50Bzno8s/embed?start=false&loop=false&delayms=3000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
'''

