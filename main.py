import csv
import requests
import re

links = []
base_url = "https://dnr.wisconsin.gov"
def get_html(url):
    f_url = base_url + url
    return requests.get(f_url).text

def get_links(text):
    pattern = '(?:href=)"([^"]+)'
    matches = re.findall(pattern, text)
    i = 0
    for m in matches:
        m = base_url + m
        i+=1
    return matches[31:44]

def parse_pargraphs_html(text):
    pattern = r'<p>(.*?)</p>'
    paragraphs = re.findall(pattern, text, re.DOTALL)
    pattern = r'<[^>]*>'
    cleaned_text = [re.sub(pattern, '', p) for p in paragraphs]
    return cleaned_text[:-2]

def export_csv(list_of_values):
    file_path = 'species_info.csv'

    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Species Name', ''])
        [csv_writer.writerow(v) for v in list_of_values]

if __name__ == '__main__':
    links.append("/topic/Fishing/species")
    main_text = get_html(links.pop())
    fish_links = get_links(main_text)
    for l in fish_links:
        links.append(l)

    information = []
    while (len(links) > 0):
        text = get_html(links.pop())
        information.append(parse_pargraphs_html(text))

    export_csv(information)

    #get html
    #parse html into paragraphs
    #get all links and add to list
    #loop until links are empty