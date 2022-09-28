#All credits to Aishik Pyne
# https://github.com/aishik-pyne
# https://aishikpyne.com/
import requests
from urllib.parse import urljoin
from datetime import datetime

class IndianKanoon:
  """
    Search query	https://api.indiankanoon.org/search/?formInput=<query>&pagenum=<pagenum>
    Document	https://api.indiankanoon.org/doc/<docid>/
    Document fragments	https://api.indiankanoon.org/docfragment/<docid>/?formInput=<query>
    Document Metainfo	https://api.indiankanoon.org/docmeta/<docid>/
  """

  def __init__(self):
    self.base_url = "https://api.indiankanoon.org/"
    self.auth_token = "aa95ddefd0a5d1ce966b7241d2811dd7aad6f62d"

    self.headers = {
        'authorization': "Token {}".format(self.auth_token),
        'cache-control': "no-cache",
    }
    self.api_session = requests.Session()
    self.api_session.headers = self.headers

  def search(self, formInput, pagenum=0,
             fromdate=None, todate=None,
             title=None, author=None,
             cite=None, bench=None):
    #  Creating parameters
    params = {
        'formInput': formInput,
        'pagenum': pagenum
    }
    if fromdate:
      assert isinstance(fromdate, datetime) 
      params['fromdate'] = fromdate.strftime('%d-%m-&Y')

    if todate:
      assert isinstance(todate, datetime) 
      params['todate'] = todate.strftime('%d-%m-&Y')

    # Making the request
    response = self.api_session.post(
        urljoin(self.base_url, 'search/'), params=params)
    response.raise_for_status()
    return response.json()

  def doc(self, docid):
    response = self.api_session.post(
        urljoin(self.base_url, 'doc/{}/'.format(docid)))
    response.raise_for_status()
    return response.json()

  def docfragment(self, docid, formInput):
    params = {
        'formInput': formInput,
    }
    response = self.api_session.post(
        urljoin(self.base_url, 'docfragment/{}/'.format(docid)), params=params)
    response.raise_for_status()
    return response.json()

  def docmeta(self, docid):
    response = self.api_session.post(
        urljoin(self.base_url, 'docmeta/{}/'.format(docid)))
    response.raise_for_status()
    return response.json()
