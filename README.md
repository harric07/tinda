# tinda
#### Buggy alpha stage.
 
## Modern wrapper for basic things. 

### Installation:

```
pip install tinda

```

## Usage:

```
from tinda import XXX   

'''
When a class defines an __init__() method,
class instantiation automatically invokes __init__() 
for the newly-created class instance. 
So in this example, a new, 
initialized instance can be obtained by:
'''

x = XXX()

'''
Method Objects:
Usually, a method is called right after it is bound:
For example,
'''

x.say('string of whatever') 

#google image search of the query string
x.image(query) 

# the same works for Google, Github, Stackoverflow, Youtube, etc.
x.google(query)
x.stackoverflow(query) 


# returns private and public ip.
x.getIp() 

# returns location data.
x.getLocation() 

# other methods:
x.time() 
x.date()
x.shutdown()
x.mousePosition()
x.goToPosition()
x.leftClick()
x.rightClick()
x.showDesktop()

x.recordScreen() # saves output file in root directory.
x.speedTest() # returns internet speed test results.
x.getLinks() # takes in url and returns all links.
x.textToMorse() # string to morse code.
```

```
# Local network Terminal Chat
import tinda

tinda.TerminalChatServer()
# once the server is running, Clients can connect to the server and begin chatting.

import tinda

tinda.TerminalChatClient()
```

```
# Local Network Audio Chat
import tinda

tinda.LocalAudioServer()
# once the server is running, Clients can connect to the server and begin chatting.

import tinda

tinda.LocalAudioClient()

```


Developed by:
Harpreet Singh © 2021
