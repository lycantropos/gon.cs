from fractions import Fraction

from hypothesis import given

from tests.binding import Point
from tests.hints import Scalar
from . import strategies


@given(strategies.scalars, strategies.scalars)
def test_basic(x: Scalar, y: Scalar) -> None:
    result = Point(x, y)

    assert isinstance(result, Point)
    assert isinstance(result.x, Fraction)
    assert isinstance(result.y, Fraction)
    assert result.x == x
    assert result.y == y
