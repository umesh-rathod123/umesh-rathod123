"""
Birthday Surprise Generator
---------------------------
A small, dependency-free Python program that creates a personalized
birthday message and calculates the person's age.

Run:
    python birthday_surprise.py
"""

from datetime import date


def calculate_age(birth_date: date, today: date | None = None) -> int:
    """Return the person's age in completed years."""
    today = today or date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def main() -> None:
    print("\n" + "=" * 48)
    print("          BIRTHDAY SURPRISE GENERATOR")
    print("=" * 48)

    name = input("\nEnter your name: ").strip()
    if not name:
        name = "Friend"

    try:
        year = int(input("Birth year (YYYY): "))
        month = int(input("Birth month (1-12): "))
        day = int(input("Birth day (1-31): "))
        birth_date = date(year, month, day)
    except ValueError:
        print("\nPlease enter a valid date. Example: 2006, 11, 16")
        return

    today = date.today()
    if birth_date > today:
        print("\nYour birthday cannot be in the future.")
        return

    age = calculate_age(birth_date, today)

    print("\n" + "*" * 48)
    print(f"  HAPPY BIRTHDAY, {name.upper()}!")
    print("*" * 48)
    print(f"  You are {age} years old.")
    print("  Another year. Another chapter. More possibilities.")
    print("  Keep learning, keep building, and keep shining!")
    print("*" * 48 + "\n")


if __name__ == "__main__":
    main()
