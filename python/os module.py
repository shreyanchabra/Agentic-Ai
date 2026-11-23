# os module allows to interact with the underlying operating system
# navigate the file systems
# get the file information
# look up and change the environment variables
# move files around
import os

# from datetime import datetime

# all the attributes and methods available in this module
# print(dir(os))

# get the current working directory
# print(os.getcwd())

# Change the current working directory
# os.chdir("C:\\Users\\Hp\\OneDrive\\Desktop")

# The names of the files in the current directory as a list.
# print(os.listdir())

# The names of the files in the specified directory as a list.
# print(os.listdir("D:\\"))

# creates a single directory and fails if parent folders are missing
# Works ONLY if "data" already exists
# os.mkdir("data/reports") 

# os.makedirs() recursively creates the target directory along with any missing parent folders
# Creates "data", "2026", and "reports" even if none exist yet
# exist_ok=True prevents an error if the folders are already there
# os.makedirs("data/2026/reports", exist_ok=True)

# os.rmdir() and os.removedirs() only delete empty directories
# os.rmdir() deletes just the single target folder
# Removes ONLY 'reports'. Folder 'data' remain intact.
# os.rmdir("data/reports")

# os.removedirs() also deletes its empty parent folders up the path
# Removes 'reports', then removes '2026' (now empty), and then 'data' (now empty)
# os.removedirs("data/2026/reports")

# os.rename("old_name", "new_name") renames a file or directory (in the current working director) without altering its contents. 
# os.rename("intro.py", "introduction.py")

# os.stat() retrieves low-level file system metadata (such as size, permissions, and timestamps) for a given file path or file 
# fields can be accessed either by attribute name (e.g., info.st_size) or by tuple index (e.g., info[6]).
# info = os.stat("string.py") # The info variable is an instance of os.stat_result (a subclass of tuple). 
# print(info)
# print(info.st_birthtime)
# print(info[2])

# getting time in human readable form
# from datetime import datetime 
# print(datetime.fromtimestamp(info.st_birthtime))

# os.walk() is a built-in generator function that recursively traverses(DFS) a directory tree. 
# On each iteration, it yields a 3-tuple containing (dirpath, dirnames, filenames) for every folder it visits.
# dirpath: A string representing the path to the current directory being inspected.
# dirnames: A list of the names of all subdirectories inside dirpath.
# filenames: A list of the names of all non-directory files inside dirpath
# for dirpath, dirname, filename in os.walk(os.getcwd()):
#     print(f"path: {dirpath}")
#     print(f"directories: {dirname}")
#     print(f"files: {filename}")
#     print()

# os.environ is a built-in, dictionary-like mapping object that represents the current process's operating system environment variables. 
# Both keys and values are stored as strings, allowing you to read, set, and delete configuration data such as API keys, database URLs, and system paths.
print(os.environ)


