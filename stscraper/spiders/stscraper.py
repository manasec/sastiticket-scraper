import scrapy
from ..items import StscraperItem
import re
from collections import OrderedDict

class Stspider(scrapy.Spider):
    name = 'offers'
    url = "https://www.sastiticket.com/offers"
    start_urls = [
        url
    ]

    def parse(self, response):
        for href in response.css(".col-lg-3.col-md-3.col-xs-12.col-sm-12 a::attr(href)"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
        #regex area
        ods = re.compile(r"Get\s[0-9]+[\s%]\s.+")
        coupreg = re.compile(r"\s[A-Z]{5,}[0-9]*")
        catreg = re.compile(r"domestic.*(&|and)\s(I|i)nternational flights.*")
        valreg = re.compile(r"(v|V)alid.*till.*[0-9]")
        minreg = re.compile(r"min.*[0-9]")
        conreg = re.compile(r"valid.*(ONCE|once|twice|TWICE).*")
        bankreg = re.compile(r"Amazon Prime|MOBIKWIK|MobiKwik|BHIM\sUPI|RuPay.*(Card|card)|ICICI.*card")
        #regex area
        item = StscraperItem()
        item["link"] = '=HYPERLINK("{}", "{}")'.format(response.request.url, "Link")
        item['Platform'] = "SastiTicket"
        offerdetails = response.css('h1::text').extract()
        ptext = response.css('p::text').extract()
        stext = response.css('strong::text').extract()

        text = ""


        for i in ptext:
            text += i + "\n "
        for i in stext:
            text += i + "\n "

        if offerdetails==[]:
            offerdetails = ods.search(text).group(0)


        category = catreg.search(text).group(0)
        ptext = response.css('p::text').extract()
        stext = response.css('strong::text').extract()
        ltext = response.css('li::text').extract()

        text = ""
        for i in ltext:
            text += i + "\n"
        minimumamount = minreg.findall(text)
        if minimumamount == []:
            minimumamount = "N/A"

        for i in ptext:
            text += i + "\n "
        validity = valreg.search(text).group(0)
        for i in stext:
            text += i + " "

        bankwallet = bankreg.search(text)
        if bankwallet == None:
            bankwallet = "N/A"
        else:
            bankwallet = bankwallet.group(0)
        constraints = conreg.findall(text)
        if constraints==[]:
            constraints = "N/A"

        coupon = coupreg.findall(text)
        coupon = list(dict.fromkeys(coupon))
        if coupon==[]:
            coupon = "nocouponrequired"
        text = ""
        item['category'] = category
        item['coupon'] = coupon
        item['validity'] = validity
        item['constraints'] = constraints
        item['bankwallet'] = bankwallet
        item["minimumamount"] = minimumamount
        item['offerdetails'] = offerdetails
        item['channel'] = "Website Only"
        key_list = ["Platform","coupon","category","offerdetails",
                    "minimumamount","channel","bankwallet",
                    "validity","constraints","link"]
        new_dict = OrderedDict((k, item[k]) for k in key_list)
        item = new_dict

        yield item
