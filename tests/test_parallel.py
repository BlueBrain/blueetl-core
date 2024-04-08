from functools import partial

import pytest

from blueetl_core import parallel as test_module


def _myfunc(n):
    return n * n


@pytest.mark.parametrize(
    "jobs, jobs_env",
    [
        (1, None),
        (3, None),
        (None, None),
        (None, 1),
        (None, 3),
    ],
)
def test_run_parallel(monkeypatch, jobs, jobs_env):
    if jobs_env is not None:
        monkeypatch.setenv("BLUEETL_JOBLIB_JOBS", str(jobs_env))
    else:
        monkeypatch.delenv("BLUEETL_JOBLIB_JOBS", raising=False)
    tasks = [test_module.Task(partial(_myfunc, n=i)) for i in range(3)]
    result = test_module.run_parallel(tasks=tasks, jobs=jobs)
    assert result == [0, 1, 4]


def test_isolated_in_sub_process(monkeypatch):
    monkeypatch.delenv("BLUEETL_JOBLIB_JOBS", raising=False)
    func = test_module.isolated(_myfunc)
    result = func(n=2)
    assert result == 4


def test_isolated_in_main_process(monkeypatch):
    monkeypatch.setenv("BLUEETL_JOBLIB_JOBS", "1")
    func = test_module.isolated(_myfunc)
    result = func(n=2)
    assert result == 4
