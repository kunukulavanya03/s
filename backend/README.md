# Community Blog and Mobile App Design

This is a community-focused blog and mobile app design website.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/community-blog-and-mobile-app-design.git`
2. Change into the directory: `cd community-blog-and-mobile-app-design`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows)
5. Install the dependencies: `pip install -r requirements.txt`
6. Run the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Endpoints

### Auth

* `POST /api/auth/register`: Register a new user account
* `POST /api/auth/login`: Log in to an existing user account

### Posts

* `GET /api/posts`: Retrieve a list of all blog posts
* `GET /api/posts/{post_id}`: Retrieve a single blog post by ID
* `POST /api/posts`: Create a new blog post
* `PUT /api/posts/{post_id}`: Update an existing blog post
* `DELETE /api/posts/{post_id}`: Delete a blog post

### Designs

* `GET /api/designs`: Retrieve a list of all mobile app designs
* `GET /api/designs/{design_id}`: Retrieve a single mobile app design by ID
* `POST /api/designs`: Create a new mobile app design
* `PUT /api/designs/{design_id}`: Update an existing mobile app design
* `DELETE /api/designs/{design_id}`: Delete a mobile app design

### Comments

* `GET /api/comments`: Retrieve a list of all comments
* `GET /api/comments/{comment_id}`: Retrieve a single comment by ID
* `POST /api/comments`: Create a new comment
* `PUT /api/comments/{comment_id}`: Update an existing comment
* `DELETE /api/comments/{comment_id}`: Delete a comment
