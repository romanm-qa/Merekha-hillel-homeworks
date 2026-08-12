import logging
import pytest

from lesson_24_cars_api_search.models import Car

logger = logging.getLogger("cars_api_tests")


class TestCarsSearch:
    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            pytest.param("brand", 5, id="sort-by-brand-limit-5"),
            pytest.param("year", 10, id="sort-by-year-limit-10"),
            pytest.param(
                "engine_volume",
                7,
                id="sort-by-engine-volume-limit-7",
            ),
            pytest.param("price", 3, id="sort-by-price-limit-3"),
            pytest.param("brand", 15, id="sort-by-brand-limit-15"),
            pytest.param("price", 25, id="sort-by-price-limit-25"),
        ],
    )
    def test_cars_search(
            self,
            authenticated_session,
            cars_api_url,
            sort_by,
            limit,
    ):
        """Проверяет сортировку, лимит и структуру данных автомобилей."""
        logger.info(
            "Searching cars with sort_by=%s and limit=%s",
            sort_by,
            limit,
        )

        response = authenticated_session.get(
            f"{cars_api_url}/cars",
            params={"sort_by": sort_by, "limit": limit},
            timeout=10,
        )

        assert response.status_code == 200, response.text

        cars_data = response.json()

        assert isinstance(cars_data, list)
        assert len(cars_data) == limit

        validated_cars = [
            Car.model_validate(car_data)
            for car_data in cars_data
        ]

        actual_values = [
            getattr(car, sort_by)
            for car in validated_cars
        ]

        assert actual_values == sorted(actual_values)

        logger.info(
            "Cars search passed: sort_by=%s, returned=%s",
            sort_by,
            len(validated_cars),
        )
