# Lil Blog

![Logo](https://github.com/miracseref/lil-blog/blob/main/website/static/images/lil-blog-logo.png)

Lil Blog, simply what a blog does: post, comment and like.

## Features

- Light/dark mode toggle
- Password & mail strength checker with RegEx
- Create & delete posts and comments
- Like post
- Create profile
- Sign up, login & logout
- Appropriate warning messages

## Screenshots

| Pages/Mode | Light                                                                                                     | Dark                                                                                                    |
| ---------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Login      | ![Login Light](https://github.com/miracseref/lil-blog/blob/main/website/static/images/login_light.png)    | ![Login Dark](https://github.com/miracseref/lil-blog/blob/main/website/static/images/login_dark.png)    |
| Sign up    | ![Sign Up Light](https://github.com/miracseref/lil-blog/blob/main/website/static/images/signup_light.png) | ![Sign Up Dark](https://github.com/miracseref/lil-blog/blob/main/website/static/images/signup_dark.png) |
| Posts      | ![Posts Light](https://github.com/miracseref/lil-blog/blob/main/website/static/images/posts_light.png)    | ![Posts Dark](https://github.com/miracseref/lil-blog/blob/main/website/static/images/posts_dark.png)    |
| User       | ![User Light](https://github.com/miracseref/lil-blog/blob/main/website/static/images/user_light.png)      | ![User Dark](https://github.com/miracseref/lil-blog/blob/main/website/static/images/user_dark.png)      |

## Tech Stack

**Client:** JavaScript, Tailwind CSS

**Server:** Flask (Python)

## Run Locally

Clone the project

```bash
git clone https://github.com/miracseref/lil-blog.git
```

Go to the project directory

```bash
  cd lil-blog
```

Install Python dependencies

```bash
pip install -r requirements.txt
```

Install JavaScript dependencies

```bash
npm install package.json
```

## Environment Variables

To run this project, you will need to create and add the following environment variables to your config.py file

`SECRET_KEY`

`SQLALCHEMY_DATABASE_URI`
