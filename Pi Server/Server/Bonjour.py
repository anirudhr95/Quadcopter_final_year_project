
from zeroconf import ServiceInfo, Zeroconf
import socket
import Constants


class Bonjour(object):
    """
    Bonjour/Zeroconf handler.
    """

    def __init__(self):
        """
        Construct a new Bonjour/Zeroconf server. This server takes values supplied in the Constants.py file.
        """

        self.zeroconf = Zeroconf()
        self.info = ServiceInfo(type = Constants.BONJOUR_TYPE,
                                name = Constants.BONJOUR_NAME + '.' + Constants.BONJOUR_TYPE,
                                address = Constants.SERVER_IP,
                                port = Constants.SERVER_PORT,
                                weight= Constants.BONJOUR_WEIGHT,
                                priority= Constants.BONJOUR_PRIORITY,
                                properties= Constants.BONJOUR_DESC,
                                server= Constants.BONJOUR_SERVICE_NAME
                                )

    def publish(self):
        """
        Publishes the server
        """
        if Constants.ENABLE_BONJOUR_REGISTER:




            # info = ServiceInfo(type=Constants.BONJOUR_TYPE,
            #                    name=Constants.BONJOUR_NAME + '.' +             Constants.BONJOUR_TYPE,
            #                    address=Constants.BONJOUR_IP_ADDRESS,
            #                    port=80
            #                    )

            print("Registration of a service, press Ctrl-C to exit...")
            self.zeroconf.register_service(self.info)
        else:
            raise AssertionError("Bonjour is disabled")


    def unpublish(self):
        """
        Unpublish the bonjour server.
        If the server was not published, this method will not do anything.
        """
        self.zeroconf.unregister_service(self.info)

    def close(self):
        """
        Close the Zeroconf instance.
        """
        self.zeroconf.close()