INSERT INTO userroles(rid,rolename,tokentime)
SELECT '1','poweruser',-1
UNION ALL
SELECT '2','orgadmin',360
UNION ALL
SELECT '101','user',60

INSERT INTO users(uid,pwd,user_name,roleid)
SELECT 'admin','adminpassword','administrator',1
UNION ALL
SELECT 'raghu','raghupassword','raghunandan',1
UNION ALL
SELECT 'yogesh','yogeshpassword','yogeshgupta',1
UNION ALL
SELECT 'ieltest','ieltestpassword','ieltestuser',2
UNION ALL
SELECT 'eaeuser','eaeuserpassword','eaeusername',101

{'aid':999,'account_name':'NuClient','instancecode':'eu','lms_custid':199,'deploy_mode':'direct','account_flag':TRUE,'eae_integration':FALSE,'channel_partner':FALSE,'onboard_type':'custom','start_date':dtm.utcnow(),'last_updated_time':dtm.utcnow()}

{"aid":999,"account_name":"WestClient","instancecode":"us-farm","lms_custid":466,"deploy_mode":"direct","account_flag":TRUE,"eae_integration":FALSE,"channel_partner":FALSE,"onboard_type":"custom","start_date":dtm.utcnow(),"last_updated_time":dtm.utcnow()}

curl -i -H "Content-Type: application/json" -X POST -d '{"account_name":"WestClient","instancecode":"us-farm","lms_custid":466,"deploy_mode":"direct","account_flag":true,"eae_integration":false,"channel_partner":false,"onboard_type":"custom","start_date":"2019-05-01","active":true}' 172.16.1.164:39099/accounts
