"""Regression tests for the profile's supported Markdown and HTML syntax."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from check_profile import check_document, online_status


class ProfileChecks(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.document = self.root / "README.md"

    def check(self, content):
        self.document.write_text(content, encoding="utf-8")
        return check_document(self.document, self.root)

    def test_valid_markdown_link(self):
        errors, urls = self.check("# Profile\n[Code](https://github.com/Miiduoa/graduation)")
        self.assertEqual(errors, [])
        self.assertEqual(len(urls), 1)

    def test_missing_local_file(self):
        errors, _ = self.check("# Profile\n[Guide](missing.md)")
        self.assertIn("missing", errors[0])

    def test_parent_traversal_is_rejected(self):
        errors, _ = self.check("# Profile\n[Guide](%2e%2e/README.md)")
        self.assertTrue(errors)

    def test_local_heading(self):
        errors, _ = self.check("# Profile\n[Work](#作品)\n## 作品\n")
        self.assertEqual(errors, [])

    def test_missing_local_heading(self):
        errors, _ = self.check("# Profile\n[Work](#missing)")
        self.assertIn("heading", errors[0])

    def test_html_image_alt_is_required(self):
        errors, _ = self.check('# Profile\n<img src="https://miiduoa.github.io/picture.png">')
        self.assertIn("alt text", errors[0])

    def test_markdown_image_alt_is_required(self):
        errors, _ = self.check("# Profile\n![](https://miiduoa.github.io/picture.png)")
        self.assertIn("alt text", errors[0])

    def test_unsafe_scheme(self):
        errors, _ = self.check('# Profile\n<a href="javascript:alert(1)">bad</a>')
        self.assertIn("scheme", errors[0])

    def test_email(self):
        self.assertEqual(self.check("# Profile\n[Email](mailto:hello@example.com)")[0], [])
        self.assertTrue(self.check("# Profile\n[Email](mailto:invalid)")[0])

    def test_code_examples_are_ignored(self):
        errors, urls = self.check("# Profile\n```md\n[Example](missing.md)\n```\n`[Example](missing.md)`")
        self.assertEqual((errors, urls), ([], set()))

    def test_duplicate_headings_have_suffixes(self):
        errors, _ = self.check("# Profile\n[Again](#work-1)\n## Work\n## Work\n")
        self.assertEqual(errors, [])

    def test_reject_credentials_and_unapproved_hosts(self):
        for url in ("https://person:password@github.com/", "https://127.0.0.1/", "//github.com/Miiduoa"):
            with self.subTest(url=url):
                self.assertTrue(self.check(f"# Profile\n[Link]({url})")[0])

    def test_remote_fragments_are_deduplicated(self):
        _, urls = self.check("# Profile\n[A](https://github.com/Miiduoa#one)\n[B](https://github.com/Miiduoa#two)")
        self.assertEqual(urls, {"https://github.com/Miiduoa"})

    def test_requires_one_main_heading(self):
        self.assertTrue(self.check("No title")[0])
        self.assertTrue(self.check("# One\n# Two")[0])

    @patch("check_profile.time.sleep")
    @patch("check_profile.urlopen")
    def test_unavailable_url_never_passes(self, open_url, sleep):
        open_url.side_effect = HTTPError("https://github.com/missing", 404, "not found", {}, None)
        _, error = online_status("https://github.com/missing")
        self.assertIn("404", error)
        self.assertEqual(open_url.call_count, 3)

    @patch("check_profile.urlopen")
    def test_head_rejection_falls_back_to_get(self, open_url):
        good = unittest.mock.MagicMock()
        good.__enter__.return_value.status = 200
        open_url.side_effect = [HTTPError("https://github.com/", 405, "method", {}, None), good]
        self.assertEqual(online_status("https://github.com/")[1], None)
        self.assertEqual(open_url.call_args_list[1].args[0].method, "GET")


if __name__ == "__main__":
    unittest.main()
