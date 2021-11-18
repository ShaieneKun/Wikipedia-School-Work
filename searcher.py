from selenium.webdriver.common.keys import Keys

import xpaths

GOOGLE_URL = "https://www.google.com"


def search_keyword_in_url(link_tags: list, keyword: str = "wikipedia") -> str | None:
    for link in link_tags:
        url = link.get_attribute("href")

        if not isinstance(url, str):
            continue

        if keyword in url.lower():
            return url
    return None


def google_search(driver, text: str) -> str | None:
    driver.get(GOOGLE_URL)

    search_bar = driver.find_element_by_xpath(xpaths.google.get("search"))
    search_bar.send_keys(text)
    search_bar.send_keys(Keys.ENTER)

    link_tags = driver.find_elements_by_tag_name("a")

    if not isinstance(link_tags, list):
        return None

    url = search_keyword_in_url(link_tags)

    return url


def wikipedia_search_summary(driver, url: str):
    driver.get(url)
    paragraph_tags = driver.find_elements_by_tag_name("p")

    if not isinstance(paragraph_tags, list):
        return None

    paragraphs_text = [paragraph.text for paragraph in paragraph_tags]

    text = "\n\n".join(paragraphs_text)
    text = text.strip()

    return text
