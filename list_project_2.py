friend_list : list[str] =["faisal", "kamal", "mir"]
print(friend_list)
friend_list.append("kamran") # Appending a new friend
print(friend_list)
friend_list.insert(2, "Tahir")
print(friend_list) # Inserting a friend at index 2
friend_list.remove("faisal") # Removing a friend
print(friend_list)
friend_list.pop(2)
print(friend_list) # Removing a friend at index 2
