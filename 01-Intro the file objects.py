'''
	#### File Objects ####

	Syntex: open(filename,[,mode])

	1-Opens a file and returns a file object
	2-By default, opens a file for reading.
	3-File Open Modes
		"r" 	Open for reading
		"w" 	Open for writing
		"a" 	Open for append
		"r+" 	Open for read/write (updates)
		"w+" 	Open for read/write


	4-File Methods
		f.read([n]) 		# Read at most n bytes
		f.readline([n]) 	# Read a line of input with max length of n
		f.readlines() 		# Read all input and return a list of lines
		f.write(s) 		# Write string s
		f.writelines(ls) 	# Write a list of strings
		f.close() 		# Close a file
		f.tell() 		# Return current file pointer
		f.seek(offset [,where]) # Seek to a new position
					  # where = 0: Relative to start
					  # where = 1: Relative to current
					  # where = 2: Relative to end
		f.isatty() 		# Return 1 if interactive terminal
		f.flush() 		# Flush output
		f.truncate([size]) 	# Truncate file to at most size bytes
		f.fileno() 		# Return integer file descriptor

	5-File Attributes
		f.closed 		# Set to 1 if file object has been closed
		f.mode 			# I/O mode of the file
		f.name 			# Name of file if created using open().
					 # Otherwise, a string indicating the source
		


'''
