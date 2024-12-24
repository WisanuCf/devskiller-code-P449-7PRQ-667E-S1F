import base64
import unittest

import app.fetch_student_details


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = app.fetch_student_details

    def test_class_exists_fetchstudentdetails(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_class_function_exists_fetchstudentdetails___init__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5fX2luaXRfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5fX2luaXRfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_fetchstudentdetails___init__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5fX2luaXRfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5fX2luaXRfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_fetchstudentdetails_clean_input(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5jbGVhbl9pbnB1dA==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5jbGVhbl9pbnB1dA==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_fetchstudentdetails_clean_input(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5jbGVhbl9pbnB1dA==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5jbGVhbl9pbnB1dA==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5jbGVhbl9pbnB1dA==").decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5jbGVhbl9pbnB1dA==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5jbGVhbl9pbnB1dA==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cm93").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5jbGVhbl9pbnB1dA==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should be called "
            f"`row`.",
        )

    def test_class_function_exists_fetchstudentdetails_get_attendance(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ=="
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_fetchstudentdetails_get_attendance(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ=="
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ=="
            ).decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ=="
            ).decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ=="
            ).decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YXR0ZW5kYW5jZV9maWxlX25hbWU=").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfYXR0ZW5kYW5jZQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should be called "
            f"`attendance_file_name`.",
        )

    def test_class_function_exists_fetchstudentdetails_get_data(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_fetchstudentdetails_get_data(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==").decode(),
        )
        self.assertEqual(
            2,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should have 2 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"ZmlsZV9uYW1l").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfZGF0YQ==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should be called "
            f"`file_name`.",
        )

    def test_class_function_exists_fetchstudentdetails_get_super_student(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfc3VwZXJfc3R1ZGVudA=="
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfc3VwZXJfc3R1ZGVudA==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_fetchstudentdetails_get_super_student(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfc3VwZXJfc3R1ZGVudA=="
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfc3VwZXJfc3R1ZGVudA==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfc3VwZXJfc3R1ZGVudA=="
            ).decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfc3VwZXJfc3R1ZGVudA==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfc3VwZXJfc3R1ZGVudA=="
            ).decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5nZXRfc3VwZXJfc3R1ZGVudA==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should be called "
            f"`self`.",
        )

    def test_class_function_exists_fetchstudentdetails_map_csv_to_class(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5tYXBfY3N2X3RvX2NsYXNz"
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5tYXBfY3N2X3RvX2NsYXNz').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_fetchstudentdetails_map_csv_to_class(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode()
        )
        self.assertIn(
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5tYXBfY3N2X3RvX2NsYXNz"
            ).decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5tYXBfY3N2X3RvX2NsYXNz').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5tYXBfY3N2X3RvX2NsYXNz"
            ).decode(),
        )
        self.assertEqual(
            1,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5tYXBfY3N2X3RvX2NsYXNz').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should have 1 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"RmV0Y2hTdHVkZW50RGV0YWlscw==").decode(),
            base64.b64decode(
                b"RmV0Y2hTdHVkZW50RGV0YWlscy5tYXBfY3N2X3RvX2NsYXNz"
            ).decode(),
        )
        self.assertEqual(
            base64.b64decode(b"cm93").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscy5tYXBfY3N2X3RvX2NsYXNz').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'RmV0Y2hTdHVkZW50RGV0YWlscw==').decode()}` "
            f"should be called "
            f"`row`.",
        )


# === Internal functions, do not modify ===
import inspect

from types import ModuleType
from typing import List


def _get_function_names(module: ModuleType) -> List[str]:
    names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            names.append(name)
    return names


def _get_function_arg_names(module: ModuleType, fn_name: str) -> List[str]:
    arg_names = []
    functions = inspect.getmembers(module, lambda member: inspect.isfunction(member))
    for name, fn in functions:
        if fn.__module__ == module.__name__:
            if fn.__qualname__ == fn_name:
                args_spec = inspect.getfullargspec(fn)
                arg_names = args_spec.args
                if args_spec.varargs is not None:
                    arg_names.extend(args_spec.varargs)
                if args_spec.varkw is not None:
                    arg_names.extend(args_spec.varkw)
                arg_names.extend(args_spec.kwonlyargs)
                break
    return arg_names


def _get_class_names(module: ModuleType) -> List[str]:
    names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for name, cls in classes:
        if cls.__module__ == module.__name__:
            names.append(name)
    return names


def _get_class_function_names(module: ModuleType, cls_name: str) -> List[str]:
    fn_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name, fn in functions:
                    fn_names.append(fn.__qualname__)
                break
    return fn_names


def _get_class_function_arg_names(
    module: ModuleType, cls_name: str, fn_name: str
) -> List[str]:
    arg_names = []
    classes = inspect.getmembers(module, lambda member: inspect.isclass(member))
    for cls_name_, cls in classes:
        if cls.__module__ == module.__name__:
            if cls_name_ == cls_name:
                functions = inspect.getmembers(
                    cls,
                    lambda member: inspect.ismethod(member)
                    or inspect.isfunction(member),
                )
                for fn_name_, fn in functions:
                    if fn.__qualname__ == fn_name:
                        args_spec = inspect.getfullargspec(fn)
                        arg_names = args_spec.args
                        if args_spec.varargs is not None:
                            arg_names.extend(args_spec.varargs)
                        if args_spec.varkw is not None:
                            arg_names.extend(args_spec.varkw)
                        arg_names.extend(args_spec.kwonlyargs)
                        break
                break
    return arg_names
