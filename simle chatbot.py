print("Hello,Welcome!")
while True:
    user=input("you:")
    if user in ["bye","quit","exit"]:
        print("bot:Goodbye!")
        break
    elif user=="hi":
        print("bot:hello")
    elif user=="how are you?":
        print("bot:I'm great")
    elif user=="eegds":
        print("bot:Im not able to understand")
    elif user==" are you eat":
        print("bot:no!!because i am not eat")
    else:
        print("bot:Goodbye!")
