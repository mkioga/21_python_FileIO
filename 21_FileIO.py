
# ===============
# 21_FileIO.py
# ===============

# =======================
# File Input Output
# =======================

# Reading text file in python

# Reading text files consist of three simple steps
# (1) Open file - using python built in function called "open"
# (2) Read the file - can read one line at a time or read entire file at one go.
# (3) Close file - when we are done with it. closing is important especially when writing to a file
#                  and if its not done well, the file can get corrupted


# This is the program that will read our sample file into python
# File is stored in path: C:\Users\moe\Documents\Python\sample.txt
# Note that you need to use / instead of \ when  giving path to open function otherwise you get error
# so we will use path: C:/Users/moe/Documents/Python/sample.txt
# You can use a "full path" like we've done here or a "relative path"

# Open the file
# Then specify the mode i.e. what you want to do with the file. In this case we want read only ("r")


myFile = open("C:/Users/moe/Documents/Python/sample.txt", "r")

for line in myFile:   # read the file one word at a time
    print(line)

myFile.close()    # close the file

print("="*60)

# Another way to do the string is to use double \\ so that \ is not translated as a command
# Output below works too.

print("Using double \ so that \ is not translated as command")
print()
myFile = open("C:\\Users\\moe\\Documents\\Python\\sample.txt", "r")

for line in myFile:   # read the file one word at a time
    print(line)

myFile.close()    # close the file

print("="*60)
# ======================
# Using relative path
# =====================

# In above examples, we used full path to show where the sample.txt was located
# We can use relative path if the sample.txt is located where our python program is located.
# Example, Sample2.txt is here: C:\Users\moe\Documents\Python\IdeaProjects\21_FileIO
# We now use relative path and it is able to find sample2.txt and read it.

print("Using Relative Path")
print()
myFile = open("sample2.txt", "r")   # using relative path

for line in myFile:   # read the file one word at a time
    print(line)

myFile.close()    # close the file
print("="*60)

# ==================================
# Printing only specific characters
# ==================================

# In other programs, you may need to write code to check for end of file using while loop.
# But in python lets you iterate through the lines of the file as if it were a list which is good.

# you can also perform other processes as you iterate through the file
# For example we can check each line and only print out the ones containing a specific character

# Say we want to only print lines that contain the word "second"


myFile = open("sample2.txt", "r")   # using relative path

for line in myFile:   # read the file one word at a time
    if "second" in line.lower():   # we check if second is in line, and convert them to lowercase.
        print(line)   # this prints only lines with word "second"

myFile.close()    # close the file

print("="*60)

# ===============================
# Getting rid of extra newline
# ===============================

# Note that output from above code prints lines that have double spacing between them.
# This is because in the file itself, every end of line contains "newline" (\n) which
# python is reading and printing new line, hence it prints extra empty line
# To get rid of the extra empty line, we add (end='')

myFile = open("sample2.txt", "r")   # using relative path

for line in myFile:   # read the file one word at a time
    if "second" in line.lower():   # we check if line has "second". Converts input to lowercase because we are testing for lower "second" after if.
        print(line, end='')   # this prints only lines with word "second"

myFile.close()    # close the file. If you don't close, subsequent attempts to read file may fail. and if you wrote to file, it may become corrupted
print("="*60)

# ===================================
# Testing for character in uppercase
# ===================================

# Here is an example of testing for SECOND in upper case
# we will convert all input to upper so if it finds "second" in lower, it converts to upper and test it.

myFile = open("sample2.txt", "r")   # using relative path

for line in myFile:   # read the file one word at a time
    if "SECOND" in line.upper():   # we check if line has "SECOND". Converts input to uppercase because we are testing for upper "SECOND" after if.
        print(line, end='')   # this prints only lines with word "second"

myFile.close()    # close the file.
print("="*60)

# =================
# "with" function
# =================

# In above codes, if there is an error in the file, the program may stops before reaching the "close" function
# That means the file will not be closed, and in windows, you may not be able to open it or move it because python program is still using it
# we can use "with" function to open files and get rid of requirements to have "close" function
# "with" will close the file automatically once it is not needed in the program anymore.
# "with" will also close the file if there is an error in file and it cannot be read anymore


with open("sample2.txt", "r") as myFile:  # Open file and save it in myFile variable
    for line in myFile:   # Iterate through myFile
        if "SECOND" in line.upper():  # Test if SECOND is in line
            print(line, end='')  # Then print the line. No need for close function

print("="*60)


# =======================
# "readline" function
# =======================

# "readline" is another way to read a text file.
# "readline reads "one line at a time"
# Therefore it is recommended for reading large files so that it does not have to commit the entire file to memory

print("===== Using readline =====")
print()
with open("sample2.txt", "r") as myFile:  # open file and save it in myFile
    line = myFile.readline()  # Reads first line to make sure there is text and assigns it to "line" to make it true.
    while line:  # tests line to see if it is True i.e. it has text inside
        print(line, end='')  # Then prints the first line
        line = myFile.readline() # Then loops to second line and goes back to while loop and prints until the end

print("="*60)


# =================================================
# "readlines" function (NOTE is has s at the end)
# =================================================

# "readlines" reads the entire file at the same time and returns it in a single string into memory
# This is not recommended if you are reading large files because it will occupy a lot of memory
# it is different from "readline" which reads one line at a time
# it is useful to print line like: lines = myFile.readlines() for debugging to show you what exactly is in the output

print("============ Using readlines ============")
print()

with open("sample2.txt", "r") as myFile:  # open file and store in myFile
    lines = myFile.readlines()  # use "readlines" to read it all and store in variable "lines". Note \n in output at end of every line
print(lines)  # This prints the entire document in one line
print()
for line in lines:  # you can use for loop to iterate through all the lines and print them
    print(line, end='')  # we use end='' to override above \n at end of every line

print("="*60)

# ================================================
# How to use "readlines" to read file in reverse
# ================================================

print("========= Using readlines in reverse ===========")
print()

with open("sample2.txt", "r") as myFile:  # open file and store in myFile
    lines = myFile.readlines()  # use "readlines" to read it all and store in variable "lines". Note \n in output at end of every line
print(lines)  # This prints the entire document in one line (same way it is written in original text file)
print()
for line in lines[::-1]:  # Reads file "lines" in reverse, from end to beginning
    print(line, end='')  # we use end='' to override above \n at end of every line


print("="*60)


# =================
# "read" function
# =================

# "read" is used to read the entire file one word at a time and if its a text file, it returns
# a string containing the contents of the file.
# "read" can also take an extra parameter specifying how much data to read. We will see this later

print("======== using read =========")
print()

with open("sample2.txt", "r") as myFile:  # open file and store in myFile
    lines = myFile.read()  # use "read" to read it all and store in variable "lines".
print(lines)  # This prints the entire document in one line (same way it is written in original text file)

print("="*60)


# =======================================
# using "read" to read files in reverse
# =======================================

# the result here is that it reverses the file one word at a time.
# Whearas "readlines' reverses the file  one line at a time

print("========== Using read in reverse ===========")
print()

with open("sample2.txt", "r") as myFile:  # open file and store in myFile
    lines = myFile.read()  # use "readlines" to read it all and store in variable "lines". Note \n in output at end of every line
print(lines)  # This prints the entire document in one line (same way it is written in original text file)
print()
for line in lines[::-1]:  # Reads file "lines" in reverse, from end to beginning
    print(line, end='')  # we use end='' to override above \n at end of every line
print()
print("="*60)



# ===============
# Writing a file
# ===============

# use command "open" with "w" for write. This will write a new file in default location
# NOTE: city_file looks like just syntax. It gives this result. probably a file containing the write instruction
# <_io.TextIOWrapper name='MN_Cities.txt' mode='w' encoding='cp1252'>
# After the file "MN_Cities.txt" is created, you will see it at the left side under our folder 21_FileIO
# Note that if file "MN_Cities.txt" already existed, it will be overwritten

# NOTE: when writing or modifying a file, you use print and specify file=file_name (very important)

cities = ["Minneapolis", "St Paul", "Anoka", "Coon Rapids", "Blaine"]  # list containing cities we want.

with open("MN_Cities.txt", 'w') as city_file:  # Command to write into a text file named MN_Cities
    print(city_file)   # This line not necessary. I just use it to view city_file
    for city in cities:  # loop through all the entries in variable "cities"
        print(city, file=city_file)  # print the entries to file "MN_cities. See file=city_file below

print("="*60)

# for "file=city_file", the = sign here is used to pass named argument "city_file" to the "file" parameter
# We should not have any spaces on either side of =, otherwise it will look like an assignment
# "city_file" is the named argument and it is used in place of "file"


# ===================
# "Flush" function
# ===================

# Computer memory is much faster than output devices like screens and external drives
# So data being written to devices is buffered i.e. data is transfered to a buffer, then contents of the buffer
# are transfered to the drives in the background while you are doing something else
# This allows the program to continue processing without waiting for the write to complete hence things seem faster.
# for example, when you run this program and it says "Process finished with exit code 0" it still may have beeb
# saving things in the background. Expecially if the file was long

# Sometimes you want the data to be written out immediately e.g if the output is a screen
# and you want to see as it comes. With buffering, data can be written to screen from the buffer
# and then immediately overwritten with other data from the buffer. As the data scrolls up, the screen
# may appear to flicker.
# Closing a file causes the buffer to be flushed automatically.
# if you want your data to be written sooner, you can pass "flush=True" to cause the data to be written immediately
# This is not very important because modern computers are very powerful compared to when "flush" was developed


cities = ["Minneapolis", "St Paul", "Anoka", "Coon Rapids", "Blaine", "Fridley"]  # list containing cities we want.

with open("MN_Cities.txt", 'w') as city_file:  # Command to write
    print(city_file)   # This line not necessary. I just use it to view city_file
    for city in cities:  # loop through all the entries in variable "cities"
        print(city, file=city_file, flush=True)  # adding "flush"

print("="*60)


# ========================
# Reading a text file
# ========================

# Now we want to read the "MN_Cities.txt" file we created.

cities = []   # We define an empty list
print("Initial cities has: {}".format(cities))  # print show empty

with open("MN_Cities.txt", 'r') as city_file:  # open MN_Cities.txt and save it as city_file
    for city in city_file:  # iterate through city_file
        cities.append(city)  # Then append every line to variable "cities"

print("Final cities has: {}".format(cities))  # This shows us all the cities. Notice the \n in results
print()
for city in cities:  # We iterate through Cities and print line by line
    print(city)  # output here shows doubleline. We can remove this using print(city, end='') or using "strip" function below

print("="*60)

# ====================
# "strip" function
# =====================

# "strip" is used to remove a specified parameter or character from BEGGINING or END of a string
print("========== strip function examples ========")
print()

print("Minneapolis".strip('M'))  # Strips M from the beggining
print("Minneapolis".strip('s'))  # Strips s from the end
print("Minneapolis".strip('p'))  # P is not stripped because it is not at the Beggining or End
print("Adelaide".strip('del'))  # It only stips de which is at the end and ignores l. Does not touch the del after A
print()

print("="*60)

# In below, we want to remove the \n when we read "city_file" and append its contents to "cities"
# note that \n appears at the end of the lines hence can be removed

cities = []   # We define an empty list
print("Initial cities has: {}".format(cities))  # print show empty

with open("MN_Cities.txt", 'r') as city_file:  # open MN_Cities.txt and save it as city_file
    for city in city_file:  # iterate through city_file
        cities.append(city.strip('\n'))  # we strip '\n here

print("Final cities has: {}".format(cities))  # Notice there is no \n in this result
print()
for city in cities:  # We iterate through Cities and print line by line
    print(city)  # No more extra line because \n was stripped


print("="*60)

# ================================
# Write and read from text files
# ================================

# Everything you can see on the screen can be written into a text file
# However its not always possible to read it back in its original form

# We will show an example below, but first we get a refresher on tuples


# ======================
# Refresher on "tuple"
# ======================

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish town walz"))

print(imelda)
print()
print("Album: {}".format(imelda[0]))
print("Title: {}".format(imelda[1]))
print("Year: {}".format(imelda[2]))
print("Tracks:")
track1, track2, track3, track4 = imelda[3]  # unpacking
print(track1)
print(track2)
print(track3)
print(track4)

print("="*60)

# ==============================================
# You can do same thing above using for loop
# ==============================================

print()
print("Method 2 using for loop for 4th element")
print()

# We unpack tuple imelda and assign it to 4 variables
# Note that track will itself contain a tuple
title, artist, year, track = imelda
print(title)
print(artist)
print(year)
print(track) # This has a tuple in itself
print("="*20)

# you can also use a for loop to print the songs in track
print("Here are the songs in track:")
for song in track:
    print(song)

print("="*60)

# =============================
# Writing into a file
# =============================

# Now we will give an example how you can write to a file
# But not read back from the file in the original form it was written

# This program creates a file imelda2.txt that is representative of the tuple imelda
# However there is no easy way to read it back into a tuple variable because it is now stored as a string
# We can use " eval" function to get content of the file back to a "tuple"


imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish town walz"))

print(imelda)  # Results here are same as those in imelda2.txt. Stored as a string in imelda2.txt
print()
with open("imelda2.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

print("="*60)


# ====================
# "eval" function
# ====================

# We will use "eval" function to read back contents of imelda2.txt (stored as string) back to a tuple
# Note that above code already created imelda2.txt

# NOTE: using "eval" allows us to retrieve contents of imelda2.txt back to tuple
# but there are much better ways of doing it instead of using "eval"
# using "eval" is not a good way of retrieving data because the data could be changed or contain harmful instructions
# and the program would still execute it.
# its good to design programs without security vulnerabilities


with open("imelda2.txt", 'r') as imelda_file:  # open imelda2.txt file and read
    contents = imelda_file.readline()  # use readline to read lines in imelda2.txt and assign results to contents

imelda = eval(contents)  # Use "eval" function on "contents" to convert it to "tuple"

print("Below is imelda as a tuple")
print(imelda)  # this is a printout of the tuple we created using "eval"
print()

title, artist, year, track = imelda  # We unpack tuple imelda and assign its elements to these variables

print("Title = {}".format(title))  # Now we print the individual variables.
print("Artist = {}".format(artist))
print("Year = {}".format(year))
print("Track = {}".format(track))


# ===================
# built-in functions
# ===================

# Check built in functions options for open() on this link
# https://docs.python.org/2/library/functions.html

# =================================
# append" or "a" function of open
# =================================

# the function "a" used with open is used to append something to a file.
# Full description here: https://docs.python.org/2/library/functions.html#open

# Write a program to append the times table to our samples3.txt file
# We want the tables from 2 to 12 (similar to output from the for loop for multiplication

# The first column of members should be right justified.
# As an example, the 2 times table should look like this
# 1 times 2 is 2
# 2 times 2 is 4
# 3 times 2 is 6
# etc until
# 12 times 2 is 24

# This is the multiplication table to show you the results. We will comment it out

print()
print("Multiplication table")
for i in range(2,13):  # When i is 1
    for j in range(1,13): # j loops four times
        print("{1:>2} times {0} is {2}".format(i, j, i*j)) # does multiplication until 2nd loop completes
    print("============")  # Change indent level on this print to see different formats

print("="*60)

# When you run this program, it will append the multiplication table above to sample3.txt
# Each time you run the program, it appends to the program

with open("sample3.txt", 'a') as tables:  # Specify sample3.txt and use 'a' for append
    for i in range(2,13):
        for j in range(1,13):
            print("{1:>2} times {0} is {2}".format(i, j, i*j), file=tables)  # write to file. use print but specify file=tables
        print("=" *20, file=tables)  # separator line. Also use file=tables since you are also writing it to file

print("="*60)


# You can also create a new file with the multiplication table by using 'w'

with open("sample4.txt", 'a') as tables:  # New file sample4.txt and use 'w' to write (create new one)
    for i in range(2,13):
        for j in range(1,13):
            print("{1:>2} times {0} is {2}".format(i, j, i*j), file=tables)  # write to file. use print but specify file=tables
        print("=" *20, file=tables)  # separator line. Also use file=tables since you are also writing it to file






