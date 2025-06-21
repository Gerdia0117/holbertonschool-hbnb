HBnB Evolution - Technical Documentation (Part 1)
Project Overview

HBnB Evolution is an AirBnB-like application that enables:

    User account management and authentication

    Property listing and management

    Review system for properties

    Amenity tracking and association

System Architecture
Three-Layer Architecture

    Presentation Layer

        REST API endpoints (UserAPI, PlaceAPI, ReviewAPI, AmenityAPI)

        Handles HTTP requests/responses

        Input validation

    Business Logic Layer

        Core domain models (User, Place, Review, Amenity)

        Business rules and validations

        Transaction management

    Persistence Layer

        Database repositories

        Data access objects

        ORM mapping

Technical Specifications
Requirements

    All entities must have:

        UUID primary key

        createdAt/updatedAt timestamps

    Users must have admin flag

    Places must reference owner

    Reviews must reference both user and place

Design Patterns

    Facade pattern between layers

    Repository pattern for data access

    DTO pattern for API responses

Implementation Guidance

    Start with Business Layer
    Implement core models first with validation logic

    Add Persistence
    Create repository interfaces before concrete implementations

    Build API Layer
    Develop endpoints after business logic is stable

    Test Vertically
    Test full stack for each feature (API → Business → DB)

Resources

    UML Basics

    Package Diagrams Guide

    Sequence Diagrams Tutorial
