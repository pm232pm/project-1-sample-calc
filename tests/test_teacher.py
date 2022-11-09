"""This is the starting test file"""
import os

from app import main


def test_main():
    # pylint: disable=line-too-long
    """My Main Test"""
    main()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print("bd", base_dir)
    sample_files_output_dir = os.path.join(base_dir, '..', 'sample_files_output')
    sample_files_output_directory_contents = os.listdir(sample_files_output_dir)
    assert len(sample_files_output_directory_contents) - 1 == 15, "There is an incorrect number of files"
