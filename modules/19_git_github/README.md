# Module 19 — Git and GitHub

## Git versus GitHub
Git is a version-control system that records changes to files. GitHub hosts Git repositories online and adds collaboration features such as issues and pull requests.

## Basic workflow
From inside your project folder:

```bash
git init
git status
git add .
git commit -m "Complete variables exercises"
```

A commit is a snapshot of selected changes. Use a meaningful message that describes what changed.

## Connect to a remote repository
Create an empty repository on GitHub, then use its URL:

```bash
git remote add origin https://github.com/YOUR-USERNAME/python-fundamentals-course.git
git branch -M main
git push -u origin main
```

If `origin` already exists, inspect it with `git remote -v` rather than adding it again.

## Typical daily workflow
```bash
git status
git add modules/02_variables
git commit -m "Complete variable exercises"
git push
```

Review `git status` before committing. Never commit `.env` files or API keys. Use `.gitignore` to keep generated files and secrets out of version control.

## Common problems
- **Nothing to commit:** files may not have changed or may not be staged.
- **Authentication failed:** sign in using an authentication method supported by GitHub.
- **Non-fast-forward rejection:** the remote has commits your local branch lacks. Inspect the situation and integrate remote changes before pushing; don't blindly overwrite remote history.
- **Wrong folder:** Git commands operate relative to the current repository.

## Practice
1. Initialise Git in a new practice folder.
2. Commit your first Python file.
3. Change the file and make a second commit.
4. Create a public GitHub repository and push the project.
5. Update the README with what you learned.
6. Practise `git status`, `git log --oneline`, and `git diff`.
7. Explain the difference between a local repository and a remote repository.

## Challenge
Maintain a public learning repository with one commit per completed module. Write clear commit messages and use the README to explain how another beginner can run your work.


## Completion checklist
- [ ] Explain Git vs GitHub
- [ ] Stage and commit changes
- [ ] Inspect status and history
- [ ] Push a repository safely

## AI review
Use `AI_TUTOR_GUIDE.md` from the repository root to request hints and marking. Include the exact exercise, your code, and test output.
