# Unacademy-Downloader
- Download Slides and Audio from Unacademy Site

## Pre-requisite:
	
- python 2.7 should be available to run this application
  
## Application Usage:

1. Run `pip install -r requirements.txt` in cmd - this will install all required library
2. Run python file using `python2.7 Unac_down_main.py` or simply double click on .py file
3. Go to unacademy website, go to a specific course, play a video(lesson), copy the URL of the current page (Application works properly only when lesson URL is provided)
4. paste the URL in the application, if it is valid it will proceed to further steps

## Options while running

5. You can select whether to download the entire course or to download the particular lesson
6. Specify whether you need Audio (y/n)
7. provide width of the slides, typically 960
8. Enter name of the course (This will be the name of the folder which the application will create)

## Where slides will be downloaded ?

1. Application will create a directory in the current working directory of the application
2. Naming for all the slides are based on lesson name

### NOTE:

1. Application is not regressively tested
2. User need to take care of the valid options (All exception catches will be added soon)

- Mean While anyone can try out. Execution is prety much Self explanatory

Bug Reports are Welcomed,

#### Thanks in advance