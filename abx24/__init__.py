# -*- coding: utf-8 -*-
"""
usage:

   >>> from abx24 import Bitrix24
   >>> bx24 = Bitrix24('https://example.bitrix24.com/rest/1/some_key')
   >>> r = await bx24.call_method('crm.product.list')

Copyright (c) 2019 by Akop Kesheshyan.
"""

__version__ = '1.1.2'
__author__ = 'Niel (Ketov) Gorev <ketov-x@yandex.ru>'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 Niel (Ketov) Gorev'

from .bitrix24 import Bitrix24
from .exceptions import BitrixError
