# CQRS + ApacheKafka + Microservices<br>

### About
A _microservice_ project demonstrating **CQRS** (Command Query Responsibility Segregation) where all _Commands_(INSERT,UPDATE,DELETE) are segregated to use the Message Bus system(Apache Kafka) and _Queries_(SELECT & SEARCH) use the direct database.

### Authentication
All endpoints are designed to use **JWT** Authentication.

### CEP
All actions performed with the endpoints are tracked and asynchronously recorded into the database in the form of events which would be a starting point for _Complex Event Processing_

### Search API
Salient feature of search API include: <br>
    - Pagination <br>
    172.x.x.172:39099/api/accounts?__page__=100 <br>
    - Integrated with '%' and works very similar to database LIKE operator <br>
    172.x.x.172:39099/api/accounts?__page__=100&accountname=%tech% <br>
    - any parameter can be suffixed with _between_ operator to get values between the parameter. <br>
    172.x.x.172:39099/api/accounts?__page__=100&accountname=%tech%&onboarddate__between__=20190101,20190331 <br>


### Deployment
_I'm preparing a document to deploy the service using ECS images_

### Working Principle
_To be documented_