from __future__ import annotations

from abc import abstractmethod, ABC


class Spy(ABC):
    @abstractmethod
    def visit_general_staff(self, general_staff: GeneralStaff): pass

    @abstractmethod
    def visit_military_base(self, military_base: MilitaryBase): pass


class SecretAgent(Spy):
    def visit_general_staff(self, general_staff: GeneralStaff):
        print(f"Secret agent has collected secret info: {general_staff}")

    def visit_military_base(self, military_base: MilitaryBase):
        print("Secret agent managed to come to military base unnoticed but found no secret info")


class Diversant(Spy):
    def visit_general_staff(self, general_staff: GeneralStaff):
        print("Diversant managed to come to general staff")

    def visit_military_base(self, military_base: MilitaryBase):
        print(f"Diversant destroyed a military base: {military_base}")


# ========= MILITARY OBJECTS ==========

class GeneralStaff:
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def __str__(self):
        return (
            f"GeneralStaff: У генеральному штабі є {self.generals} геренералів "
            f"та {self.secretPaper} секретних паперів."
        )

    def accept(self, spy: Spy):
        spy.visit_general_staff(self)


class MilitaryBase:
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        return (
            f"MilitaryBase: На військовій базі є {self.officers} офіцерів,"
            f" {self.soldiers} солдатів, {self.jeeps} джипів та {self.tanks} танків."
        )

    def accept(self, spy: Spy):
        spy.visit_military_base(self)


if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100)
    militaryBase = MilitaryBase(10, 1000, 300, 20)

    secret_agent = SecretAgent()
    diversant = Diversant()
    secret_agent.visit_military_base(militaryBase)
    secret_agent.visit_general_staff(generalStaff)
    diversant.visit_military_base(militaryBase)
    diversant.visit_general_staff(generalStaff)