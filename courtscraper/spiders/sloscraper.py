# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
import pymysql
from CourtScraper.items import CourtscraperItem
from scrapy.http import Request

class SloscraperSpider(scrapy.Spider):
    name = 'sloscraper'
    allowed_domains = ['www.slo.courts.ca.gov']
    start_urls = ['http://www.slo.courts.ca.gov/']
    def start_requests(self):
        list = ["https://www.slo.courts.ca.gov/dv/index.htm",
            "https://www.slo.courts.ca.gov/ff/index.htm",
            "https://www.slo.courts.ca.gov/gi/index.htm",
            "https://www.slo.courts.ca.gov/index.htm",
            "https://www.slo.courts.ca.gov/os/index.htm",
            "https://www.slo.courts.ca.gov/sh/index.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-glossary.htm",
            "https://www.slo.courts.ca.gov/dv/civil-adr.htm",
            "https://www.slo.courts.ca.gov/dv/civil-mediation.htm",
            "https://www.slo.courts.ca.gov/dv/civil.htm",
            "https://www.slo.courts.ca.gov/dv/collections-communityservice.htm",
            "https://www.slo.courts.ca.gov/dv/collections.htm",
            "https://www.slo.courts.ca.gov/dv/criminal-addresschange.htm",
            "https://www.slo.courts.ca.gov/dv/criminal.htm",
            "https://www.slo.courts.ca.gov/dv/familycourt.htm",
            "https://www.slo.courts.ca.gov/dv/juvenile.htm",
            "https://www.slo.courts.ca.gov/dv/paying-criminal-fines.htm",
            "https://www.slo.courts.ca.gov/dv/paying-family-fees.htm",
            "https://www.slo.courts.ca.gov/dv/probate.htm",
            "https://www.slo.courts.ca.gov/dv/traffic-appearance.htm",
            "https://www.slo.courts.ca.gov/dv/traffic-contestcitation.htm",
            "https://www.slo.courts.ca.gov/dv/traffic-payticket.htm",
            "https://www.slo.courts.ca.gov/dv/traffic-school.htm",
            "https://www.slo.courts.ca.gov/dv/traffic-tickets101.htm",
            "https://www.slo.courts.ca.gov/dv/traffic-violations.htm",
            "https://www.slo.courts.ca.gov/dv/traffic.htm",
            "https://www.slo.courts.ca.gov/ff/forms.htm",
            "https://www.slo.courts.ca.gov/ff/schedules.htm",
            "https://www.slo.courts.ca.gov/gi/ada.htm",
            "https://www.slo.courts.ca.gov/gi/announcements.htm",
            "https://www.slo.courts.ca.gov/gi/benefits.htm",
            "https://www.slo.courts.ca.gov/gi/contact-location.htm",
            "https://www.slo.courts.ca.gov/gi/contracts.htm",
            "https://www.slo.courts.ca.gov/gi/court-calendars.htm",
            "https://www.slo.courts.ca.gov/gi/court-holidays.htm",
            "https://www.slo.courts.ca.gov/gi/court-reporter-protem.htm",
            "https://www.slo.courts.ca.gov/gi/court-reporter.htm",
            "https://www.slo.courts.ca.gov/gi/employment.htm",
            "https://www.slo.courts.ca.gov/gi/interpreters.htm",
            "https://www.slo.courts.ca.gov/gi/job-descriptions.htm",
            "https://www.slo.courts.ca.gov/gi/jury-grandjury-application.htm",
            "https://www.slo.courts.ca.gov/gi/jury-grandjury-complaints.htm",
            "https://www.slo.courts.ca.gov/gi/jury-grandjury-statistics.htm",
            "https://www.slo.courts.ca.gov/gi/jury-grandjury.htm",
            "https://www.slo.courts.ca.gov/gi/jury-qualifications.htm",
            "https://www.slo.courts.ca.gov/gi/jury-reporting.htm",
            "https://www.slo.courts.ca.gov/gi/jury.htm",
            "https://www.slo.courts.ca.gov/gi/media.htm",
            "https://www.slo.courts.ca.gov/gi/rules.htm",
            "https://www.slo.courts.ca.gov/gi/scams.htm",
            "https://www.slo.courts.ca.gov/gi/uiapprovedarbitrators.htm",
            "https://www.slo.courts.ca.gov/os/efiling.htm",
            "https://www.slo.courts.ca.gov/os/pay-fines.htm",
            "https://www.slo.courts.ca.gov/os/tentativerulings.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-bankruptcy.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-changename-adult.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-changename-minorwithparent.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-changename-minorwithparents.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-civilappeals.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-civilcourtfiles.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-civilrestraining.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-cleanrecord.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-conduct.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-conservatorship.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-courtstaff.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-criminalappeals.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-criminallaw-inforequest.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-criminallaw.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-custody-finishcase.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-custody-respond.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-custody-startcase.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-custody.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-defaulthearing-checklist.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-defaulthearing.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-defaultnohearing.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-finishcase.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-finishdefault.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-finishtrial.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-finishuncontested.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-respond.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce-startcase.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-divorce.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-domesticviolence.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-estate.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-eviction.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-familylaw.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-genderchange.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-glossary.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-guardianship.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-namechange.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-requestorder.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-resources.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-restrictedlicense.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-smallclaims.htm",
            "https://www.slo.courts.ca.gov/sh/selfhelp-warrant.htm"]
        
        for link in list:
            request = scrapy.Request(link)
            yield request

#        yield Request("https://www.slo.courts.ca.gov/dv/civil.htm",headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (.html, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})

    def parse(self, response):
        item = CourtscraperItem()
        item['url']=response.url
        item['headerh1']=pymysql.escape_string(response.css("h1::text").extract_first())
        item["title"]=pymysql.escape_string(response.xpath("string(//html/head/title)").get())
        item["dv"]=pymysql.escape_string(response.css("a.active::text").extract_first())
        item["content"]=pymysql.escape_string(response.xpath("string(//html/body/div/div/div[3]/div/div/div/div[4]/div[2]/div/div[3]/div[1]/div/div)").get().strip())
        item["htmlcontent"]=response.xpath("//html/body/div/div/div[3]/div/div/div/div[4]/div[2]/div/div[3]/div[1]/div/div").get().strip()
        yield item