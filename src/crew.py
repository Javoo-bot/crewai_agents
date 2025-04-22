# src/your_project/crew.py
from crewai import Crew, Process
from src.research_bot.tasks import (
    generate_strategy_task,
    review_strategy_task,
    execute_strategy_task,
    monitor_command_output_task,
    handle_error_task,
    write_report_task
)
from src.research_bot.agents import alex, jordan, taylor, morgan, casey, riley

crew = Crew(
  agents=[alex, jordan, taylor, morgan, casey, riley],
  tasks=[
    generate_strategy_task,
    review_strategy_task,
    execute_strategy_task,
    monitor_command_output_task,
    handle_error_task,
    write_report_task
  ],
  process=Process.sequential,
  verbose=True
)
