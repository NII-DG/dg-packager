from urllib.parse import urlparse, urlunparse
from urllib.parse import urljoin
from urllib.parse import urlunparse

class UrlOperator:
    def __init__(self, url) -> None:
        self.url = url

    def get_url(self)->str:
        return self.url

    def get_scheme(self)->str:
        '''
        return http, https or ssh
        '''
        return urlparse(self.url).scheme

    def get_netloc(self) -> str:
        '''
        return domain
        '''
        return urlparse(self.url).netloc

    def get_path(self) -> str:
        '''
        return path
        '''
        return urlparse(self.url).path

    def get_params(self) -> str:
        return urlparse(self.url).params

    def get_query(self) -> str:
        return urlparse(self.url).query

    def get_fragment(self) -> str:
        return urlparse(self.url).fragment

    def get_baseurl(self) -> str:
        return urlunparse(
            (
                self.get_scheme(),
                self.get_netloc(),
                '',
                '',
                '',
                '',
            )
        )

    def join_to(self, relative_path):
        return urljoin(self.get_baseurl(), relative_path)

    def update_url(self, url):
        self.url = url

    def update_scheme_to_url(self, scheme:str):
        updated_url = urlunparse(
            (
                scheme,
                self.get_netloc(),
                self.get_path(),
                self.get_params(),
                self.get_query(),
                self.get_fragment(),
            )
        )
        self.url = updated_url

    def update_netloc_to_url(self, netloc:str):
        updated_url = urlunparse(
            (
                self.get_scheme(),
                netloc,
                self.get_path(),
                self.get_params(),
                self.get_query(),
                self.get_fragment(),
            )
        )
        self.url = updated_url



    def update_path_to_url(self, path:str):
        updated_url = urlunparse(
            (
                self.get_scheme(),
                self.get_netloc(),
                path,
                self.get_params(),
                self.get_query(),
                self.get_fragment(),
            )
        )
        self.url = updated_url

    def add_path_to_url(self, additional_path:str):
        path = f'{self.get_path()}/{additional_path}'
        self.update_path_to_url(path)
