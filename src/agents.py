# src/your_project/agents.py

from crewai import Agent
from src.research_bot.tools.remote_executor_tool import execute_remote_command
from src.research_bot.tools.logger_tool import log_command_output
from src.research_bot.llm_config import my_llm

# Estratega
alex = Agent(
  role="Vulnerability Assessment Strategist",
  goal="Create an effective vulnerability scanning strategy",
  backstory=(
    "You are Alex, a methodical penetration tester who always starts with recon. "
    "You build strategies that are logical, executable, and thorough."
  ),
  verbose=True,
  memory=True,
  allow_delegation=False,
  llm=my_llm
)

# Revisor Senior
jordan = Agent(
  role="Senior Security Reviewer",
  goal="Review scanning strategies and ensure technical correctness",
  backstory=(
    "You are Jordan, the most experienced pentester on the team. "
    "Your job is to ensure quality, completeness, and technical soundness."
  ),
  verbose=True,
  memory=True,
  allow_delegation=False,
  llm=my_llm
)

# Executor remoto
taylor = Agent(
  role="Remote Command Executor",
  goal="Execute strategy commands on a remote Kali Linux machine",
  backstory=(
    "You are Taylor, a skilled operator executing each scanning command remotely. "
    "You report the output and handle command failures gracefully."
  ),
  tools=[execute_remote_command, log_command_output],
  verbose=True,
  memory=True,
  allow_delegation=False,
  llm=my_llm
)

# Analista de output
morgan = Agent(
  role="Command Output Analyst",
  goal="Determine whether the command output requires further input",
  backstory=(
    "You are Morgan, an expert in interpreting command-line tool outputs. "
    "You assist Taylor by analyzing whether input is needed or the command is still running."
  ),
  verbose=True,
  memory=True,
  allow_delegation=False,
  llm=my_llm
)

# Fixer de errores
casey = Agent(
  role="Linux Error Troubleshooter",
  goal="Diagnose and fix Linux shell command errors",
  backstory=(
    "You are Casey, a Linux wizard. You provide quick fixes and clear explanations "
    "whenever errors appear during remote execution."
  ),
  verbose=True,
  memory=True,
  allow_delegation=False,
  llm=my_llm
)

# Generador de reportes
riley = Agent(
  role="Vulnerability Report Writer",
  goal="Write professional, client-ready Markdown vulnerability reports",
  backstory=(
    "You are Riley, a security analyst and skilled technical writer. "
    "You translate technical findings into clear, structured reports."
  ),
  verbose=True,
  memory=True,
  allow_delegation=False,
  llm=my_llm
)
