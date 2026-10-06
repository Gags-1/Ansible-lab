# Ansible EC2 Docker Deployment

A small infrastructure automation project using Ansible to provision an Ubuntu EC2 instance, install Docker, and deploy a containerized FastAPI application.

## Architecture

```text
Developer / Control Node
          |
          | SSH
          v
     Ubuntu EC2
          |
       Ansible
          |
    +-----+------+
    |            |
 Docker       Application
    |            |
    +-----+------+
          |
     FastAPI Container
