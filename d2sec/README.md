## DSquare Elliot Plugin for vFeed Professional Services
### (beta)

To run properly this plugin, you must have a valid "Elliot Framework" subscription.

With this first beta release, the `d2sec plugin` comes with few methods:

* **start()** : basic command to start the framework
* **version()** : returns the framework version
* **get_exploits()** : retrieves the list of all available exploit
* **get_sessions()** : enumerates the valid sessions whenever an exploit succeeded.
* **set_target()** : sets and lists the target to be exploited


### CMD usage

You must run from `pyvfeed.py` with the following:

    pyvfeed.py --plugin d2sec ""

and with a target (case of set_target)

    pyvfeed.py --plugin d2sec http://www.toolswatch.org

### Set the appropriate method in pyvfeed.py

        import importlib
        sys.path.append("..")
        api_class = getattr(importlib.import_module(module),"api")

        # check the plugin name and version
        api_class().test()

        # start the framework
        api_class().start()

        # check framework version
        print(api_class().version())

        # list exploits
        print(api_class().get_exploits())

        # retrieve available sessions
        print(api_class().get_sessions())

        # setting the target
        api_class().set_target(target)

