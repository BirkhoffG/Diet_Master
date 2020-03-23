# Workflow of Commit Code

## Assumption

1. Your computer has `git` installed.

2. You have already `clone` the repository from GitHub. If not, you can clone by

   ```
   github clone https://github.com/BirkhoffG/Diet_Master.git
   ```

3. Check the `setup.md` if the developing environment has not been set up.

## Ground Rules

1. The `master` branch is the stable branch. DO NOT PUSH CODE DIRECTLY TO THE `master` BRANCH.  
2. Developers should create a new branch and submit the **pull request** to merge code into `master`.
3. Before merging any pull request, code review should be done. At least one approved review is required.

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

### 4. Push code into the Repository

1. Go to `master` branch first

   ```
   > git checkout master
   ```

2. Ensure the `master` branch is up-to-date

   ```
   > git pull
   ```

3. Go to `dev` again and push your code to the GitHub.

   ```
   > git checkout dev
   > git push
   ```

   You will find message requiring to specify the exact branch like

   ```
   ^[[Afatal: The current branch hangzhi has no upstream branch.
   To push the current branch and set the remote as upstream, use
   
       git push --set-upstream origin dev
   ```

   Follow the message 

   ```
   > git push --set-upstream origin dev
   ```

### 5. Now it is time to create a pull request in GitHub

1. Log in your GitHub account.
2. Go to our `BirkhoffG/Diet_Master` repository. On your committed branch, you can find the `Pull Request` button.

![](D:\CPS\Course\Capstone\Diet_Master\docs\imgs\start_pull_request.png)

3. After clicking the pull request, one following page will pop up. Select a reviewer to check the code and leave some comment if necessary. 

   > **Important**: This workflow mandatorily requires code review before merging into the `master` branch. Selecting a reviewer can accelerate reviewing process.

![](D:\CPS\Course\Capstone\Diet_Master\docs\imgs\open_pull_request.png)

4. The reviewer can check the changed code by clicking "Add your review".

![](D:\CPS\Course\Capstone\Diet_Master\docs\imgs\new_request.png)

5. The reviewer can make comment, approve or request change.

![](D:\CPS\Course\Capstone\Diet_Master\docs\imgs\review.png)

6. If the code is approved, reviewer or the committer can merge pull request into the `master` branch.

![](D:\CPS\Course\Capstone\Diet_Master\docs\imgs\merge.png)

