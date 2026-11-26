import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Logo
BEAR = "ʕ •ᴥ•ʔ"

# Employee list
emp = {
    "mike.s": {
        "password": "1983",
        "title": "Employee#1002",
        "location": "Freddy Fazbear's Jr's",
        "cameras": ["Main Stage", "Dining Area", "Parts and Service"],
    },
    "ralph.c": {
        "password": "foxy87",
        "title": "Night shift/ Manager",
        "location": "Freddy Fazbear Pizza",
        "cameras": ["Main Stage", "Dining Area", "Pirate Cove"],
    },
}

def show_list(title, items):
    """Print a numbered list, or 'None' if it's empty."""
    print("Loading....")
    if not items:
        print(f"Your {title}: None")
        return
    print(f"Your {title}:")
    for number, item in enumerate(items, start=1):
        print(f"  {number}. {item}")

# Employee login
MAX_ATTEMPTS = 3

def employee_login():
    """Return the username on success, or None after too many failures."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        emp_user = input("Please enter employee username: ").strip().lower()
        emp_pass = input("Please enter employee password: ").strip().lower()

        employee = emp.get(emp_user)
        if employee and emp_pass == employee["password"].lower():
            return emp_user

        print(f"Error Employee credentials not matched. {MAX_ATTEMPTS - attempt} attempt(s) left.")

    print(f"The FazCams system is shutting off. An executive is coming to terminate your position. "
          f"Have a Faztastic day! {BEAR}")
    return None

# Employee cams
def emp_menu(emp_user):
    employee = emp[emp_user]
    print(f"\nWelcome, {employee['title']} {BEAR}. "
          f"Are you ready to start the FazCams system or night shift?")

    while True:
        print("\nNight Shift / FazCams / Logout")
        pick = input("> ").strip().lower()

        if pick == "logout":
            print("Have a Faztastic rest of your day!")
            break
        if pick == "night shift":
            print(f"Night shift started at 12:00AM with {employee['at location']}.")
        elif pick == "fazcams":
            show_list("monitoring cameras", employee["cameras"])
        else:
            print("Please use a valid Fazbear Entertainment option!")

# User entry
def main():
    print("Welcome to the FazCams!")
    print("These cams are property of Fazbear Entertainment. "
          "They are for security use only to monitor Fazbear locations "
          f"using state-of-the-art motion sensors! {BEAR}")
    print(f"Welcome User to the Fazbear Entertainment FazCams! {BEAR}")

    choice = input("Please type continue: ").strip().lower()

    if choice == "continue":
        emp_user = employee_login()
        if emp_user:
            emp_menu(emp_user)
    else:
        print("Unknown option.")


if __name__ == "__main__":
    main()
