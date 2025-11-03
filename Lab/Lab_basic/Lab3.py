# 1. Create a list
playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]
print(f"Original playlist: {playlist}")

# 2. Add a new song
playlist.append("Imagine")
print(f"After adding a song: {playlist}")

# 3. Remove a song
playlist.remove("Stairway to Heaven")
print(f"After removing a song: {playlist}")

# 4. Sort the playlist
playlist.sort()
print(f"Final sorted playlist: {playlist}")

#Exercise 2: Storing Configuration Data

# 1. Create a tuple
screen_resolution = (1920, 1080)
print(f"Screen resolution tuple: {screen_resolution}")

# 2. Unpack the tuple
width, height = screen_resolution
print(f"Width: {width}, Height: {height}")

# 3. Attempt to modify the tuple (this will raise an error)
try:
    screen_resolution[0] = 1600
except TypeError as e:
    print(f"\nError when trying to change the tuple: {e}")
