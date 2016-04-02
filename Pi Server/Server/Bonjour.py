
from zeroconf import ServiceInfo, Zeroconf
import socket
import Constants


class Bonjour(object):
    """
    DAAPServer Bonjour/Zeroconf handler.
    """

    def __init__(self):
        """
        Construct a new Bonjour/Zeroconf server. This server takes `DAAPServer`
        instances and advertises them.
        """

        self.zeroconf = Zeroconf()
        # self.info = ServiceInfo("_http._tcp.local.",
        #                                "Paul's aaTest Web Site._http._tcp.local.",
        #                                socket.inet_aton("127.0.0.1"), 80, 0, 0,
        #                                {'path': '/~paulsm/'}, "ash-2.local.")


        self.info = ServiceInfo(type = Constants.BONJOUR_TYPE,
                                name = Constants.BONJOUR_NAME + '.' + Constants.BONJOUR_TYPE,
                                address = socket.inet_aton(Constants.SERVER_IP),
                                port = Constants.SERVER_PORT,
                                weight= 0, priority= 0,
                                properties= Constants.BONJOUR_DESC,
                                server= Constants.BONJOUR_SERVICE_NAME
                                )

    def publish(self):
        """
        Publish a given `DAAPServer` instance.
        The given instances should be fully configured, including the provider.
        By default Zeroconf only advertises the first database, but the DAAP
        protocol has support for multiple databases. Therefore, the parameter
        `preferred_database` can be set to choose which database ID will be
        served.
        If the provider is not fully configured (in other words, if the
        preferred database cannot be found), this method will not publish this
        server. In this case, simply call this method again when the provider
        is ready.
        If the server was already published, it will be unpublished first.
        :param DAAPServer host_server: DAAP Server instance to publish.
        :param int preferred_database: ID of the database to advertise.
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
        Unpublish a given server.
        If the server was not published, this method will not do anything.
        :param DAAPServer daap_server: DAAP Server instance to publish.
        """

        self.zeroconf.unregister_service(self.info)

    def close(self):
        """
        Close the Zeroconf instance.
        """

        self.zeroconf.close()