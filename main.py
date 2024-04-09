# Redirect stdout to nothing (/dev/null) in Python

import contextlib

with contextlib.redirect_stdout(None):
    print('This gets redirected to nothing')

print('This message is shown')