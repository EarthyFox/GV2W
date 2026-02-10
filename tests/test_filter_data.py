"""Test cases."""

# from pathlib import Path

# import pandas as pd

from src.filter_data import (
    # capital_case,
    # df_to_word,
    # filter_text_data,
    separate_names_into_first_last,
    # template_w_pathlib,
)


def test_separate_names_into_first_last_succeeds(input_data) -> None:
    """Separate names into first and last names."""
    # result = separate_names_into_first_last()
    result = separate_names_into_first_last(
        pat=input_data["name_separate_pattern_match"],
        fullname=input_data["sample_name"],
    )

    expected = {
        "full_name": "DECOTEAU, BRANDI TERRESITA",
        "first_name": " BRANDI TERRESITA",
        "last_name": "DECOTEAU",
    }
    expected_type = dict

    assert expected == result
    assert isinstance(result, expected_type)
    print(result)


# def test_filter_text_data_succeeds(input_data) -> None:
#     """Test filter text data using regular expression."""
#     result = filter_text_data(
#         directory=input_data["split_text_directory"],
#         pat_match=input_data["pat"],
#     )

#     expected_type = pd.DataFrame


# def test_template_w_pathlib(return_faker_data, input_data) -> None:
#     """Test output data using template."""
#     result = template_w_pathlib(
#         input_dict_name=return_faker_data,
#         template_name=input_data["template_name"],
#     )

#     expected = "{'firstName': '"
#     expected_type = str

#     assert expected in result
# assert isinstance(result, expected_type)
# print(result)
