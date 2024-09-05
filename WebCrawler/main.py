import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

response = requests.get("https://www.scrapingcourse.com/ecommerce/")
k = (response.content.decode("utf-8"))

k = k.strip("/")

urls = ["https://www.scrapingcourse.com/ecommerce/"]
while len(urls) > 0:
    cur = urls.pop()
    # print(cur)
    products = []
    try:
        response  = requests.get(cur)
        # print(response.content.decode("utf-8")[0])
        soup = BeautifulSoup(response.content, "html.parser")

        links = soup.find_all('a')
        # The loop iterates over each link and prints the href value.
        for link in links:
            href = link.get('href') #Retrieves the href attribute of the <a> tag, which contains the URL of the link.
            urls.append(href)
            # print(href)
        # if current_url is product page

        # images = soup.find_all('img')
        # for img in images:
        #     src = img.get('src')
        #     if src:
        #         full_url = urljoin(cur, src)  # Construct full URL
        #         print("Image URL:", src)

        # Find and print all product names
        # product_names = soup.find_all('h2', class_='product-title')
        # for product in product_names:
        #     name = product.get_text(strip=True)
        #     print("Product Name:", name)

        # if current_url is product page
        product = {}
        product["url"] = cur
        product["image"] = soup.select_one(".wp-post-image")["src"]
        product["name"] = soup.select_one(".product_title").text()
        product["price"] = soup.select_one(".price")
     
        print(product)
        
        # Modify your code to extract the product names based on the structure you identified. 
        # For this example, let’s assume product names are in <h2> tags with the class product-title.
        # You would need to adapt this to the actual structure of the webpage you are scraping.

        
    except Exception as e: 
        # print("Failed to fetch urls from " + cur + " Exception details: " + str(e.__traceback__))
        pass
    
    with open('products.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
    
        # populating the CSV
        for product in products:
            writer.writerow(product.values())