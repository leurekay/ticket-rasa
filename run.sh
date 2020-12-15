#!bin/bash
ports="5055"
#$*
for port in $ports
do
	lsof -i:$port | awk '{print $2}'> tmp
	pid=$(awk 'NR==2{print}' tmp);
	echo "$port $pid"
	kill -9 $pid
done

rasa run actions & rasa shell --debug
