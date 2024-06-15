import xml.etree.ElementTree as ET
class xmlfile():

    def XMLFile_read(self):
        tree = ET.parse('C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\sample.xml')
        root = tree.getroot()
        print(root)
        #print(len(root))
        for child in root:
            print(child.tag, child.attrib)
            print(child.attrib)
        print(root[0][1].text)
        for eachele in root.iter():
            print(eachele.tag)
        for neighbor in root.iter('neighbor'):
            print(neighbor.tag, neighbor.attrib)
        for rank in root.iter('rank'):
            new_rank = int(rank.text) + 1
            rank.text = str(new_rank)
            rank.set('Status', 'Pass')

        tree.write('C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\sample.xml')


obj=xmlfile()
obj.XMLFile_read()