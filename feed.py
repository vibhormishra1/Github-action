import xml.etree.ElementTree as ET
import yaml

with open('feed.yaml', 'r') as file:
    feed_data = yaml.safe_load(file)

    rss_element = ET.Element('rss', {    'version':'2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'})

channel_element = ET.SubElement(rss_element, 'channel')
link_prefix = feed_data['link']
ET.SubElement(channel_element, 'title').text = feed_data['title']

ET.SubElement(channel_element, 'format').text = feed_data['format']

ET.SubElement(channel_element, 'subtitle').text = feed_data['subtitle']

ET.SubElement(channel_element, 'itunes:author').text = feed_data['author']

ET.SubElement(channel_element, 'itunes:category',{'text':feed_data['category']})

ET.SubElement(channel_element, 'language').text = feed_data['language']
ET.SubElement(channel_element, 'link').text = link_prefix

for item in feed_data['item']:
    item_element = ET.SubElement(channel_element, 'item')
    ET.SubElement(item_element, 'title').text = item['title']
    ET.SubElement(item_element, 'itunes:author').text = feed_data['author']
    ET.SubElement(item_element, 'description').text = item['description']
    ET.SubElement(item_element, 'itunes:duration').text = item['duration']
    
    ET.SubElement(item_element, 'pubDate').text = item['published']
    # ET.SubElement(item_element, 'enclosure', {'url': link_prefix + item['enclosure']['url'], 'type': item['enclosure']['type']})

    enclosure = ET.SubElement(item_element, 'enclosure',{
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']

    })

output_tree = ET.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='utf-8', xml_declaration=True)

    
