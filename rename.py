import os

print("Enter path:")
rootdir = input ()

counter = 0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if str.isdigit(file[0]) and file[1] == '_':
            counter = counter + 1
            os.chdir(subdir)
            os.rename(file, file[2:])

print("Converting ", counter, "files...")
print("Done!")
