# Workflow of Commit Code

## Assumption

1. Your computer has `git` installed.

2. You have already `clone` the repository from GitHub. If not, you can clone by

   ```
   github clone https://github.com/BirkhoffG/Diet_Master.git
   ```

3. Check the `setup.md` if the developing environment has not been set up.

## Procedure

### 1. Create a new branch

1. Type `git branch` and see which branch you are currently in. If you are in the `master ` branch, you will see

    ```
    * master
    ```

2. Create a new branch, which contains the copy of 

   ```
   > git branch dev
   ```

   > Naming the new branch `dev` is actually not recommended. Naming the new branch as a descriptive branch name such as specific feature name (e.g. frontpage) or developer's name (e.g. birkhoff) might be a better choice.
   
   Now we have two branches `git branch`
   
   ```
     dev
   * master
   ```

3. Go to the new branch

   ```
   > git checkout dev
   ```

   You can see now you are in `dev` branch

   ```
   * dev
     master
   ```

### 2. Edit in the new branch

Edit code in the new branch. 

### 3. Git Commit 

Remember you are in the new branch while commiting the code.

1. Add changed files by

   ```
   > git add [your-file-name]
   ```

   or add all changed files by

   ```
   > git add -A
   ```

2. Commit to the local repository

   ```
   > git commit -m "[commit message]"
   ```

   > Write descriptive messages such as "Add a front page", "Fix bug in header". The more descriptive, the better the commit message's quality can be.

### 4. Create a Pull Request

1. Go to `master` branch first

   ```
   > git checkout master
   ```

   