import os
import csv
from pathlib import Path
from dbfread import DBF


def dbf_to_csv(dbf_file_path: Path, csv_file_path: Path) -> None:
    """
    Convert a single DBF file to CSV format.

    Args:
        dbf_file_path (Path): Path to the input DBF file.
        csv_file_path (Path): Path to the output CSV file.
    """
    try:
        dbf = DBF(dbf_file_path)

        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # Write the header
            writer.writerow(dbf.field_names)

            # Write the rows
            for record in dbf:
                writer.writerow(record.values())

        print(f"Converted: {dbf_file_path.name} -> {csv_file_path.name}")
    except Exception as e:
        print(f"Error converting {dbf_file_path.name}: {str(e)}")


def process_directory(input_dir: Path, output_dir: Path) -> None:
    """
    Process all DBF files in the input directory and convert them to CSV in the output directory.

    Args:
        input_dir (Path): Path to the input directory containing DBF files.
        output_dir (Path): Path to the output directory for CSV files.
    """
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process each DBF file in the input directory
    for dbf_file in input_dir.glob('*.dbf'):
        csv_file = output_dir / dbf_file.with_suffix('.csv').name
        dbf_to_csv(dbf_file, csv_file)

    print(f"Conversion complete. CSV files saved in {output_dir}")
