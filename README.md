# Unacademy-Downloader
Download Slides and Audio from Unacademy Site

pre-requisite:
	
	1. python 2.7 should be available to run this application
	2. Disk space of atleast 100 MB
	3. Following Python packages should be available
		i) BeautifulSoup
		ii) urllib 
		iii) requests
  
Application Usage:

	1. Run the application in the same way as running a normal python script (or simply double click - works when environment variable is set) or easier way is running the script through an IDE like 'spyder'
	2. Go to unacademy website, go to a specific course, play a video(lesson), copy the URL of the current page (Application works properly only when lesson URL is provided)
	3. paste the URL in the application, if it is valid it will proceed to further steps

Options while running

	4. You can select whether to download the entire course or to download the particular lesson
	5. Specify whether you need Audio (y/n)
	6. provide width of the slides, typically 960
	7. Enter name of the course (This will be the name of the folder which the application will create)

Where slides will be downloaded?

	1. Application will create a directory in the current working directory of the application
	2. Naming for all the slides are based on lesson name

NOTE:

	1. Application is not regressively tested
	2. User need to take care of the valid options (All exception catches will be added soon)


Mean While anyone can try out. Execution is prety much Self explanatory

Bug Reports are Welcomed,
Thanks in advance
