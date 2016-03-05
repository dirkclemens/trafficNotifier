# trafficNotifier
Send push notifications with traffic informations (pushover, Bing Maps Traffic)

The script calls a Bing Maps Service to analyze the current traffic between two waypoints 
and sends a push notification when called 

I use the script because I have serveral options to drive from home to my office and back.
This script helps me to decide which way to choose.

The traffic information is based on Bing maps traffic
https://msdn.microsoft.com/en-us/library/ff701717.aspx

Requirements:
	BingMapsKey	(https://msdn.microsoft.com/de-de/library/gg650598.aspx)
	Pushover Acoount (https://pushover.net)
	
You can call the script using cron jobs in the morning or afternoon:
In the morning at 7:45 am:
45 7 * * *	/usr/bin/python3 /path/to/script.py >/dev/null 2>&1
In the afternoon every 30 minutes between 4 pm and 6 pm:
0,30 16-18 * * *	/usr/bin/python3 /path/to/script.py >/dev/null 2>&1	

	
