## 1
names = ['Bob','John','Mark','Mike']
if len(names) > 3:
    print("The room is too crowded")
names.pop()
names.pop()
print(names)
if len(names) > 3:
    print("The room is too crowded")

## 2
names = ['Bob','John','Mark','Mike']
if len(names) > 3:
    print("The room is too crowded")
else:
    print("The room is not crowded")
names.pop()
names.pop()
print(names)
if len(names) > 3:
    print("The room is too crowded")
else:
    print("The room is not crowded")

## 3
names = ['Bob','John','Mark','Mike','James']
if len(names) > 5:
    print("There is a mob in the room")
elif len(names) > 3:
    print("The room is too crowded")
elif len(names) > 1:
    print("The room is not crowded")
else:
    print("This room is empty")
names.pop()
names.pop()
print(names)
if len(names) > 5:
    print("There is a mob in the room")
elif len(names) > 3:
    print("The room is too crowded")
elif len(names) > 1:
    print("The room is not crowded")
else:
    print("This room is empty")
