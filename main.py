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


#Add proxies only if needed
download_file(file_url, destination)
