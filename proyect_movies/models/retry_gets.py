import requests
from requests.adapters import HTTPAdapter
from urllib3 .util.retry import Retry

def make_session(
        retries=5,
        backoff_factor=0.5,
        backoff_jitter=0.1,
        status_forcelist=(429, 500, 502, 503, 504),
):

    session = requests.Session()

    retry = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        backoff_jitter=backoff_jitter,
        status_forcelist=status_forcelist,
        allowed_methods=frozenset(["GET", "HEAD", "OPTIONS"]),
        raise_on_status=False,
    )

    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    
    return session








