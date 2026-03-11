import click
import sys
import subprocess
import json
from .manager import GcloudConfig

config_mgr = GcloudConfig()

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """gcctx: Google Cloud SDK configuration manager"""
    if ctx.invoked_subcommand is None:
        configs = config_mgr.list_configurations()
        selected = config_mgr.select_with_fzf(configs)
        if selected:
            config_mgr.activate(selected)
            click.echo(f"Switched to configuration: [{selected}]")
        else:
            click.echo("No configuration selected.")

@cli.command()
def get():
    """現在アクティブなconfigurationを表示する"""
    active = config_mgr.get_active()
    if active:
        click.echo(active)
    else:
        click.echo("No active configuration found.")

@cli.command(name="ls")
def list_configs():
    """登録されている全configurationを一覧表示する"""
    configs = config_mgr.list_configurations()
    for c in configs:
        click.echo(c)

@cli.command()
@click.argument("old_name")
@click.argument("new_name")
def cp(old_name, new_name):
    """configurations の別名コピーを作成する"""
    try:
        click.echo(f"Copying configuration {old_name} to {new_name}...")
        config_mgr.create(new_name)
        
        result = subprocess.run(
            ["gcloud", "config", "configurations", "describe", old_name, "--format", "json"],
            capture_output=True, text=True, check=True
        )
        props = json.loads(result.stdout).get("properties", {})
        
        for section, values in props.items():
            for key, value in values.items():
                try:
                    subprocess.run(
                        ["gcloud", "config", "set", f"{section}/{key}", str(value), "--configuration", new_name],
                        check=True, capture_output=True, text=True
                    )
                except subprocess.CalledProcessError as e:
                    # 認証情報の不足などで set が失敗しても警告を出して続行する
                    click.echo(f"Warning: Could not set {section}/{key} for {new_name}. "
                               f"Error: {e.stderr.strip()}", err=True)
        
        click.echo(f"Successfully created and configured {new_name}.")
    except Exception as e:
        click.echo(f"Error copying configuration: {e}", err=True)
        sys.exit(1)

@cli.command(name="new")
@click.argument("name")
def new_config(name):
    """空のconfigurationを新規追加する"""
    try:
        config_mgr.create(name)
        click.echo(f"Created configuration: {name}")
    except Exception as e:
        click.echo(f"Error creating configuration: {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument("name")
def rm(name):
    """指定したconfigurationを削除する"""
    if click.confirm(f"Are you sure you want to delete configuration '{name}'?"):
        try:
            config_mgr.delete(name)
            click.echo(f"Deleted configuration: {name}")
        except Exception as e:
            click.echo(f"Error deleting configuration: {e}", err=True)
            sys.exit(1)

@cli.command()
@click.argument("name")
def use(name):
    """指定したconfigurationに直接切り換える"""
    try:
        config_mgr.activate(name)
        click.echo(f"Switched to configuration: {name}")
    except Exception as e:
        click.echo(f"Error switching configuration: {e}", err=True)
        sys.exit(1)

def main():
    cli()

if __name__ == "__main__":
    main()
