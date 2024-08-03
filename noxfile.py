import nox

nox.options.sessions = ["tests", "pylint"]


@nox.session
def tests(session: nox.Session) -> None:
    """
    Run the unit and regular tests.
    """
    session.install("-e.[test]")
    session.run("pytest")


@nox.session
def pylint(session: nox.Session) -> None:
    """
    Run pylint.
    """
    session.install("-e.[lint]")
    session.run("pylint", "brazilcep")


@nox.session
def coverage(session: nox.Session) -> None:
    """
    Run coverage.
    """
    session.install("-e.[coverage]")
    session.run("pytest", "--cov", "brazilcep")


@nox.session
def check_manifest(session: nox.Session) -> None:
    """
    Ensure all needed files are included in the manifest.
    """

    session.install("check-manifest")
    session.run("check-manifest", *session.posargs)


@nox.session
def docs(session: nox.Session) -> None:
    """
    Build the docs. Will serve unless --non-interactive
    """
    session.install("-e.[docs]")
    session.run("mkdocs", "serve" if session.interactive else "build")
