# 📝 GIT COMMANDS - ImmoExpert

## 🚀 Push to GitHub (Quick Guide)

### Step 1: Setup Local Git
```bash
cd C:\Users\DELL\Documents\projet\immo

# Initialize git
git init

# Add all files
git add .

# Initial commit
git commit -m "feat: Initial commit - ImmoExpert demo complete with documentation"
```

### Step 2: Create GitHub Repository
1. Visit: https://github.com/new
2. Fill in:
   - Repository name: `immo` or `immoexpert`
   - Description: "Professional real estate management platform"
   - Choose: Public or Private
3. **DON'T** check "Initialize with README"
4. Click "Create repository"

### Step 3: Connect Local to GitHub
```bash
# Replace YOUR_USERNAME and YOUR_REPO
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

---

## 📦 Common Git Commands

### First Time Setup
```bash
# Configure git (if not done before)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Verify
git config --global user.name
git config --global user.email
```

### Daily Commands
```bash
# See status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Message describing changes"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# See commit history
git log --oneline
```

### Branch Management
```bash
# Create new branch
git checkout -b feature/my-feature

# Switch to branch
git checkout branch-name

# List branches
git branch -a

# Push branch to GitHub
git push origin feature/my-feature

# Delete local branch
git branch -d feature/my-feature

# Delete remote branch
git push origin --delete feature/my-feature
```

### Undo Changes
```bash
# Undo unstaged changes
git checkout -- file-name

# Undo all changes (careful!)
git reset --hard HEAD

# Revert specific commit
git revert commit-hash

# Amend last commit
git commit --amend -m "New message"
```

---

## 📊 Commit Message Format

### Best Practices
```
feat:     Add new feature
fix:      Fix bug
docs:     Update documentation
style:    Code style changes
refactor: Refactor code
test:     Add tests
chore:    Update dependencies/build
```

### Examples
```bash
git commit -m "feat: Add demo mode with 6 properties"
git commit -m "fix: Correct filter functionality in admin"
git commit -m "docs: Update GitHub setup guide"
git commit -m "refactor: Simplify API structure"
git commit -m "style: Format code with prettier"
```

---

## 🔍 View Changes

```bash
# See differences
git diff

# See differences for specific file
git diff file-name

# See commit history
git log

# See detailed log
git log -p

# See log with branches
git log --oneline --graph --all

# See specific commit
git show commit-hash
```

---

## 🔐 GitHub SSH Setup (Optional but Recommended)

```bash
# Generate SSH key (if not done)
ssh-keygen -t ed25519 -C "your@email.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub:
# Settings → SSH and GPG keys → New SSH key → Paste
```

Then use:
```bash
git remote remove origin
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

---

## 📋 Full Workflow Example

```bash
# 1. Create and commit initial code
cd C:\Users\DELL\Documents\projet\immo
git init
git add .
git commit -m "feat: Initial commit - ImmoExpert complete"

# 2. Create GitHub repository and note the URL

# 3. Connect and push
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/immo.git
git push -u origin main

# 4. Later, make changes
git checkout -b feature/my-feature
# ... make changes ...
git add .
git commit -m "feat: Add amazing feature"
git push origin feature/my-feature

# 5. Create pull request on GitHub

# 6. After approval, merge and delete branch
git checkout main
git pull origin main
git branch -d feature/my-feature
git push origin --delete feature/my-feature
```

---

## 🆘 Common Issues & Solutions

### Problem: "fatal: not a git repository"
```bash
# Solution: Initialize git in the right directory
cd your-project-directory
git init
```

### Problem: "fatal: remote origin already exists"
```bash
# Solution: Remove existing remote
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

### Problem: "You do not have permission to push"
```bash
# Solution 1: Check your git credentials
git config --global user.email

# Solution 2: Check GitHub access
# Settings → Developer settings → Personal access tokens

# Solution 3: Use SSH instead of HTTPS
git remote remove origin
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git
```

### Problem: "error: src refspec main does not match any"
```bash
# Solution: Rename branch to main
git branch -M main
git push -u origin main
```

---

## 📚 Useful Resources

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/
- Pro Git Book: https://git-scm.com/book
- GitHub Help: https://help.github.com/

---

## ✅ Verification Checklist

Before pushing to GitHub:
- [ ] `git init` ✅
- [ ] `git add .` ✅
- [ ] `git commit` ✅
- [ ] Repository created on GitHub ✅
- [ ] Remote URL correct ✅
- [ ] `git push` successful ✅
- [ ] Files visible on GitHub ✅
- [ ] README loads correctly ✅

---

## 🎯 Next Steps

1. Run the commands in "Step 1: Setup Local Git"
2. Create repository on GitHub
3. Run the commands in "Step 3: Connect Local to GitHub"
4. Verify your code is on GitHub
5. Start collaborating! 🎉

---

**Note**: If you're not comfortable with command line, GitHub has a desktop app!
Download: https://desktop.github.com/

---

**Good luck with your ImmoExpert project! 🚀**

