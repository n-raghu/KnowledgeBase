- Store Accounts data in Account Lookup Service
- All apps like LMS/PHISHPROOF/IPP/StatZen/Zoltar would connect to this datastore to get any data related to accounts and opportunities.
- Initially we use the agent to get data, however, gradually we fork a consumer to get data from Accounts datastore.


Phase-I
- Link between SFDC account and LMS org
- GET & FIND accounts

*PainPoints*
- If IM Assisted, unable to trace the LMS Org

Phase-II
- Store PII information and other apps will use this.
