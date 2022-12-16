# pzlogs

hey gamer. i see you want to be able to extract the riches available for you, huh? let's get started

1. you probably want an IDE that can run python. microsoft visual basic works, but i use pycharm once you have that, download the two files and run 'databasemaker.py'. 
2. go into insertlines.py change the filepath at line 15 from [YOUR USERNAME HERE] to whatever your user profile is called on your computer (should be 5 characters, mine is noahi)
3. run insertlines.py

congratulations! you should now have all the chatlogs youve ever received now stored in a database, organised by the time and date, with none of the clutter of the text bubbles.
however. this does not include what YOU have typed. i honestly don't know where that is and i haven't had a proper look for it. if you find it, tell me! in theory if you get the logs from someone you were in the scene of, you'd have every single line from that scene (however, there will be desync in the time at which messages were received by the host computer, so if you're in an rp with multiple people you will almost certainly get duplicates in the database. the fix for this is changing the check at line 52 of insertlines.py from checking if the datetime is already in the database, to checking if the message text is already in the database. (why didn't i do that right away? a) it's more computationally expensive to compare the big strings of text than the little ones, and b) that factor didnt occur to me until now LMAO)

at this point, you're gonna need some way to extract stuff from the database, or at least look at it. you can use https://extendsclass.com/sqlite-browser.html# to upload your database.db file and have a look at what's there, and organising by datetime will let you view stuff sequentially. i'm working on using PySimpleGUI to make something similar to the pz chat window which lets you scroll through indefinitely, but i am struggling LMAO. 

