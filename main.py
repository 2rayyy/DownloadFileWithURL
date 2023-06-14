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
http_proxy = "proxy:8080"
https_proxy = "proxy:8080"
ftp_proxy = "proxy:8080"

#if you are not using proxies, remove the variable called proxies
proxies = {
    "http": http_proxy,
    "https": https_proxy,
    "ftp": ftp_proxy
}

#again - if you are not using proxies, remove the variable called proxies
download_file(file_url, destination, proxies)
