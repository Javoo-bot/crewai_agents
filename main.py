import time
from src.research_bot.crew import crew  # asegúrate de que esta ruta es correcta

if __name__ == "__main__":
    target_ip = "185.15.58.224"
    scan_description = "Full web vulnerability scan focusing on SQL injection and XSS"

    for attempt in range(5):  # Hasta 5 reintentos
        try:
            result = crew.kickoff(inputs={
                "target_ip": target_ip,
                "scan_description": scan_description
            })

            if result:
                print("\n✅ Resultado final:\n")
                print(result)
                break  # ¡Éxito!
            else:
                print("❌ El LLM devolvió una respuesta vacía, intentando nuevamente...")
                time.sleep(5)

        except ValueError as e:
            print(f"⚠️ {e}. Reintentando en 5 segundos...")
            time.sleep(5)

        except Exception as e:
            print("❌ Error inesperado:")
            raise e
