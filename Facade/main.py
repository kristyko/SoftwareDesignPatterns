import car_components


class CarFacade:
    def drive(self):
        ignition = car_components.Ignition()
        clutch = car_components.Clutch()
        accelerator = car_components.Accelerator()
        gearStick = car_components.GearStick()
        handbrake = car_components.Handbrake()

        ignition.turn_on()
        clutch.press()
        gearStick.change_gear(1)
        accelerator.press()
        clutch.lift()
        handbrake.push_down()
        accelerator.press()
        clutch.press()


if __name__ == '__main__':
    print("===Mechanic===")
    ignition = car_components.Ignition()
    clutch = car_components.Clutch()
    accelerator = car_components.Accelerator()
    gearStick = car_components.GearStick()
    handbrake = car_components.Handbrake()

    ignition.turn_on()
    clutch.press()
    gearStick.change_gear(1)
    accelerator.press()
    clutch.lift()
    handbrake.push_down()
    accelerator.press()
    clutch.press()

    # use Facade
    print()
    print("===Automatic===")
    car = CarFacade()
    car.drive()

