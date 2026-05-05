from rich.console import Console
from handlers import parse_input, add_contact, change_contact, show_phone, show_all

def main() -> None:
    # Ініціалізація rich-консолі та пам'яті бота
    console = Console()
    contacts = {}
    
    console.print("[bold blue]Welcome to the assistant bot![/bold blue]")
    
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
            
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            console.print("[bold magenta]Good bye![/bold magenta]")
            break
            
        elif command == "hello":
            console.print("How can I help you?", style="cyan")
            
        elif command == "add":
            response = add_contact(args, contacts)
            console.print(response)
            
        elif command == "change":
            response = change_contact(args, contacts)
            console.print(response)
            
        elif command == "phone":
            response = show_phone(args, contacts)
            console.print(response)
            
        elif command == "all":
            response = show_all(contacts)
            console.print(response)
            
        else:
            console.print("[red]Invalid command.[/red]")

if __name__ == "__main__":
    main()
