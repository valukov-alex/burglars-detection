import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for dir in ['train', 'test']:
        image_path = os.path.join(os.getcwd(), 'annotations/{}'.format(dir))
        xml_df = xml_to_csv(image_path)
        for i in range(xml_df['filename'].size):
            name = xml_df['filename'][i]
            if name[-5:] != '.JPEG':
                xml_df.set_value(i, 'filename', '{}.JPEG'.format(name))
                label = xml_df['class'][i]
                if label == 'n02764044':
                    xml_df.set_value(i, 'class', 'axe')
                elif label == 'n03481172':
                    xml_df.set_value(i, 'class', 'hammer')
        xml_df.to_csv('data/{}_labels.csv'.format(dir), index=None)
    print('Successfully converted xml to csv.')


main()
