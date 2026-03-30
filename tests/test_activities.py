def test_get_activities_returns_all_activity_data(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_each_activity_has_expected_shape(client):
    # Arrange
    endpoint = "/activities"
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for _, details in payload.items():
        assert required_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)
