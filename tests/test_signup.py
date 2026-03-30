def test_signup_adds_new_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    endpoint = f"/activities/{activity}/signup?email={email}"

    # Act
    response = client.post(endpoint)
    all_activities = client.get("/activities").json()

    # Assert
    assert response.status_code == 200
    assert email in all_activities[activity]["participants"]


def test_signup_returns_404_for_missing_activity(client):
    # Arrange
    endpoint = "/activities/Unknown%20Activity/signup?email=student@mergington.edu"

    # Act
    response = client.post(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_for_duplicate_participant(client):
    # Arrange
    activity = "Chess Club"
    duplicate_email = "michael@mergington.edu"
    endpoint = f"/activities/{activity}/signup?email={duplicate_email}"

    # Act
    response = client.post(endpoint)

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"
