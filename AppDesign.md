Account Lookup Service
- Store Accounts data in Account Lookup Service
- All apps like LMS/PHISHPROOF/IPP/StatZen/Zoltar would connect to this datastore to get any data related to accounts
- Initially we use the agent to get data, however, gradually we fork a consumer to get data from Accounts datastore

Phase-I
- Link between SFDC account and LMS org
- GET & FIND accounts

*PainPoints*
- If IM Assisted, unable to trace the LMS Org

Phase-II
- Store PII information and other apps will use this.


Customer Management Service
- *customers* Table is similar to *tbl_customer_lookup* and will have customer id fetched from *AccountLookup Service* which is an UUID and will be unique across all farms and instances.
- *user_master* is a combination of *tbl_user_master* and *tbl_student_lookup* with an unique userid across farms. Text field to identify the user status(Active/Inactive/Delete).
- *customer_groups* has all information about groups that each customer has created.
- *user_groups* is a fact table which contains ID's of all userid and groupid representing the user membership with the groups.


May 16:
1. Map and search customers, No communication.
Yogesh Suggestions:
 - LMS should hold the account id.
 - SFDC invokes API and gives accountdid to LMS.
 - Two way communication between LMS and ALS.
 - LMS gets account details from drop down for which no orgs created and IM chooses the appropriate one and LMS gives the orgid to ALS.
2. Extend to other apps
3. All systems should access ALS to get regarding customers on fly --Very far
4. ALS should be a base for both LMS and PhishProof
