# Copyright (c) 2022 University of Glasgow
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import datetime
import json

from pathlib                  import Path
from ietfdata.rfcindex        import *
from ietfdata.datatracker     import *
from ietfdata.datatracker_ext import *

dt   = DataTrackerExt()
ri   = RFCIndex()
http = requests.Session()
rfcs = {}

for rfc in ri.rfcs(since="2000-08", until="2022-07"):
    rfcs[rfc.doc_id] = {
        "doc_id"  : rfc.doc_id,
        "title"   : rfc.title,
        "authors" : rfc.authors,
        "date"    : rfc.date().strftime("%Y-%m"),
        "draft"   : rfc.draft,
        "stream"  : rfc.stream,
        "area"    : rfc.area,
        "wg"      : rfc.wg
    }

with open("data/rfc_list.json", "w") as outf:
    outf.write(json.dumps(rfcs, indent=4))

