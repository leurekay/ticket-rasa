#只训练core
rasa train core
rasa run -m models/core-20201217-175914.tar.gz  --enable-api

##调用方式post
http://10.15.83.131:5005/conversations/111/trigger_intent
{
  "name": "inform",
  "entities": {
    "date_time": "null",
		"start":"null",
		"end":"北京"
  }
}
