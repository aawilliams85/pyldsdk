# Deprecated

As of Logix Designer SDK v2.01.00, python clients are supported natively, so this is not useful.

# pyldsdk

PyLDSDK (Python Logix Designer SDK) is a simple wrapper for some of the features available in Rockwell Automation's Logix Designer SDK v1.01.00.<br>

Use at your own risk.<br>

## Installation

To install from pip:
```console
pip install pyldsdk
```

To upgrade from pip:
```console
pip install pyldsdk --upgrade
```

Since I cannot redistribute the C# client packaged with the Logix Designer SDK, there is a second step required to get started.  Copy all of the following files to a common directory (ex: C:\\YourDllPath).  Then when using pyldsdk, reference that path (and more specifically the *CSClient.dll) as shown in the Examples section.

There is probably a better way, but I found it easiest to compile any of the SDK's sample projects and copy these from the resulting Debug folder.

```console
FtspAdapter.exe
Google.Protobuf.dll
Grpc.Core.Api.dll
Grpc.Net.Client.dll
Grpc.Net.Common.dll
Microsoft.Extensions.Logging.Abstractions.dll
Newtonsoft.Json.dll
RockwellAutomation.LogixDesigner.LogixProject.CSClient.dll
```

## Basic Examples

Use the download function to transfer an *.ACD file to the PLC:

```python
from pyldsdk import LogixProject
proj = LogixProject('C:\\YourDllPath\\RockwellAutomation.LogixDesigner.LogixProject.CSClient.DLL')
proj.download('C:\\YourFolder\\YourProgram.ACD', 'YourDriver\\YourControllerIpAddress')
```

Use the upload function to transfer an *.ACD file from the PLC:

```python
from pyldsdk import LogixProject
proj = LogixProject('C:\\YourDllPath\\RockwellAutomation.LogixDesigner.LogixProject.CSClient.DLL')
proj.upload_new('C:\\YourFolder\\YourProgram.ACD', 'YourDriver\\YourControllerIpAddress')
```
