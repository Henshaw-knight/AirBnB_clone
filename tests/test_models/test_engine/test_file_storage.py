#!/usr/bin/python3
"""FileStorage class unit tests"""
import io
import unittest
from contextlib import redirect_stdout
from datetime import datetime
from pycodestyle import Checker
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test class or BaseModel"""
    def test_pep8_compliance(self):
        """checks that code conforms to pep8 style"""
        files_to_check = [
                'models/engine/file_storage.py',
                'tests/test_models/test_engine/test_file_storage.py'
                ]

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            style = Checker(paths=files_to_check)
            result = style.check_all()

        output = stdout.getvalue().strip()
        self.assertFalse(output, f"PEP8 violations found:\n{output}")
