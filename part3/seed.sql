-- HBnB Initial Data Seed
-- This script inserts initial data into the HBnB database

-- Insert administrator user
-- Password: admin123 (hashed with bcrypt)
INSERT INTO users (id, created_at, updated_at, first_name, last_name, email, password, is_admin)
VALUES (
    'admin-user-uuid-1234',
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    'Admin',
    'User',
    'admin@hbnb.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyPWpOKgAb76',  -- bcrypt hash of 'admin123'
    TRUE
);

-- Insert common amenities
INSERT INTO amenities (id, created_at, updated_at, name) VALUES
    ('amenity-wifi-uuid-001', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'WiFi'),
    ('amenity-pool-uuid-002', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Swimming Pool'),
    ('amenity-parking-uuid-003', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Parking'),
    ('amenity-ac-uuid-004', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Air Conditioning'),
    ('amenity-kitchen-uuid-005', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Kitchen'),
    ('amenity-tv-uuid-006', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'TV'),
    ('amenity-gym-uuid-007', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Gym'),
    ('amenity-laundry-uuid-008', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Laundry'),
    ('amenity-pets-uuid-009', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Pet Friendly'),
    ('amenity-balcony-uuid-010', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Balcony');

-- Optional: Insert a sample place owned by admin
INSERT INTO places (id, created_at, updated_at, name, description, city, price, latitude, longitude, owner_id)
VALUES (
    'place-sample-uuid-001',
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    'Cozy Downtown Apartment',
    'Beautiful apartment in the heart of the city',
    'San Francisco',
    150.0,
    37.7749,
    -122.4194,
    'admin-user-uuid-1234'
);

-- Link some amenities to the sample place
INSERT INTO place_amenity (place_id, amenity_id) VALUES
    ('place-sample-uuid-001', 'amenity-wifi-uuid-001'),
    ('place-sample-uuid-001', 'amenity-ac-uuid-004'),
    ('place-sample-uuid-001', 'amenity-kitchen-uuid-005'),
    ('place-sample-uuid-001', 'amenity-tv-uuid-006');

-- Display inserted data
SELECT 'Users:' AS '';
SELECT id, email, is_admin FROM users;

SELECT 'Amenities:' AS '';
SELECT id, name FROM amenities;

SELECT 'Places:' AS '';
SELECT id, name, city, price FROM places;

SELECT 'Place Amenities:' AS '';
SELECT p.name AS place_name, a.name AS amenity_name
FROM place_amenity pa
JOIN places p ON pa.place_id = p.id
JOIN amenities a ON pa.amenity_id = a.id;
