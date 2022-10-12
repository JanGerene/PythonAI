from ai import AI

alf = AI()
print ("say something")
message = ""
while True and message != 'good bye':
    message = alf.listen()
    if message:
        print(message)
