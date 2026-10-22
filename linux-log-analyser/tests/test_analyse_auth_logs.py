import tempfile
import unittest
from pathlib import Path

from src.analyse_auth_logs import analyse_log


class AnalyseAuthLogsTests(unittest.TestCase):
    def test_counts_failures_and_applies_threshold(self):
        contents = (
            "Failed password for admin from 192.0.2.10 port 1001 ssh2\n"
            "Failed password for admin from 192.0.2.10 port 1002 ssh2\n"
            "Failed password for admin from 192.0.2.10 port 1003 ssh2\n"
            "Failed password for analyst from 198.51.100.8 port 1004 ssh2\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "auth.log"
            path.write_text(contents, encoding="utf-8")
            total, flagged = analyse_log(path, threshold=3)

        self.assertEqual(total, 4)
        self.assertEqual(flagged, {"192.0.2.10": 3})


if __name__ == "__main__":
    unittest.main()
