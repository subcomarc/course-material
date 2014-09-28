# -*- coding: utf-8 -*-
import sys
jackinabox = list(enumerate(sys.argv))
for i in jackinabox:
    print(' '.join(map(str, i)))
