
uhm


Set ssm on the right region

```
aws ssm put-parameter --name ecoleUid --type String --value XXX --region us-east-1
aws ssm put-parameter --name secretUid --type String --value XXX --region us-east-1
```

then deploy with

`sls deploy -v`
