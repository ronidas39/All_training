import boto3,io
#initialize ec2 client
ec2_client=boto3.client("ec2")

#reading the input file
with io.open("log.txt","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
#start parsing
row=data.split("\n")
#start iteration throuh the row came from line 10
for lines in row:
    instance_id=lines.split(",")[0]
    key_name=lines.split(",")[1]
    key_value=lines.split(",")[2]
    response=ec2_client.create_tags(
        Resources=[instance_id],
        Tags=[
            {
                'Key':key_name,
                'Value':key_value
            }
        ]
    )
    print(response)

   