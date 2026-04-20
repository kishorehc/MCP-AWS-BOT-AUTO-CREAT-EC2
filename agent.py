import aws_tools
import re

def run_agent(user_input):
    user_input_lower = user_input.lower()
    user_input_original = user_input
    
    # CREATE with name
    if "create" in user_input_lower or "launch" in user_input_lower:
        instance_name = None
        
        # Look for name after "named", "called", or "name"
        patterns = [
            r'named\s+([A-Za-z0-9_-]+)',
            r'called\s+([A-Za-z0-9_-]+)',
            r'name\s+([A-Za-z0-9_-]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, user_input_original, re.IGNORECASE)
            if match:
                instance_name = match.group(1)
                break
        
        # If no pattern, check last word
        if not instance_name:
            words = user_input_original.split()
            if len(words) >= 3:
                last_word = words[-1]
                if last_word.lower() not in ['instance', 'ec2', 'an', 'a']:
                    instance_name = last_word
        
        return aws_tools.create_ec2_instance(instance_name)
    
    # LIST instances
    elif "list" in user_input_lower or "show" in user_input_lower:
        return aws_tools.list_ec2_instances()
    
    # STOP instance (by ID or Name)
    elif "stop" in user_input_lower:
        # Check for instance ID (starts with i-)
        id_match = re.search(r'i-[a-f0-9]+', user_input_lower)
        if id_match:
            return aws_tools.stop_ec2_instance(id_match.group())
        
        # Check for name after "stop"
        words = user_input_original.split()
        if len(words) > 1:
            potential_name = words[1].strip('"\'')
            if potential_name.lower() not in ['instance', 'my', 'the']:
                return aws_tools.stop_ec2_instance(potential_name)
        
        return "⚠️ Please provide an instance ID or Name (e.g., stop MyServer or stop i-123456789)"
    
    # TERMINATE instance (by ID or Name)
    elif "terminate" in user_input_lower or "delete" in user_input_lower:
        # Check for instance ID (starts with i-)
        id_match = re.search(r'i-[a-f0-9]+', user_input_lower)
        if id_match:
            return aws_tools.terminate_ec2_instance(id_match.group())
        
        # Check for name after "terminate"
        words = user_input_original.split()
        if len(words) > 1:
            potential_name = words[1].strip('"\'')
            if potential_name.lower() not in ['instance', 'my', 'the']:
                return aws_tools.terminate_ec2_instance(potential_name)
        
        return "⚠️ Please provide an instance ID or Name (e.g., terminate MyServer or terminate i-123456789)"
    
    # HELP
    else:
        return """🤖 AWS EC2 Management Bot - Now with NAME support!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 LIST instances:
   "list my EC2 instances"

🚀 CREATE instance:
   "create an EC2 instance"
   "create EC2 instance named MyServer"
   "create MyServer"

⏹️ STOP instance (by ID OR Name):
   "stop i-1234567890abcdef0"
   "stop MyServer"

🗑️ TERMINATE instance (by ID OR Name):
   "terminate i-1234567890abcdef0"
   "terminate MyServer"
   "delete MyServer"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 TIP: Use names to easily manage your instances!
"""