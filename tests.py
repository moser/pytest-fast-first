import subprocess, time


def _run(*additional_args):
    res = subprocess.run(
        ["pytest", "example_tests", "-v", *additional_args], stdout=subprocess.PIPE
    )
    res.check_returncode()
    tests = [
        line.split(" ")[0]
        for line in res.stdout.decode().splitlines()
        if line.startswith("example_tests/test_mod")
    ]
    print(tests)
    return tests


def test_default():
    assert _run() == [
        "example_tests/test_mod1.py::test_fastest",
        "example_tests/test_mod2.py::test_fast",
        "example_tests/test_mod1.py::test_kind_of_slow",
        "example_tests/test_mod1.py::test_slow",
        "example_tests/test_mod2.py::test_slowest",
    ]


def test_grouped():
    assert _run("--ff-group-by-module") == [
        "example_tests/test_mod1.py::test_fastest",
        "example_tests/test_mod1.py::test_kind_of_slow",
        "example_tests/test_mod1.py::test_slow",
        "example_tests/test_mod2.py::test_fast",
        "example_tests/test_mod2.py::test_slowest",
    ]


def test_inverse():
    assert _run("--ff-inverse") == [
        "example_tests/test_mod2.py::test_slowest",
        "example_tests/test_mod1.py::test_slow",
        "example_tests/test_mod1.py::test_kind_of_slow",
        "example_tests/test_mod2.py::test_fast",
        "example_tests/test_mod1.py::test_fastest",
    ]


def test_grouped_inverse():
    assert _run("--ff-inverse", "--ff-group-by-module") == [
        "example_tests/test_mod2.py::test_slowest",
        "example_tests/test_mod2.py::test_fast",
        "example_tests/test_mod1.py::test_slow",
        "example_tests/test_mod1.py::test_kind_of_slow",
        "example_tests/test_mod1.py::test_fastest",
    ]


def test_xdist():
    assert _run("-n", "2")


def main():
    failed, passed = 0, 0
    for test in [
        test_default,
        test_inverse,
        test_grouped,
        test_grouped_inverse,
        test_xdist,
    ]:
        try:
            test()
            passed += 1
        except Exception as exc:
            print(test, exc)
            failed += 1

    if failed:
        print("FAILED")
        exit(1)
    else:
        print("PASSED")


if __name__ == "__main__":
    main()
