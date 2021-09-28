#!/usr/bin/env python3
"""
Convert the conda environment-dev.yml to the pip requirements-dev.txt,
or check that they have the same packages (for the CI)
Usage:
    Generate `environment.yml`
    $ python scripts/generate_pip_deps_from_conda.py
    Compare and fail (exit status != 0) if `requirements-dev.txt` has not been
    generated with this script:
    $ python scripts/generate_pip_deps_from_conda.py --compare
"""
import argparse
import copy
import io
import pathlib
import textwrap

import yaml


def pathlib_dir(path):
    """Checks if a path is an existing directory

    Parameters
    ----------
    path: str | pathlib.Path
        File system path to a directory (must exist)
    Returns
    -------
    path: pathlib.Path
        Same path as input coerced to a pathlib.Path object
    Raises
    ------
    ValueError
        If inputted path is not an existing directory
    """
    path = pathlib.Path(path)
    if path.is_dir():
        return path
    raise ValueError("Specified argument is not a valid directory")


def load_nondev_yaml(dev_path: pathlib.Path) -> bool:
    """
    Partially reads a yaml file and stores results in a dictionary.

    Parameters
    ----------
    dev_path : pathlib.Path
        Path to the conda file with dependencies (e.g. `environment-dev.yml`).
        This file should contain a line that begins with '## Developer' so that
        only dependencies above this line are parsed into the output

    Returns
    -------
    env_config : dict
        Returns a dictionary representing the parsed yaml file, curtailing all
        dependencies below the line starting with '## Developer'
    """
    with open(dev_path) as dev_file, io.StringIO() as buffer:
        for line in dev_file:
            if line.strip().lower().startswith("## developer"):
                break

            buffer.write(line)
        buffer.seek(0)
        env_config = yaml.safe_load(buffer)

    return env_config


def strip_dev_suffix(env_config: dict):
    """

    Parameters
    ----------
    env_config : dict
        dictionary representing the contents of valid anaconda environment.yml.

    Returns
    -------
    env_config : dict
        Returns a dictionary representing the parsed yaml file, curtailing all
        dependencies below the line starting with '## Developer'

    Raises
    ------
    ValueError
        If inputted `env_config` dictionary is missing a key named "name"
        If inputted `env_config["name"]` does not end with "-dev"
    """
    env_config = copy.deepcopy(env_config)
    if "name" not in env_config.keys():
        raise ValueError("Environment config missing `name` attribute")

    dev_env_name = env_config["name"]
    if not dev_env_name.endswith("-dev"):
        raise ValueError("Environment config `name` must end with '{env_name}-dev'")

    env_config["name"] = dev_env_name.replace("-dev", "")
    return env_config


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(
            """
        Converts environment-dev.yml to environment.yml file allowing
        simple management of dependent environments.
        The env-dev file must contain 2 components:

        1) A name that is suffixed with "-dev". In the outputted enviornment
        file (the non-developer version), this suffix is removed. This rule is
        enforced to ensure environments are not accidentally overwritten.

        2) A comment line that begins with '## Developer' somewhere within
        the dependencies of the file, essentially acting as a seperator
        where this program will stop parsing the yml format.

        All dependencies above this line will be added into the
        outputted environment.yml file, and all dependencies below this line
        are ignored.
        """
        ).strip(),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--output-path",
        type=pathlib_dir,
        default=None,
        help="Directory to store outputted environment file to.\n"
        "Defaults to same directory as the environment-dev.yml file",
    )
    args = parser.parse_args()

    repo_path = pathlib.Path(__file__).parents[1].absolute()
    dev_fpath = repo_path / "environment-dev.yml"

    if args.output_path is None:
        args.output_path = repo_path

    out_fpath = args.output_path.resolve() / "environment.yml"

    env_config = load_nondev_yaml(dev_fpath)
    env_config = strip_dev_suffix(env_config)

    with open(out_fpath, "w") as f:
        f.write(f"# This file is auto-generated from {dev_fpath.name}\n")
        yaml.safe_dump(env_config, f, sort_keys=False)
