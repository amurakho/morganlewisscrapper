# 1. pip install -r req.txt
# 2. cd morganlevis
# 3. scrapy crawl morgan -o <BASE_NAME>.csv

## NOTES:

### I didn't use CrawlSpider because it would be much more difficult to implement pagination
## !! My first request is long... but I don't need pagination. I think it will be better
### I use Simple Scrapper. I pass the first request and take total results to count from the response, next I create a new request to take all results by one request
### next i parse bio


### I dint use pipelines and Item containers because the parse is too simple and I don't need to prepare data

