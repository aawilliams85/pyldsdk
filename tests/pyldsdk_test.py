import unittest

from pyldsdk import LogixProject

# Turn off sort so that tests run in line order
unittest.TestLoader.sortTestMethodsUsing = None

class pyldsdk_tests(unittest.TestCase):
    def test_download(self):
        proj = LogixProject()
        proj.download('C:\\Users\\vm\\Desktop\\uploadtest.acd', 'HL\\192.168.40.122')

    def test_upload_new(self):
        proj = LogixProject()
        proj.upload_new('C:\\Users\\vm\\Desktop\\uploadtest.acd', 'HL\\192.168.40.122')

if __name__ == '__main__':
    unittest.main()