"""Run nox commands."""

import nox

locations = "src", "tests"

# @nox.session(python=["3.8", "3.7"])
# def lint(session):
#     args = session.posargs or locations
#     install_with_constraints(
#         session,
#         "flake8",
#         "flake8-annotations",
#         "flake8-bandit",
#         "flake8-black",
#         "flake8-bugbear",
#         "flake8-import-order",
#     )
#     session.run("flake8", *args)


@nox.session(python="3.10")
def black(session):
    """Run black."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.10"])
def lint(session):
    """Run linter."""
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-black",
        "flake8-import-order",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session
def tests(session):
    """Run tests."""
    args = session.posargs or locations
    session.install("-r", "requirements.txt")
    session.run("pytest", "-v", *args)


# @nox.session
# def mypy(session):
#     """Mypy checking."""
#     args = session.posargs or locations
#     session.install("-r", "requirements.txt")
#     # install_with_constraints(session, "mypy")
#     session.run("mypy", *args)

