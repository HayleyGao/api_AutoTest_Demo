# content of conftest.py
import pytest
import smtplib


@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.qq.com", 465, timeout=5)

@pytest.fixture(scope="module")
def hello():
    return "hello!"


@pytest.fixture(scope="session")
def scope_session():
    return 'scope="session"'


@pytest.fixture(scope="class")
def scope_class():
    return 'scope="class"'


@pytest.fixture(scope="function")
def scope_function():
    return 'scope="function"'



