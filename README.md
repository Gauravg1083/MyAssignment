# OTP auth microservice

This repository contains the code for otp auth microservice.

Tech Stack consist of :

- python
- django
- djangorestframework
- django-otp
- twilio
- and some basic libraries.

# Introduction

The Authentication Microservice is a standalone application designed to provide secure user authentication functionality for web applications. It includes OTP-based authentication, password reset, account information update, and optionally, role-based authorization. This microservice follows RESTful architecture principles.

## Purpose

The purpose of this microservice is to establish a robust and secure authentication system for web applications. It allows users to authenticate using OTP-based methods, reset their passwords when necessary, and update their account information while ensuring scalability and fault tolerance.

## Scope

- Developed as a standalone service.
- Follows RESTFUL API design principles.
- Functionalities:
  - User Registration
  - User Login with OTP-based Authentication
  - Password Reset
  - Account Information Update


## Functional Requirements

### User Registration

- Collect the following information during registration:
  - First name
  - Last name
  - Email address
  - Phone number
  - Password
Validates user information.
Triggers an email with an OTP for email verification.

### User Login with OTP-based Authentication

- Enables users to log in using their phone number and OTP-based authentication.
- Sends OTP via SMS.
- Validates OTP and authenticates the user.

### Password Reset

- Allows users to reset their passwords using their email address.
- Sends an email with a link for password reset.

### Account Information Update

- Enables users to update their account information, including:
  - First name
  - Last name
  - Email
  - Phone number
  - Password
Validates the updated information.


## Conclusion

The Authentication Microservice is a critical component to ensure the secure and reliable authentication of users in our web applications. While the listed features and non-functional requirements are essential, they serve as guidelines to assess your problem-solving approach.
