# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# The next 2 lines bring in libraries for scraping pages
import scraperwiki
import lxml.html
# Print hello
print("hello")
# Bring in the whole page, assign it to variable html
html = scraperwiki.scrape("http://foo.com")
# Print to check what's there in html (the full html of the website foo.com)
print(html)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
