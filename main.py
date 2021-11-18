import sys

from selenium import webdriver

import searcher
import write_to_file


def main():
    search_text, maximized = get_args()

    with webdriver.Chrome() as driver:
        if not maximized:
            driver.minimize_window()

        url = found_wikipedia_page = searcher.google_search(driver, search_text)

        if not found_wikipedia_page:
            print("A Wikipedia link was not found")
            return

        text = searcher.wikipedia_search_summary(driver, url)

        if not text:
            print("Summary was not found")
            return

    write_to_file.write(text)


def get_args():
    USAGE = (
        "Usage: python3.10 main.py [OPTIONS]\n"
        "-m              Shows the browser on screen (defaults to minimized).\n"
        "-k [key_phrase]  Searches for key_phrase, defaults to 'hello world'.\n"
    )
    args = sys.argv

    key_phrase = "hello world"
    maximized = False

    match len(args):
        case 1:
            print(USAGE)
        case 2:
            print(USAGE)
            if args[1] == "-m":
                maximized = True
        case 3:
            if args[1] == "-m":
                print(USAGE)
                maximized = True
            elif args[1] == "-k":
                key_phrase = args[2]
        case 4:
            if args[1] == "-m":
                maximized = True
            if args[2] == "-k":
                key_phrase = args[3]

    return (key_phrase, maximized)


if __name__ == "__main__":
    main()
