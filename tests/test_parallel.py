from functools import partial

import pytest

from blueetl_core import parallel as test_module


def _myfunc(n):
    return n * n


@pytest.mark.parametrize("jobs", [1, 3, None])
def test_run_parallel(jobs):
    tasks = [test_module.Task(partial(_myfunc, n=i)) for i in range(3)]
    result = test_module.run_parallel(tasks=tasks, jobs=jobs)
    assert result == [0, 1, 4]


def test_isolated():
    func = test_module.isolated(_myfunc)
    result = func(n=2)
    assert result == 4
