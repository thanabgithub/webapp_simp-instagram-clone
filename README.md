# webapp_simp-instagram-clone

DEMO: Inspired by Instagram.
By Thana B. and Punyapat

Hey everyone, I have just finished only the backbone backend part of the project.

To summarize the my outcome, let me share api docs as the following

[api docs](http://api.insta.thana.team/docs)

But the complete version is coming soon.

Here are what I have in mind.

# Architecture/Stack

- Docker
- Postgresql
- SQLAlchemy
- Alembic
- FastAPI
- React
- NGINX
- strapi

# Well-thought-out points

Backend

- Usage of a docker container to achieve the independence of environment and reliability of deployment
- Usage of CRUD generator to enhance the efficiency of the backend development
  Frontend
- Usage of CMS for administration console to enhance the efficiency of the backend development

# Phase

Phase 1 : Backend development
Phase 2.1 : Frontend development (Client)
Phase 2.2 : Frontend development (Admin)
Development procedures are grouped by timeline. In concrete, Frontend developments for client and admin will be conducted at the same time.

# Possible upgrade

Implementation of Jamstack is one of the choices I may consider making in the future.
According to jamstack.org, "The core principles of pre-rendering, and decoupling, enable sites and applications to be delivered with greater confidence and resilience than ever before.". I may break down service from what mentioned "Traditional Web" into "Jamstack".
![Jamstack architecture](https://d33wubrfki0l68.cloudfront.net/b7d16f7f3654fb8572360301e60d76df254a323e/385ec/img/svg/architecture.svg)
ref: https://jamstack.org/
The required procedure would be

1. migration webserver to CDN
2. conversion of monolithic to microservices

# Acknowledge

Big thanks to the following content providers

- Very Academy
  https://www.youtube.com/watch?v=NH4VZaP3_9s&t=2183s
- Luis Luis
  https://github.com/LuisLuii/FastAPIQuickCRUD
- awtkns
  https://fastapi-crudrouter.awtkns.com/
- Docker Captain Program
  https://www.udemy.com/course/docker-mastery-for-nodejs/
- Catalin Stefan
  https://www.udemy.com/course/completefastapi
  https://www.udemy.com/course/instagram-clone
  and other content providers from Youtube, Udemy, Stackoverflow, etc.
