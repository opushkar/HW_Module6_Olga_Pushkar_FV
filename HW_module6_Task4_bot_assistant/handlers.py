from typing import Dict, List

def parse_input(user_input: str) -> tuple[str, List[str]]:
    """Розбирає введення користувача на команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Додає новий контакт."""
    if len(args) < 2:
        return "[bold red]Error:[/bold red] Give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return f"Contact [bold green]{name}[/bold green] added."

def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Змінює існуючий номер телефону."""
    if len(args) < 2:
        return "[bold red]Error:[/bold red] Give me name and phone please."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact [bold cyan]{name}[/bold cyan] updated."
    return f"[bold yellow]Warning:[/bold yellow] Contact {name} not found."

def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Виводить номер телефону за ім'ям."""
    if not args:
        return "[bold red]Error:[/bold red] Enter user name."
    name = args[0]
    return contacts.get(name, f"[bold yellow]Warning:[/bold yellow] Contact {name} not found.")

def show_all(contacts: Dict[str, str]) -> str:
    """Повертає список всіх контактів."""
    if not contacts:
        return "[italic]Contact list is empty.[/italic]"
    
    result = "[bold underline]My Contacts:[/bold underline]\n"
    for name, phone in contacts.items():
        result += f"• [bold]{name}[/bold]: {phone}\n"
    return result.strip()
