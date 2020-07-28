# 1. pip install -r req.txt
# 2. cd morganlevis
# 3. scrapy crawl morgan -o <BASE_NAME>.csv

## NOTES:
### I didn't use CrawlSpider because it would be much more difficult to implement pagination
### I use Simple Scrapper. I pass the first request and take total results to count from the response, next I create a new request to take all results by one request
### next i parse bio

### i dint use pipelines and Item containers because parse is too simple and i dont need to prepare data

