import json, pathlib, collections

PATH = pathlib.Path(".pytest-runtimes")
RUNTIMES = {}


def pytest_addoption(parser):
    group = parser.getgroup("fast-first")
    group.addoption(
        "--ff-inverse",
        action="store_true",
        dest="ff_inverse",
        help="Inverts the order (can be used to optimize the runtime of a test suite when run with xdist).",
    )
    group.addoption(
        "--ff-group-by-module",
        action="store_true",
        dest="ff_group_by_module",
        help="By default tests are just ordered by their runtime. If you have module-scoped fixtures, this can help with better fixture reuse..",
    )


def pytest_configure():
    if PATH.exists():
        with open(".pytest-runtimes", "r") as fp:
            RUNTIMES.update(**json.load(fp))


def pytest_unconfigure():
    with open(".pytest-runtimes", "w") as fp:
        json.dump(RUNTIMES, fp, sort_keys=True, indent=4)


def pytest_runtest_makereport(item, call):
    if call.when == "call" and not call.excinfo:
        name = f"{item.module.__name__}--{item.name}"
        RUNTIMES[name] = call.duration


def pytest_collection_modifyitems(session, config, items):
    def get_runtime(item):
        return RUNTIMES.get(f"{item.module.__name__}--{item.name}", 0.1)

    inverse = config.getoption("ff_inverse")
    if config.getoption("ff_group_by_module"):
        mod_runtime = collections.defaultdict(float)
        for item in items:
            mod_runtime[item.module.__name__] += get_runtime(item)

        items.sort(
            key=lambda item: (
                mod_runtime.get(item.module.__name__, 0.1),
                get_runtime(item),
            ),
            reverse=inverse,
        )
    else:
        items.sort(key=get_runtime, reverse=inverse)
