import urllib.request

def download_file(url, destination, proxies=None):
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(proxies)
    )
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, destination)

# Example usage
file_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/114.0.5735.90/win32/chrome-win32.zip"
destination = "chrome-win32.zip"

# Specify your proxy details (optional)
http_proxy = "webguard.posten.no:8080"
https_proxy = "webguard.posten.no:8080"
ftp_proxy = "webguard.posten.no:8080"

proxies = {
    "http": http_proxy,
    "https": https_proxy,
    "ftp": ftp_proxy
}

download_file(file_url, destination, proxies)
