import base64 as b64
from collections import Counter

text = 'V2F0ZXI='

try:
    org_text = b64.b16decode(text)
except Exception as err:
    print(err)

try:
    org_text = b64.b32decode(text)
except Exception as err:
    print(err)

try:
    org_text = b64.b64decode(text)
except Exception:
    print(err)

print(org_text)
