from nox import session

@session(python=['3.8', '3.9', '3.10', '3.11'], reuse_venv=True)
def test(session):
    session.run('poetry', 'shell', external=True)
    session.run('poetry', 'install', external=True)
    session.run('pytest')
