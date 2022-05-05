import requests

for i in range(1,11):
    print(f"Page nuumber : {i}")
    response = requests.get(url=f"https://quotes.toscrape.com/page/{i}/")
    response.raise_for_status()
    website_text = response.text.split("\n")
    with open("Authors.txt","a",encoding="utf-8") as file:
        for line in website_text:
            if '<span>by <small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">',"").replace("</span>","").replace("</small>","")
                line = line.strip()
                file.write(line)
                file.write("\n")

        print(f"Authors names were written to the file.")

