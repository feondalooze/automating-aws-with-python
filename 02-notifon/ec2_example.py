# coding: utf-8

import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.rsource('ec2')
ec2 = session.resource('ec2')
key_name = 'pythonAutomation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)

import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ls -al
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img =ec2.Image('ami-09d95fab7fff3776c')
img.Image
img.name
ami_name = 'amzn2-ami-hvm-2.0.20200520.1-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img
key
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instance(id='i-0780e87c098d7937d')
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst= instances[0]
inst.public.dns_name
inst.public_dns_name
inst.wait_until_running()
inst.public_dns_name
inst.reload()
inst.public_dns_name
ssh ec2-user@ec2-54-83-130-217.compute-1.amazonaws.com -i pythonAutomation_key.pem
ssh -i pythonAutomation_key.pem ec2-user@ec2-54-83-130-217.compute-1.amazonaws.com
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId']
)
sg.authorize_ingress(IpPermissions=
[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 'IpRanges':[{'CidrIp':'72.188.116.146/32'}]}
])
ssh ec2-user@ec2-54-83-130-217.compute-1.amazonaws.com -i pythonAutomation_key.pem
sg.authorize_ingress(IpPermissions=
[{'FromPort':80, 'ToPort':80, 'IpProtocol':'TCP', 'IpRanges':[{'CidrIp':'0.0.0.0/0'}]}
])
%history
