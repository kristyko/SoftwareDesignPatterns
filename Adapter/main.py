from .customs.auto import Auto
from .customs.customs import CustomsAdapter


if __name__ == '__main__':
    adapter = CustomsAdapter()

    ford = Auto(age=1, model="Ford", damaged=False, mileage=3000)
    car_price_ua, car_tax_ua = adapter.vehicle_price(ford), adapter.tax(ford)
    print(f"{ford}\nprice={car_price_ua}, tax={car_tax_ua}")

    print()
    truck = Auto(model="truck", age=5, mileage=10000, damaged=False)
    car_price_ua, car_tax_ua = adapter.vehicle_price(truck), adapter.tax(truck)
    print(f"{truck}\nprice={car_price_ua}, tax={car_tax_ua}")
