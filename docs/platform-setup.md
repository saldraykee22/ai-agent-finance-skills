# Platform setup

The collection uses the common Agent Skills contract: one folder per skill, a required `SKILL.md`, and portable `name` and `description` frontmatter. Supporting `references/` files stay beside each skill for progressive disclosure.

## Install skills

Run from the repository root:

```bash
# Codex global: ~/.codex/skills
python scripts/install_skills.py --platform codex

# Hermes Agent global: ~/.hermes/skills
python scripts/install_skills.py --platform hermes

# Antigravity global: ~/.gemini/config/skills
python scripts/install_skills.py --platform antigravity

# Antigravity workspace: <workspace>/.agents/skills
python scripts/install_skills.py --platform antigravity --target /path/to/workspace/.agents/skills
```

The installer refuses to replace existing folders. Review a dry run, then use `--force` only when replacement is intended:

```bash
python scripts/install_skills.py --platform codex --dry-run
python scripts/install_skills.py --platform codex --force
```

Hermes can alternatively use this repository directly. Add its `skills/` directory to `skills.external_dirs` in `~/.hermes/config.yaml`, or add the GitHub repository as a tap:

```bash
hermes skills tap add saldraykee22/ai-agent-finance-skills
```

## Connect `borsa-mcp`

For research-only remote access, the upstream server documents `https://borsa.surucu.dev/mcp`. Keep the local GitHub/`uvx` route available when remote availability, privacy, or version pinning requires it.

Hermes (`~/.hermes/config.yaml`):

```yaml
mcp_servers:
  borsa-mcp:
    url: "https://borsa.surucu.dev/mcp"
    timeout: 60
```

Antigravity (`~/.gemini/config/mcp_config.json` globally or `.agents/mcp_config.json` in a workspace):

```json
{
  "mcpServers": {
    "borsa-mcp": {
      "serverUrl": "https://borsa.surucu.dev/mcp",
      "headers": {"Content-Type": "application/json"}
    }
  }
}
```

For Codex, add the local stdio server in `~/.codex/config.toml` (or the applicable project configuration):

```toml
[mcp_servers.borsa-mcp]
command = "uvx"
args = ["--from", "git+https://github.com/saidsurucu/borsa-mcp", "borsa-mcp"]
```

Set `EVDS_API_KEY` only in the platform's secret/environment configuration when EVDS series retrieval needs it. Never commit the key.

## Connect `saldraykee22/binance-trader-mcp`

Clone and prepare the upstream project first. Keep `BINANCE_DRY_RUN=true` until an intentionally supervised live-execution setup is complete.

Hermes:

```yaml
mcp_servers:
  binance-mcp:
    command: "/absolute/path/binance-trader-mcp/.venv/bin/python"
    args: ["/absolute/path/binance-trader-mcp/server.py"]
    timeout: 60
    tools:
      exclude:
        - place_market_order
        - place_limit_order
        - place_oco_order
        - cancel_order
        - place_stock_token_order
```

Antigravity stdio entry:

```json
{
  "mcpServers": {
    "binance-mcp": {
      "command": "/absolute/path/binance-trader-mcp/.venv/bin/python",
      "args": ["/absolute/path/binance-trader-mcp/server.py"],
      "env": {"BINANCE_DRY_RUN": "true"}
    }
  }
}
```

Codex stdio entry in `~/.codex/config.toml`:

```toml
[mcp_servers.binance-mcp]
command = "/absolute/path/binance-trader-mcp/.venv/bin/python"
args = ["/absolute/path/binance-trader-mcp/server.py"]
env = { BINANCE_DRY_RUN = "true" }
```

Store Binance API credentials in the platform's secret store or local environment, never in this repository. Prefer read-only API keys for research/account review. Enable trading permissions only for a deliberately isolated execution profile.

## Verify

```bash
python scripts/validate_skills.py
python scripts/validate_platform_compatibility.py
python scripts/validate_professional_contract.py
```

After installation, restart or reload the platform, confirm that `finance-agent-orchestrator` is discoverable, and ask it to perform a read-only BIST or crypto analysis before testing any account-aware workflow.
