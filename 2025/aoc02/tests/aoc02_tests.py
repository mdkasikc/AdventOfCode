import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.aoc02 import get_invalid_ids, is_invalid_id, add_up_invalid_ids

TEST_INPUT = (
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
    "1698522-1698528,446443-446449,38593856-38593862,"
    "565653-565659,824824821-824824827,2121212118-2121212124"
)

def test__invalid__id():
    assert is_invalid_id(1212) == True
    assert is_invalid_id(123123) == True
    assert is_invalid_id(9999) == True
    assert is_invalid_id(122345) == False
    assert is_invalid_id(123456) == False
    assert is_invalid_id(111111) == True
    assert is_invalid_id(1234554321) == False
    assert is_invalid_id(101) == False
    assert is_invalid_id(1001) == False
    assert is_invalid_id(111) == False
    assert is_invalid_id(565656) == False
    assert is_invalid_id(2121212121) == False

def test__count_invalid_ids():
    assert len(get_invalid_ids("11-22")) == 2
    assert len(get_invalid_ids("95-115")) == 1
    assert len(get_invalid_ids("998-1012")) == 1
    assert len(get_invalid_ids("1188511880-1188511890")) == 1
    assert len(get_invalid_ids("222220-222224")) == 1
    assert len(get_invalid_ids("1698522-1698528")) == 0
    assert len(get_invalid_ids("446443-446449")) == 1
    assert len(get_invalid_ids("38593856-38593862")) == 1

def test__summed_invalid_ids():
    assert add_up_invalid_ids("11-22,95-115,998-1012,1188511880-1188511890,222220-222224," \
    "1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827," \
    "2121212118-2121212124") == 1227775554