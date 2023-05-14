import boto3
import botocore.exceptions
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCES_KEY, AWS_SESSION_TOKEN, REGION_NAME, LAUNCH_TEMPLATE_ID, AMI_ID

resource_ec2 = boto3.resource("ec2", region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCES_KEY, aws_session_token=AWS_SESSION_TOKEN)

class AWS_SERVICE:

    @staticmethod
    def create_ec2_instance(quantity:int=1):
        instance = None
        try:
            instance_params = {
                "LaunchTemplate": {
                    "LaunchTemplateId": LAUNCH_TEMPLATE_ID
                },
                "ImageId": AMI_ID
            }
            instance = resource_ec2.create_instances(**instance_params, MinCount=quantity, MaxCount=quantity)[0]
            print("RUNNING INSTANCE(S)...")
            instance.wait_until_running
        except botocore.exceptions.ClientError as err:
            print("Couldn't create instance with Launch Template " + LAUNCH_TEMPLATE_ID + ".\nHere's why: " + err.response['Error']['Code'] + ": " + err.response['Error']['Message'])
            raise
        else:
            print("SUCCESS! Instance(s) running")

    @staticmethod
    def list_all_instances():
        instances = []
        for instance in resource_ec2.instances.all():
            instance_name = None
            if instance.tags != None:
                for tag in instance.tags:
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value']
            instance_data = {
                "id": instance.id,
                "platform": instance.platform,
                "instance_type": instance.instance_type,
                "public_ip_address": instance.public_ip_address,
                "image_id": instance.image.id,
                "state": instance.state,
                "name": instance_name
            }
            instances.append(instance_data)
        return instances
    
    @staticmethod
    def get_instance_by_ip(ip_addr:str):
        for instance in resource_ec2.instances.all():
            if instance.public_ip_address == ip_addr:
                return instance.id

    @staticmethod
    def stop_instance(instance_id:str):
        response = None
        try:
            instance = resource_ec2.Instance(instance_id)
            response = instance.stop()
            print("STOPPING INSTANCE...")
            instance.wait_until_stopped()
        except botocore.exceptions.ClientError as err:
            print("Couldn't stop instance " + instance_id + ". Here's why: " + err.response['Error']['Code'] + ": " + err.response['Error']['Message'])
            raise
        else:
            print(response)

    @staticmethod
    def start_instance(instance_id:str):
        response = None
        try:
            instance = resource_ec2.Instance(instance_id)
            response = instance.start()
            print("STARTING INSTANCE...")
            instance.wait_until_running()
        except botocore.exceptions.ClientError as err:
            print("Couldn't start instance " + instance_id + ". Here's why: " + err.response['Error']['Code'] + ": " + err.response['Error']['Message'])
            raise
        else:
            print(response)

    @staticmethod
    def terminate_instance(instance_id:str):
        response = None
        try:
            instance = resource_ec2.Instance(instance_id)
            response = instance.terminate()
            print("TERMINATING INSTANCE...")
            instance.wait_until_terminated()
        except botocore.exceptions.ClientError as err:
            print("Couldn't start instance " + instance_id + ". Here's why: " + err.response['Error']['Code'] + ": " + err.response['Error']['Message'])
            raise
        else:
            print(response)