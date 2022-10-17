from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

PATH = r"C:\Users\ivank\PycharmProjects\my_assistant\auto_google\chromedriver.exe"

"""
It's better to use any special package(library)
"""


class ContextTranslateParser(object):
    """
    it translates just frase that could be translated definitely
    """

    def __init__(self):
        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": r"C:\Users\User\PycharmProjects\fackingNews",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        self.driver = webdriver.Chrome(executable_path=PATH, options=options)

    def translate(self, text_to_translate: str, input_lang: str, output_land: str) -> str:
        """
        get translation
        href="https://www.reverso.net/перевод-текста#sl=rus&tl=eng&text=inquiry"
        :param output_land:
        :param input_lang:
        :param text_to_translate: enter text, you want to translate
        :return: the translation of your text in english
        """

        base_inquiry = \
            f"""https://www.reverso.net/перевод-текста#sl={input_lang}&tl={output_land}&text={text_to_translate}"""

        self.driver.get(base_inquiry)

        try:
            self.driver.find_element(by=By.ID, value="didomi-notice-agree-button").click()
        except Exception as ex:
            pass

        time.sleep(2)
        translation = self.driver.find_element(by=By.CLASS_NAME, value="sentence-wrapper_without-hover")

        return translation.text

    def exit_(self):
        self.driver.close()