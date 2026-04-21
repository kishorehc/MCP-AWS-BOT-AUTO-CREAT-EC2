import boto3

ec2 = boto3.client('ec2')


def find_instance_by_name(instance_name):
    """Find instance ID by its Name tag"""
    try:
        response = ec2.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': [instance_name]
                },
                {
                    'Name': 'instance-state-name',
                    'Values': ['pending', 'running', 'stopping', 'stopped']
                }
            ]
        )

        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance['InstanceId'])

        return instances
    except Exception as e:
        return []


def create_ec2_instance(instance_name=None):
    try:
        response = ec2.run_instances(
            ImageId='ami-0f5ee92e2d63afc18',
            MinCount=1,
            MaxCount=1,
            InstanceType='t3.micro'
        )

        instance_id = response['Instances'][0]['InstanceId']

        if instance_name:
            ec2.create_tags(
                Resources=[instance_id],
                Tags=[{'Key': 'Name', 'Value': instance_name}]
            )
            return f"✅ EC2 Created!\n   ID: {instance_id}\n   Name: {instance_name}"
        else:
            return f"✅ EC2 Created!\n   ID: {instance_id}"

    except Exception as e:
        return f"❌ Error: {str(e)}"


def list_ec2_instances():
    try:
        response = ec2.describe_instances()
        instances = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                instance_type = instance['InstanceType']

                name = "No name"
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                            break

                if state != 'terminated':
                    instances.append(
                        f"• {instance_id} | Name: {name} | Status: {state}")

        if not instances:
            return "📭 No active EC2 instances found."

        return "📋 Your EC2 Instances:\n" + "\n".join(instances)

    except Exception as e:
        return f"❌ Error: {str(e)}"


def stop_ec2_instance(identifier):
    """Stop instance by ID or Name"""
    try:
        # Check if identifier is an instance ID (starts with i-)
        if identifier.startswith('i-'):
            instance_ids = [identifier]
        else:
            # Treat as name and find matching instances
            instance_ids = find_instance_by_name(identifier)
            if not instance_ids:
                return f"❌ No running instance found with name: {identifier}"

        ec2.stop_instances(InstanceIds=instance_ids)
        return f"⏹️ Stopping instance(s): {', '.join(instance_ids)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


def terminate_ec2_instance(identifier):
    """Terminate instance by ID or Name"""
    try:
        # Check if identifier is an instance ID (starts with i-)
        if identifier.startswith('i-'):
            instance_ids = [identifier]
        else:
            # Treat as name and find matching instances
            instance_ids = find_instance_by_name(identifier)
            if not instance_ids:
                return f"❌ No instance found with name: {identifier}"

        ec2.terminate_instances(InstanceIds=instance_ids)
        return f"🗑️ Terminating instance(s): {', '.join(instance_ids)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"
