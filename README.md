Movie Review API

A simple REST API built with Django and Django REST Framework (DRF) for managing movie reviews.

_____________________________________________________________________________________________________

I Created two apps;
-Users to handle user authentication and profile.
-Reviews for movie reviews

Users:
Accessed Django’s built-in authentication system for login and logout functions.
Created a signup method for registering new users.
Each user acquires a profile and can update it and view it when logged in.
Each user can view other user's profiles but cannot edit them.
A user's profile also shows the movies reviewed by that user.

Reviews:
I Created two models Movie and Review,
Movie enables a user to add a new movie for review and a description plus the date.
Review enables a user to rate a movie and add review content about it.
A user cannot review the same movie twice.

_______________________________________________________________________________________________________

End Points.

Auth Endpoints:

POST /api/users/signup/ – Register user

POST /api-auth/login/ – Login user

POST /api-auth/logout/ – Logout user

GET /api/users/ - UserList

PUT /api/users/{id}/ – Update user

DELETE /api/users/{id}/ – Delete user

GET /api/users/profile/ – view user profile

GET /api/users/profile/{id} - view user's profile

PUT /api/users/profile/update/ - update user profile


Movie Endpoints:

POST /api/reviews/movies/ - Create movie


Review Endpoints:

GET /api/reviews/reviews – List all reviews

POST /api/reviews/reviews – Create review

GET /api/reviews/reviews/{id}/ – Get single review

PUT /api/reviews/reviews/{id}/ – Update review

DELETE /api/reviews/reviews/{id}/ – Delete review