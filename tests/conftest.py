"""Put test fixtures here."""


from click.testing import CliRunner

from faker import Faker

import pytest


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.fixture(scope="session")
def return_faker_data():
    """Return fake faker library data."""
    faker = Faker(locale="en_US")
    input_dict = dict(
        firstName=faker.first_name(),
        lastName=faker.last_name(),
        userId=faker.random_number(digits=5),
        email=faker.email(),
    )
    return input_dict


@pytest.fixture
def fake_filesystem(fs):  # pylint:disable=invalid-name
    """Create a fake filesystem."""
    yield fs


@pytest.fixture(scope="session")
def input_data():
    """Use for data in tests."""
    input_dict = dict(
        sample_name="DECOTEAU, BRANDI TERRESITA",
        split_text_directory="./tests/after_google_processing.txt",
        pat=r"(DEFENDANT\nNAME:(.*))STREET:(.*)CITY/STATE/ZIP:\n(.*)CASE I",
        name_separate_pattern_match="(.*),(.*)",
        report_name="docxdemodata.docx",
        df_data=dict(
            calorierbes=[420, 380, 390],
            duratierbn=[50, 40, 45],
        ),
        template_name="conftest_template_name.jinja2",
    )
    return input_dict


# df_to_word_data=dict(
#             "calorierbes"=[420, 380, 390],
#             "duratierbn"=[50, 40, 45],
#         )
#         report_name='./__output_files/wordreportname'
