import csv
import json
from pathlib import Path

MIN_VALID = -40.0
MAX_VALID = 125.0
HOT_THRESHOLD = 30.0


def read_temperatures(path: str | Path) -> tuple[list[float], int]:
    """Return (valid temperatures, number of rows skipped)."""
    temperatures = []
    skipped = 0
    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            value = parse_temperature(row.get("temperature_c"))
            if value is None:
                skipped += 1
            else:
                temperatures.append(value)
    return temperatures, skipped

def parse_temperature(text: str | None) -> float | None:
    """Return the temperature as a number, or None if it is not a usable reading."""
    try:
        value = float(text)
    except (ValueError, TypeError):
        return None
    if not MIN_VALID <= value <= MAX_VALID:
        return None
    return value


def build_report(temperatures: list[float], skipped: int) -> str:
    """Turn the numbers into a short text report."""
    if not temperatures:
        return "No valid readings found.\n"
    mean = sum(temperatures) / len(temperatures)
    above = count_above(temperatures, HOT_THRESHOLD)
    return (
        f"Valid readings: {len(temperatures)}\n"
        f"Skipped rows:   {skipped}\n"
        f"Lowest:  {min(temperatures):.1f}\n"
        f"Highest: {max(temperatures):.1f}\n"
        f"Average: {mean:.2f}\n"
    )


def write_report(text: str, path: str | Path) -> None:
    """Save the report text to a file."""
    with open(path, "w") as file:
        file.write(text)

def count_above(temperatures: list[float], threshold: float) -> int:
    """Count how many readings are above the threshold."""
    count = 0
    for value in temperatures:
        if value > threshold:
            count += 1
    return count


def average_by_sensor(path: str | Path) -> dict[str, float]:
    """Return the average valid temperature for each sensor_id."""
    groups = {}
    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            value = parse_temperature(row.get("temperature_c"))
            if value is None:
                continue
            sensor = row.get("sensor_id", "unknown")
            if sensor not in groups:
                groups[sensor] = []
            groups[sensor].append(value)

    averages = {}
    for sensor, values in groups.items():
        averages[sensor] = round(sum(values) / len(values), 2)
    return averages

def write_json(summary: dict, path: str | Path) -> None:
    """Save the summary dictionary as a JSON file."""
    with open(path, "w") as file:
        json.dump(summary, file, indent=2)

def main() -> None:
    here = Path(__file__).parent
    data_file = here / "sample_data" / "sensor_log.csv"

    try:
        temperatures, skipped = read_temperatures(data_file)
    except FileNotFoundError:
        print(f"Error: could not find {data_file}")
        print("Run make_sample_data.py first to create it.")
        return

    report = build_report(temperatures, skipped)
    print(report)
    write_report(report, here / "report.txt")

    if not temperatures:
        return

    averages = average_by_sensor(data_file)
    print("Average by sensor:")
    for sensor, average in averages.items():
        print(f"  {sensor}: {average}")

    summary = {
        "valid_readings": len(temperatures),
        "skipped_rows": skipped,
        "lowest": min(temperatures),
        "highest": max(temperatures),
        "average": round(sum(temperatures) / len(temperatures), 2),
        "above_threshold": count_above(temperatures, HOT_THRESHOLD),
        "average_by_sensor": averages,
    }
    write_json(summary, here / "summary.json")

if __name__ == "__main__":
    main()