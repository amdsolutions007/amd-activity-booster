# 🚀 AMD Activity Booster

**Keep your GitHub contribution graph green with automated daily activity logs!**

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-AMD%20Activity%20Booster-blue?logo=github)](https://github.com/marketplace/actions/amd-activity-booster)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub release](https://img.shields.io/github/v/release/amdsolutions007/amd-activity-booster)](https://github.com/amdsolutions007/amd-activity-booster/releases)

## ✨ Features

- 🤖 **Automated Daily Updates** - No manual intervention required
- 💡 **AI-Powered Quotes** - Fresh motivational and tech quotes daily
- 📊 **Activity Tracking** - Maintains consistent GitHub activity
- ⚙️ **Configurable** - Customize file names and commit messages
- 🎯 **Zero Dependencies** - Pure Python, no external packages needed
- 🔒 **Secure** - Uses official GitHub Actions and tokens

## 🎯 Why Use This?

- Keep your contribution graph active during breaks
- Demonstrate consistent engagement
- Automated repository maintenance
- Professional activity logging
- No spam commits - meaningful, timestamped logs

## 🚀 Quick Start

### 1. Create Workflow File

Create `.github/workflows/daily-activity.yml` in your repository:

```yaml
name: Daily Activity Update

on:
  schedule:
    # Runs every day at 8:00 AM UTC
    - cron: '0 8 * * *'
  workflow_dispatch: # Manual trigger

jobs:
  update-activity:
    runs-on: ubuntu-latest
    
    permissions:
      contents: write
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      
      - name: Run AMD Activity Booster
        uses: amdsolutions007/amd-activity-booster@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

### 2. Customize (Optional)

```yaml
      - name: Run AMD Activity Booster
        uses: amdsolutions007/amd-activity-booster@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          activity_file: 'ACTIVITY.md'  # Custom filename
          commit_message: '📈 Auto-update'  # Custom message
```

### 3. Commit and Push

That's it! Your repository will now update automatically every day at 8 AM UTC.

## ⚙️ Configuration Options

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `github_token` | GitHub token for authentication | Yes | - |
| `activity_file` | Name of the activity log file | No | `activity_log.md` |
| `commit_message` | Commit message prefix | No | `🤖 Daily Activity Update` |

## 📊 Example Output

The action creates/updates a file with entries like:

```markdown
---

## 🤖 System Active: 2025-12-26 08:00:00 UTC

**Date:** December 26, 2025

> **Daily Quote:**  
> *AI is the new electricity. - Andrew Ng*

**Status:** ✅ Operational  
**Automation:** Active  
**Next Update:** +24 hours
```

## 🔧 Advanced Usage

### Multiple Schedules

Run at different times:

```yaml
on:
  schedule:
    - cron: '0 8 * * *'   # 8 AM UTC
    - cron: '0 20 * * *'  # 8 PM UTC
```

### Different Files for Different Repos

```yaml
jobs:
  update-main-log:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: amdsolutions007/amd-activity-booster@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          activity_file: 'logs/main.md'
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🌟 Support

- ⭐ Star this repo if you find it useful!
- 🐛 [Report issues](https://github.com/amdsolutions007/amd-activity-booster/issues)
- 💡 [Request features](https://github.com/amdsolutions007/amd-activity-booster/issues/new)

## 👨‍💻 Author

**AMD Solutions** - Building automation tools for developers

- GitHub: [@amdsolutions007](https://github.com/amdsolutions007)
- Website: [Coming Soon]

---

**🤖 Built with automation in mind. Deploy once, forget forever.**
