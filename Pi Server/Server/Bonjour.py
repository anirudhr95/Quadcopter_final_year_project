from zeroconf import ServiceInfo, Zeroconf
import socket
import Constants


class Bonjour(object):
    """
    Bonjour/Zeroconf handler.
    """

    def __str__(self):
        return self.name

    def __repr__(self):
        return {'Name': self.name,
                "type": Constants.BONJOUR_TYPE,
                "name": Constants.BONJOUR_NAME + '.' + Constants.BONJOUR_TYPE,
                "addres": Constants.SERVER_IP,
                "port": Constants.SERVER_PORT,
                "weight": Constants.BONJOUR_WEIGHT,
                "priority": Constants.BONJOUR_PRIORITY,
                "properties": Constants.BONJOUR_DESC,
                "server": Constants.BONJOUR_SERVICE_NAME
                }

    def __init__(self, logger):
        """
        Construct a new Bonjour/Zeroconf server. This server takes values supplied in the Constants.py file.
        """


        self.logger = logger
        self.name = "Bonjour"

        self.zeroconf = Zeroconf()
        self.info = ServiceInfo(type=Constants.BONJOUR_TYPE,
                                name=Constants.BONJOUR_NAME + '.' + Constants.BONJOUR_TYPE,
                                address=Constants.SERVER_IP,
                                port=Constants.SERVER_PORT,
                                weight=Constants.BONJOUR_WEIGHT,
                                priority=Constants.BONJOUR_PRIORITY,
                                properties=Constants.BONJOUR_DESC,
                                server=Constants.BONJOUR_SERVICE_NAME
                                )

    def publish(self):
        """
        Publishes the server
        """

        self.logger.setup_init(self.name)
        if Constants.ENABLE_BONJOUR_REGISTER:

            # info = ServiceInfo(type=Constants.BONJOUR_TYPE,
            #                    name=Constants.BONJOUR_NAME + '.' +             Constants.BONJOUR_TYPE,
            #                    address=Constants.BONJOUR_IP_ADDRESS,
            #                    port=80
            #                    )

            print("Registration of a service, press Ctrl-C to exit...")
            self.zeroconf.register_service(self.info)
            self.logger.setup_success(self.name)
        else:
            self.logger.setup_failure(self.name)
            raise AssertionError("Bonjour is disabled")

    def unpublish(self):
        """
        Unpublish the bonjour server.
        If the server was not published, this method will not do anything.
        """
        self.logger.setup_message(self.name + "has been unpublished")
        self.zeroconf.unregister_service(self.info)

    def close(self):
        """
        Close the Zeroconf instance.
        """
        self.zeroconf.close()
