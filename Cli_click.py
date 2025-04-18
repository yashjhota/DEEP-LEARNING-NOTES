from CacCli.cal import *
import click

@click.group()
def cli():
    """This is a simple calculator CLI."""

@cli.command("add")
@click.argument("num1", type=float)
@click.argument("num2", type=float)

def add_command(num1, num2):
    """Add two numbers.
    
    Example usage:
    $ cac add 2 3
    
    """
    result = add(num1, num2)
    # Display the result in color for better visibility
    click.echo(click.style(f"The result of adding {num1} and {num2} is: {result}", fg="green"))

@cli.command("subtract")
@click.argument("num1", type=float)
@click.argument("num2", type=float)

def subtract_command(num1, num2):
    """Subtract two numbers."""
    result = subtract(num1, num2)
    # Display the result in color for better visibility
    click.echo(click.style(f"The result of subtracting {num2} from {num1} is: {result}", fg="blue"))

@cli.command("multiply")
@click.argument("num1", type=float)
@click.argument("num2", type=float)
def multiply_command(num1, num2):
    """Multiply two numbers."""
    result = multiply(num1, num2)
    # Display the result in color for better visibility
    click.echo(click.style(f"The result of multiplying {num1} and {num2} is: {result}", fg="yellow"))

@cli.command("divide")
@click.argument("num1", type=float)
@click.argument("num2", type=float)
def divide_command(num1, num2):
    """Divide two numbers."""
    if num2 == 0:
        click.echo(click.style("Error: Division by zero is not allowed.", fg="red"))
        return
    result = divide(num1, num2)
    # Display the result in color for better visibility
    click.echo(click.style(f"The result of dividing {num1} by {num2} is: {result}", fg="magenta"))

@cli.command("power")
@click.argument("base", type=float)
@click.argument("exponent", type=float)
def power_command(base, exponent):
    """Calculate the power of a number."""
    result = power(base, exponent)
    # Display the result in color for better visibility
    click.echo(click.style(f"The result of raising {base} to the power of {exponent} is: {result}", fg="cyan"))

if __name__ == "__main__":
    cli()


