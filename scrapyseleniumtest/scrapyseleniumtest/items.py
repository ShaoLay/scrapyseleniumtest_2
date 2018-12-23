from scrapy import Item, Field


class ProductItem(Item):

    collection = 'products_scrapy'
    image = Field()
    price = Field()
    deal = Field()
    title = Field()
    shop = Field()
    location = Field()