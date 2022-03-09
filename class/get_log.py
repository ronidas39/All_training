import boto3,sys,io
#initialize ec2 client object
ec2_client=boto3.client("ec2")
#getting all ec2 instance info
data=ec2_client.describe_instances()
#getting info from root key 
data=data["Reservations"]
#opening a file with log.txt as name and write as mode 
with io.open("log.txt","w",encoding="utf-8")as f1:
    #iteration from the output of above
    for xx in data:
        instances=xx["Instances"]
        for instance in instances:
        #getting instance id from inner key
            print(f"writing instance id {instance['InstanceId']} in log")
            f1.write(instance["InstanceId"]+"\n")
    f1.close()