from SoftwareDesignPatterns.AbstractFactory.MunicipalTransport.abstract_classes import Bus, Tram, Trolley, TransportFactory


class SkodaBus(Bus):
    def __init__(self):
        super().__init__(4500000, 25)

    def go_by_road(self):
        print("Skoda Bus runs!")


class SkodaTram(Tram):
    def __init__(self):
        super().__init__(9000000, 8)

    def go_by_rails(self):
        print("Skoda Tram goes!")


class SkodaTrolley(Trolley):
    def __init__(self):
        super().__init__(6800000, 13)

    def go_by_contact_network(self):
        print("Skoda Trolleybus runs!")


class SkodaFactory(TransportFactory):
    def create_bus(self) -> Bus:
        return SkodaBus()

    def create_tram(self) -> Tram:
        return SkodaTram()

    def create_trolley(self) -> Trolley:
        return SkodaTrolley()
