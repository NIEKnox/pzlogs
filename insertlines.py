# imports
import os  # for getting the filenames
import sqlite3  # for db mgmt

# setup
files = []
dump_lines = ["1", "2", "3"]


# connect to database
con = sqlite3.connect("database.db")
c = con.cursor()

# find all .txt files in current dir
for dirpath, subdirs, filenames in os.walk("C:/Users/[YOUR USERNAME HERE]/Zomboid/Logs"):
    for file in filenames:
        if file.endswith(".txt") and not (file.endswith("DebugLog.txt") or file.endswith("ZombieSpawn.txt")):
            files.append(os.path.join(dirpath, file))

print(files)

# do some check to filter out some i guess

# iterate through remaining files
for filename in files:
    currentlines = []
    file = open(filename, 'r')
    # go thru each line
    for line in file.readlines()[3::]:
        # filter out chat bubbles
        try:
            indicator = line[-10]
        except:
            continue
        if line[-10] not in dump_lines:
            # add to new list
            currentlines.append(line)

    # split time and chatmsg, split dictionary for each line
    for line in currentlines:
        # split into separate parts
        newline = line.replace(']', '[').replace('{', '[').replace('}', '[')
        splitline = newline.split('[')

        print(splitline)

        # take 2nd datetime as entry and 2nd to last as text
        pkey = splitline[1]
        linedict = splitline[-2].split("text='")
        linedict = linedict[-1]

        check = c.execute("SELECT datetime FROM lines WHERE datetime=?", (pkey,))
        if check.fetchone() is None:
            c.execute("""INSERT INTO lines VALUES (?, ?)""", (pkey, linedict,))


con.commit()

