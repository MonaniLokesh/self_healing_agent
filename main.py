from agents.coder_agent import generate_code
from agents.test_agent import generate_tests
from agents.debugger_agent import debug_code
from execution.test_runner import run_tests
from config.settings import MAX_ITERATIONS


def self_heal(task):

    code = generate_code(task)
    print("Code:", code)

    for i in range(MAX_ITERATIONS):

        tests = generate_tests(code)
        print("Tests:", tests)
        rc, logs = run_tests(code, tests)
        print("Logs:", logs)

        if rc == 0:
            print("Tests Passed")
            return code

        print(f"Iteration {i+1} failed. Debugging...")
        code = debug_code(code, logs)

    return code


if __name__ == "__main__":
    task = "Write a Python function to check if a number is prime"
    print(self_heal(task))
