from .session import *


class UpgradableCookieSession(CookieSession):
    "A CookieSession with different expiry parameters for elevated privileges"

    def __init__(self, request, elevated=False,
                 cookie_expires=True, elevated_expires=False, **kwargs):
        self.elevated = elevated
        self.elevated_expires = elevated_expires
        self.basic_expires = cookie_expires
        super(UpgradableCookieSession, self).__init__(
            request, cookie_expires=cookie_expires, **kwargs)

    def _set_cookie_expires(self, expires):
        if self.elevated:
            self.expires = elevated_expires
        else:
            self.expires = basic_expires
        super(UpgradableCookieSession, self)._set_cookie_expires(expires)

    def elevate_privilege(self, elevated=True):
        # Indicate whether a session has elevated privileges.
        # Maybe this should be added to Session.
        if self.elevated != elevated:
            self.elevated = elevated
            self.regenerate_id()
