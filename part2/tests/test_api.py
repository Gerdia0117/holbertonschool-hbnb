# tests/test_api.py
import unittest
import json
from run import app

class TestHBnBAPI(unittest.TestCase):
    """Test suite for HBnB API endpoints (Part 2)"""

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.user_id = None
        cls.place_id = None
        cls.amenity_id = None
        cls.review_id = None

    # ---------------------
    # User Endpoints
    # ---------------------
    def test_1_create_user(self):
        res = self.client.post("/api/v1/users/",
            data=json.dumps({"email": "test@example.com", "password": "123456"}),
            content_type="application/json")
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertIn("id", data)
        self.assertNotIn("password", data)
        TestHBnBAPI.user_id = data["id"]

    def test_2_get_users(self):
        res = self.client.get("/api/v1/users/")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertIsInstance(data, list)
        self.assertTrue(any(u["id"] == TestHBnBAPI.user_id for u in data))

    def test_3_update_user(self):
        res = self.client.put(f"/api/v1/users/{TestHBnBAPI.user_id}",
            data=json.dumps({"email": "new@example.com"}),
            content_type="application/json")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["email"], "new@example.com")

    # ---------------------
    # Place Endpoints
    # ---------------------
    def test_4_create_place(self):
        payload = {
            "name": "Beach House",
            "owner_id": TestHBnBAPI.user_id,
            "price": 200
        }
        res = self.client.post("/api/v1/places/",
            data=json.dumps(payload),
            content_type="application/json")
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertIn("id", data)
        TestHBnBAPI.place_id = data["id"]

    def test_5_get_places(self):
        res = self.client.get("/api/v1/places/")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(any(p["id"] == TestHBnBAPI.place_id for p in data))

    def test_6_update_place(self):
        payload = {"name": "Mountain Cabin", "price": 150}
        res = self.client.put(f"/api/v1/places/{TestHBnBAPI.place_id}",
            data=json.dumps(payload),
            content_type="application/json")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["name"], "Mountain Cabin")
        self.assertEqual(data["price"], 150)

    # ---------------------
    # Amenity Endpoints
    # ---------------------
    def test_7_create_amenity(self):
        res = self.client.post("/api/v1/amenities/",
            data=json.dumps({"name": "WiFi"}),
            content_type="application/json")
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertIn("id", data)
        TestHBnBAPI.amenity_id = data["id"]

    def test_8_get_amenities(self):
        res = self.client.get("/api/v1/amenities/")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(any(a["id"] == TestHBnBAPI.amenity_id for a in data))

    # ---------------------
    # Review Endpoints
    # ---------------------
    def test_9_create_review(self):
        payload = {
            "text": "Amazing stay!",
            "user_id": TestHBnBAPI.user_id,
            "place_id": TestHBnBAPI.place_id
        }
        res = self.client.post("/api/v1/reviews/",
            data=json.dumps(payload),
            content_type="application/json")
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertIn("id", data)
        TestHBnBAPI.review_id = data["id"]

    def test_10_get_reviews_by_place(self):
        res = self.client.get(f"/api/v1/reviews/place/{TestHBnBAPI.place_id}")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(any(r["id"] == TestHBnBAPI.review_id for r in data))

    def test_11_delete_review(self):
        res = self.client.delete(f"/api/v1/reviews/{TestHBnBAPI.review_id}")
        self.assertEqual(res.status_code, 200)
        # Confirm deletion
        res = self.client.get(f"/api/v1/reviews/{TestHBnBAPI.review_id}")
        self.assertEqual(res.status_code, 404)

if __name__ == "__main__":
    unittest.main()
