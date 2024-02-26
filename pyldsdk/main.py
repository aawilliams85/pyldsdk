import os
from pythonnet import load
from pythonnet import get_runtime_info

from .types import *

class LogixProject(object):
    def __init__(self, dll_path: str):
        self.log = []
        self.dll_path = dll_path
        self.__validate_dll_path()

        load('coreclr')
        import clr
        clr.AddReference(self.dll_path)
        from RockwellAutomation.LogixDesigner import LogixProject as LogixProjectModule
        self._ldsdk = LogixProjectModule

    def __download(self):
        self.log.append(f'Starting Download.')
        self._proj.DownloadAsync().Result
        self.log.append(f'Finished Download.')

    def __open(self, file_path: str):
        self.log.append(f'Opening project {file_path}.')
        self._proj = self._ldsdk.OpenLogixProjectAsync(file_path).Result
        self.log.append(f'Opened project {file_path}.')

    def __get_comms_path(self) -> str:
        self.log.append(f'Getting communications path.')
        return self._proj.GetCommunicationsPathAsync().Result

    def __get_controller_mode(self) -> ControllerMode:
        self.log.append(f'Getting controller mode.')
        return self._proj.ReadControllerModeAsync().Result
    
    def __save(self):
        self.log.append(f'Saving.')
        self._proj.SaveAsync().Result

    def __set_comms_path(self, comms_path: str):
        self.log.append(f'Setting communications path {comms_path}')
        self._proj.SetCommunicationsPathAsync(comms_path).Result

    def __set_controller_mode(self, mode):
        self.log.append(f'Setting controller to {mode} mode.')
        self._proj.ChangeControllerModeAsync(mode).Result
    
    def __set_controller_mode_program(self):
        return self.__set_controller_mode(self._ldsdk.RequestedControllerMode.Program)

    def __set_controller_mode_run(self):
        return self.__set_controller_mode(self._ldsdk.RequestedControllerMode.Run)

    def __upload_new(self, file_path: str, comms_path: str):
        self.log.append(f'Uploading controller {comms_path} to file {file_path}.')
        self._ldsdk.UploadToNewProjectAsync(file_path, comms_path).Result
    
    def __validate_dll_path(self):
        dir = os.path.dirname(self.dll_path)
        files = ['FtspAdapter.exe',
                 'Google.Protobuf.dll',
                 'Grpc.Core.Api.dll',
                 'Grpc.Net.Client.dll',
                 'Grpc.Net.Common.dll',
                 'Microsoft.Extensions.Logging.Abstractions.dll',
                 'Newtonsoft.Json.dll',
                 'RockwellAutomation.LogixDesigner.LogixProject.CSClient.dll']
        for file in files:
            file_path = os.path.join(dir, file)
            if not(os.path.exists(file_path)): raise Exception(f'File {file} not found in DLL Path {self.dll_path}.')

    def download(self, file_path: str, comms_path: str, **kwargs):
        require_start_in_program_mode = kwargs.get('require_start_in_program_mode', True)
        require_end_in_run_mode = kwargs.get('require_end_in_run_mode', False)

        self.__open(file_path)
        self.__set_comms_path(comms_path)
        self._initial_controller_mode = self.__get_controller_mode()
        if (self._initial_controller_mode != ControllerMode.Program):
            if require_start_in_program_mode:
                raise Exception('Controller was not in PROGRAM mode.  Change controller mode or use kwarg require_program_mode=False to bypass.')
            else:
                self.__set_controller_mode_program()

        self.__download()
        if (self._initial_controller_mode == ControllerMode.Run) or (require_end_in_run_mode): self.__set_controller_mode_run()
        self.__save()

    def upload_new(self, file_path: str, comms_path: str):
        self.__upload_new(file_path, comms_path)