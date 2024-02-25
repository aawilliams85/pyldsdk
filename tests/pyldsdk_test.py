import json
import os
import unittest

from pyldsdk import LogixProject

# Turn off sort so that tests run in line order
unittest.TestLoader.sortTestMethodsUsing = None

class pyldsdk_tests(unittest.TestCase):
    def setUp(self):
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        self.config_path = os.path.join(self.base_path, 'config.json')
        with open(self.config_path, 'r') as f:
            self.config_data = json.load(f)

        self.download_folder_path = os.path.join(self.base_path, 'download')
        self.upload_folder_path = os.path.join(self.base_path, 'upload')
        self.proj = LogixProject()
        print('')

    def test_download(self):
        self.download_file_path = os.path.join(self.download_folder_path, self.config_data['file']['download']['good'])
        self.proj.download(self.download_file_path, self.config_data['comms_path']['good'])

    def test_upload_new(self):
        self.upload_file_path = os.path.join(self.upload_folder_path, self.config_data['file']['upload']['good'])
        if os.path.exists(self.upload_file_path): os.remove(self.upload_file_path)
        self.proj.upload_new(self.upload_file_path, self.config_data['comms_path']['good'])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()