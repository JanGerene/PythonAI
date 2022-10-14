from time import sleep
from eventhook import EventHook

def test_event_hook_after():
    print("this is an event hook for after")

def test_event_hook_before():
    print("this is an event hook for before")

def moosay():
    print("this is a moosay")

before = EventHook()
after = EventHook()

before.register(test_event_hook_before)
after.register(test_event_hook_after)
after.register(moosay)

while True:

    before.trigger()
    print("loop de loop")
    after.trigger()
    print("")
    print("*"*20)
    print("")
    sleep(1)