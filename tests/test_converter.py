import csv
import pytest
import dbf
from pathlib import Path
from src.dbf_loader.converter import process_directory


def create_sample_dbf(file_path: Path, records: list):
    table_def = dbf.Table(str(file_path), 'NAME C(20); AGE N(3,0)')
    table_def.open(mode=dbf.READ_WRITE)
    for record in records:
        table_def.append(record)
    table_def.close()


def test_process_directory(tmp_path):
    # Create input and output directories
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()

    # Create sample DBF files
    create_sample_dbf(input_dir / "file1.dbf", [('Alice', 30), ('Bob', 25)])
    create_sample_dbf(input_dir / "file2.dbf",
                      [('Charlie', 35), ('David', 40)])

    # Process the directory
    process_directory(input_dir, output_dir)

    # Check if CSV files were created
    assert (output_dir / "file1.csv").exists()
    assert (output_dir / "file2.csv").exists()

    # Verify the contents of the CSV files
    for csv_file in output_dir.glob('*.csv'):
        with open(csv_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 2
        if csv_file.name == "file1.csv":
            assert rows[0]['NAME'] == 'Alice' and int(rows[0]['AGE']) == 30
            assert rows[1]['NAME'] == 'Bob' and int(rows[1]['AGE']) == 25
        elif csv_file.name == "file2.csv":
            assert rows[0]['NAME'] == 'Charlie' and int(rows[0]['AGE']) == 35
            assert rows[1]['NAME'] == 'David' and int(rows[1]['AGE']) == 40
