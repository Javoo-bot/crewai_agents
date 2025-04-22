# src/your_project/tools/logger_tool.py
from crewai.tools import tool

@tool("Command Logger Tool")
def log_command_output(command_output: str) -> str:
    """Loguea salida de un comando para análisis posterior."""
    with open("/tmp/command_log.txt", "a") as f:
        f.write(command_output + "\n" + "-"*80 + "\n")
    return "Output logged successfully."
