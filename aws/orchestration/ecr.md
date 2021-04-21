# Elastic Container Registry

### Configure Amazon profile
Create a file ~/.aws/credentials

```
[default]
aws_access_key_id=AKI************I4Q
aws_secret_access_key=Cd8************rhP
region=us-east-1
```

### Create a registry in Amazon
```
aws ecr create-repository --repository-name <water>
```

### ECR Login
```
aws ecr get-login-password --region <us-east-1> | docker login --username AWS --password-stdin <842017991225>.dkr.ecr.<us-east-1>.amazonaws.com
```
_Note: This is a temporary login and will remain active for around 12h_

### Push image to ECR
```
docker tag <e456ladfn69> <amazon_acc>.dkr.ecr.<us-east-1>.amazonaws.com/<water>
docker push <amazon_acc>.dkr.ecr.<us-east-1>.amazonaws.com/<water>
```

### List ECR
```
aws ecr list-images --repository-name <water>
```

### Describer
This gives **image size**, **timestamp** & **digesh hash**

```
aws ecr describe-images --repository-name water
```

_Observation: ECR compresses the image and the space is reduced by almost (33-50)%_
