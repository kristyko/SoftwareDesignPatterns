from company import Employee, StaffList


def main():
    # Create team class object
    employees = [Employee("Zak"), Employee("Sarah"), Employee("Anna")]
    company = StaffList(employees)

    print('*** Iterate over the team object using for loop ***')
    # Iterate over team object(Iterable)
    for member in company:
        print(member)

    print('*** Iterate over the team object using while loop ***')
    # Get Iterator object from Iterable Team class object
    iterator = iter(company)
    # Iterate over the team object using iterator
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
