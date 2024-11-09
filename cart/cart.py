class Cart():
    def __init__(self,request):
        self.session=request.session
        #get session key 
        cart=self.session.get('session_key')
        
        #if user is new no session key ! create one 
        if 'session_key'  not in request.session:
            cart= self.session['session_key'] ={}

        #make sure cart is availabel on all pages 
        self.cart= cart 

