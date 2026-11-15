import re


def parse_subjects(subjects_input):
    subjects = {}
    for item in subjects_input:
        subject_name = item[0].strip()
        if not subject_name:
            raise ValueError("Subject name cannot be empty.")
        count = int(item[1])
        if count <= 0:
            raise ValueError(f"Periods for {subject_name} must be a positive integer.")
        subjects[subject_name] = subjects.get(subject_name, 0) + count
    return subjects


def generate_timetable(days, periods_per_day, subjects):
    if days <= 0 or periods_per_day <= 0:
        raise ValueError("Days and periods per day must be positive integers.")

    total_slots = days * periods_per_day
    total_periods = sum(subjects.values())
    if total_periods != total_slots:
        raise ValueError(
            f"Total weekly periods ({total_periods}) must equal available slots ({total_slots})."
        )

    for sub, count in subjects.items():
        if count > days * 2:
            day_text = "1 day" if days == 1 else f"{days} days"
            raise ValueError(
                f"Timetable cannot be generated: {sub} needs {count} periods in {day_text}, but the limit is 2 per day."
            )

    order = list(subjects.keys())
    remaining = dict(subjects)
    day_usage = [{sub: 0 for sub in order} for _ in range(days)]
    timetable = [[] for _ in range(days)]

    def search(day_index, period_index):
        if day_index == days:
            return True
        if period_index == periods_per_day:
            return search(day_index + 1, 0)

        current_usage = day_usage[day_index]
        candidates = [
            sub for sub in order if remaining[sub] > 0 and current_usage[sub] < 2
        ]
        if not candidates:
            return False

        candidates.sort(key=lambda sub: (-remaining[sub], order.index(sub)))

        for sub in candidates:
            remaining[sub] -= 1
            current_usage[sub] += 1
            timetable[day_index].append(sub)

            if search(day_index, period_index + 1):
                return True

            timetable[day_index].pop()
            current_usage[sub] -= 1
            remaining[sub] += 1

        return False

    if not search(0, 0):
        raise ValueError("Timetable cannot be generated with given constraints.")

    return timetable


def main():
    try:
        days = int(input("Enter number of days: "))
        periods = int(input("Enter periods per day: "))
    except ValueError:
        print("Error: Days and periods per day must be valid integers.")
        return

    if days <= 0 or periods <= 0:
        print("Error: Days and periods per day must be positive integers.")
        return

    try:
        n = int(input("Enter number of subjects: "))
        if n <= 0:
            print("Error: Number of subjects must be a positive integer.")
            return

        entries = []
        for _ in range(n):
            name = input("Enter subject name: ")
            count = int(input(f"Enter periods for {name}: "))
            entries.append((name, count))

        subjects = parse_subjects(entries)
        timetable = generate_timetable(days, periods, subjects)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for day_index in range(days):
        day_name = day_names[day_index] if day_index < len(day_names) else f"Day {day_index + 1}"
        print(f"{day_name}: {', '.join(timetable[day_index])}")


if __name__ == "__main__":
    main()
