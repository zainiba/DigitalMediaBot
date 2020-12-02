from bs4 import BeautifulSoup
import requests


source = requests.get('http://switch.sjsu.edu/archive/wp/v28/index.html%3Fp=571.html').text
soup = BeautifulSoup(source, 'lxml')
final_text = []
essay = soup.find('div',class_='content clearfix')
summary = essay.find_all('p')
with open(r"C:\Users\zai_n\Documents\pythonbottexts\article22.txt", "w") as file:
    file.write(str(summary))
print(summary)
