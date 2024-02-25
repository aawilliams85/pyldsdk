from pythonnet import load
from pythonnet import get_runtime_info

from .types import *

class LogixProject(object):
    def __init__(self, **kwargs):
        self.dll_path = kwargs.get('dll_path', 'C:\\AAA_LDSDK\\RockwellAutomation.LogixDesigner.LogixProject.CSClient.DLL')
        load('coreclr')
        import clr
        clr.AddReference(self.dll_path)
        from RockwellAutomation.LogixDesigner import LogixProject as LogixProjectModule
        self._ldsdk = LogixProjectModule

    def __download(self) -> bool:
        print(f'Starting Download.')
        self._proj.DownloadAsync().Result
        print(f'Finished Download.')
        return True

    def __open(self, file_path: str) -> bool:
        print(f'Opening project {file_path}')
        self._proj = self._ldsdk.OpenLogixProjectAsync(file_path).Result
        return True

    def __get_comms_path(self) -> str:
        pass

    def __get_controller_mode(self) -> ControllerMode:
        print(f'Getting controller mode.')
        return self._proj.ReadControllerModeAsync().Result
    
    def __save(self) -> bool:
        print(f'Saving.')
        self._proj.SaveAsync().Result
        return True

    def __set_comms_path(self, comms_path: str) -> bool:
        print(f'Setting communications path {comms_path}')
        self._proj.SetCommunicationsPathAsync(comms_path).Result
        return True

    def __set_controller_mode(self, mode) -> bool:
        print(f'Setting controller to {mode} mode.')
        self._proj.ChangeControllerModeAsync(mode).Result
        return True
    
    def __set_controller_mode_program(self):
        return self.__set_controller_mode(self._ldsdk.RequestedControllerMode.Program)

    def __set_controller_mode_run(self):
        return self.__set_controller_mode(self._ldsdk.RequestedControllerMode.Run)

    def __upload_new(self, file_path: str, comms_path: str) -> bool:
        print(f'Uploading controller {comms_path} to file {file_path}.')
        self._ldsdk.UploadToNewProjectAsync(file_path, comms_path).Result
        return True
    
    def download(self, file_path: str, comms_path: str) -> bool:
        self.__open(file_path)
        self.__set_comms_path(comms_path)

        self._initial_controller_mode = self.__get_controller_mode()
        if (self._initial_controller_mode != ControllerMode.Program): self.__set_controller_mode_program()

        self.__download()
        if (self._initial_controller_mode == ControllerMode.Run): self.__set_controller_mode_run()
        self.__save()
        return True

    def upload_new(self, file_path: str, comms_path: str) -> bool:
        self.__upload_new(file_path, comms_path)
        return True