# trello-bot
------------

A trello bot to move your trello cards around for you, so that you get more free time to debate and discuss about git commit frequency. 


## how does it work?

- deploy this project on heroku
- get trello oauth tokens 
- set these environment variables on heroku
  `TRELLO_API_KEY`
  `TRELLO_SECRET_KEY`
  `TRELLO_OAUTH_TOKEN`
  `TRELLO_TOKEN_SECRET`
  `UNDER_REVIEW_LIST_ID`
  `MERGED_LIST_ID`

- created a webhook on github on your project which sends event on your deployed heroku URL
- and you are set
- just add trello card ids in the commit messages like this `TRELLO:shot_url_id`
- and the card will automatically be moved from one list to another





# TODO:

- show how to get trello oauth tokens
- authenticate github webhook requests with the secret key
- this is a hack (developed in hackathon), make it more generic
