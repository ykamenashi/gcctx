import os
import subprocess
import sys
from typing import List, Optional

class GcloudConfig:
    def __init__(self):
        self.active_config_path = os.path.expanduser("~/.config/gcloud/active_config")

    def get_active(self) -> str:
        """現在アクティブなconfiguration名を取得する"""
        try:
            result = subprocess.run(
                ["gcloud", "config", "configurations", "list", "--filter", "is_active:true", "--format", "value(name)"],
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            if os.path.exists(self.active_config_path):
                with open(self.active_config_path, "r") as f:
                    return f.read().strip()
            return ""

    def list_configurations(self) -> List[str]:
        """登録されている全てのconfiguration名をリストで取得する"""
        result = subprocess.run(
            ["gcloud", "config", "configurations", "list", "--format", "value(name)"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split("\n")

    def activate(self, name: str):
        """指定したconfigurationをアクティブにする"""
        subprocess.run(["gcloud", "config", "configurations", "activate", name], check=True)

    def create(self, name: str):
        """新規configurationを作成する"""
        subprocess.run(["gcloud", "config", "configurations", "create", name], check=True)

    def delete(self, name: str):
        """指定したconfigurationを削除する"""
        subprocess.run(["gcloud", "config", "configurations", "delete", name, "--quiet"], check=True)

    def check_fzf(self) -> bool:
        """fzfがインストールされているか確認する"""
        return subprocess.run(["which", "fzf"], capture_output=True).returncode == 0

    def select_with_fzf(self, configs: List[str]) -> Optional[str]:
        """fzfを使ってconfigurationを選択する"""
        if not self.check_fzf():
            print("Error: fzf is not installed. Please install fzf to use this feature.")
            sys.exit(1)
        
        try:
            process = subprocess.Popen(
                ["fzf", "--height", "10", "--border"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                text=True
            )
            stdout, _ = process.communicate(input="\n".join(configs))
            if process.returncode == 0:
                return stdout.strip()
            return None
        except Exception as e:
            print(f"Error running fzf: {e}")
            return None
