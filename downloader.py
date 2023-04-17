import os
import urllib.request
from bs4 import BeautifulSoup


def get_raw_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "Referer": "https://www.statsf1.com/en/1950/grande-bretagne.aspx",
    }
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req)


def get_image_urls(html_code, filename):
    soup = BeautifulSoup(html_code, "html.parser")
    div = soup.find("div", {"class": "gpaffiche"})
    name = div.find_all("a")
    img = div.find_all("img")
    return (
        ["https://www.statsf1.com" + url["src"] for url in img],
        [n.text + f"_{filename}" for n in name],
    )


def download_images(image_url, filename):
    opener = urllib.request.build_opener()
    opener.addheaders = [
        (
            "User-Agent",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
        ),
        ("Referer", "https://www.statsf1.com/en/1950/grande-bretagne.aspx"),
    ]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(image_url, filename)
    print(f"Image downloaded: {filename}")


def create_folder(path, folder_name):
    path = os.path.join(path, folder_name)
    os.makedirs(path, exist_ok=True)
    print(f"Folder {folder_name} created successfully...")
    return path


def main():
    for year in range(1950, 2022):
        folder = create_folder(
            path="/home/fingerbruno/Pictures/f1_images", folder_name=str(year)
        )
        html = get_raw_html(f"https://www.statsf1.com/en/{year}.aspx")
        urls, names = get_image_urls(html, str(year))

        for url, name in zip(urls, names):
            download_images(url, os.path.join(folder, name))


if __name__ == "__main__":
    main()
