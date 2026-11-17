import pytest
from bowling_alley import lane_cost, frame_score, lane_assignment


@pytest.mark.parametrize(
    "args, expected",
    [
        (("weekday", 2, 4, 2, False), 900),
        (("weekend", 1, 5, 1, False), 750),
        (("weekday", 1, 2, 0, True), 320),
        (("weekend", 2, 6, 6, True), 1360),
    ],
)
def test_valid_lane_costs(args, expected):
    assert lane_cost(*args) == expected


@pytest.mark.parametrize(
    "args",
    [
        ("holiday", 1, 2, 0, False),
        ("weekday", 0, 2, 0, False),
        ("weekday", 1, 0, 0, False),
        ("weekday", 1, 7, 0, False),
        ("weekday", 1, 2, 3, False),
    ],
)
def test_invalid_lane_cost_bookings(args):
    with pytest.raises(ValueError):
        lane_cost(*args)


@pytest.mark.parametrize(
    "rolls, expected",
    [
        ((3, 4, []), 7),
        ((10, 0, [5, 2]), 17),
        ((7, 3, [8]), 18),
        ((0, 0, []), 0),
    ],
)
def test_valid_frame_scores(rolls, expected):
    assert frame_score(*rolls) == expected


@pytest.mark.parametrize(
    "rolls",
    [((-1, 0, [])), ((11, 0, [])), ((0, -1, [])), ((8, 3, []))],
)
def test_invalid_frame_rolls(rolls):
    with pytest.raises(ValueError):
        frame_score(*rolls)


@pytest.mark.parametrize(
    "args, expected",
    [
        ((2, False, 0), "wait"),
        ((2, True, 1), "bumper lane"),
        ((7, False, 2), "two lanes"),
        ((7, False, 1), "wait"),
        ((6, False, 1), "standard lane"),
    ],
)
def test_lane_assignment_outcomes(args, expected):
    assert lane_assignment(*args) == expected


