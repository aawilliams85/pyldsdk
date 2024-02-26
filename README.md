# pyldsdk

PyLDSDK (Python Logix Designer SDK) is a simple wrapper for some of the features available in Rockwell Automation's Logix Designer SDK v1.01.<br>

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