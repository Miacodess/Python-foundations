import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

def main() -> None:
    random.seed(42)

    rows = []
    start = datetime(2026, 10, 1, 8, 0)
    for i in range(60):
        timestaamp = (start + timedelta(minutes=10 * i)).strftime("%Y-%m-%d %H:%M")
        sensor_id = f"S{i % 3 + 1}"
        temperature = round(random.uniform(22, 34), 1)
        rows.append([timestaamp, sensor_id, temperature])

    # Damage some rows on purpose, like a faulty real-world sensor
    rows[5][2] = "N/A"
    rows[12][2] = ""
    rows[20][2] = "error"
    rows[33][2] = 999.0
    rows[47][2] = "-"

    output = Path(__file__).parent / "sample_data" / "sensor_log.csv"
    with open(output, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "sensor_id", "temperature_c"])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {output}")

if __name__ == "__main__":
    main()