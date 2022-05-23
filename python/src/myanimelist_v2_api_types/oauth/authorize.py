from typing_extensions import Literal, NotRequired, TypedDict


class AuthorizeParams(TypedDict):
    """
    AuthorizeParams(data: Dict[str, Any]) -> AuthorizeParams
    AuthorizeParams(**attrs: Any) -> AuthorizeParams
    Query parameters for constructing an oauth authorization URL.

    Taken from https://myanimelist.net/blog.php?eid=835707.
    """
    response_type: Literal["code"]
    """The response type. Must be ``code``."""

    client_id: str
    """The app's client ID."""

    code_challenge: str
    """The code challenge for the request.
    
    .. epigraph::
    
        The OAuth workflow is susceptible to the authorisation code interception attack.
        The PKCE protocol has been designed to mitigate this threat.
        
        Before you can authenticate a user, your client needs to generate a Code Verifier
        and a Code Challenge. A Code Verifier is a high-entropy, cryptographic, random
        string containing only the characters ``[A-Z]`` / ``[a-z]`` / ``[0-9]`` / ``-`` / ``.`` / ``_`` / ``~``.
        The length of the string must be between 43 and 128 characters (128 characters is recommended).
        
        MAL only allows the plain transformation for the Code Challenge. In other words,
        it means that you have to set the Code Challenge equal to the Code Verifier. Simple.
        
        This is a small example of a PKCE generator written in Python (`GitLab Snippet 
        <https://gitlab.com/snippets/1992501>`_):
        
        .. code-block:: python
        
            import secrets
            
            def get_new_code_verifier() -> str:
                token = secrets.token_urlsafe(100)
                return token[:128]
            
            code_verifier = code_challenge = get_new_code_verifier()
            
            print(len(code_verifier))
            print(code_verifier)
    """

    state: NotRequired[str]
    """A string which can be used to maintain state between the request and callback.
    It is later returned by the MAL servers to the API client. It is recommended to supply
    a random unique string for every authorization request."""

    redirect_uri: NotRequired[str]
    """The URL to redirect to after the authorization request is completed."""

    code_challenge_method: NotRequired[Literal["plain"]]
    """The method used to generate the code challenge. Must be ``plain``."""
