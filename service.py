from resources import Flask,JWTManager,Api
from resources import AccountID,getPostAcc,getNewToken,cfg,GetEvents

app=Flask(__name__)
app.config['JWT_SECRET_KEY']=cfg['app']['key']
jwt=JWTManager(app)
api=Api(app)

api.add_resource(getNewToken,'/v1/login')
api.add_resource(getPostAcc,'/v1/accounts')
api.add_resource(AccountID,'/v1/accounts/<accid>')
api.add_resource(GetEvents,'/v1/events/<eid>')

app.run(debug=cfg['app']['debug'],host=cfg['app']['host'],port=cfg['app']['port'])
