from typing import Optional

from SoftwareDesignPatterns.AbstractFactory.MunicipalTransport.abstract_classes import TransportFactory
from SoftwareDesignPatterns.AbstractFactory.MunicipalTransport.skoda import SkodaFactory
from SoftwareDesignPatterns.AbstractFactory.MunicipalTransport.volvo import VolvoFactory


def client_code(brand: str) -> Optional[int]:
    number_buses, number_trams, number_trolleys = 10, 5, 40
    N = 200000  # орієнтований пробіг експлуатації

    if brand == "Skoda":
        factory: TransportFactory = SkodaFactory()
    elif brand == "Volvo":
        factory: TransportFactory = VolvoFactory()
    else:
        return

    buses = [factory.create_bus() for _ in range(number_buses)]
    trams = [factory.create_tram() for _ in range(number_trams)]
    trolleys = [factory.create_trolley() for _ in range(number_trolleys)]

    final_cost_contract = (
        sum([bus.get_cost() + bus.get_usage_cost() * N for bus in buses])
        + sum([tram.get_cost() + tram.get_usage_cost() * N for tram in trams])
        + sum([trolley.get_cost() + trolley.get_usage_cost() * N for trolley in trolleys])
    )
    return final_cost_contract


if __name__ == "__main__":
    contract_cost = client_code("Volvo")  # returns 541000000
    # contract_cost = client_code("Skoda")  # returns 524000000
    print(contract_cost)
