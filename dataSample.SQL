INSERT INTO users(uid,pwd,user_name)
SELECT 'admin','adminpassword','administrator'
UNION ALL
SELECT 'raghu','raghupassword','raghunandan'
UNION ALL
SELECT 'yogesh','yogeshpassword','yogeshgupta'
UNION ALL
SELECT 'ieltest','ieltestpassword','ieltestuser'
UNION ALL
SELECT 'eaeuser','eaeuserpassword','eaeusername'

CREATE TABLE IF NOT EXISTS accounts(
  instancecode TEXT,
  account_flag TEXT,
  aid UUID DEFAULT uuid_generate_v1(),
  lms_custid BIGINT,
  account_name TEXT,
  deploy_mode TEXT,
  eae_integration BOOL,
  channel_partner BOOL,
  onboard_type TEXT,
  start_date DATE,
  last_updated_time TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
)

{'aid':999,'account_name':'NuClient','instancecode':'eu','lms_custid':199,'deploy_mode':'direct','account_flag':TRUE,'eae_integration':FALSE,'channel_partner':FALSE,'onboard_type':'custom','start_date':dtm.utcnow(),'last_updated_time':dtm.utcnow()}

{"aid":999,"account_name":"WestClient","instancecode":"us-farm","lms_custid":466,"deploy_mode":"direct","account_flag":TRUE,"eae_integration":FALSE,"channel_partner":FALSE,"onboard_type":"custom","start_date":dtm.utcnow(),"last_updated_time":dtm.utcnow()}

curl -i -H "Content-Type: application/json" -X POST -d '{"account_name":"WestClient","instancecode":"us-farm","lms_custid":466,"deploy_mode":"direct","account_flag":true,"eae_integration":false,"channel_partner":false,"onboard_type":"custom","start_date":"2019-05-01","active":true}' 172.16.1.164:39099/accounts
