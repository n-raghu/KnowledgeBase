INSERT INTO accounts
SELECT 'us-farm',55,10101,TRUE,'abc-t','pot',TRUE,TRUE,'direct',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP
UNION ALL
SELECT 'us-farm',59,10102,TRUE,'xyz-t','pot',TRUE,TRUE,'partner',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP
UNION ALL
SELECT 'us-farm',75,10103,TRUE,'fif-t','pot',TRUE,TRUE,'partner',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP
UNION ALL
SELECT 'eu',85,10104,TRUE,'mc-t','pot',TRUE,TRUE,'direct',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP
UNION ALL
SELECT 'eu',95,10141,FALSE,'t-client','pot',TRUE,TRUE,'partner',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP
UNION ALL
SELECT 'eu',155,10196,FALSE,'x-client','pot',TRUE,TRUE,'partner',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP
UNION ALL
SELECT 'swiss',666,14,TRUE,'ZBNF','custom',TRUE,TRUE,'direct',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP
UNION ALL
SELECT 'swiss',555,1,TRUE,'AKS','custom',TRUE,TRUE,'direct',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP

{'aid':999,'account_name':'NuClient','instancecode':'eu','lms_custid':199,'deploy_mode':'direct','account_flag':TRUE,'eae_integration':FALSE,'channel_partner':FALSE,'onboard_type':'custom','start_date':dtm.utcnow(),'last_updated_time':dtm.utcnow()}

{"aid":999,"account_name":"WestClient","instancecode":"us-farm","lms_custid":466,"deploy_mode":"direct","account_flag":TRUE,"eae_integration":FALSE,"channel_partner":FALSE,"onboard_type":"custom","start_date":dtm.utcnow(),"last_updated_time":dtm.utcnow()}

curl -i -H "Content-Type: application/json" -X POST -d '{"aid":949,"account_name":"WestClient","instancecode":"us-farm","lms_custid":466,"deploy_mode":"direct","account_flag":true,"eae_integration":false,"channel_partner":false,"onboard_type":"custom","start_date":dtm.utcnow(),"last_updated_time":dtm.utcnow()}' 172.31.16.16:39099/accounts


CREATE TABLE IF NOT EXISTS accounts(
  instancecode TEXT,
  account_flag TEXT,
  aid BIGINT GENERATED ALWAYS AS IDENTITY,
  lms_custid BIGINT,
  account_name TEXT,
  deploy_mode TEXT,
  eae_integration BOOL,
  channel_partner BOOL,
  onboard_type TEXT,
  start_date DATE,
  last_updated_time TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
)
