App.net
=======

App.net uses OAuth2. In order to enable the backend follow:

- Register an application at `Your Apps`_,
  set the ``Redirect URI`` to ``http://<your hostname>/complete/appdotnet/``

- Fill in the **Client ID** and **Client Secret** values in your settings::

    SOCIAL_AUTH_APPDOTNET_KEY = ''
    SOCIAL_AUTH_APPDOTNET_SECRET = ''

.. _Your Apps: https://account.app.net/developer/apps/
