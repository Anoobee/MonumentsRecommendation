# Database Schema

## Monument Table

Stores information about each monument.

| Column       | Type         | Description                    |
| ------------ | ------------ | ------------------------------ |
| id           | INT          | Primary key                    |
| name         | VARCHAR(255) | Name of the monument           |
| latitude     | FLOAT        | Latitude coordinate            |
| longitude    | FLOAT        | Longitude coordinate           |
| location     | VARCHAR(255) | Textual location description   |
| type         | VARCHAR(50)  | Type of monument               |
| popularity   | FLOAT        | Popularity score (0-1)         |
| indoor       | BOOLEAN      | Whether the monument is indoor |
| best\_season | VARCHAR(20)  | Best season to visit           |
| best\_time   | VARCHAR(20)  | Best time of day to visit      |
| description  | TEXT         | Monument description           |
| image\_url   | VARCHAR(255) | URL to monument image          |

## Events Table

Stores information about events at monuments.

| Column       | Type         | Description                |
| ------------ | ------------ | -------------------------- |
| id           | INT          | Primary key                |
| monument\_id | INT          | Foreign key to monument.id |
| name         | VARCHAR(255) | Name of the event          |
| start\_date  | DATE         | Event start date           |
| end\_date    | DATE         | Event end date             |
| description  | TEXT         | Event description          |
