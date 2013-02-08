gdg-twilio
==========

This code was developed as part of a coding challenge that took place at the GDG Utah meeting on February 7, 2013. We were asked to complete a series of tasks utilizing the Twilio API and upload our code to GitHub

Phase 1 - Send a specific SMS message to a specific telephone number

Phase 2 - Send a specific SMS message to a specific telephone number. Parse the SMS response and extract the URL. Initiate a phone call with a second specific telephone number and play back the audio file found at the URL optained from the SMS response.

I'm trying to become more familiar with Python, so I chose to use it for these tasks.

Requirements
------------
- Python 2.? (not really sure - developed with 2.7.3)
- [twilio-python](https://github.com/twilio/twilio-python) (Official Twilio SDK for Python)
- [bottle](https://github.com/defnull/bottle) (simple micro-framework for small web applications)

How To Run
----------
Phase 1 - Replace the dummy values with your own and run the script.

Phase 2 - Replace the dummy values in both scripts. Upload `callbackServer.py` to a web server and run it, making sure it's publicly accessible. Run `sendSms.py` from the web server or your local machine.
