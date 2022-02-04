from SoftwareDesignPatterns.AbstractFactory.MunicipalTransport.abstract_classes import Bus, Tram, Trolley, TransportFactory


class VolvoBus(Bus):
    def __init__(self):
        super().__init__(6000000, 20)

    def go_by_road(self):
        print("Volvo Bus runs!")


class VolvoTram(Tram):
    def __init__(self):
        super().__init__(10000000, 7)

    def go_by_rails(self):
        print("Volvo Tram goes!")


class VolvoTrolley(Trolley):
    def __init__(self):
        super().__init__(7000000, 13)

    def go_by_contact_network(self):
        print("Volvo Trolleybus runs!")


class VolvoFactory(TransportFactory):
    def create_bus(self) -> Bus:
        return VolvoBus()

    def create_tram(self) -> Tram:
        return VolvoTram()

    def create_trolley(self) -> Trolley:
        return VolvoTrolley()
