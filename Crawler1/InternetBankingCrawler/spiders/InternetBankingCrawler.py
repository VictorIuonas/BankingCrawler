# -*- coding: utf-8 -*-
import logging

from scrapy import Spider, FormRequest
from scrapy.utils.response import open_in_browser

from InternetBankingCrawler.spiders.factories import build_login_request_service

logger = logging.getLogger(__name__)


class InternetBankingCrawlerSpider(Spider):
    name = 'crawl_ib'
    allowed_domains = ['bancsabadell.com']
    proxy_list = ['http://165.227.71.60:80', 'http://192.140.42.83:52852', 'http://182.52.238.44:37758']

    def __init__(self, *args, **kwargs):
        super(InternetBankingCrawlerSpider, self).__init__(*args, **kwargs)
        self.login_req_service = build_login_request_service()

    def start_requests(self):
        print('calling start requests')

        url, form_data, headers, cookies = self.login_req_service.get_do_login_request()

        req = FormRequest(
            url=url,
            callback=self.parse_do_login_page,
            errback=self.parse_error,
            headers=headers,
            cookies=cookies,
            formdata=form_data,
            meta={
                # 'proxy': self.proxy_list[randrange(len(self.proxy_list))],
                'max_retry_times': 0
            }
        )

        yield req

    def parse_error(self, failure):
        print(f'failure: {repr(failure)}')

    def parse_do_login_page(self, response):
        print(f'response for public IB page {response.status}, content: {response.text}')
        self.login_req_service.set_cookies(response.headers.getlist("Set-Cookie"))

        url, form_data, headers, cookies = self.login_req_service.get_set_logged_in_request()

        req = FormRequest(
            url=url,
            callback=self.parse_set_logged_in_page,
            errback=self.parse_error,
            headers=headers,
            cookies=cookies,
            formdata=form_data,
            meta={
                # 'proxy': self.proxy_list[randrange(len(self.proxy_list))],
                'max_retry_times': 0
            }
        )

        yield req

    def parse_set_logged_in_page(self, response):
        print(f'response for the second request {response.status}')
        open_in_browser(response)
