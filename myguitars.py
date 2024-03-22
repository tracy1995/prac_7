from guitar import Guitar

def main():
    guitars = Guitar.load_guitars()

    print("My Guitars!")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

    guitars.sort()

    print("\nSorted Guitars by Year:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

    # Prompt user for new guitars
    add_another = input("Would you like to add another guitar? (yes/no): ").lower()
    while add_another == "yes":
        name = input("Enter the name of the guitar: ")
        year = int(input("Enter the year the guitar was made: "))
        cost = float(input("Enter the cost of the guitar: $"))
        guitars.append(Guitar(name, year, cost))
        add_another = input("Would you like to add another guitar? (yes/no): ").lower()

    Guitar.save_guitars(guitars)
    print("Guitars saved to guitars.csv.")

if __name__ == "__main__":
    main()
