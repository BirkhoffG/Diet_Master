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

   > Naming the new branch `dev` is actually not recommended. Naming the new branch as a specific feature name (e.g. frontpage) or developer's name (e.g. birkhoff) might be a better choice.
   
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

