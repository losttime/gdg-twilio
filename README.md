gdg-twilio
==========

This code was developed as part of a coding challenge that took place at the GDG Utah meeting on February 7, 2013. We were asked to complete a series of tasks utilizing the Twilio API and upload our code to GitHub

Phase 1 - Send a specific SMS message to a specific telephone number

Phase 2 - Send a specific SMS message to a specific telephone number. Parse the SMS response and extract the URL. Initiate a phone call with a second specific telephone number and play back the audio file found at the URL optained from the SMS response.

I'm trying to become more familiar with Python, so I chose to use it for these tasks.

Dependencies
------------
- Python 2.? (not really sure - developed with 2.7.3)
- [twilio-python](https://github.com/twilio/twilio-python) (Official Twilio SDK for Python)
- [bottle](https://github.com/defnull/bottle) (simple micro-framework for small web applications)

Requirements
------------
- A Twilio account.
- A way to run python scripts (local machine, virtual machine, remote server, etc).
- A web accessible server capable of running python scripts (for Phase 2 only).
  - Code has been modified to deploy easily to [heroku](http://www.heroku.com/).

How To Run (general)
--------------------
Phase 1 - Replace the dummy values with your own and run the script.

Phase 2
- Configure your Twilio SMS Request URL to point to your webserver at http://www.example.com/smsReceived.
- Replace the dummy values in both scripts with valid Twilio credentials and server information.
- Upload `callbackServer.py` to a web server and run it, making sure it's publicly accessible.
- Run `sendSms.py` from the web server or your local machine.

How To Run (heroku)
-------------------
Phase 2 (only) - 
- You still need to configure your Twilio SMS Request URL and replace the dummy values in both scripts. Then commit your changes. This is not a secure way of storing your credentials, so only commit this code if you are willing to give out access to your Twilio account or your code will never be shared.

    $ git commit -a

- Create a new heroku app

    $ heroku create
    
- Push the app to heroku

    $ git push heroku master

The initial texting script (`sendSms.py`) still needs to be run from a command line (likely on your local machine), but the the app on heroku will handle the rest.
