from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "student@example.com"

    from urllib.parse import quote

    activity_path = quote(activity_name, safe="")
    client.post(f"/activities/{activity_path}/signup", params={"email": email})

    response = client.delete(
        f"/activities/{activity_path}/unregister", params={"email": email}
    )
    assert response.status_code == 200
    assert email not in response.json()["participants"]
