

class Cart():
    
    def __init__(self, request):

        # Returning user - obtain his/her existing session
        
        self.session = request.session
        cart = self.session.get('session_key')

        # New user - generate a new session

        if 'session_key' not in request.session:

            cart = self.session['session_key'] = {}

        self.cart = cart