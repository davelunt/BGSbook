#!/usr/bin/env python
# coding: utf-8

# # Introduction to the unix command line
# In this practical class you will be introduced to Bioinformatics, the computational study of large scale DNA or amino acid data. 
# 
# Bioinformatics is a truly central discipline in all of biology, scientists with bioinformatics skills are highly sought after and the employment opportunities are superb. Our learning goals are that you will have the skills to begin a bioinformatics investigation, and these same skills will also make you excellent at handling big data more generally.
# 
# **DON’T PANIC! YOU DO NOT NEED COMPUTATIONAL SKILLS TO CARRY OUT THIS ASSESSMENT. EVERYTHING YOU NEED TO KNOW YOU CAN LEARN IN THIS CLASS**
# 
# It is essential however that you engage with the exercises, reading them carefully, trying for yourself, and asking questions of your lab partners and the demonstrators.

# **TIP**
# 
# If I had to pick one thing that makes the biggest difference in how easily students learn this it would be **re-typing and trying the commands for themselves in this notebook** not just reading how to do it.

# ## Learning Outcomes
# At the end of this class you should:
# - **Understand the utility** of the command line
# - Be able to **navigate** files and directories from the command line
# - Perform **grep searches** on very large files
# - Be able to **sort**, filter and manipulate data sets

# ## Competency Assessments
# 
# The competencies you must demonstrate highlighted in this document. Read the instructions for each, then type out and run the commands to give the appropriate output. You will be taught how to do this before the competency, it is just a demonstration that you have the skills. You can do them as many times as you wish until you have it to your satisfaction

# ## Table of Contents

# 1. Introduction to the command line and Jupyter notebooks
# 2. Navigating the file system
# 3. Inspecting file contents
#     - Competency part 1 viewing files
#     - Competency part 2 grep searching
# 4. Wildcards
# 5. Search, replace, and write output to a new file
# 6. Sorting and filtering lists
#     - Competency part 3 cancer associated gene lists
# 7. Uploading your competency evidence to Canvas
# 
# <HR>

# # 1. Introduction to the command line and Jupyter notebooks
# Below we will give only a very simple overview. The best way to learn the command line is to Google search for instructions and then try it yourself, experimenting as much as you can. We have also given links to other teaching resources at the end.
# 
# Here we have embedded the unix command line into a Jupyter notebook so that you have the manual and the exercises together. A normal terminal would be a seperate window (you used one for the git clone command), but otherwise it is the same. In the instructions in this notebook we denote commands typed at the terminal with a `$` sign, whereas the output, the info returned by the terminal, has no dollar sign.
# ```
# $ a typed command
# output output output
# ```
# 
# The *actual* terminal sections are the grey cells (boxes) prefixed by `[ ]:`  
# Here is one:

# In[ ]:





# You can run commands in a terminal cell by clicking in it, typing a command, and then Shift-Enter to run the command. Else you click the triangular run button in the menu bar. Try it below, the 'hello world' echo command has been entered for you.

# In[ ]:


echo 'Hello World!'


# Clicking in the box and pressing Shift-Enter will display the output `Hello World!` direcly below the cell. We'll introduce the `echo` command later but you can probably already guess what it does.

# # 2 Navigating the file system
# 
# The first thing to do is to learn the basics of moving between places on your computer, checking where you are, checking what files are present and having a quick look at them. 
# 
# Some of the terminology is perhaps slightly new (‘directories’ rather than ‘folders’) but using the right words will mean you are speaking the same language as everyone else and make your life easier when Googling for solutions (yes Googling is encouraged, it is NOT cheating).
# 
# **THIS IS IMPORTANT --> As the navigation commands are introduced below try them on your own system**

# ## 2.1 Checking where you are (`pwd`), changing directories (`cd`) and listing contents (`ls`)

# ### 2.1.1 Where am I? `pwd`

# At the command line you need to know “where you are” i.e. which directory (folder) you have open and are working in. Question: If you issue the command to ‘list all files’ which files will be listed? Answer: Those in the directory where you are currently working, called the **working directory**. The command to find out where you are is `pwd` short for ‘print working directory’. NB: ‘print’ when working at the command line means ‘display on the screen’ rather than ‘write this to a piece of paper’. 
# 
# Type the command to print working directory (`pwd`) below, and hit Shift-Enter to run the command.

# In[ ]:





# You should see something like this:
# 
# ```
# $ pwd
# /home/bs/username/BGS
# ```

# **Tip:** if you want to try something and there isn't an empty terminal cell, use the menu bar + to Insert Cell
# 
# **Try inserting a cell below and check your working directory again**

# It would be useful now to know what folders and files are present in this location

# ### 2.1.2 Listing the contents of a directory with `ls`
# 
# A very common thing you will want to do is to **display the contents of a directory**, i.e. list all the files. 
# 
# You can list the files (and directories) in your working directory using the `ls` command. Try `ls` now

# In[ ]:





# You will see the files and directories in your current folder displayed by `ls`. The jupyter notebook you are now reading will have the extension `.ipnb`, there are 4 Jupyter notebooks in total. There are also README.md and LICENCE files which may be ignored (though you will soon learn how to examine them if you wish). There will also be a directories called **/data** and **/images** that may be displayed in a different colour to show that it is a directory not a file.

# ### 2.1.3 Changing directories with cd

# But maybe this isn’t where you want to be, maybe you need to have a look at your new data, in which case you need to `‘change directory’` and the command for that is `cd`
# 
# ```
# $ cd data
# $ cd my_sequences
# $ pwd
# 
# /home/bs/username/BGS/data/my_sequences
# ```

# <HR>
# 
# **Explanation:** Spaces in file and directory names cause difficulties as spaces are treated as the end of a file name. When looking for ‘my sequences' it complains that it can’t find ‘my’. 
# ```
# $ cd my sequences
# -bash: cd: my: No such file or directory
# ```
# 
# Although this can be got around by using quotes ‘`my file`’ it is better to name files replacing spaces with underscores (e.g. `my_file`), hyphens (e.g. `my-file`), or concatenating the words (e.g. `myfile`).
# <HR>

# **Try navigating for yourself down to the `my_sequences` directory as outlined above.** Remember you can add extra cells, and use `pwd` and `ls` to help you

# In[ ]:





# In[ ]:





# You can see that the `/` symbol denotes levels of directories, so that the ‘my_sequences’ directory is contained within the ‘data’ directory which is within the user's 'home' directory, and ultimately in the system’s ‘home’ directory. 
# 
# These **file paths** can sometimes be long but they are always explicit, which is a very good thing for reproducibility. There is no excuse for failing to remember where the data was stored for your analysis, here it is written out, and in the real world you will want to record this as part of your experiment.
# 
# #### up one level with a double dot
# 
# You can go up one level (to 'data') by using double dots (ensure there is always a space between the `cd` command and the directory you wish to go to).
# ```
# $ cd ..
# $ pwd
# 
# /home/bs/userename/BGS/data
# ```
# 
# **Try it for yourself** (remember to always try new commands for yourself, it is an important part of your learning, don't wait for my typed reminders)

# In[ ]:





# In[ ]:





# #### home directory

# What happens if you use the `cd` command without telling the system where you would like to change directories to?  
# Try it. How can you find out which directory you are now in?

# In[ ]:





# ```
# $ cd 
# $ pwd 
# /home/bs/username
# ```
# 
# Using `cd` command on its own returns you to your **user’s home directory**, in this case `/username` from wherever you are. NB it is **your** home directory, in my case called davelunt, and its nested within the directory called home by the computer where all users' directories are kept. **your home directory** is an important concept, this other home folder is the only difficult part, and can be ignored for the rest of today. In the example below *username* means your username, whatever it is.
# 
# The tilde symbol (`~`) is shorthand for your home directory so `username/BGS` and `~/BGS` refer to the same directory, which saves a little typing.

# #### previous directory with a dash
# 
# Another very useful shortcut is `cd -` (dash) which takes you to the previous directory that you were in. This is really useful when you need to swap between directories that are separated by several levels or that have long names.

# ```
# $ cd ~/BGS/data/my_sequences
# $ pwd
# /home/bs/username/BGS/data/my_sequences
# $ cd
# $ pwd
# /home/bs/username
# $ cd -
# $ pwd
# /home/bs/username/BGS/data/my_sequences
# $ cd -
# $ pwd
# /home/bs/username
# ```
# 
# Make sure that you are actually typing this out for yourself rather than just reading along. Work through the example above. This **active learning** will really help it to stick in memory, and come back when you need it, a bit like developing muscle memory.

# ### 2.1.4 tab completion saves time and errors

# You are probably slightly annoyed now that you have to type in all these directory names, which are long and complex. If you make one typo it will result in an error. Real bioinformaticians make use of the tab key a lot. tab will suggest completions of your file path.
# 
# If I am in the home directory and I type `$ cd BGS/data/m<tab>` it will autocomplete to `$ cd BGS/data/my_sequences`
# 
# Because of the way this Jupyter notebook is set up it may instead give you a list of options, you can navigate using the arrow keys, and hit RETURN when you have the right option.
# This saves a LOT of typing and prevents errors. Insert a cell below and try it now. 

# ### 2.1.5 Chaining commands together with a semicolon
# Above we were issuing commands one at a time; first `cd` then `pwd`. To chain commands together on the same line separate them with a semicolon ie `cd;pwd`
# 
# Try the exercise from the `cd -` section above again, but now using semicolons. You should only need 4 commands not 8.
# 
# Are you tab completing the addresses?

# In[ ]:





# ## Quiz 1: Ways to return home
# There are 5 ways that you should now know to return to your home directory. Most people only remember 2 or 3, what can you do? Please work with someone nearby, tell a demonstrator, list them below, and we'll see who are the champions.
# 

# ### 2.1.6 Summary
# ```
# pwd	print working directory, show where you are
# ls	list, show all the files in your current directory
# cd	change directory, move to another location
# ;	semicolons can chain together commands on one line
# ```
# 
# <HR>
# 
# PAUSE HERE AND CHECK BEFORE GOING FURTHER
# 
# <HR>

# # 3 Inspecting file contents, and searching within text files

# ## 3.1 Inspecting files

# Much of bioinformatics is the inspection and retrieval of information from text files. This data is the source of all subsequent analyses and we need to make sure it is the right data in the right format.
# 
# If we  want to inspect a file we can display its contents using several unix programs:
# ```
# cat  	to print the whole file to the screen
# head 	to print the first few lines of the file on screen
# tail 	to print the last few lines of the file on screen
# ```
# One of the problems with DNA sequence files is that they can be large - several hundred megabytes to a few gigabytes is not uncommon. Viewing these files can be difficult, as the files need to be loaded into memory, and can therefore take a great deal of time for the text editor to read from the disk. The `head` and `tail` commands are very efficient for viewing large files such as these. 
# 
# Remember Googling things is encouraged, it is a great way to learn bioinformatics! Google `unix command head` and `tail` to learn more about them if you wish. 
# 
# Both `head` and `tail` display 10 lines by defualt, but they allow you to specify the number of lines to display, so `head -20` would display the first 20 lines and `tail -5` the last 5 lines.
# 
# Remembering tab completion navigate to the directory `/data/my_sequences`. Tip; when navigating use `ls` to see what is available.

# Some of these files e.g. `C.09.F.fasta` are quite large (~30Mb), while the others are smaller. Only one of the commands above is inappropriate for large files all the others will be useful. If you have a problem don't panic, ask a demonstrator.
# 
# #### big files
# 
# Which commands should you use for big or small files and why? The problem is that if you command a really big file to display to the screen (eg `cat mybigfile.fasta`) then it will just keep scrolling data in an unhelpful way. **Tip** `control-z` can make it stop. If you want to try it on `C.09.F.fasta` go ahead, you can't do any damage. Ask a demonstrator to help you clean up afterwards
# 
# If unsure about the size of a file `head` is a good way to have a quick look at it. If you actually want to know how big a file is you can display this with a version of the `ls` command `ls -lh` Try it.
# 
# **All the commands above will be very useful for basic bioinformatics work, they are key skills**

# In[ ]:





# ----
# ## Competency part A - viewing files
# 
# Navigate to the `data/headers` directory.
# 
# How big are the files?

# In[ ]:





# In the 3 cells below use each of the following commands to view the contents of the file `display-test.fas`.
# 1. cat
# 2. head
# 3. tail 

# In[ ]:





# In[ ]:





# In[ ]:





# **Bonus** can you display the last 15 lines of `display-test.fas`? (optional)

# In[ ]:





# End of competency

# <HR>
# PAUSE HERE AND CHECK BEFORE GOING FURTHER
# <HR>

# ## 3.2 Searching within files `grep`

# Searching within very large files however can also be problematic, especially using the standard 'find' functions in a text editor, which aren’t optimised for performing searches across very large files. For this reason various tools have been created that allow users to search within large files from the command line, and are highly optimised for their function. One of the most useful utilities for searching within a file is `grep` (global regular expression parser).
# 
# `grep` is very simple to use. At the command line you will need to type the word `grep`, followed by the text you are searching for, followed by where (the filename) to look for it. For example, to search for the word Fungi in our `18S_seqs.fas` file we do the following:
# ```
# $ cd ~/BGS/data/my_sequences/
# $ grep 'Fungi' 18S_seqs.fas
# >AY642706_10 1401 Eukarya/Fungi
# ```

# This returns the text `>AY642706_10 1401 Eukarya/Fungi` which is the single line that contains the word Fungi. This is the output of `grep`, the line on which the search phrase is found.
# 
# Make sure that you are trying this for yourself, by inserting cells and giving the command
# 
# We can confirm that there is only one instance by using the **count flag** (`-c`) with `grep` as follows:
# ```
# $ grep -c 'Fungi' 18S_seqs.fas
# 1
# ```

# #### Flags
# 
# Flags are useful things, they allow the default behaviour of a command to be refined. 
# You have already used a flag (`-lh`) with the `ls` command to make it show you files sizes. Using flags to set parameters and modify the default settings is very comman in bioinformatics.

# ### 3.2.1 How many sequences do I have?
# A very common question is to ask is ‘how many DNA sequence records are in this enormous fasta file?’ 
# 
# **Tip: Do you know what a sequence record looks like? Quickly learn about fasta sequence files from Appendix 1. Now try to see if the sequence file '18S_seqs.fas' matches your expectations. You already have the skills to do this without loading the whole file into memory, can you remember how? Check above if not.**
# 
# In order to find out the number of sequences you could of course search for all the greater than `>` symbols, which is almost certainly the number of records. However, you should really search for all the lines *starting with* > rather than the number of times it occurs, as it is possible for a fasta header to contain an internal > . ‘Line starts with’ is represented by the `^` symbol. 

# Try to design a `grep` search to count the number of fasta header lines. Do not copy/paste from any web resource. Discuss your solution with your partner and/or demonstrator.

# ----
# # Competency part B `grep` 

# Use a `grep` search to count the number of fasta header lines in the two files `18S_seqs.fas` and  `C.09.F.fasta`. Ensure that the searches and output are below.

# In[ ]:





# In[ ]:





# End of competency

# **Help in case of problems:** 
# 
# Have you remembered the quotation marks around the search phrase? (eg `'Fungi'`)
# 
# Unfortunately if you haven't use quotes your solution may delete the data file! Why? Look at section 5 below and discuss. If you have deleted your file a spare file can be found in `/data/backup`. You only need to copy from /backup if you have deleted your file. Can you find a way from the command line to **copy** this file to your current directory? Google for a solution on how to copy a file at the unix command line. Try it, and list the files to see if you have been successful. Check with a demonstrator if you need.

# You may try your `grep` search again in a new cell below and still get the marks for completing this assessment. A correct `grep` for counting sequence records, and using it to search these two files will get you the marks

# In[ ]:





# <HR>

# ## 3.3 Summary
# ```
# head	show the first few lines of a file
# tail	show the last few lines of a file
# cat 	print the whole file to the screen
# grep	search, the -c flag counts the matches
# ```

# ## Quiz 2 (Googling is OK)
# How many lines does `head` display? How can that be changed? Show me
# 
# Now write a `grep` search with the correct syntax to find "Nematoda" in `18S_seqs.fas`. How many times does it occur?
# 
# Write a `grep` search to find the DNA sequence "GCCATGCG" in `18S_seqs.fas`. Why does it print out so much DNA sequence? How many times does GCCATGCG occur?

# <HR>
# PAUSE HERE AND CHECK BEFORE GOING FURTHER
# <HR>

# # 4 Wildcards

# We have learned about displaying files and basic searches. Later you will create and move information into files. We need more detailed control however, not just displaying one named file, or all files, but instead the files we have specifically chosen. Wildcards allow us to select text and file names in a powerful and flexible way that makes life much easier.

# ## 4.1 What are wildcards?

# Wildcards represent characters, and allow you to create a search term to select files or directories. 
# 
# They allow selections to be both very broad (by having a general matching criteria, eg all file names beginning with a letter) and very specific (by having very detailed matching criteria, eg all files with `f` as the second letter and a number between 1 and 5 at the end).
# 
# **Here is the basic set of wildcards:**
# 
# `*` - represents any character ocurring zero or more times (nothing or everything). eg `f*` represents the letter `f` followed by any number of characters whatever they are. So files `fez.txt`, `f1234.jpg` and `fibonacci.mpeg` would all match, as would a file just called `f`.
# 
# `?` - represents any single character. eg `d?g` would match dog, dig, or d8g, but not doog
# 
# `[ ]` - represents a specified range of single characters. eg `d[a-n]g` would match dag, dbg, dcg etc but not dog because the letter o is not in the set a-n
# 
# The most useful for you today will be the star (*) wildcard. Like all wildcards * helps to create a pattern (series of characters) and that pattern is used by the program to define what it does.

# ## 4.2 Listing using wildcards

# Previously `ls` has been used to display all files in a directory, but now lets select only certain files. In the world of big data there may be thousands of files of different file types, or with different metadata included in the file name. Selecting only the files meeting certain criteria is very useful. Later you will learn how to use these selected files, and only those selected.
# 
# `ls` lists the contents of the working directory
# 
# `ls data` lists the contents of the data directory
# 
# `ls data/my_sequences/sequence1.fas` will list the specified file (sequence1.fas)
# 
# `ls data/my_sequences/*.fas` will list all files whose names are any number of any characters followed by “.fas”. So the files `sequence1.fas`, `shortseqs.fas`, `18S_seqs.fas`, but not `C.09.F.fasta` will match the pattern created by the * wildcard (*.fas).

# Try this wildcard search for yourself

# In[ ]:





# If you are getting `No such file or directory` errors please check that you are in the main folder, above data

# ## Quiz 3
# With your partner write a command to list each of the following in any directory (you do not actually need these files to exist, just write a `ls` command to do the job):
# 
# 1. write a `ls` command to display all the .txt files 
# 2. write a `ls` command to display all the .jpeg files
# 3. write a `ls` command to display all the files named 1234 whatever file extension they have (.jpeg, .txt, .fas)

# 4. How would you list only the fasta files beginning with “sequence” and not “Dave” or anything else? As a complication, one user has put sequence files with a `.fas` suffix, another with `.fasta`, and a third with `.fa`. This is bad naming practice, but we need all the fasta files. What wildcard command would list them out? Discuss this with a demonstrator
# ----

# ## 4.3 unix commands are case sensitive 

# Most commands at the terminal are case sensitive, so `ls Dave.*` and `ls dave.*` will produce different results. 
# This is a common error you should watch out for. There are ways to make commands **case insensitive** (so `Dave.fas` and `dave.fas` are treated the same) but it is not the default behaviour of command line programs.

# ## 4.4 file filtering and copying

# Your wildcard skills can be deployed in lots of situations, they are not specific to `ls`
# 
# It is actually the underlying bash kernel (the program that runs the command line terminal) that does the hard work. It translates your wildcard pattern (`sequence*.fas`) into a list of files that match (eg `sequence1.fas` ... `sequence100.fas`) and feeds those to the `ls` program. 
# 
# The good news is that it does this for every program not just `ls` so your new wildcard skills can be used anywhere. Next you will use these skills to select files (based on the metadata in their filenames) and copy them to a new location.

# The command to copy a file is `cp`. Google it if you need. You can use `cp` in the same way as you used `ls`, incorporating wildcards to copy only certain files just as you have been doing already.
# 
# Copy commands are structured like this (just an example, don't copy and paste it):
# 
# `cp directory1/selected_files directory2/`
# 
# You will have to supply three terms and assemble them correctly:
# 1. "directory1" refers to where the files are
# 2. "directory2" refers to where you will copy them
# 3. “selected_files” term is your wildcard search for fasta files containing "sequence". You probably already wrote something similar above (Quiz 3.4).
# 

# **Copy all the fasta files in the `data/sequences` directory that contain the word “sequence” and copy them to the `data/seqs_filtered` directory**

# Check what files are present in this directory before and after the copy. Have you copied what you intended? If not a demonstrator can help you to delete the files, and you can try again.

# In[ ]:





# In[ ]:





# ----

# ## 4.5 Wildcards, optional extras 

# **This section can be skipped over if you are pushed for time** just go to section 5, but it provides details of other types of wildcard beyond the asterisk `*`. These are higher level skills. The more complex your search, the more you will have to use a full range of wildcards. You can read and see examples by Googling unix wildcards
# 
# ### 4.5.1 the `?` wildcard
# As a brief example let's introduce the `?` wildcard. 
# 
# `ls ?i*`
# 
# In this example we are looking for each file whose second letter is “i” because our term translates as “list filenames with any single character, followed by the letter ‘i’, followed by any number of characters”. As you can guess, the pattern can be built up using several wildcards.
# 
# How would you find  every file with a three letter extension? 
# 
# `ls *.???`
# 
# This is “any number of characters, followed by a dot, followed by 3 single characters but not more or less”

# ### 4.5.2 the range operator (`[ ]`) wildcard
# The range operator (`[ ]`), unlike the previous 2 wildcards which specified any character, allows you to limit to a subset of characters. 
# 
# In this example we are looking for every file whose name either begins with an s or v.
# 
# `ls [sv]*`
# 
# And here any .fas file beginning with an s or d
# 
# `ls data/[sd]*.fas`
# 
# With ranges we may also include a set by using a hyphen. So for example if we wanted to find every file whose name includes a digit we could do the following:
# 
# `ls *[0-9]*`
# 
# To find all the numerically labelled fasta files (sequence1.fas, sequence100.fas) in our directory we could try this:
# 
# `ls seq*[0-9].fas`

# ## Summary
# ```
# ls	list contents of the directory
# cp	copy
# *	wildcard, stands for 'any characters'
# ?	wildcard, stands for a 'single character'
# []	wildcard, specifies a range of characters
# ```
# 

# <HR>
# PAUSE HERE AND CHECK BEFORE GOING FURTHER
# <HR>

# # 5 Search, replace, and write output to a new file

# `grep` is an excellent tool for undertaking simple yet fast searches within text files. But to search and replace within a text file, or to redirect changes to a new file, we will need to use either `sed` or a simple script (OK there are actually numerous ways of doing this utilizing other tools and python scripts but this manual will only deal with simple examples with `sed`). First though we will write text using `echo` and learn about routing data to the right location with `>` `>>` and `<`.

# ## 5.1 `echo` to write data

# A useful way to write to a text file is with `echo`. This will print to the screen or a file. 
# Try these commands
# ```
# $ echo Hello world!
# $ echo Hello world! > greeting.txt
# ```

# In[ ]:


echo Hello world! > greeting.txt


# It may not seem like this second command has done anything, but it has. You have used the `>` to route the output to a file (`greeting.txt`) rather than to the screen.

# ## 5.2 routing, determine where your data goes

# If the file `greeting.txt` does not exist it will be created. We have routed the information to a location (the file) with the greater than (`>`) symbol. If the file does exist it will be overwritten. Keep this in mind when dealing with important data, the `>` will overwrite all previous data in the file.

# 
# Check the file now exists (how?), then you can use one of the commands above (`cat` maybe? Do you remember the others?) to inspect the file you have just created. 

# In[ ]:





# 
# If you wish to **append** text to a file rather than **replace** it you can use the `>>` symbol:
# 
# `echo ‘Hello again world!’ >> greeting.txt`
# 
# Try this and check your success. 

# In[ ]:





# **Routing syntax** (`>`, `>>`) is general to UNIX and can be used with other programs too. Imagine that you need to add an extra fasta sequence to the end of a big sequence file, the append symbol `>>` will be helpful. In reality you would want to take your new text from a file rather than typing it it. We have similar examples in the `sed` section below where the source file is specified using a less than (`<`) symbol. 

# ----

# ## Quiz 3 Concatenation

# **Background thought experiment, discuss**
# 
# Describe to your partner how, using MS Word, you would open a directory of 3 fasta files and copy the contents of each file into a new "all_seqs.fas" file and estimate how quickly you could do this.
# 
# Now describe how you would do that in Word with 3000 fasta files, or 3,000,000 files and estimate how long it would take. At the command line these solutions (3; 3,000; 3,000,000) are identical and the same amount of work for you! 
# 
# A common bioinformatics task is to **concatenate** a lot of individual sequence files into one single file as described above. This is very time consuming to do in a GUI if you have more than a couple of files to open, copy, close, open, paste. The task at the command line however scales easily to almost any number of files. 
# 
# **Now come up with a solution**
# 
# You already have all the skills to do this if you learned about wildcards and routing before. Don't worry if not, discuss it and ask for help. It is most important that you know that the command line *scales*. Your cammand that you write here will be *exactly* the same if you concatenate 3 or 3,000,000 fasta files. If you can work out how to do this, and get the syntax correct, show a demonstrator or myself.
# 
# **Try these 3 tasks:**
# 
# Go to the `fasta-to-combine` directory. 
# 
# Concatenate all 10 sequence files into a new file with an informative name. 
# 
# Can you do the same excluding the contents of the README.md file? Demonstrate your success (show me) by inserting cells below

# <HR>
# 
# **The next sections below, and section 6, are starting to build really powerful and useful bioinformatics skills to manipulate data. Don't get overwhelmed trying to remember alll the syntax, you can just scroll back to look it up, or google it. Instead for each section try to think of real-world uses- "I've just collected a lot of data in a lot of files, how could this help me to wrangle it?"**
# 
# **If you need it take a break, or chat to one of us about the work, but don't just skip ahead**
# 
# <HR>

# ## 5.3 (Optional) stucturing data files with `echo`

# `echo` also allows us to format files correctly. If we need newlines or tabs inserted we can do this by using the `-e` flag. The tab symbol is `\t` and newline `\n`. 
# 
# Can you use these to better format the file "greeting.txt" that you created before in the "routing, determine where your data goes" section above?
# 
# Try to imagine what the following command will write, maybe sketch it out & discuss with others:
# 
# `echo -e “column1\tcolumn2\nRNA\tDNA” > rna-dna-columns.txt`

# Give it a go and check what has been written. These commands are useful when writing a lot of data to a file programmatically, and when format is important, which is a very common situation for bioinformatics work.

# In[ ]:





# #### `echo` and file names
# 
# Something that is often useful when working with lots of files, as bioinformaticians do, is to know that `echo` can write file information like file names
# 
# `echo *.fas > fasta-file-names.txt`
# 
# This would write the name of every file in the current directory with a `.fas` extension to a file called `fasta-file-names.txt`.
# 
# This could be very useful when you need process lots of information about output file, perhaps when the file names contain information like sample location, or organism, or date. Although I am talking only about bioinformatics today, big data is everywhere in biology. You can manipulate files of any type of data using your new skills.

# ## 5.4 `sed`, the stream editor

# `sed` works best when we need to deal with files as single lines, or rows of text data. Since `sed` doesn’t try to take the whole file into memory, instead dealing with a line at a time, it has real advantages when files are enormous- as they often are for sequence data.
# To search for and replace `Fungi` with `Fungus` in our `18S_seqs.fas` file we could do the following:
# 
# `sed 's/Fungi/Fungus/' < 18S_seqs.fas > fungi-to-fungus.fas`
# 
# This will replace the single word Fungi with the word Fungus, but output these changes to the file `fungi-to-fungus.fas`, leaving the original file unchanged. It is always good practice to leave the original data unchanged when modifying it.

# The `s` within the single quotes signifies this is a substitution command and the `/` characters are delimiters that separate the text to search for, and the text to replace it with. 
# 
# In UNIX based systems the `<` signifies an input, so we are taking input from our `18S_seqs.fas` file and outputting (`>`) to `fungi-to-fungus.fas`

# ## Summary
# ```
# echo	write to a file
# sed	search and replace
# <	take input from named file
# >	direct output to named file, replacing
# >>	direct output to named file, appending
# *	wildcard, stands for 'any characters'
# ```
# 
# Test yourselves. In pairs ask each other to explain what items from the list above do. Each of you ask the other to come up with a (not too difficult) command line using one or two of them.

# ----
# 

# # 6 Sorting and filtering lists

# Not all files of data are convenient to look at. Sometimes there is too much data and it is not structured for the human brain. In these cases it is very useful to filter, sort, count the instances of each record, and write bespoke lists.

# You have already learned some filtering by searching for key phrases with `grep`, using wildcards, and routing data to new files. You are now going to learn to sort and combine identical records and count them.

# ## 6.1 counting characters, words, and lines

# unix has a word count program called `wc`
# 
# There are many ways to use this but useful options are:
# ```
# -m count the number of characters
# -w count the number of words
# -l count the number of lines
# 
# ```
# 
# 
# Of course wc, like other programs because more powerful when part of a workflow linked by pipes |. Can you determine what this cammand would do?
# 
# `cat *.csv | wc -l`

# Try to word count the number of lines in some files in `data/my_sequences`

# ## 6.2 sort uniq

# The `sort` command rearranges the lines of a file into alphabetical and numerical order, which can be very useful. 

# The `uniq` command is a way of filtering out repeated lines in a file. It operates by comparing adjacent lines and determining if they are the same. This strategy requires the file to be sorted first, so `sort` and `uniq` are often employed together. The output of `uniq` are the non-redundant (ie unique, occuring once) lines of a file.

# `uniq` can report the number of times a line occurred by using the `-c` flag. It prepends the number of occurrances to the line. We could do something like this:
# ```
# sort file.txt
# uniq -c file.txt
# head -4 file.txt
# 
# 7 apples
# 2 bananas
# 1 cherries
# 1 durian
# ```

# It might be better however to link the commands together with pipes, each action passing its results to the next. Doing so would reduce typing and errors.

# Try to sort and count the fruit in `data/fruit.txt` using pipes and no pipes. Next display the top three Next write the top three to a `fruit_top3.txt` file using the greater than symbol.

# In[ ]:





# ## Summary
# ```
# wc	word count, `-m` characters, `-w` words, `-l` lines
# sort	rearrange into alphabetical or numerical order
# uniq	remove duplicate lines
# |	pipe, used to chain together commands (see below)
# ```

# <HR>
# PAUSE HERE AND CHECK BEFORE GOING FURTHER
# <HR>

# # Competency part C: cancer associated gene lists

# This final piece of work is by far the most challenging. Remember though, that everything I am asking you to do you have pretty much already just done above in section 6. You may discuss and exchange ideas with others in the class. Google it if you wish! But you must learn enough to carry it out yourself. Do not give up, this sounds harder than it is, you have made great progress up until here!
# 
# Unlike the other competencies this is a complete section and you must do all 5 parts in bold labeled C3.1 - C3.5

# ## Differential expression of genes in cancer tissue

# Dr Smith is studying which genes are overexpressed in different cancers. She designs a small pilot project before launching into her main research in order to get candidate genes that she will focus on later. 
# 1. take cancerous tissues samples from both lung and heart
# 2. convert mRNA to cDNA and sequence
# 3. identify the gene name for each DNA sequence
# 4. organise the gene name data into heart and lung collections
# 5. count and compare the unique gene names in both tissues
# 
# Steps 1-3 have been completed for you. It is now time for the bioinformaticians to get to work. You will now carry out steps 4 and 5 by completing the whole of this section.

# ## Analysis

# You have been provided with a file called `data/genes/genelist.txt`. This contains the name of each gene found, with a suffix indicating in what tissue the mRNA originated. 
# 
# **C3.1 Examine the list using your file-reading skills**

# In[ ]:





# **C3.2 determine how many records it contains**

# In[ ]:





# ## Organising the data into files

# You will need to separate the two classes of records (heart, lung) into two separate files in order to work with them easily. You have previously done something similar with `grep`. You should use carefully chosen file names so that it is clear what is in each. A common error would be to analyse the wrong file because it has a similar name.

# **C3.3 Create and run a search term to separate the two types of gene names and write them into separate well-named files**

# In[ ]:





# You should check both files to confirm there is only one type of tisue data, and count the number of records in each as you did before

# In[ ]:





# In[ ]:





# ## Sorting and counting gene names

# For each file you are are first going to determine the number of times each gene name occurs. That is how many unique records exist. You have already combined `sort` and `uniq`. You should remember how to write data to a file, and have used this with several programs already. A challenging aspect here are determining how many times you will need to sort. Also (although its not necessary if you have a good plan) many people will want to have the most frequently expressed genes at the top of the file. You may need to look up `sort` flags to do this. 

# **C3.4 create two files (ie both heart and lung), each containing a sorted list of all the unique gene names, with the gene-name frequency counts next to them**

# In[ ]:





# **C3.5 Write the lines containing the most frequent 5 gene names from each tissue to a file**

# In[ ]:





# You have almost finishd, well done, please ask a demonstrator for a high five.
# 
# Now you can upload a PDF of this workbook to complete your assessment. Read section 7 below.

# ----
# 
# # THIS IS REALLY IMPORTANT DON'T SKIP SECTION 7
# 
# ----
# 

# ## 7. Uploading your competency work

# **You must save and upload your practical notebook as a PDF**
# 
# 1. Check your name and student ID are in the cell at the top of this notebook. 
# 2. Use the internet browser menu to `print as PDF`
# 3. Save this PDF somewhere safe. You should rename it informatively (Bloggs_unixprac.pdf, 978675_commandline.pdf). 
# 4. Validate your work. Check how many pages it has and **if it is >20 pages you have done something wrong, probably by using `cat` on a very large file**. Do not submit, go back and have another try. Now upload it to the Canvas assignment for "Week C unix competency"

# # YOU ARE NOW COMPLETELY FINISHED, WELL DONE

# You have achieved A LOT today. The skills you have learned are very valuable in biology and any area of science. Remember you don't have to have memorised all this, you can look up the syntax whenever you need it. In bioinformatics its not cheating to look things up (or Google it) whenever you need to use them, its encouraged.
# 
# What I do want you to take away are:
# 
# 1. a knowledge of the sorts of things you know how to do: search by criteria, list, count, sort, find uniques, and write to files. I would like you to recognise problems you can solve, and feel confident to write or loook up the syntax to solve them.
# 2. know that all your skills scale: a single command that searched, sorted, and counted unique data in 1 file will do the same in 1000 files just by changing the input term. I would like you to feel confident that big data is something you can deal with.
# 
# You can now check with someone and go.

# ----
# 
# # Appendix 1 the fasta file format
# Fasta (pronounced “fast- ay” to rhyme with May) is a concise standard text file format used for sequence data. A fasta file may contain one or many separate sequence records, each in fasta format. You will need to use this format several times during today’s session. Both DNA and amino acid sequences can be formatted this way. Essentially it is a greater than symbol “>” followed by any title you want to give it, then, starting on the next line, the sequence.
# 
# ### Here is the description of FASTA from GenBank.
# “A sequence in FASTA format begins with a single-line description, followed by lines of sequence data. The description line is distinguished from the sequence data by a greater-than (">") symbol in the first column”
# 
# Example sequences in FASTA format are: 
# ```
# >AAH22472.1 Malic enzyme 3, NADP(+)-dependent, mitochondrial [Homo sapiens]
# MGAALGTGTRLAPWPGRACGALPRWTPTAPAQGCHSKPGPARPVPLKKRGYDVTRNPHLNKGMAFTLEER
# LQLGIHGLIPPCFLGQDVQLLRIMGYYERQQSDLDKYIILMTLQDRNEKLFYRVLTSDVEKFMPIVYTPT
# VGLACQHYGLTFRRPRGLFITIHDKGHLATMLNSWPEDNIKAVVVTDGERILGLGDLGCYGMGIPVGKLA
# LYTACGGVNPQQCLPVLLDVGTNNEELLRDPLYIGLKHQRVHGKAYDDLLDEFMQAVTDKFGINCLIQFE
# 
# >My sequence
# CCGGGCTCTGCCTCGATGCAAACGTTATGCATATATGTATTATCACCATTATTTTATATCAAACATATCC
# TATATATTAATACATCTCATTTAACAGAAATATAGGTAGATATACCACATATTTGTCAACAACATTTTAA
# CTAAGGGGTACATAAACCATAACTAAGTACTCTCCAATAAATATTTATTAATTACTGAACGATAGTTTAA
# GACCGATCACAACTCTCACTGGTTAAGATATACCAAGTACCCACCATCCTATTTACCTCCCTTATTTAAT
# GTAGTAAGAGCCCACCATCAGTTGATTTCTTAATGTTAACGGTTCTTGAAGGTCAAGGACAAATATTCGT
# GGGGGTTTCACTTAGTGAACTATTCCTGGCATCTGGTTCCTATTTCAGGTCCAATAATTGTTATAATTCC
# CCATACTTTCATCGACGCTTGCATAAGTTAATGGTGGTAATACATACTCCTCGTTACCCACCATGCCGGG
# CGTTCTTTCCAGCGTGTGGGGGGTTCTCTTTTTTTTTNNCCTTTCA
# ```
# ### Fasta format records and fasta files
# Above are two fasta records. A fasta record contains only a single header with a single sequence. It is one thing. The record is in fasta format because it is a greater than symbol, then a header, then the sequence.
# 
# A fasta file is a text file. It usually has the extension .fas or .fsa or .fna or .fasta. Each text file may contain one or more than one fasta record. It is not uncommon to have tens of thousands of fasta records in a single text file. For it to count as a fasta file all the records must be in valid fasta format.

# ## Appendix 2
# ### Some reading if you wish to extend your knowledge
# - UNIX Tutorial for Beginners http://www.ee.surrey.ac.uk/Teaching/Unix/
# - Command line history tricks http://www.thegeekstuff.com/2008/08/15-examples-to-master-linux-command-line-history/
# - Software Carpentry Introduction to the unix shell on YouTube (great short videos) 
# - Unix and Perl Primer for Biologists http://korflab.ucdavis.edu/Unix_and_Perl/unix_and_perl_v3.0.pdf
# - Bradnam and Korf. (2012) UNIX and Perl to the Rescue!: A Field Guide for the Life Sciences (and Other Data-rich Pursuits). ISBN-10: 0521169828  ISBN-13: 978-0521169820 http://www.amazon.co.uk/gp/product/0521169828
# - GREP http://www.gnu.org/software/grep/manual/grep.html
# - SED http://www.gnu.org/software/sed/manual/sed.html
# - Software Carpentry Introduction to programming in Python (great short YouTube videos) 
# - Python for Biologists http://pythonforbiologists.com
# - Python for non-programmers https://wiki.python.org/moin/BeginnersGuide/NonProgrammers

# In[ ]:




