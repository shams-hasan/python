# Book Web-Scraping Project
This is a web scraping project done on a book example website, which places book titles on each page into various star-rated categories such as one star, two star, three star, so on and so forth. 

**See [webScraping.ipynb](https://github.com/shamshasan0/Python/blob/d4d023b7aabcf4d437899a13d99d4d026c0ff27b/webScraping/webScraping.ipynb) for source code!**

## How It's Made:
By utilizing the Python BeautifulSoup and Request libraries to extract and organize data, this simplified locating classes within the 
website. The class that represented each book item was a 'product_pod' class, so we selected this class using a soup object to find every instance and found that there are twenty results for each page (so 20 books) - we then further inspected the HTML to peek at the star-rating of the book. I created two functions to place the book titles into a list of the rated category that they belong to. One function is made for scraping singular webpages, the other for a range of multiple webpages.
**Tech used:** Python

## Lessons Learned:
After making this project and having somewhat explored the concept of scraping, I can understand why people web-scrape various websites in their day-to-day life. Scraping is essential for not only extracting and locating data, but also organizing it.


Code snippets using the function for individual pages, as well as the function for a range of pages:

<img width="978" alt="Screenshot 2023-08-15 at 12 08 15 AM" src="https://github.com/shamshasan0/Python/assets/105460072/8c224199-6eaa-48f2-8890-5fa25a3a2b05">

<img width="974" alt="Screenshot 2023-08-15 at 12 08 28 AM" src="https://github.com/shamshasan0/Python/assets/105460072/f6a19a21-d9b3-43f1-a773-00540332de26">

<img width="864" alt="Screenshot 2023-08-15 at 12 10 13 AM" src="https://github.com/shamshasan0/Python/assets/105460072/5e73f1a6-55a9-41fa-9eb2-2217cddba0a7">
