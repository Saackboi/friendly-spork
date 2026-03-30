def test_unregister_removes_existing_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    endpoint = f"/activities/{activity}/participants?email={email}"

    # Act
    response = client.delete(endpoint)
    all_activities = client.get("/activities").json()

    # Assert
    assert response.status_code == 200
    assert email not in all_activities[activity]["participants"]


def test_unregister_returns_404_for_missing_activity(client):
    # Arrange
    endpoint = "/activities/Unknown%20Activity/participants?email=student@mergington.edu"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_missing_participant(client):
    # Arrange
    endpoint = "/activities/Chess%20Club/participants?email=unknown@mergington.edu"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
