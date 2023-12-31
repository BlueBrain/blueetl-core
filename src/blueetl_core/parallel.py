"""Utilities for parallelization."""
import logging
import os
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any, Callable, Optional

import numpy as np
from joblib import Parallel, delayed

from blueetl_core.constants import (
    BLUEETL_JOBLIB_BACKEND,
    BLUEETL_JOBLIB_JOBS,
    BLUEETL_JOBLIB_VERBOSE,
    BLUEETL_SUBPROCESS_LOGGING_LEVEL,
)
from blueetl_core.logging import L, setup_logging


@dataclass
class TaskContext:
    """TaskContext class containing information to be passed to the tasks in subprocesses."""

    task_id: int
    loglevel: int
    seed: Optional[int] = None
    ppid: Optional[int] = None


class Task:
    """Task class."""

    def __init__(self, func: Callable) -> None:
        """Initialize the Task object.

        Args:
            func: function to be executed whe the Task is called in a subprocess.
        """
        self.func = func

    def _setup_logging(self, ctx: TaskContext) -> None:
        """Initialize logging in a subprocess."""
        loglevel = os.getenv(BLUEETL_SUBPROCESS_LOGGING_LEVEL)
        if loglevel:
            logformat = f"%(asctime)s %(levelname)s %(name)s [task={ctx.task_id}]: %(message)s"
            setup_logging(loglevel=loglevel, logformat=logformat, force=True)

    @staticmethod
    def _setup_seed(ctx: TaskContext) -> None:
        """Initialize seed in a subprocess."""
        if ctx.seed is not None:
            np.random.seed(ctx.seed)

    def __call__(self, ctx: TaskContext) -> Any:
        """Call the wrapped function and return the result.

        It's intended to be called in a subprocess.

        Args:
            ctx: TaskContext instance containing the context information.
        """
        if ctx.ppid and ctx.ppid != os.getpid():
            # only when the task is executed in a subprocess
            self._setup_logging(ctx)
            self._setup_seed(ctx)
        return self.func()


def run_parallel(
    tasks: Iterable[Callable[[TaskContext], Any]],
    jobs: Optional[int] = None,
    backend: Optional[str] = None,
    verbose: Optional[int] = None,
    base_seed: Optional[int] = None,
) -> list[Any]:
    """Run tasks in parallel.

    Args:
        tasks: iterable of callable objects that will be called in separate threads or processes.
            The callable must accept a single parameter ctx, that will contain a TaskContext.
        jobs: number of jobs. If not specified, use the BLUEETL_JOBLIB_JOBS env variable,
            or use half of the available cpus. Set to 1 to disable parallelization.
        backend: backend passed to joblib. If not specified, use the BLUEETL_JOBLIB_BACKEND env
            variable, or use the joblib default (loky).
            Possible values: loky, multiprocessing, threading.
        verbose: verbosity of joblib. If not specified, use the BLUEETL_JOBLIB_VERBOSE.
        base_seed: initial base seed. If specified, a different seed is added to the task context,
            and passed to each callable object.

    Returns:
        list of objects returned by the callable objects, in the same order.
    """
    loglevel = L.getEffectiveLevel()
    if verbose is None:
        verbose_env = os.getenv(BLUEETL_JOBLIB_VERBOSE)
        verbose = int(verbose_env) if verbose_env else 0 if loglevel >= logging.WARNING else 10
    if not jobs:
        jobs_env = os.getenv(BLUEETL_JOBLIB_JOBS)
        jobs = int(jobs_env) if jobs_env else max((os.cpu_count() or 1) // 2, 1)
    if not backend:
        backend = os.getenv(BLUEETL_JOBLIB_BACKEND)
    parallel = Parallel(n_jobs=jobs, backend=backend, verbose=verbose)
    return parallel(
        delayed(task)(
            ctx=TaskContext(
                task_id=i,
                loglevel=loglevel,
                seed=None if base_seed is None else base_seed + i,
                ppid=os.getpid(),
            )
        )
        for i, task in enumerate(tasks)
    )
