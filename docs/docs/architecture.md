# System Architecture

## Overview

The Monument Recommendation system follows a microservices architecture with the following components:

1. **FastAPI Backend**: Handles API requests and recommendation logic
2. **MySQL Database**: Stores monument and user data
3. **MkDocs**: Provides system documentation

## Component Diagram

```
┌────────────────┐     ┌────────────────┐
│                │     │                │
│  FastAPI API   │◄────►  MySQL Database│
│   (Port 8000)  │     │   (Port 3307)  │
│                │     │                │
└────────────────┘     └────────────────┘
        ▲
        │
        │
        ▼
┌────────────────┐
│                │
│  MkDocs Docs   │
│   (Port 8001)  │
│                │
└────────────────┘
```

## Recommendation Algorithm

The recommendation system uses weighted scoring based on multiple factors:

1. **Distance**: Proximity to user's current location
2. **Type Match**: Match with user's preferred monument type
3. **Popularity**: Overall popularity of the monument
4. **Seasonal Factors**: Current season and weather conditions
5. **Events**: Ongoing or upcoming events at the monument

The final score is calculated as a weighted sum of these individual scores, and monuments are ranked based on their final scores.

## Data Flow

1. User submits location and preferences
2. System retrieves monument data from the database
3. Recommendation algorithm calculates scores for each monument
4. Monuments are sorted by score
5. Top recommendations are returned to the user
