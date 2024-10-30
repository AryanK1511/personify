from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        data = {
            'title': soup.title.string if soup.title else 'No Title',
            'meta_description': '',
            'headings': {},
            'paragraphs': [],
            'images': [],
            'links': [],
            'metadata': {},
            'text_content': '',
        }

        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description and meta_description.get('content'):
            data['meta_description'] = meta_description['content']

        meta_tags = soup.find_all('meta')
        for meta in meta_tags:
            if meta.get('name') and meta.get('content'):
                data['metadata'][meta['name']] = meta['content']
            elif meta.get('property') and meta.get('content'):
                data['metadata'][meta['property']] = meta['content']

        for level in range(1, 7):  # h1 through h6
            heading_tag = f'h{level}'
            data['headings'][heading_tag] = [
                h.get_text(strip=True) for h in soup.find_all(heading_tag)
            ]

        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            data['paragraphs'].append(text)
            data['text_content'] += text + '\n'

        images = soup.find_all('img', src=True)
        for img in images:
            data['images'].append(
                {
                    'alt': img.get('alt', 'No alt text'),
                    'src': urljoin(url, img['src']),
                }
            )

        links = soup.find_all('a', href=True)
        for link in links:
            link_url = urljoin(url, link['href'])
            data['links'].append(
                {
                    'text': link.get_text(strip=True),
                    'url': link_url,
                    'type': 'internal' if url in link_url else 'external',
                }
            )

        return data

    except requests.exceptions.RequestException as e:
        print(f'Error fetching the URL: {e}')
        return None
