# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads import test_config

ad_account_id = test_config.account_id

# _DOC open [ADLABEL_CREATE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdLabel

label = AdLabel(parent_id=ad_account_id)
label[AdLabel.Field.name] = 'AdLabel name'
label.remote_create()
# _DOC close [ADLABEL_CREATE]

ad_label_id = label[AdLabel.Field.id]

# _DOC open [ADLABEL_UPDATE]
# _DOC vars [ad_label_id]
from facebookads.objects import AdLabel

adlabel = AdLabel(ad_label_id)
adlabel[AdLabel.Field.name] = 'New AdLabel Name'
adlabel.remote.update()
# _DOC close [ADLABEL_UPDATE]

# _DOC open [ADLABEL_DELETE]
# _DOC vars [ad_label_id]
from facebookads.objects import AdLabel

adlabel = AdLabel(ad_label_id)
adlabel.remote.delete()
# _DOC close [ADLABEL_DELETE]