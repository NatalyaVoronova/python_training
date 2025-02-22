import pytest
from fixture.application import Application


#pytest.fixture() # фикстура создается для каждого теста
@pytest.fixture(scope="session")  # фикстура создается одна для всех тестов
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
