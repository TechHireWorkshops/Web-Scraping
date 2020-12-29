# Web Scraping

![](https://cdn-media-1.freecodecamp.org/images/8D8WScVgBMYV3BTVbL52-HS9v9f8LoV9fCR7)

Web scraping, also known as web harvesting or web data extraction, is the process of extracting data from websites for a variety of purposes. Web scraping is usually used to grab data from sites that can't be obtained through an API, either because the site doesn't offer one or does not provide the desired data in the API.

Web scraping is really the practice copying and pasting from web sites in an automated fashion. Many websites provide loads of data to their users, though this data needs to be processed by the browser. Web scraping usually involves downloading a web page in HTML format, parsing it to a more readable format, and finding specific pieces of data in it. The process of scraping data from websites takes place in a few stages.

![](https://hirinfotech.com/wp-content/uploads/2019/10/What-is-Web-Scraping.png)

- Web crawling: Web crawling is the process of fetching data from a page.  This involves knowing the urls where our data lives.
- Data parsing and cleaning: After we obtain the data (usually in html form), we need to identify the specific data we want, and possibly clean and format it.
- Use: We can then use our data however we want, often aggregating it into a spreadsheet.

![](https://www.promptcloud.com/wp-content/uploads/2020/02/001-efficient-web-scraping.png)

Web scraping is used in many ways, including contact aggregation, price comparison and graphing for products, search engine analysis and ranking, social media tracking, market research and others.

## Legality

Web scraping is legal, usually. It is sometimes against the terms of service of sites, though the enforceability of these terms is often unclear. Website owners can claim copyright infringement or other violations if the web scraping they are the target of meets certain conditions, though cases vary and the law on many of these cases are ill-defined. Companies like eBay and American Airlines have successfully stopped web scrapers from operating on their sites.

Some sites use measures to stop web scraping, like blocking IPs, monitoring use for human-usage traits, obfuscating their data inside their HTML, or tools like CAPTCHA. In response, web scraping tools have been developed to counteract those measures.

## Building a Web Scraper

Each web scraper needs to be customized to the site it's scraping, and the site we'll be looking at today is the monster.com, specifically job postings for software development jobs in New York.  We need to start by finding the appropriate URL, which looks to be

	https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York
	
Once we've found that, we can download this page to our python app using an HTTP request.  We're going to do that with a python library called `requests`.  Once we've installed and imported requests, we can get the page data using

```
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York'
page = requests.get(URL)
```

Now we've got the page, and we can view the content using `print(page.content)`, but man does it suck to look at.  What we need to do now is parse our HTML into a more readable format.  For this, we'll be using a parser called Beautiful Soup.  We can install this using

	pip install beautifulsoup4
	
and import it with

	from bs4 import BeautifulSoup
	
Now that we have our parse, let's parse!

	soup = BeautifulSoup(page, 'html.parser')

creates a parsed version of the webpage, and we can view a nicer version of our HTML now, using `print(soup.prettify())`.  The first argument in the soup constructor is the HTML to parse, and the second is the parser. html.parse is native to Beautiful Soup, but it can use others.  Beautiful Soup can also be used to search and navigate our HTML. We can use things like

	soup.title
	soup.p
	
To view the HTML's title, or the first p tag.  We can also navigate from one element to the other using `.parent`, `.children`, `.next_sibling`, and other commands.  Usually though, we'll be using Beautiful Soup to search for specific HTML elements using classes or ids.  We can search in a new ways, such as

	soup.find_all("p", class_="job-title")
	soup.find_all("a", id="posting-link")
	soup.find_all("div", class_="section-card")

The find_all command should be familiar to most of you, and Beautiful Soups's version takes in the type of HTML element you're searching for, and a class, id, or even string that the element contains.  There are other syntaxes with which we can write our find_all commands as well.

To be able to use this effectively, we need to look at the site we want to scrape using our inspect dev tools, and find classes and id's for the information we need.  Let's get into it.

![](https://miro.medium.com/max/2560/0*5l1YDbdnkWmQwDU5.jpg)

Now that we've found some of the information we want, we can clean up the data a bit and lose the HTML tags using the `.text` method.  We can clean up the whitespace characters using Python's `.strip()`

Now that we have our data, we can do with it as we choose. One of the easiest and most common things to do with this data is aggregate it into a spreadsheet that we can use for our own purposes.  We can use pandas (or other libraries) to create a spreadsheet that we can manage on our own.