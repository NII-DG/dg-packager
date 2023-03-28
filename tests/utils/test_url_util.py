from unittest import TestCase
from dg_packager.utils.url_util import UrlOperator

class TestUrlOperator(TestCase):
    # test exec : python -m unittest tests.utils.test_url_util

    def test_url_operator(self):
        url = "http://sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1"
        url_ope = UrlOperator(url)

        self.assertEqual('http', url_ope.get_scheme())
        self.assertEqual('sample.co.jp', url_ope.get_netloc())
        self.assertEqual('/sanmple/path', url_ope.get_path())
        self.assertEqual('param1', url_ope.get_params())
        self.assertEqual('key1=value11&key2=value2', url_ope.get_query())
        self.assertEqual('frag1', url_ope.get_fragment())
        self.assertEqual('http://sample.co.jp', url_ope.get_baseurl())


        url = "http://sample.co.jp"
        url_ope = UrlOperator(url)

        self.assertEqual('http', url_ope.get_scheme())
        self.assertEqual('sample.co.jp', url_ope.get_netloc())
        self.assertEqual('', url_ope.get_path())
        self.assertEqual('', url_ope.get_params())
        self.assertEqual('', url_ope.get_query())
        self.assertEqual('', url_ope.get_fragment())
        self.assertEqual('http://sample.co.jp', url_ope.get_baseurl())

    def test_join_to(self):
        url = "http://sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1"
        url_ope = UrlOperator(url)

        new_path = 'newsanmple/newpath'
        self.assertEqual('http://sample.co.jp/newsanmple/newpath', url_ope.join_to(new_path))


    def test_update_scheme_to_url(self):
        url = "http://sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1"
        url_ope = UrlOperator(url)

        url_ope.update_scheme_to_url('https')
        self.assertEqual('https://sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1', url_ope.get_url())

        url = "http://sample.co.jp/sanmple/path"
        url_ope = UrlOperator(url)

        url_ope.update_scheme_to_url('https')
        self.assertEqual('https://sample.co.jp/sanmple/path', url_ope.get_url())

    def test_update_netloc_to_url(self):
        url = "http://sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1"
        url_ope = UrlOperator(url)

        url_ope.update_netloc_to_url('user:pass@sample.co.jp')
        self.assertEqual('http://user:pass@sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1', url_ope.get_url())

    def test_update_url(self):

        url = "http://sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1"
        url_ope = UrlOperator(url)
        new_url = "http://new_sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1"
        url_ope.update_url(new_url)
        self.assertEqual('http://new_sample.co.jp/sanmple/path;param1?key1=value11&key2=value2#frag1', url_ope.get_url())
