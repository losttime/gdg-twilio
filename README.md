gdg-twilio
==========

This code was developed as part of a coding challenge that took place at the [GDG Utah](https://plus.google.com/u/0/111917982940065392922) meeting on February 7, 2013. We were asked to complete a series of tasks utilizing the Twilio API and upload our code to GitHub. The code has since been modified to easily deploy to [heroku](http://www.heroku.com/).

Dependencies
------------
- Python 2.? (not really sure - developed with 2.7.3)
- [twilio-python](https://github.com/twilio/twilio-python) (Official Twilio SDK for Python)
- [bottle](https://github.com/defnull/bottle) (simple micro-framework for small web applications)

Requirements
------------
- A Twilio account.
- A web accessible server capable of running python scripts.
  - Code has been refactored for easy deployment to heroku.

How To Run (general)
--------------------
1. Configure variables in server.py according to your setup
  - webserver information (host, port, dns)
  - Twilio information (account, token, phone number)
2. Configure your Twilio SMS Request URL to point to your webserver at http://www.example.com/smsReceived.
3. Upload `server.py` to a webserver and run it, making sure it's publicly accessible.
4. Point your browser to your webserver to send an SMS message.
  - Something like http://www.example.com/

How To Run (heroku)
-------------------
1. Create a new heroku app.
2. Copy `set_configs_sample.sh` to `set_configs.sh`
3. Modify the variables in `set_configs.sh` to match your setup
  - HOST should likely be 0.0.0.0
  - DNS should be the domain for your new heroku app
  - The rest should match your Twilio account information
4. Run `set_configs.sh` to set your heroku app's environment variables

    $ ./set_configs.sh
    
5. Push your app to heroku

    $ git push heroku master
    
6. Configure your Twilio SMS Request URL to point to your app
  - Something like http://xxxxxxx-xxxxxxx-####.herokuapp.com/smsReceived
7. Point your browser to your app to send an SMS message.
  - Something like http://xxxxxxx-xxxxxxx-####.herokuapp.com/
