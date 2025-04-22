# src/your_project/tools/remote_executor_tool.py
from crewai.tools import tool
import pexpect
import os

@tool("Remote SSH Kali Linux Command Executor")
def execute_remote_command(command: str) -> str:
    """Ejecuta un comando remoto en una máquina Kali Linux vía SSH usando clave privada."""
    try:
        ssh_user = "root"
        ssh_ip = "128.140.46.243"
        ssh_key_path = os.path.expanduser("~/.ssh/automation/jlmenendez")

        # Spawn SSH session con clave
        ssh_command = f"ssh -i {ssh_key_path} -o StrictHostKeyChecking=no {ssh_user}@{ssh_ip} '{command}'"
        child = pexpect.spawn(ssh_command, timeout=500)

        child.expect(pexpect.EOF)
        output = child.before

        return output
    except Exception as e:
        return f"Error ejecutando comando remoto: {str(e)}"

# if __name__ == "__main__":
#     print("🧪 Ejecutando prueba de conexión SSH a Kali...")

#     test_command = "uname -a"
#     result = execute_remote_command.func(test_command)  
#     print("\n📤 Resultado del comando:")
#     print(result)