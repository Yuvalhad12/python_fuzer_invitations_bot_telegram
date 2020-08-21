# python_fuzer_invitations_bot_telegram
This one is a bot that automatically proccesses the invitation system of Fuzer, thus:

1. gets an email address through telegram 
2. if it's valid, it invites the email address to fuzer. If it's not, than it asks for a valid email address
3. auto "refills" the invitations if there are less than 5 remaining invitations.
4. "FXP.py" is NOT a crucial part of this bot. Essentially, what it does is simply commenting on an FXP post. In my case, it runs whenever I want (Essentially every week via crontab) and comments that my invitation program is still relevant. ONCE AGAIN, THIS IS NOT A CRUCIAL PART OF THE BOT AND THE BOT ITSELF CAN RUN WITHOUT IT.


This bot IS HIGHLY UNOPTIMIZED and only a little project that I constructed in less than an hour. I wanted to upload it so people see how easy it is to get into the basics of web scraping and telegram botting.


NOTE: You will have to collect cookies of fuzer yourself. Don't forget that you must also delete "expiry" entries from cookies.

TO DO LIST:
--
1. Add proper bot conversation (confirm email address, find a way to minimize spam from telegram)
