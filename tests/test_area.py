from src.area import (
    area_circle,
    area_rectangle,
    area_triangle,
    area_square,
    area_trapezoid,
    area_parallelogram,
    area_ellipse,
)


def test_area_circle():
    assert area_circle(5) == 78.53975


def test_area_rectangle():
    assert area_rectangle(5, 10) == 50


def test_area_triangle():
    assert area_triangle(5, 10) == 25


def test_area_square():
    assert area_square(5) == 25


def test_area_trapezoid():
    assert area_trapezoid(5, 10, 15) == 112.5


def test_area_parallelogram():
    assert area_parallelogram(5, 10) == 50


def test_area_ellipse():
    assert area_ellipse(5, 10) == 157.0795
