""" Authentikate is a simple token based authentication library for Python

Authentikate is a simple token based authentication library for Python. It 
provides convenient functions to authenticate requests and decode tokens, 
authenticating users and applications.

It is designed to be used with Django, but can be used with any Python
framework.

Supported Token Types
- JWT (JSON Web Tokens) (with client_id, user_id, scopes, and expiration)
- Static tokens (for testing and pre-defined tokens)


 """
from authentikate.structs import Auth, AuthentikateSettings
from authentikate.utils import authenticate_header, authenticate_token

__version__ = "0.0.1"

__all__ = ["Auth", "AuthentikateSettings", "authenticate_header", "authenticate_token"]
