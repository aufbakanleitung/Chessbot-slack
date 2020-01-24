# Chessbot-slack
Slackbot that keeps score of CIC-Groningen Chessgames. Written in Python, running on Bluemix.

# Addition development software 

Ngrok: https://ngrok.com/ - secure introspectable tunnels to localhost so you can test on the machine
Start with: `ngrok http 5000`

Flask: http://flask.pocoo.org/docs/0.12/quickstart/#quickstart - To run a weblistener that Slack can connect to

Cloud-Foundry: to push to Bluemix - `cf login -a https://api.ng.bluemix.net` `cf push chessbot`

Guide: https://pmbaumgartner.github.io/blog/slack-commands-with-python-and-flask/

# ToDo list
1. Make integration layer agnostic of database type 

2. Switch database from GoogleSheets to NoSQL (MongoDb)

3. Unit tests + git push hooks