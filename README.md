# sastiticket-scraper
  This tool is a offers scraper for "sastiticket.com" created with Scrapy framework. This will scrape all the offers currently available at "Sastiticket" and store them into a workbook.
### Packages used
* **Scrapy**
> _An open source and collaborative framework for extracting the data you need from websites.
> In a fast, simple, yet extensible way._
  documentation and further reading - [Scrapy](https://docs.scrapy.org/en/latest/index.html).

* **openpyxl**
  > _openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files._
  
  documentation - [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
  
### Usage
  first of all clone this repo with:
```
git clone https://github.com/manasec/sastiticket-scraper.git
```
  then install required dependencies and libraries using:
```
pip install -r requirements.txt
```
  And finally inside the project-stscraper release the spider to crawl:
```
scrapy crawl offers
```
### Important notes:
* flush/clear all the data of data.xlsx file everytime before running the package to avoid redundancy, this can be automated with a small code snippet but i will update it later
* if error "no module named win32api" then 
```
pip install pywin32
```
* The offer directories and the html structure of the website may change in future, i will try to keep up with that.
* The regex's used are not strict but does the work for now.
* use rotating proxies and different user-agents to avoid getting blocked
* cliche warning **I'm not responsible for any action/ban by makemytrip on anyone for scraping their website, use this tool at your own risk.**
  
    
