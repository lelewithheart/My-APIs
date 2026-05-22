from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
APIS_DIR = REPO_ROOT / "apis"


class ApiSpecValidationTest(unittest.TestCase):
    def test_all_api_folders_have_openapi_spec(self) -> None:
        self.assertTrue(APIS_DIR.exists(), "apis directory must exist")
        api_folders = sorted([p for p in APIS_DIR.iterdir() if p.is_dir()])
        self.assertGreaterEqual(len(api_folders), 10, "expected a broad API catalog")
        for folder in api_folders:
            spec = folder / "openapi.yaml"
            self.assertTrue(spec.exists(), f"{folder.name} is missing openapi.yaml")
            content = spec.read_text(encoding="utf-8")
            self.assertIn("openapi: 3.0.3", content)
            self.assertIn("paths:", content)
