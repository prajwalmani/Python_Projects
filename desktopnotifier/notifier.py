import time
from newsscript import topstories
import notify2
# icon path
icon = "newsicon.png"
#fetch the list from the newsscript using topstories
newsitems = topstories()

# initilize the d-bus connection
# d-bus connection is used to communicate between applications
notify2.init("News Notifer")

# create a notification object
n = notify2.Notification(None,icon=icon)

# set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)

# set timeout fr the notification
n.set_timeout(1000)

for newsitem in newsitems:

    # update the notification
    n.update(newsitem['title'],newsitem['description'])

    # to show the notification
    n.show()

    # sleep
    time.sleep(15)