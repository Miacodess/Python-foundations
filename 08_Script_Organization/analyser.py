"""A command-line tool:  python analyse.py <csv_file> --threshold 28
"""

import argparse
import csv
import sys
from pathlib import Path


target_dir = Path(__file__).parent.parent / "07_File_Handling"
sys.path.insert(0, str(target_dir))
from analyser import read_temperatures

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyse a temperature CSV log.")
    parser.add_argument("csv_file", help="path to the CSV file")
    parser.add_argument(
        "--threshold", type=float, default=28.0, help="alert above this value (default: 28)"
    )
    parser.add_argument(
        "--output", type=str, help="optional file path to save the output"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        temperatures, skipped = read_temperatures(args.csv_file)
    except FileNotFoundError:
        print(f"Error: file '{args.csv_file}' not found")
        return 1

    above = [t for t in temperatures if t > args.threshold]

    # Format the output into a single string
    result_text = (
        f"Readings: {len(temperatures)}\n"
        f"Above {args.threshold}: {len(above)}\n"
    )
    if args.output:
        with open(args.output, "w") as f:
            f.write(result_text)
        print(f"Success: Results saved to {args.output}")
    else:
        # We use end="" because result_text already contains newlines
        print(result_text, end="")
        
    return 0


if __name__ == "__main__":
    sys.exit(main())
