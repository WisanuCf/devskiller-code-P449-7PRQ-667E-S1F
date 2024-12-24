import base64
import unittest

import app.student


class StructureTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.MODULE = app.student

    def test_class_exists_student(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"is not found, but it was marked as required.",
        )

    def test_class_function_exists_student___init__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"U3R1ZGVudA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}`, "
            f"but it was marked as required.",
        )

    def test_class_function_signature_match_student___init__(self):
        classes = _get_class_names(self.MODULE)
        self.assertIn(
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            classes,
            msg=f"The class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"is not found, but it was marked as required.",
        )
        functions = _get_class_function_names(
            self.MODULE, base64.b64decode(b"U3R1ZGVudA==").decode()
        )
        self.assertIn(
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
            functions,
            msg=f"The function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"is not found in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}`, "
            f"but it was marked as required.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            8,
            len(args),
            msg=f"The function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should have 8 argument(s).",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c2VsZg==").decode(),
            args[0],
            msg=f"The argument #0 of function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should be called "
            f"`self`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"bmFtZQ==").decode(),
            args[1],
            msg=f"The argument #1 of function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should be called "
            f"`name`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c3R1ZGVudF9pZA==").decode(),
            args[2],
            msg=f"The argument #2 of function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should be called "
            f"`student_id`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YWdl").decode(),
            args[3],
            msg=f"The argument #3 of function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should be called "
            f"`age`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"c3ViamVjdHM=").decode(),
            args[4],
            msg=f"The argument #4 of function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should be called "
            f"`subjects`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"Z3JhZGU=").decode(),
            args[5],
            msg=f"The argument #5 of function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should be called "
            f"`grade`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YXZlcmFnZV9zY29yZQ==").decode(),
            args[6],
            msg=f"The argument #6 of function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should be called "
            f"`average_score`.",
        )
        args = _get_class_function_arg_names(
            self.MODULE,
            base64.b64decode(b"U3R1ZGVudA==").decode(),
            base64.b64decode(b"U3R1ZGVudC5fX2luaXRfXw==").decode(),
        )
        self.assertEqual(
            base64.b64decode(b"YXR0ZW5kYW5jZQ==").decode(),
            args[7],
            msg=f"The argument #7 of function "
            f"`{base64.b64decode(b'U3R1ZGVudC5fX2luaXRfXw==').decode()}` "
            f"in class "
            f"`{base64.b64decode(b'U3R1ZGVudA==').decode()}` "
            f"should be called "
            f"`attendance`.",
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
