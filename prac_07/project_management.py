"""
Project_management
Estimate time: 45 minutes
Actual time: 110 minutes
"""
from project import Project
import datetime

DEFAULT_FILENAME = "projects.txt"


def main():
    """Main function to run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)

    while True:
        print("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
              "- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save: ")
            save_projects(projects, filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            filter_projects_by_date(projects, date)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
            if save_choice.startswith("y"):
                save_projects(projects, DEFAULT_FILENAME)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)
            for line in file:
                parts = line.strip().split("\t")
                name = parts[0]
                start_date = parts[1]
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion_percentage = int(parts[4])
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return projects


def save_projects(projects, filename):
    """Save projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display projects grouped by completion status and sorted by priority."""
    incomplete_projects = [p for p in projects if p.completion_percentage < 100]
    completed_projects = [p for p in projects if p.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    """Display projects that start after the given date, sorted by date."""
    filtered_projects = [p for p in projects if datetime.datetime.strptime(p.start_date, "%d/%m/%Y") > date]
    for project in sorted(filtered_projects, key=lambda x: datetime.datetime.strptime(x.start_date, "%d/%m/%Y")):
        print(project)


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print("Project added.")


def update_project(projects):
    """Update the completion percentage and/or priority of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_percentage = input("New Percentage: ")
        new_priority = input("New Priority: ")
        if new_percentage:
            project.completion_percentage = int(new_percentage)
        if new_priority:
            project.priority = int(new_priority)
        print("Project updated.")
    except (ValueError, IndexError):
        print("Invalid selection.")




if __name__ == "__main__":
    main()