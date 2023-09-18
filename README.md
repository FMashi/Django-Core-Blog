# Django-Core-Blog
Django-Core-Blog is a simple and basic blog project built with Django. It provides essential functionality for managing posts, categories (cats), and tags. The project also includes a straightforward Bootstrap-based front-end for presentation.

## Project Overview

This project serves as a foundational starting point for building a blog using Django. It offers the following key features:

- **Posts:** Create, edit, and manage blog posts with rich content using the CKEditor library.

- **Categories:** Organize posts into categories, providing a structured way to group related content.

- **Tags:** Add tags to posts to improve content discoverability and navigation.

- **Bootstrap Front-End:** A minimalistic front-end design based on Bootstrap for displaying blog content.

The project is intentionally kept simple, making it an ideal starting point for developers looking to build more advanced blogging platforms.

## Search Functionality

Django-Core-Blog includes built-in search functionality that allows users to search for specific content within the blog. You can perform searches for posts, categories, and tags. The search feature provides a convenient way to discover relevant content quickly.

To use the search functionality:

1. Navigate to the search bar on the website's front-end.

2. Enter your search query, such as keywords, post titles, categories, or tags.

3. Click the "Go!" button to initiate the search.

The search results will be displayed, helping users find the content they are looking for efficiently.

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/FMashi/Django-Core-Blog.git
 
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
 
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser account to access the admin panel:

   ```bash
   python manage.py createsuperuser

6. Start the development server:

   ```bash
    python manage.py runserver

The project should now be running locally at http://localhost:8000/. You can access the admin panel at http://localhost:8000/admin/ and use the superuser credentials created in step 5 to log in.

## Usage

    Create and manage posts in the admin panel by adding content and specifying categories and tags.

    Navigate to the front-end to view and interact with the published blog posts.

## Dependencies

The main libraries and packages used in this project include:

    Django: A high-level Python web framework.

    CKEditor: A rich text editor for creating and editing blog content.

    Pillow: A Python Imaging Library that simplifies image handling.

## Future Development
This project can be further developed and extended to include additional features and improvements, such as user registration, comments, search functionality, and more. Feel free to contribute or build upon this foundation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

   ```vbnet
   Please replace `"https://github.com/yourusername/Django-Core-Blog.git"` with the actual URL of your project's GitHub repository.

   This README provides an overview of your Django project, installation instructions, usage guidance, information about dependencies, and hints for future development. You can extend it further to include more details, such as project structure, customization instructions, and contribution guidelines, based on your specific project requirements.


