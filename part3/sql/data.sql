-- HBnB Sample Data
-- This script inserts sample data for testing and demonstration

-- Insert sample users
INSERT INTO users (id, created_at, updated_at, first_name, last_name, email, password, is_admin) VALUES
    ('user-sample-001', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Alice', 'Johnson', 'alice@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyPWpOKgAb76', FALSE),
    ('user-sample-002', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Bob', 'Smith', 'bob@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyPWpOKgAb76', FALSE),
    ('user-sample-003', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Carol', 'Williams', 'carol@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyPWpOKgAb76', FALSE);

-- Insert sample places
INSERT INTO places (id, created_at, updated_at, name, description, city, price, latitude, longitude, owner_id) VALUES
    ('place-sample-002', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Modern Loft', 'Stylish loft in downtown area', 'New York', 200.0, 40.7128, -74.0060, 'user-sample-001'),
    ('place-sample-003', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Beach Cottage', 'Relaxing cottage by the beach', 'Miami', 180.0, 25.7617, -80.1918, 'user-sample-001'),
    ('place-sample-004', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Mountain Retreat', 'Peaceful cabin in the mountains', 'Denver', 150.0, 39.7392, -104.9903, 'user-sample-002'),
    ('place-sample-005', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'City Studio', 'Compact studio in the heart of the city', 'San Francisco', 175.0, 37.7749, -122.4194, 'user-sample-003');

-- Link amenities to places
INSERT INTO place_amenity (place_id, amenity_id) VALUES
    -- Modern Loft amenities
    ('place-sample-002', 'amenity-wifi-uuid-001'),
    ('place-sample-002', 'amenity-ac-uuid-004'),
    ('place-sample-002', 'amenity-tv-uuid-006'),
    ('place-sample-002', 'amenity-gym-uuid-007'),
    
    -- Beach Cottage amenities
    ('place-sample-003', 'amenity-wifi-uuid-001'),
    ('place-sample-003', 'amenity-pool-uuid-002'),
    ('place-sample-003', 'amenity-parking-uuid-003'),
    ('place-sample-003', 'amenity-ac-uuid-004'),
    
    -- Mountain Retreat amenities
    ('place-sample-004', 'amenity-wifi-uuid-001'),
    ('place-sample-004', 'amenity-parking-uuid-003'),
    ('place-sample-004', 'amenity-kitchen-uuid-005'),
    ('place-sample-004', 'amenity-pets-uuid-009'),
    
    -- City Studio amenities
    ('place-sample-005', 'amenity-wifi-uuid-001'),
    ('place-sample-005', 'amenity-ac-uuid-004'),
    ('place-sample-005', 'amenity-kitchen-uuid-005'),
    ('place-sample-005', 'amenity-laundry-uuid-008');

-- Insert sample reviews
INSERT INTO reviews (id, created_at, updated_at, text, rating, user_id, place_id) VALUES
    ('review-sample-001', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Amazing place! Very clean and comfortable.', 5, 'user-sample-002', 'place-sample-002'),
    ('review-sample-002', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Great location and beautiful view.', 5, 'user-sample-003', 'place-sample-002'),
    ('review-sample-003', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Perfect beach getaway! Loved every minute.', 5, 'user-sample-002', 'place-sample-003'),
    ('review-sample-004', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Very peaceful and relaxing. Highly recommend!', 4, 'user-sample-003', 'place-sample-004'),
    ('review-sample-005', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Good value for money. Clean and convenient.', 4, 'user-sample-001', 'place-sample-005');

-- Display summary of inserted data
SELECT 'Summary of Sample Data:' AS '';
SELECT '========================' AS '';
SELECT '' AS '';

SELECT 'Users:' AS '';
SELECT COUNT(*) AS total_users FROM users WHERE id LIKE 'user-sample-%';

SELECT 'Places:' AS '';
SELECT COUNT(*) AS total_places FROM places WHERE id LIKE 'place-sample-%';

SELECT 'Reviews:' AS '';
SELECT COUNT(*) AS total_reviews FROM reviews WHERE id LIKE 'review-sample-%';

SELECT 'Place-Amenity Links:' AS '';
SELECT COUNT(*) AS total_links FROM place_amenity WHERE place_id LIKE 'place-sample-%';

SELECT '' AS '';
SELECT 'Sample Places with Amenities:' AS '';
SELECT p.name AS place, p.city, p.price, GROUP_CONCAT(a.name, ', ') AS amenities
FROM places p
LEFT JOIN place_amenity pa ON p.id = pa.place_id
LEFT JOIN amenities a ON pa.amenity_id = a.id
WHERE p.id LIKE 'place-sample-%'
GROUP BY p.id;
