import subprocess
import tempfile
import os


def run_tests(code: str, tests: str):

    with tempfile.TemporaryDirectory() as tmpdir:

        code_path = os.path.join(tmpdir, "solution.py")
        test_path = os.path.join(tmpdir, "test_solution.py")

        with open(code_path, "w") as f:
            f.write(code)

        with open(test_path, "w") as f:
            f.write(tests)

        result = subprocess.run(
            ["pytest", tmpdir, "-q"],
            capture_output=True,
            text=True
        )

        return result.returncode, result.stdout + result.stderr
