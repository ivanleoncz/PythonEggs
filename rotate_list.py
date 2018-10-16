
import string

l = list(string.ascii_lowercase)
print("Pre Rotate: ", l)

rotate = 4

for i in range(rotate):
    move_beggining = l.pop(-1)
    l.insert(0, move_beggining)
    
print("Post Rotate:", l)
