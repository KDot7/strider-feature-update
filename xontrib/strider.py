"""Xontrib for Strider."""

import strider

@aliases.register("s")
def _strider():
    strider.main()