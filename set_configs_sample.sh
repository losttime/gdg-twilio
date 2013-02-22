#!/bin/bash

# This (set_configs_sample.sh) is a sample file.
# To prevent your tokens from being saved to github, don't edit the values here.

# 1) Copy this file as set_configs.sh
#    You can save it as anything, but set_configs.sh is already in .gitignore,
# 2) Update the values in the new file.
# 3) Run the new file from the terminal `$ ./set_configs.sh`
#
# Your config variables should now be set on heroku, ready to use.

heroku config:add DNS=www.example.com
heroku config:add TWILIO_ACCT=ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:add TWILIO_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:add TWILIO_NUMBER=+15005550006