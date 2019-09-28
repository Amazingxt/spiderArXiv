###############################################################################
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:04:45 2015

@author: Mingzhong
"""
###############################################################################

import json
json_file = open('./quantum_article.json','rb+')

da = json.dumps(json_file)
data = json.loads(da)
print data