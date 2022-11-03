import requests
import lxml, bs4

from PIL import Image
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Parser(object):

    def __init__(self, inquiry: str):
        total_inquiry = str("+".join(inquiry.split()))
        self.pre = "https://www.google.com"
        if self.pre not in inquiry:
            self.inquiry = f"""https://www.google.com/search?q={total_inquiry}"""
        else:
            self.inquiry = inquiry
        self.headers = {
            "Accept": "* / *",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }

        self.html_text = requests.get(self.inquiry, self.headers).text
        self.soup = bs4.BeautifulSoup(self.html_text, "lxml")  # полученный код штмл странички


class MainPage(Parser):
    def __init__(self, inquiry: str):
        super().__init__(inquiry)
        self.up_tools = []
        self.up_link = []
        self.content = {}

    def main_page_tools(self):
        self.up_tools = self.soup.find_all("a", class_="eZt8xd")
        self.up_link = [i.get("href") for i in self.up_tools]
        itog = []
        for i in self.up_link:
            itog.append(self.pre + i)

        return itog


class ImageParsing(MainPage):
    """ It downloads images """

    def __init__(self, inquiry: str):
        super().__init__(inquiry)
        total_inquiry = str("+".join(inquiry.split()))
        self.pre = "https://www.google.com"
        if self.pre not in inquiry:
            self.inquiry = f"""https://www.google.com/search?q={total_inquiry}"""
        else:
            self.inquiry = inquiry
        self.headers = {
            "Accept": "* / *",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }

        self.html_text = requests.get(self.inquiry, self.headers).text
        self.soup = bs4.BeautifulSoup(self.html_text, "lxml")  # полученный код штмл странички
        parser = MainPage(inquiry)
        for _ in parser.main_page_tools():
            if "tbm=isch" in _:
                self.image_link = _

        EXE_PATH = r'chromedriver.exe'
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(executable_path=EXE_PATH, chrome_options=options)
        driver.set_window_size(1440, 900)

        driver.get(str(self.image_link))
        driver.execute_script("""
                var elems = document.getElementsByClassName(" bRMDJf islir");
        elems[0].click();""")
        s = driver.page_source
        q = s
        self.res = []
        new = s.rfind('.png"')
        while new != -1:
            w = s[new - 100:new + 5]
            self.res.append(w[w.rfind('"https') + 1:-1])
            s = s[0:new - 10]
            new = s.rfind('.png"')
        self.res.pop(-1)
        self.res.pop(-1)
        self.res.pop(-1)

        new = q.rfind('.jpg"')
        while new != -1:
            w = q[new - 300:new + 5]
            self.res.append(w[w.rfind('"https') + 1:-1])
            q = q[0:new - 10]
            new = q.rfind('.jpg"')

    def download_image(self):
        for i, url in enumerate(self.res):
            try:
                img = requests.get(url)
                img_file = open(f"image_{i}", 'wb')
                img_file.write(img.content)
                img_file.close()
                dog_jpg = Image.open(f"image_{i}")
                dog_jpg.save(f'images/image_{i}.png', format='PNG')
                try:
                    os.remove(f"image_{i}")
                except:
                    pass
            except Exception:
                pass
            if i == 10:
                break


if __name__ == "__main__":

    impa = ImageParsing(input())
    impa.download_image()