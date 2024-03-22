import datetime
from project import Project


def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split('\t')
                name, start_date, priority, estimate, completion = data
                start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                priority = int(priority)
                estimate = float(estimate)
                completion = int(completion)
                projects.append(Project(name, start_date, priority, estimate, completion))
    except FileNotFoundError:
        print("File not found.")
    return projects


def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project.display_details()}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project.display_details()}")


def main():
    continue_program = True

    # Load projects from default file
    projects = load_projects('projects.txt')
    print(f"Loaded {len(projects)} projects from projects.txt")

    while continue_program:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            # Load projects from a file
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects(file_name)
            print(f"Loaded {len(projects)} projects from {file_name}")

        elif choice == 's':
            # Save projects to a file
            file_name = input("Enter filename to save projects to: ")
            save_projects(file_name, projects)
            print("Projects saved successfully.")

        elif choice == 'd':
            # Display projects
            display_projects(projects)

        elif choice == 'f':
            # Filter projects by date
            pass  # To be implemented

        elif choice == 'a':
            # Add new project
            pass  # To be implemented

        elif choice == 'u':
            # Update project
            pass  # To be implemented

        elif choice == 'q':
            # Quit the program
            save_choice = input("Would you like to save to projects.txt? ").strip().lower()
            if save_choice.startswith('y'):
                save_projects('projects.txt', projects)
                print("Projects saved to projects.txt")
            print("Thank you for using custom-built project management software.")
            continue_program = False

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
