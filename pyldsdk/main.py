from pythonnet import load
from pythonnet import get_runtime_info

class LogixProject(object):
    def __init__(self, **kwargs):
        self.dll_path = kwargs.get('dll_path', 'C:\\AAA_LDSDK\\RockwellAutomation.LogixDesigner.LogixProject.CSClient.DLL')
        load('coreclr')
        import clr
        clr.AddReference(self.dll_path)
        from RockwellAutomation.LogixDesigner import LogixProject as LogixProjectModule
        self.ldsdk = LogixProjectModule
    
    def download(self, file_path: str, comms_path: str) -> int:
        print(f'Opening project {file_path}')
        self.proj = self.ldsdk.OpenLogixProjectAsync(file_path).Result

        print(f'Setting communications path {comms_path}')
        self.proj.SetCommunicationsPathAsync(comms_path).Result

        print(f'Getting controller mode.')
        self.initial_mode = self.proj.ReadControllerModeAsync().Result
        print(f'Controller is in {self.initial_mode} mode.')
        if (self.initial_mode != self.ldsdk.ControllerMode.Program):
            print(f'Controller needs to change to PROGRAM mode.')
            self.proj.ChangeControllerModeAsync(self.ldsdk.RequestedControllerMode.Program)
            print(f'Controller changed to PROGRAM mode.')

        print(f'Starting Download.')
        self.result = self.proj.DownloadAsync().Result
        print(f'Finished Download.')

        if (self.initial_mode != self.ldsdk.ControllerMode.Program) or (1):
            print(f'Controller needs to change to RUN mode.')
            self.proj.ChangeControllerModeAsync(self.ldsdk.RequestedControllerMode.Run)
            print(f'Controller changed to RUN mode.')

        print(f'Saving.')
        self.result = self.proj.SaveAsync().Result
        print(f'Finished saving.')        

        return 0

    def upload_new(self, file_path: str, comms_path: str) -> int:
        return self.ldsdk.UploadToNewProjectAsync(file_path, comms_path).Result