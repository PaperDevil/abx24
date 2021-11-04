# Async Bitrix24 client for Python 3.6+
 
Клиент разработан на основе синхронного клиента Bitrix24-rest - https://pypi.org/project/bitrix24-rest/

## Usage
```python
from aiohttp import ClientSession
from abx24 import Bitrix24
bx24 = Bitrix24('')
await bx24.call_method('crm.customer.add', ClientSession(), fields={
    "NAME": 'Niel',
    "SECOND_NAME": 'Ketov'
})
```