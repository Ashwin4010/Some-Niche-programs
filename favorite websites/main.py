import webbrowser as wb


def webauto():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    URLS = (
        "stackoverflow.com",
        "github.com/ashwin4010",
        "youtube.com"
    )

    for URL in URLS:
        print(f"opening: {URL}")
        wb.get(chrome_path).open(URL)

webauto()
