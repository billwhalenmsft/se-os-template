from __future__ import annotations

import unittest

from scripts.validate_template import run_validation


class TemplateHygieneTests(unittest.TestCase):
    def test_public_template_is_portable(self) -> None:
        self.assertEqual(run_validation(), [])


if __name__ == "__main__":
    unittest.main()
