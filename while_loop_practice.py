
responses = {}
active = True

while active:
    name = input("What is your name? ")
    destination = input("If you could go anywhere in the world, where would you go? ")

    responses[name] = destination

    repeat = input("Would you like to continue this poll? (yes/no): ")

    if repeat == 'no':
        active = False

print("\n--- Polling Results ---")

for name, destination in responses.items():
    print(f"{name.title()} would like to go to {destination.title()}.")