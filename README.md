# pymeu

PyLDSDK (Python Logix Designer SDK) is a set of helper functions built around pythonnet to interface with Rockwell Automation Logix 5000 PLCs.<br>

Use at your own risk.<br>

## Installation

Todo.  Not yet packaged, not sure best way to handle setup for components that can't be distributed.

## Basic Examples

Use the download function to transfer an *.ACD file to the PLC:

```python
from pyldsdk import LogixProject
proj = LogixProject()
proj.download('C:\\YourFolder\\YourProgram.ACD', 'YourDriver\\YourControllerIpAddress')
```

Use the upload function to transfer an *.ACD file from the PLC:

```python
from pyldsdk import LogixProject
proj = LogixProject()
proj.upload_new('C:\\YourFolder\\YourProgram.ACD', 'YourDriver\\YourControllerIpAddress')
```