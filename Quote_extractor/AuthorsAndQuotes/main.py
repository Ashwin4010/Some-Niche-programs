import requests
res = requests.get("https://quotes.toscrape.com/")
html = res.text

with open("quotes.csv","w") as file:
    for line in html.split("\n"):
        if '<span class="text" itemprop="text">' in line:
            line = line.replace('<span class="text" itemprop="text">',"")
            line = line.replace('</span>',"")
            quote = line.strip()

        if '<span>by <small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">',"")
            line = line.replace('</small>',"")
            author = line.strip()
            file.write(author +","+ quote)
            file.write("\n")