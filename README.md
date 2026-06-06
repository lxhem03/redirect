# Koyeb Multi-Backend Redirect

Set:

BACKEND_URLS=https://app1.herokuapp.com,https://app2.herokuapp.com,https://app3.koyeb.app

Every request is redirected to a randomly selected backend.

Examples:

/watch/7189/file.zip?hash=ABC
/7189/file.zip?hash=ABC

All path and query parameters are preserved.
