from zipfile import as ZipFile as zp

file_path = "" #Define the path of the zipfile over here

with zp(file_path, "r") as zip_:
	zip_.printdir()		#to print all the content
	zip_.extractall()	#to extract the zip file


