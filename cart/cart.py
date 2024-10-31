

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
    def add(self, product):
        product_id = str(product.id)

        #logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)