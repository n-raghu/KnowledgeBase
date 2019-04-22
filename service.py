import sys
if len(sys.argv)<2:
	pwd='nuPassword'
else:
	pwd=sys.argv[1]

from resources import Flask,JWTManager,Api,AccountID,getPostAcc,getNewToken,cfg

app=Flask(__name__)
app.config['JWT_SECRET_KEY']=cfg['app']['key']
jwt=JWTManager(app)
api=Api(app)

api.add_resource(getPostAcc,'/accounts')
api.add_resource(AccountID,'/accounts/<int:accid>')
api.add_resource(getNewToken,'/accounts/login')

app.run(debug=cfg['app']['debug'],host=cfg['app']['host'],port=cfg['app']['port'])
