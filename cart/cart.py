class Cart():
    def __init__(self, request):
        self.session = request.session


        # key bo'lsa ishlat
        cart = self.session.get('session_key')

        # key yo'qmi top 

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        
        # karzinka hammasida bor

        self.cart = cart
        