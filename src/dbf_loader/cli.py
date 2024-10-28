import sys
from pathlib import Path
from .converter import process_directory


def main():
    """
    Main entry point for the CLI.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_directory> <output_directory>")
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    if not input_dir.is_dir():
        print(f"Error: {input_dir} is not a valid directory")
        sys.exit(1)

    process_directory(input_dir, output_dir)


if __name__ == "__main__":
    main()
