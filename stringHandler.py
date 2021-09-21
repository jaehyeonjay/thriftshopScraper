# File of all constant strings used in scraping

chromeDriverPath = '/Users/jaypark/Downloads/chromedriver'
searchEngineXPath = "//input[@type='text']"

# For Karrot
karrotURL = 'https://www.daangn.com/'
karrotLoadMore = "//div[contains(@onclick, 'moreResult')]"
karrotCatalogue = "flea-market-article flat-card"
karrotName = "article-title"
karrotPrice = "article-price"
karrotNoElement = "empty-result-message"

# For Bunjang
bunjangURL = 'https://m.bunjang.co.kr/'
bunjangLoadMore = "//a[@class='sc-ccbnFN jbSbET']//img[@src='data:image/svg+xml;" \
             "base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdp" \
             "ZHRoPSIxMiIgaGVpZ2h0PSIxMiIgdmlld0JveD0iMCAwIDEyIDEyIj4KICAgIDx" \
             "wYXRoIGZpbGw9IiM5Qjk5QTkiIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTMuNiA" \
             "xMmEuNTk2LjU5NiAwIDAgMCAuNDQ5LS4yMDJsNC44LTUuNGEuNi42IDAgMCAwIDA" \
             "tLjc5N2wtNC44LTUuNGEuNi42IDAgMSAwLS44OTcuNzk3TDcuNTk4IDYgMy4xNTI" \
             "gMTFBLjYuNiAwIDAgMCAzLjYgMTIiLz4KPC9zdmc+Cg==']"
bunjangCatalogue = "sc-elNKlv cpNpD"
bunjangName = "sc-clNaTc eVmuLh"
bunjangPrice = "sc-etwtAo hoDAwD"
bunjangNoElement = "//*[contains(text(), '검색결과가 없습니다')]"

# For Joongna
joongnaURL = 'https://m.joongna.com/home'
joongnaLoadMore = "//button[@class='SearchList_moreButton__11RNU']"
joongnaCatalogue = "ProductItemV2_info__1tF2R"
joongnaName = "ProductItemV2_title__1KDby"
joongnaPrice = "ProductItemV2_price__1a5yb mt3"
joongnaNoElement = "SearchListNoResult_title__1QrDd"