# Simple webscraping script

Created by: Pedro Sartori Dias dos Reis
GitHub: https://github.com/pedrosdr

If you want to run this script on your machine you must: 

-> Make sure that the chromedriver is compatible with your chrome browser version.
   The chromedriver version used in this script is the 114.0.5735.90 version.
   You can find other versions at: https://sites.google.com/chromium.org/driver/downloads

-> Create a virtual environment and activate it:
	python -m venv venv
	.\venv\Scripts\activate

-> Install the packages "selenium" and "bs4":
	pip install selenium
	pip install bs4

-> Delete the "db.sqlite3" database:
	rm .\databases\db.sqlite3

-> Run the db.py file:
	python .\databases\db.py

-> Run the main.py file:
	python .\main.py